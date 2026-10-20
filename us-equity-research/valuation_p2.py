#!/usr/bin/env python3
"""P2 auditable valuation vintage freeze, walk-forward review and non-causal attribution.

Offline only; does not download historical prices or create fictitious financial actuals.
Run from this file's directory or the repository root, Python 3.11+.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import hashlib
import itertools
import json
import math
from pathlib import Path
import statistics
import sys

from valuation_engine import ValidationError, day, fact, fail, fields, mapping, required, validated_input
from valuation_p1 import evaluate as evaluate_p1


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def finite(value, path, *, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        fail(path, "expected a finite number")
    if positive and value <= 0:
        fail(path, "must be positive")
    return float(value)


def number_fact(item, name, cutoff, *, basis=None, positive=False):
    value, observed = fact(item, name, cutoff, positive=positive)
    if basis is not None and item["basis"] != basis:
        fail(name + ".basis", "expected " + basis)
    return value, observed


def model_result(doc, name):
    ver = doc.get("schema_version")
    if ver == 1:
        output = validated_input(doc)
        matches = [r for r in output["results"] if r["name"] == name]
        case = next((c for c in doc["cases"] if c["name"] == name), None)
        if case is None:
            fail("name", "P0 case not found")
        target = case["target_date"]
    elif ver == 2:
        output = evaluate_p1(doc)
        matches = [r for r in output["results"] if r["name"] == name]
        if not matches:
            fail("name", "P1 analysis not found")
        selected = matches[0]
        if selected["method"] == "forward_pe":
            fail("name", "forward_pe is a market comparable, not a standalone intrinsic forecast")
        if selected["method"] == "fcff_dcf":
            target = selected["years"][-1]["end_date"]
        else:
            # Segment terminal horizons can differ. Never invent one consolidated realization date.
            target = None
    else:
        fail("schema_version", "P2 freeze supports original P0 v1 or P1 v2 only")
    if len(matches) != 1:
        fail("name", "expected exactly one named model result")
    result = matches[0]
    return output, result, target


def forecast_metrics(doc, output, result, name):
    if doc["schema_version"] == 1:
        case = next(c for c in doc["cases"] if c["name"] == name)
        x = {k: v["value"] for k, v in case["inputs"].items()}
        metrics = {"revenue_m": x["revenue_m"]}
        if result["method"] == "equity_pe":
            metrics.update(net_income_m=x["revenue_m"] * x["net_margin"],
                           diluted_shares_m=x["forecast_shares_m"])
        else:
            metrics["ebit_m"] = x["revenue_m"] * x["ebit_margin"]
            if "forecast_shares_m" in x:
                metrics["diluted_shares_m"] = x["forecast_shares_m"]
        return metrics
    if result["method"] == "fcff_dcf":
        last = result["years"][-1]
        return {k: last[k] for k in ("revenue_m", "ebit_m", "fcff_m")}
    return {}


def freeze(doc, name, *, captured_at=None):
    """Replay the original model; preserve exact frozen inputs & derived output plus hashes."""
    output, result, target = model_result(doc, name)
    market = output["price"] if doc["schema_version"] == 1 else output["reference_price_usd"]
    intrinsic = result.get("present_value_per_share_usd")
    if intrinsic is None:
        fail("result", "selected model does not produce an intrinsic scenario value")
    finite(intrinsic, "result.price", positive=True)
    timestamp = captured_at or datetime.now(timezone.utc).isoformat()
    recorded = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if recorded.tzinfo is None:
        fail("captured_at", "timezone required")
    valuation_date = day(doc["valuation_date"], "valuation_date")
    if recorded.date() < valuation_date:
        fail("captured_at", "record creation cannot precede research valuation date")
    item = {
        "schema_version": 3, "kind": "valuation_snapshot",
        "ticker": doc["ticker"], "model_version": doc["schema_version"],
        "name": name, "method": result["method"],
        "scenario": result.get("scenario", name),
        "valuation_date": doc["valuation_date"],
        "target_date": target, "frozen_at": timestamp,
        "record_class": ("contemporaneous_record" if recorded.date() == valuation_date
                         else "retrospective_reconstruction"),
        "reference_price_usd": market,
        "intrinsic_price_usd": intrinsic,
        "forecast_metrics": forecast_metrics(doc, output, result, name),
        "original_input": doc, "original_input_sha256": digest(doc),
        "original_result": result, "original_result_sha256": digest(result),
        "capital": output.get("capital"),
        "model_warnings": output.get("warnings", []),
    }
    item["snapshot_sha256"] = digest(item)
    return item


def verify(snapshot):
    snap = mapping(snapshot, "snapshot")
    if snap.get("schema_version") != 3 or snap.get("kind") != "valuation_snapshot":
        fail("snapshot", "unsupported snapshot version/kind")
    sealed = dict(snap)
    expected = sealed.pop("snapshot_sha256", None)
    if expected != digest(sealed):
        fail("snapshot.snapshot_sha256", "snapshot contents changed after freeze")
    original = required(snap, "original_input", "snapshot")
    if digest(original) != snap.get("original_input_sha256"):
        fail("snapshot.original_input_sha256", "frozen source input changed")
    output, result, target = model_result(original, snap["name"])
    if digest(result) != snap.get("original_result_sha256"):
        fail("snapshot.original_result_sha256", "model output has drifted; version pin / replay required")
    if snap["target_date"] != target or result["method"] != snap["method"]:
        fail("snapshot", "method or horizon differs from recomputed source")
    current = result["present_value_per_share_usd"]
    if not math.isclose(current, snap["intrinsic_price_usd"], rel_tol=1e-9, abs_tol=1e-6):
        fail("snapshot.intrinsic_price_usd", "frozen valuation does not match replay")
    expected_price = output["price"] if snap["model_version"] == 1 else output["reference_price_usd"]
    if not math.isclose(expected_price, snap["reference_price_usd"], rel_tol=1e-10):
        fail("snapshot.reference_price_usd", "price differs from replayed input")
    if snap["forecast_metrics"] != forecast_metrics(original, output, result, snap["name"]):
        fail("snapshot.forecast_metrics", "forecast metrics differ from sealed model")
    return snap


def price_observations(doc, cutoff):
    found = {}
    for i, item in enumerate(required(doc, "prices", "observations")):
        q = f"observations.prices[{i}]"
        fields(item, {"observed_on", "price"}, q)
        observed_on = day(required(item, "observed_on", q), q + ".observed_on")
        if observed_on > cutoff or observed_on in found:
            fail(q, "future or duplicate observation date")
        price, asof = number_fact(required(item, "price", q), q + ".price", cutoff, basis="market", positive=True)
        if asof != observed_on:
            fail(q, "market price timestamp must equal observation date")
        found[observed_on] = price
    return found


def actual_observations(doc, cutoff):
    actuals = {}
    for i, item in enumerate(required(doc, "actuals", "observations")):
        q = f"observations.actuals[{i}]"
        fields(item, {"period_end", "published_on", "metrics"}, q)
        period = day(required(item, "period_end", q), q + ".period_end")
        published = day(required(item, "published_on", q), q + ".published_on")
        if published > cutoff or published < period:
            fail(q, "financial results must be published after period close and by evaluation cutoff")
        if period in actuals:
            fail(q, "only one verified actual filing for a given period allowed")
        metrics = mapping(required(item, "metrics", q), q + ".metrics")
        if not metrics:
            fail(q, "at least one actual metric required")
        values = {}
        for k, metric in metrics.items():
            if k not in ("revenue_m", "net_income_m", "ebit_m", "fcff_m", "diluted_shares_m"):
                fail(q + ".metrics", "unrecognized actual metric " + k)
            value, observed = number_fact(metric, q + ".metrics." + k, cutoff, basis="filing")
            if observed != published:
                fail(q + ".metrics." + k, "input as_of must be the filing publication date")
            values[k] = value
        actuals[period] = {"published_on": published.isoformat(), "metrics": values}
    return actuals


def get_observations(doc):
    doc = mapping(doc, "observations")
    fields(doc, {"schema_version", "ticker", "evaluation_date", "prices", "actuals"}, "observations")
    if doc.get("schema_version") != 3:
        fail("observations.schema_version", "expected schema_version=3")
    cutoff = day(required(doc, "evaluation_date", "observations"), "observations.evaluation_date")
    ticker = required(doc, "ticker", "observations")
    if not isinstance(ticker, str) or not ticker.strip():
        fail("observations.ticker", "expected nonempty ticker")
    prices = price_observations(doc, cutoff)
    actuals = actual_observations(doc, cutoff)
    return ticker, cutoff, prices, actuals


def score(snapshot, cutoff, prices, actuals):
    asof = day(snapshot["valuation_date"], "snapshot.valuation_date")
    if cutoff < asof:
        fail("evaluation_date", "evaluation precedes an original valuation date")
    target_raw = snapshot["target_date"]
    if target_raw is None:
        return {"status": "unscorable_horizon", "model_name": snapshot["name"],
                "valuation_date": str(asof), "reason": "mixed SOTP segment horizons; no single forecast maturity"}
    target = day(target_raw, "snapshot.target_date")
    data = {"model_name": snapshot["name"], "method": snapshot["method"],
            "valuation_date": str(asof), "target_date": str(target),
            "record_class": snapshot["record_class"],
            "original_reference_price_usd": snapshot["reference_price_usd"],
            "original_conditional_value_usd": snapshot["intrinsic_price_usd"]}
    if target > cutoff:
        return {**data, "status": "open", "reason": "target period has not ended; exclude from accuracy sample"}
    dates = [d for d in prices if target <= d <= min(cutoff, target.fromordinal(target.toordinal()+7))]
    if dates:
        d = min(dates)
        observed_price = prices[d]
        data["price_diagnostic"] = {
            "observed_on": str(d), "exit_price_usd": observed_price,
            "observed_price_return": observed_price/snapshot["reference_price_usd"]-1,
            "model_gap_to_exit_price_usd": snapshot["intrinsic_price_usd"]-observed_price,
            "note": "Market price vs intrinsic estimate is a diagnostic, not proof of misvaluation or trading alpha."}
    else:
        data["price_diagnostic"] = None
    actual = actuals.get(target)
    comparisons = {}
    if actual is not None:
        for key, pred in snapshot["forecast_metrics"].items():
            if key in actual["metrics"]:
                real = actual["metrics"][key]
                comparisons[key] = {"forecast": pred, "actual": real,
                                    "signed_error": pred-real,
                                    "absolute_error": abs(pred-real),
                                    "absolute_percentage_error": None if real == 0 else abs(pred-real)/abs(real)}
    data["fundamental_diagnostics"] = comparisons
    data["actuals_published_on"] = None if actual is None else actual["published_on"]
    data["status"] = "matured_scored" if comparisons or data["price_diagnostic"] else "matured_missing_evidence"
    return data


def shapley(start, end, function):
    """Exact symmetric average contribution; order independent, no residual fudge."""
    names = list(start)
    if set(names) != set(end):
        fail("attribution", "factor definitions changed between vintages")
    n = len(names)
    if n > 12:
        fail("attribution", "too many factors for exact Shapley")
    factorial = math.factorial
    weight = [factorial(k)*factorial(n-k-1)/factorial(n) for k in range(n)]
    values = {}
    for mask in range(1 << n):
        args = {key: (end[key] if mask & (1 << i) else start[key]) for i, key in enumerate(names)}
        values[mask] = function(args)
    contributions = {}
    for i, key in enumerate(names):
        contribution = 0.0
        for mask in range(1 << n):
            if mask & (1 << i):
                continue
            contribution += weight[mask.bit_count()] * (values[mask | (1 << i)]-values[mask])
        contributions[key] = contribution
    return {"factors_usd_per_share": contributions,
            "start_model_value": values[0], "end_model_value": values[(1 << n)-1],
            "delta_model_value": values[(1 << n)-1]-values[0],
            "rounding_residual": (values[(1 << n)-1]-values[0]) - sum(contributions.values())}


def factors(snapshot):
    method = snapshot["method"]
    result = snapshot["original_result"]
    cap = snapshot["capital"]
    if snapshot["model_version"] == 1:
        x = result["inputs"]
        if method == "equity_pe":
            f = {"revenue": x["revenue_m"], "margin": x["net_margin"],
                 "multiple": x["exit_pe"], "shares": x["forecast_shares_m"],
                 "discount_rate": x["cost_of_equity"], "years": result["years"]}
            def calc(z):
                return z["revenue"]*z["margin"]*z["multiple"]/z["shares"]/(1+z["discount_rate"])**z["years"]
        elif method == "enterprise_ebit":
            f = {"revenue":x["revenue_m"],"margin":x["ebit_margin"],"multiple":x["exit_ev_ebit"],
                 "discount_rate":x["wacc"],"years":result["years"],"shares":cap["shares_m"],
                 "cash":cap["cash_m"],"debt":cap["debt_m"],"claims":cap["other_claims_m"]}
            def calc(z):
                ev=z["revenue"]*z["margin"]*z["multiple"]/(1+z["discount_rate"])**z["years"]
                return (ev+z["cash"]-z["debt"]-z["claims"])/z["shares"]
        else:
            f={"revenue":x["revenue_m"],"margin":x["ebit_margin"],"multiple":x["exit_ev_ebit"],
               "terminal_net_cash":x["terminal_net_cash_m"],"shares":x["forecast_shares_m"],
               "discount_rate":x["cost_of_equity"],"years":result["years"]}
            def calc(z):
                return (z["revenue"]*z["margin"]*z["multiple"]+z["terminal_net_cash"])/z["shares"]/(1+z["discount_rate"])**z["years"]
        return f, calc, "mechanical scenario revaluation; not causal market-price attribution"
    if method == "fcff_dcf":
        f={"explicit_fcff_pv":result["pv_explicit_fcff_m"],"terminal_pv":result["pv_terminal_m"],
           "net_claims":cap["cash_m"]-cap["debt_m"]-cap["other_claims_m"],"shares":cap["shares_m"]}
        def calc(z):
            return (z["explicit_fcff_pv"]+z["terminal_pv"]+z["net_claims"])/z["shares"]
        return f, calc, "DCF PV components mix operating changes, discount shifts and passage of time; not separate causal drivers"
    if method == "sotp":
        f={"segments_pv":result["owned_segments_ev_m"],
           "corporate_cost":result["corporate_cost_pv_m"],
           "nonoperating_assets":result["nonoperating_assets_m"],
           "net_claims":cap["cash_m"]-cap["debt_m"]-cap["other_claims_m"],
           "shares":cap["shares_m"]}
        def calc(z):
            return (z["segments_pv"]-z["corporate_cost"]+z["nonoperating_assets"]+z["net_claims"])/z["shares"]
        return f, calc, "SOTP group attribution is accounting decomposition; segment boundary drift must be assessed separately"
    fail("attribution", "unsupported intrinsic valuation method")


def compare_vintages(first, second):
    a, b = verify(first), verify(second)
    keys = ("ticker", "name", "method", "scenario", "model_version", "target_date")
    if any(a[k] != b[k] for k in keys):
        fail("attribution", "vintage models, scenario or target horizon are not comparable")
    if day(a["valuation_date"], "first.date") >= day(b["valuation_date"], "second.date"):
        fail("attribution", "new snapshot must have strictly later valuation date")
    fa, fn, explanation = factors(a)
    fb, _, _ = factors(b)
    result = shapley(fa, fb, fn)
    for snap, key in ((a, "start_model_value"), (b, "end_model_value")):
        if not math.isclose(result[key], snap["intrinsic_price_usd"], abs_tol=2e-5, rel_tol=1e-7):
            fail("attribution", "reconstructed values differ from frozen model (method version mismatch)")
    delta_market = b["reference_price_usd"] - a["reference_price_usd"]
    result.update({
        "ticker": a["ticker"], "name": a["name"], "method": a["method"],
        "from_valuation_date": a["valuation_date"], "to_valuation_date": b["valuation_date"],
        "reference_price_change_usd": delta_market,
        "market_change_minus_model_revision_usd": delta_market-result["delta_model_value"],
        "explanation": explanation,
        "caveat": "The unexplained price-versus-valuation gap is NOT proof of sentiment, alpha or market irrationality."})
    return result


def evaluate_history(snapshots, observed, *, compare=False):
    ticker, cutoff, prices, actuals = get_observations(observed)
    if not isinstance(snapshots, list) or not snapshots:
        fail("snapshots", "need nonempty array")
    checked = [verify(x) for x in snapshots]
    for snap in checked:
        if snap["ticker"] != ticker:
            fail("snapshots", "all snapshots must match observations ticker")
    ids = [(s["name"], s["valuation_date"]) for s in checked]
    if len(ids) != len(set(ids)):
        fail("snapshots", "duplicate model snapshot at same valuation date")
    evaluated = [score(s, cutoff, prices, actuals) for s in checked]
    errors = {}
    for e in evaluated:
        for metric, row in e.get("fundamental_diagnostics", {}).items():
            errors.setdefault(metric, []).append(row)
    calibration = {}
    for key, rows in errors.items():
        calibration[key] = {
            "sample_size": len(rows),
            "mean_absolute_error": statistics.mean(v["absolute_error"] for v in rows),
            "mean_signed_error_forecast_minus_actual": statistics.mean(v["signed_error"] for v in rows),
            "wape": None if sum(abs(v["actual"]) for v in rows)==0 else (
                sum(v["absolute_error"] for v in rows)/sum(abs(v["actual"]) for v in rows)),
            "note": "Retrospective reconstructions, overlapping target dates and selection bias invalidate out-of-sample performance claims.",
        }
    revisions = []
    if compare:
        groups = {}
        for snap in checked:
            key=(snap["ticker"],snap["name"],snap["method"],snap["scenario"],snap["model_version"],snap["target_date"])
            groups.setdefault(key, []).append(snap)
        for group in groups.values():
            ordered=sorted(group,key=lambda v:v["valuation_date"])
            for older,newer in zip(ordered,ordered[1:]):
                revisions.append(compare_vintages(older,newer))
    return {
        "schema_version":3, "kind":"valuation_review", "ticker":ticker,
        "evaluation_date":str(cutoff), "total_snapshots":len(checked),
        "statuses":{s:sum(e["status"]==s for e in evaluated) for s in sorted(set(e["status"] for e in evaluated))},
        "vintages":evaluated, "fundamental_calibration":calibration,
        "revision_attribution":revisions,
        "warnings":[
            "A fair-value estimate is not a promised market price at the forecast date.",
            "No transaction costs, dividends, delisting returns, risk adjustment, survivorship corrections or investable trading simulation included.",
            "Backdated research created after its valuation date is labelled retrospective, not an original out-of-sample forecast.",
            "Missing quotes and unpublished financial results are excluded and their absence is visible; do not substitute fabricated actuals.",
            "Shapley attribution explains model revaluation mechanically, NOT observed share-price causes.",
        ]}


def load(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream, parse_constant=lambda s: fail("json", "invalid constant "+s))


def write(value, output):
    serialized = json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+"\n"
    if output:
        Path(output).write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    cmd=parser.add_subparsers(dest="command",required=True)
    freezing=cmd.add_parser("freeze",help="Replay P0/P1 original input and create sealed snapshot")
    freezing.add_argument("input",type=Path)
    freezing.add_argument("--name",required=True,help="P0 case name or P1 analysis name")
    freezing.add_argument("-o","--output",type=Path)
    reviewing=cmd.add_parser("review",help="Score matured vintages against dated observations")
    reviewing.add_argument("--observations",required=True,type=Path)
    reviewing.add_argument("snapshots",nargs="+",type=Path)
    reviewing.add_argument("--compare",action="store_true",help="Attribute matched vintage model revisions")
    reviewing.add_argument("-o","--output",type=Path)
    args=parser.parse_args(argv)
    try:
        if args.command=="freeze":
            result=freeze(load(args.input),args.name)
        else:
            result=evaluate_history([load(p) for p in args.snapshots], load(args.observations),compare=args.compare)
        write(result,args.output)
    except (OSError,ValueError,KeyError,TypeError,OverflowError) as error:
        print("P2 REVIEW BLOCKED: "+str(error),file=sys.stderr)
        return 2
    return 0


if __name__=="__main__":
    raise SystemExit(main())
