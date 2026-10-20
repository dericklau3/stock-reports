#!/usr/bin/env python3
"""P1 auditable cross-checks: annual FCFF DCF, point-in-time forward P/E, segment SOTP.

This calculates conditional scenarios, not authoritative securities price targets.
Inputs use P0 provenance objects; all money and shares are USD millions / millions.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import statistics
import sys
from datetime import date

from valuation_engine import ValidationError, day, fact, fail, fields, mapping, required


def nonempty(value, path, minimum=1):
    if not isinstance(value, str) or len(value.strip()) < minimum:
        fail(path, f"must be a meaningful string (min {minimum} characters)")
    return value.strip()


def num(node, path, asof, *, minimum=None, maximum=None):
    value, d = fact(node, path, asof)
    if minimum is not None and value < minimum or maximum is not None and value > maximum:
        fail(path, f"outside permitted range [{minimum},{maximum}]")
    return value, d


def v(node, path, asof, *, minimum=None, maximum=None):
    return num(node, path, asof, minimum=minimum, maximum=maximum)[0]


def root_metadata(doc):
    fields(doc, {"schema_version", "ticker", "valuation_date", "currency", "price", "capital", "analyses"}, "root")
    if doc.get("schema_version") != 2:
        fail("schema_version", "required: 2")
    nonempty(required(doc, "ticker", "root"), "ticker")
    asof = day(required(doc, "valuation_date", "root"), "valuation_date")
    if doc.get("currency") != "USD":
        fail("currency", "only USD and million-unit accounting supported")
    p = mapping(required(doc, "price", "root"), "price")
    price, quote_on = num(p, "price", asof, minimum=0.0000000001)
    if p["basis"] != "market" or (asof - quote_on).days > 7:
        fail("price", "market price required; quote cannot be >7 calendar days old")
    capital = None
    warnings = []
    if "capital" in doc:
        cap = mapping(doc["capital"], "capital")
        fields(cap, {"bridge_as_of", "reconciliation_note", "shares_m", "cash_m", "debt_m", "other_claims_m"}, "capital")
        if day(required(cap, "bridge_as_of", "capital"), "capital.bridge_as_of") != asof:
            fail("capital.bridge_as_of", "claims bridge must be as of valuation date")
        capital = {}
        ages = []
        for key in ("shares_m", "cash_m", "debt_m", "other_claims_m"):
            value, item_day = num(required(cap, key, "capital"), "capital." + key, asof, minimum=0)
            if key == "shares_m" and value <= 0:
                fail("capital.shares_m", "must be > 0")
            capital[key] = value
            if item_day != asof:
                ages.append(key)
        if ages:
            nonempty(cap.get("reconciliation_note"), "capital.reconciliation_note", 20)
            warnings.append("Provisional capital bridge: dated inputs " + ", ".join(ages) + ". Interim financing and dilution MUST be independently reconciled.")
    return asof, price, quote_on, capital, warnings


def years_cashflows(items, asof, path, warnings):
    if not isinstance(items, list) or not 5 <= len(items) <= 10:
        fail(path, "need 5-10 consecutive forward annual cash-flow periods")
    previous = asof
    rows = []
    for i, item in enumerate(items):
        q = f"{path}[{i}]"
        item = mapping(item, q)
        fields(item, {"end_date", "revenue_m", "ebit_margin", "cash_tax_rate", "d_and_a_m", "capex_m", "delta_nwc_m"}, q)
        end = day(required(item, "end_date", q), q + ".end_date")
        delta = (end - previous).days
        if not 300 <= delta <= 430:
            fail(q + ".end_date", "period length must be approximately one year (300-430 days), no gaps or stubs")
        values = {key: v(required(item, key, q), q + "." + key, asof)
                  for key in ("revenue_m", "ebit_margin", "cash_tax_rate", "d_and_a_m", "capex_m", "delta_nwc_m")}
        if values["revenue_m"] <= 0 or not -1 <= values["ebit_margin"] <= 1 or not 0 <= values["cash_tax_rate"] <= .6:
            fail(q, "revenue positive; EBIT margin [-100%,100%], tax rate [0,60%]")
        if values["d_and_a_m"] < 0 or values["capex_m"] < 0:
            fail(q, "depreciation and capex must be nonnegative")
        ebit = values["revenue_m"] * values["ebit_margin"]
        # Negative EBIT generates no automatic tax refund; NOL utilization needs an explicit tax schedule.
        tax = max(0, ebit) * values["cash_tax_rate"]
        fcff = ebit - tax + values["d_and_a_m"] - values["capex_m"] - values["delta_nwc_m"]
        rows.append({"end_date": end.isoformat(), "years_from_valuation": (end-asof).days/365.25,
                     "ebit_m": ebit, "cash_taxes_m": tax, "fcff_m": fcff, "revenue_m": values["revenue_m"]})
        if ebit < 0:
            warnings.append(f"{q}: negative EBIT gives zero cash taxes; no speculative tax refund or NOL benefit assumed")
        previous = end
    return rows


def terminal_value(rows, terminal, asof, path, discount):
    terminal = mapping(terminal, path)
    method = required(terminal, "method", path)
    fields(terminal, {"method", "growth"} if method == "perpetuity" else {"method", "exit_ev_ebit"}, path)
    if method == "perpetuity":
        g = v(required(terminal, "growth", path), path + ".growth", asof, minimum=-.10, maximum=.10)
        if g >= discount:
            fail(path + ".growth", "perpetual growth must be below WACC")
        if rows[-1]["fcff_m"] <= 0:
            fail(path, "perpetuity requires positive final-year normalized FCFF")
        tv = rows[-1]["fcff_m"] * (1 + g) / (discount - g)
        return method, g, tv
    if method == "exit_ev_ebit":
        multiple = v(required(terminal, "exit_ev_ebit", path), path + ".exit_ev_ebit", asof, minimum=0)
        if multiple <= 0 or rows[-1]["ebit_m"] <= 0:
            fail(path, "exit multiple and final EBIT must be positive")
        return method, multiple, rows[-1]["ebit_m"] * multiple
    fail(path + ".method", "must be perpetuity or exit_ev_ebit")


def discounted_fcff(rows, wacc, terminal_method, param):
    if not 0 < wacc <= 1:
        fail("wacc", "discount rate must be in (0,1]")
    explicit = sum(r["fcff_m"] / (1+wacc)**r["years_from_valuation"] for r in rows)
    if terminal_method == "perpetuity":
        if param >= wacc:
            return None
        tv = rows[-1]["fcff_m"] * (1+param) / (wacc-param)
    else:
        tv = rows[-1]["ebit_m"] * param
    terminal_pv = tv / (1+wacc)**rows[-1]["years_from_valuation"]
    return {"pv_explicit_fcff_m": explicit, "pv_terminal_m": terminal_pv,
            "enterprise_value_m": explicit+terminal_pv}


def calc_dcf(node, asof, capital, prefix, warnings, bridge=True):
    fields(node, {"name", "scenario", "method", "wacc", "years", "terminal", "justification"}, prefix)
    nonempty(required(node, "justification", prefix), prefix + ".justification", 30)
    wacc = v(required(node, "wacc", prefix), prefix + ".wacc", asof, minimum=.00001, maximum=1)
    rows = years_cashflows(required(node, "years", prefix), asof, prefix + ".years", warnings)
    tm, param, _ = terminal_value(rows, required(node, "terminal", prefix), asof, prefix + ".terminal", wacc)
    value = discounted_fcff(rows, wacc, tm, param)
    if value["enterprise_value_m"] <= 0:
        fail(prefix, "discounted enterprise value is nonpositive")
    if value["pv_terminal_m"] / value["enterprise_value_m"] > .75:
        warnings.append(prefix + ": terminal value exceeds 75% of EV; conclusions are terminal-assumption sensitive")
    dcf = {**value, "wacc": wacc, "terminal_method": tm, "terminal_parameter": param,
           "years": rows, "terminal_share_of_ev": value["pv_terminal_m"] / value["enterprise_value_m"]}
    if not bridge:
        return dcf
    if capital is None:
        fail(prefix, "fcff_dcf needs a current, reconciled or provisional capital bridge")
    def eq_per_share(ev):
        eq = ev + capital["cash_m"] - capital["debt_m"] - capital["other_claims_m"]
        return None if eq <= 0 else eq / capital["shares_m"]
    price = eq_per_share(value["enterprise_value_m"])
    if price is None:
        fail(prefix, "DCF enterprise value is less than debt and other claims net of cash")
    matrix = []
    rates = [max(.00001, wacc-.01), wacc, min(1, wacc+.01)]
    terminal_params = ([param-.005, param, param+.005] if tm == "perpetuity"
                       else [param*.8, param, param*1.2])
    for rate in rates:
        matrix.append({"wacc": rate, "cells": [{"terminal_parameter": p,
            "per_share_usd": (None if (calc := discounted_fcff(rows, rate, tm, p)) is None
                              else eq_per_share(calc["enterprise_value_m"]))} for p in terminal_params]})
    implied_ev = None
    # Reverse DCF fixes intermediate FCFF and solves the terminal assumption that implies the observed price.
    # Compare against independently observed current capital bridge, not a synthetic future diluted market cap.
    reverse = {"type": "required_perpetual_growth" if tm == "perpetuity" else "required_exit_ev_ebit", "value": None}
    dcf.update({"present_value_per_share_usd": price, "sensitivity": matrix, "reverse": reverse})
    return dcf


def reverse_dcf(dcf, market_price, capital):
    wacc = dcf["wacc"]
    rows = dcf["years"]
    t = rows[-1]["years_from_valuation"]
    market_ev = market_price*capital["shares_m"] - capital["cash_m"] + capital["debt_m"] + capital["other_claims_m"]
    terminal_ev_needed = (market_ev - dcf["pv_explicit_fcff_m"]) * (1+wacc)**t
    if dcf["terminal_method"] == "perpetuity":
        f = rows[-1]["fcff_m"]
        denominator = terminal_ev_needed + f
        candidate = (terminal_ev_needed*wacc - f)/denominator if abs(denominator)>1e-12 else None
        if candidate is not None and -1 < candidate < wacc:
            dcf["reverse"]["value"] = candidate
    else:
        ebit = rows[-1]["ebit_m"]
        if ebit > 0 and terminal_ev_needed >= 0:
            dcf["reverse"]["value"] = terminal_ev_needed / ebit
    dcf["reverse"]["implied_market_ev_m"] = market_ev
    dcf["reverse"]["required_terminal_ev_m"] = terminal_ev_needed
    return dcf


def forward_pe(node, asof, price, quote_on, prefix):
    fields(node, {"name", "scenario", "method", "basis", "horizon", "period_start", "period_end", "eps", "peers", "history"}, prefix)
    basis = node.get("basis")
    horizon = node.get("horizon")
    if basis not in ("gaap", "adjusted") or horizon not in ("NTM", "FY1", "FY2"):
        fail(prefix, "basis must be gaap/adjusted and horizon NTM/FY1/FY2")
    start = day(required(node, "period_start", prefix), prefix + ".period_start")
    end = day(required(node, "period_end", prefix), prefix + ".period_end")
    if end <= quote_on or not 300 <= (end-start).days <= 430:
        fail(prefix, "forecast EPS must refer to a real 300–430-day fiscal/NTM period ending after quote")
    eps, eps_day = num(required(node, "eps", prefix), prefix + ".eps", asof, minimum=0)
    if eps <= 0 or eps_day > quote_on or (quote_on-eps_day).days > 7:
        fail(prefix + ".eps", "positive EPS with point-in-time snapshot <= price date within 7 days required")
    peers = required(node, "peers", prefix)
    if not isinstance(peers, list) or len(peers) < 2:
        fail(prefix + ".peers", "at least two distinct matched forward P/E peers required")
    multiples = []
    names = set()
    matched_peers = []
    for i, peer in enumerate(peers):
        q = f"{prefix}.peers[{i}]"
        peer = mapping(peer, q)
        fields(peer, {"ticker", "basis", "horizon", "period_start", "period_end", "price", "eps", "comparable_reason"}, q)
        peer_name = nonempty(required(peer, "ticker", q), q + ".ticker")
        if peer_name in names:
            fail(q, "duplicate comparable")
        names.add(peer_name)
        nonempty(required(peer, "comparable_reason", q), q + ".comparable_reason", 20)
        if peer.get("basis") != basis or peer.get("horizon") != horizon:
            fail(q, "peer EPS basis/horizon mismatches target")
        ps = day(required(peer, "period_start", q), q + ".period_start")
        pe = day(required(peer, "period_end", q), q + ".period_end")
        if not 300 <= (pe-ps).days <= 430 or abs((pe-end).days) > (30 if horizon=="NTM" else 190):
            fail(q, "peer EPS period misaligned to target")
        pp, pp_day = num(required(peer, "price", q), q + ".price", asof, minimum=0)
        ep, ep_day = num(required(peer, "eps", q), q + ".eps", asof, minimum=0)
        if pp <= 0 or ep <= 0 or max(abs((quote_on-d).days) for d in (pp_day,ep_day)) > 7 or pp_day>quote_on or ep_day>quote_on:
            fail(q, "positive peer price/EPS and matched historical snapshots within 7 days of reference quote required")
        ratio = pp/ep
        multiples.append(ratio)
        matched_peers.append({"ticker": peer_name, "forward_pe": ratio, "price_as_of": str(pp_day), "eps_as_of": str(ep_day), "forecast_period": [str(ps),str(pe)]})
    history_rows=[]
    for i, point in enumerate(node.get("history", [])):
        q=f"{prefix}.history[{i}]"
        point=mapping(point,q)
        fields(point,{"observed_on","price","eps","basis","period_start","period_end"},q)
        on=day(required(point,"observed_on",q),q+".observed_on")
        if on>quote_on or (quote_on-on).days>366 or point.get("basis")!=basis:
            fail(q,"history must be from last year with same EPS basis")
        hs=day(required(point,"period_start",q),q+".period_start")
        he=day(required(point,"period_end",q),q+".period_end")
        if not 300 <= (he-hs).days <= 430 or he<=on:
            fail(q,"history requires contemporaneous future EPS period")
        hp,hpd=num(required(point,"price",q),q+".price",asof,minimum=0)
        heps,hed=num(required(point,"eps",q),q+".eps",asof,minimum=0)
        if hp<=0 or heps<=0 or hpd>on or hed>on or max((on-hpd).days,(on-hed).days)>7:
            fail(q,"history EPS and price must be observed at historical time (no look-ahead)")
        history_rows.append({"observed_on":str(on),"forward_pe":hp/heps,"forecast_period":[str(hs),str(he)]})
    multiples.sort()
    median = statistics.median(multiples)
    return {"method":"forward_pe","basis":basis,"horizon":horizon,"period":[str(start),str(end)],
            "current_forward_pe": price/eps,"peer_median_forward_pe":median,
            "peer_implied_price_usd":eps*median,"peers":matched_peers,
            "history_sample_extrema": (None if not history_rows else {"min":min(r["forward_pe"] for r in history_rows),"max":max(r["forward_pe"] for r in history_rows),"points":len(history_rows),"coverage":"sample_extrema_not_full_year"}),
            "warning":"Trading-comparable benchmark, NOT an independent intrinsic-value target; peer multiple needs qualitative adjustment."}


def sotp(node, asof, capital, prefix, warnings):
    fields(node, {"name", "scenario", "method", "segments", "corporate_cost_pv_m", "nonoperating_assets_m", "overlap_reconciliation"}, prefix)
    if capital is None:
        fail(prefix, "SOTP needs valuation-date capital bridge")
    nonempty(required(node,"overlap_reconciliation",prefix),prefix+".overlap_reconciliation",50)
    cost=v(required(node,"corporate_cost_pv_m",prefix),prefix+".corporate_cost_pv_m",asof,minimum=0)
    assets=v(required(node,"nonoperating_assets_m",prefix),prefix+".nonoperating_assets_m",asof,minimum=0)
    segments=required(node,"segments",prefix)
    if not isinstance(segments,list) or len(segments)<2:
        fail(prefix+".segments","need 2+ non-overlapping businesses for SOTP")
    names=set()
    rows=[]
    for i,s in enumerate(segments):
        q=f"{prefix}.segments[{i}]"
        s=mapping(s,q)
        kind=required(s,"kind",q)
        common={"name","kind","ownership","boundary_note"}
        methods={
            "current_ev":{"enterprise_value_m"},
            "exit_ebit":{"target_date","revenue_m","ebit_margin","exit_ev_ebit","wacc"},
            "milestone_ev":{"target_date","success_ev_m","failure_ev_m","success_probability","wacc"},
            "fcff_dcf":{"wacc","years","terminal","justification"}}
        if kind not in methods:
            fail(q+".kind","unknown segment kind")
        fields(s,common|methods[kind],q)
        name=nonempty(required(s,"name",q),q+".name")
        if name in names:
            fail(q,"duplicate segment")
        names.add(name)
        nonempty(required(s,"boundary_note",q),q+".boundary_note",30)
        ownership=v(required(s,"ownership",q),q+".ownership",asof,minimum=0,maximum=1)
        if ownership<=0:
            fail(q+".ownership","must exceed zero")
        if kind=="current_ev":
            ev, observed=num(required(s,"enterprise_value_m",q),q+".enterprise_value_m",asof)
            if (asof-observed).days>7:
                fail(q,"current EV must have fresh as-of date, not a stale segment market value")
        elif kind=="fcff_dcf":
            dcf=calc_dcf({"name": name, "scenario": "base", "method": "fcff_dcf",
                          "wacc": s["wacc"], "years": s["years"], "terminal": s["terminal"],
                          "justification": s["justification"]}, asof, None, q, warnings, bridge=False)
            ev=dcf["enterprise_value_m"]
        else:
            target=day(required(s,"target_date",q),q+".target_date")
            if target<=asof:
                fail(q+".target_date","target must be after valuation date")
            wacc=v(required(s,"wacc",q),q+".wacc",asof,minimum=.00001,maximum=1)
            if kind=="exit_ebit":
                revenue=v(required(s,"revenue_m",q),q+".revenue_m",asof,minimum=0)
                margin=v(required(s,"ebit_margin",q),q+".ebit_margin",asof,minimum=0,maximum=1)
                multiple=v(required(s,"exit_ev_ebit",q),q+".exit_ev_ebit",asof,minimum=0)
                if revenue<=0 or margin<=0 or multiple<=0:
                    fail(q,"positive EBIT and exit multiple required; pre-profit segment needs milestone/FCFF")
                future_ev=revenue*margin*multiple
            else:
                success=v(required(s,"success_ev_m",q),q+".success_ev_m",asof,minimum=0)
                failure=v(required(s,"failure_ev_m",q),q+".failure_ev_m",asof,minimum=0)
                probability=v(required(s,"success_probability",q),q+".success_probability",asof,minimum=0,maximum=1)
                future_ev=success*probability+failure*(1-probability)
                warnings.append(q+": milestone probability is subjective unless independently supported; both outcomes exclude duplicated legacy operations")
            ev=future_ev/(1+wacc)**((target-asof).days/365.25)
        rows.append({"name":name,"kind":kind,"ownership":ownership,"owned_enterprise_pv_m":ev*ownership})
    ev_owned=sum(r["owned_enterprise_pv_m"] for r in rows) - cost + assets
    equity=ev_owned+capital["cash_m"]-capital["debt_m"]-capital["other_claims_m"]
    if equity<=0:
        fail(prefix,"SOTP equity value <=0 after corporate costs and claims")
    return {"method":"sotp","segments":rows,"owned_segments_ev_m":sum(r["owned_enterprise_pv_m"] for r in rows),
            "corporate_cost_pv_m":cost,"nonoperating_assets_m":assets,"enterprise_and_nonoperating_m":ev_owned,
            "equity_value_m":equity,"present_value_per_share_usd":equity/capital["shares_m"],
            "warning":"Ownership %, corporate costs, net debt, minority claims, intercompany eliminations and financing must be reconciled manually."}


def evaluate(doc):
    doc=mapping(doc,"root")
    asof,price,quote_on,capital,warnings=root_metadata(doc)
    analyses=required(doc,"analyses","root")
    if not isinstance(analyses,list) or not analyses:
        fail("analyses","must be a nonempty array")
    results=[]
    ids=set()
    for i,analysis in enumerate(analyses):
        q=f"analyses[{i}]"
        analysis=mapping(analysis,q)
        name=nonempty(required(analysis,"name",q),q+".name")
        if name in ids:
            fail(q,"duplicate analysis name")
        ids.add(name)
        scenario=analysis.get("scenario")
        if scenario not in ("bear","base","bull"):
            fail(q+".scenario","use bear/base/bull")
        method=required(analysis,"method",q)
        if method=="fcff_dcf":
            result=calc_dcf(analysis,asof,capital,q,warnings)
            reverse_dcf(result,price,capital)
        elif method=="forward_pe":
            result=forward_pe(analysis,asof,price,quote_on,q)
        elif method=="sotp":
            result=sotp(analysis,asof,capital,q,warnings)
        else:
            fail(q+".method","unknown P1 method")
        result.update({"name":name,"scenario":scenario,"method":method})
        if "present_value_per_share_usd" in result:
            result["upside_vs_reference"]=result["present_value_per_share_usd"]/price-1
        results.append(result)
    checks=[]
    for scenario in ("bear","base","bull"):
        intrinsic=[r for r in results if r["scenario"]==scenario and r["method"] in ("fcff_dcf","sotp")]
        if len(intrinsic)>=2:
            low=min(r["present_value_per_share_usd"] for r in intrinsic)
            high=max(r["present_value_per_share_usd"] for r in intrinsic)
            checks.append({"scenario":scenario,"models":[r["name"] for r in intrinsic],"min_usd":low,"max_usd":high,
                           "high_over_low":high/low,"material_disagreement":high/low>=1.3,
                           "note":"Do not average conflicting models or treat similar assumptions as independent evidence"})
    warnings.extend(["No model blends/weights outputs; reconcile differences explicitly rather than averaging prices.",
                     "P1 is an offline assumption calculator. Source URLs and financial forecasts MUST be checked by the researcher.",
                     "FCFF DCF uses current economic shares and does not automatically model future equity issuance or financing shortfalls; material expected dilution requires independent adjustment."])
    return {"schema_version":2,"ticker":doc["ticker"],"valuation_date":str(asof),"currency":"USD",
            "reference_price_usd":price,"reference_price_as_of":str(quote_on),
            "capital":capital,"capital_status": "not_provided" if capital is None else ("provisional" if any(w.startswith("Provisional capital") for w in warnings) else "as_of_declared"),
            "results":results,"crosschecks":checks,"warnings":warnings}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path)
    parser.add_argument("-o","--output",type=Path)
    args=parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as f:
            data=json.load(f,parse_constant=lambda val:fail("json",f"invalid constant {val}"))
        output=evaluate(data)
        result=json.dumps(output,ensure_ascii=False,indent=2,allow_nan=False)+"\n"
        if args.output:
            args.output.write_text(result,encoding="utf-8")
        else:
            print(result,end="")
        return 0
    except (OSError,ValueError) as err:
        print("VALUATION BLOCKED: "+str(err),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
