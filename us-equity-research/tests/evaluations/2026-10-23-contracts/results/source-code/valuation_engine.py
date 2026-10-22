#!/usr/bin/env python3
"""Auditable, deterministic P0 valuation calculator (Python standard library only).

Input is JSON. All money is USD millions, all share counts millions, ratios decimals.
This is a terminal-multiple scenario calculator, NOT a multi-year DCF.
"""

from __future__ import annotations

import argparse
from datetime import date
import json
import math
from pathlib import Path
import sys


class ValidationError(ValueError):
    """Unsafe or incomplete valuation input; no target price should be published."""


def fail(path: str, reason: str) -> None:
    raise ValidationError(f"{path}: {reason}")


def required(obj: dict, field: str, path: str):
    if field not in obj:
        fail(f"{path}.{field}", "missing required field")
    return obj[field]


def mapping(value, path: str) -> dict:
    if not isinstance(value, dict):
        fail(path, "must be an object")
    return value


def day(raw, path: str) -> date:
    if not isinstance(raw, str):
        fail(path, "expected YYYY-MM-DD")
    try:
        result = date.fromisoformat(raw)
    except ValueError:
        fail(path, "invalid date; expected YYYY-MM-DD")
    if result.isoformat() != raw:
        fail(path, "expected YYYY-MM-DD without a time or timezone")
    return result


def number(value, path: str, *, positive: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        fail(path, "expected a JSON number")
    result = float(value)
    if not math.isfinite(result):
        fail(path, "must be finite")
    if positive and result <= 0:
        fail(path, "must be > 0")
    return result


def fact(node, path: str, valuation_date: date, *, positive: bool = False) -> tuple[float, date]:
    """Accept a number only with research date and verifiable provenance/assumption rationale."""
    item = mapping(node, path)
    value = number(required(item, "value", path), path + ".value", positive=positive)
    basis = required(item, "basis", path)
    if basis not in ("filing", "market", "guidance", "consensus", "analyst"):
        fail(path + ".basis", "use filing, market, guidance, consensus or analyst")
    as_of = day(required(item, "as_of", path), path + ".as_of")
    if as_of > valuation_date:
        fail(path + ".as_of", "look-ahead: source/assumption created after valuation date")
    if basis == "analyst":
        rationale = item.get("rationale")
        if not isinstance(rationale, str) or len(rationale.strip()) < 15:
            fail(path + ".rationale", "analyst assumption needs a specific rationale (>=15 chars)")
    else:
        url = item.get("source_url")
        if not isinstance(url, str) or not url.startswith("https://") or len(url) < 12:
            fail(path + ".source_url", "external numeric input needs an HTTPS evidence URL")
    return value, as_of


def fields(obj: dict, allowed: set[str], path: str) -> None:
    extra = set(obj) - allowed
    if extra:
        fail(path, "unknown fields: " + ", ".join(sorted(extra)))


def validated_input(raw: dict) -> dict:
    data = mapping(raw, "root")
    fields(data, {"schema_version", "ticker", "valuation_date", "currency", "price", "capital", "cases"}, "root")
    if required(data, "schema_version", "root") != 1:
        fail("schema_version", "only schema_version=1 supported")
    ticker = required(data, "ticker", "root")
    if not isinstance(ticker, str) or not ticker.strip():
        fail("ticker", "required nonempty ticker")
    if required(data, "currency", "root") != "USD":
        fail("currency", "P0 supports USD only; convert external currency and document rate")
    valuation_date = day(required(data, "valuation_date", "root"), "valuation_date")
    price, quoted_on = fact(required(data, "price", "root"), "price", valuation_date, positive=True)
    if (valuation_date - quoted_on).days > 7:
        fail("price.as_of", "reference quote is older than 7 calendar days")
    if data["price"]["basis"] != "market":
        fail("price.basis", "reference price must be market-sourced")

    capital_data = data.get("capital")
    capital = None
    warnings: list[str] = []
    if capital_data is not None:
        capital_data = mapping(capital_data, "capital")
        fields(capital_data, {"bridge_as_of", "reconciliation_note", "shares_m", "cash_m", "debt_m", "other_claims_m"}, "capital")
        cap_day = day(required(capital_data, "bridge_as_of", "capital"), "capital.bridge_as_of")
        if cap_day != valuation_date:
            fail("capital.bridge_as_of", "current enterprise-to-equity bridge MUST use the valuation date")
        capital = {"bridge_as_of": str(cap_day)}
        source_ages = []
        for key in ("shares_m", "cash_m", "debt_m", "other_claims_m"):
            val, observed = fact(required(capital_data, key, "capital"), "capital." + key, valuation_date)
            if val < 0 or (key == "shares_m" and val == 0):
                fail("capital." + key, "shares must be positive; balance components nonnegative")
            capital[key] = val
            source_ages.append((key, (valuation_date - observed).days))
        stale = [name for name, age in source_ages if age > 0]
        if stale:
            note = capital_data.get("reconciliation_note")
            if not isinstance(note, str) or len(note.strip()) < 20:
                fail("capital.reconciliation_note", "dated capital components need explicit as-of bridge/limitations (>=20 chars)")
            warnings.append("Capital bridge is provisional: underlying dated inputs " + ", ".join(stale) + "; independently verify interim financing, dilution and cash use.")
        elif capital_data.get("reconciliation_note"):
            warnings.append("Capital reconciliation note supplied; source links are recorded but NOT checked online.")

    cases = required(data, "cases", "root")
    if not isinstance(cases, list) or not cases:
        fail("cases", "must be a nonempty array")
    seen = set()
    results = []
    method_fields = {
        "equity_pe": {"revenue_m", "net_margin", "forecast_shares_m", "exit_pe", "cost_of_equity"},
        "enterprise_ebit": {"revenue_m", "ebit_margin", "exit_ev_ebit", "wacc"},
        "equity_exit_ebit": {"revenue_m", "ebit_margin", "exit_ev_ebit", "terminal_net_cash_m", "forecast_shares_m", "cost_of_equity"},
    }
    for index, node in enumerate(cases):
        path = f"cases[{index}]"
        item = mapping(node, path)
        fields(item, {"name", "method", "target_date", "interim_distributions", "inputs"}, path)
        name = required(item, "name", path)
        if not isinstance(name, str) or not name.strip() or name in seen:
            fail(path + ".name", "must be a unique, nonempty scenario name")
        seen.add(name)
        method = required(item, "method", path)
        if method not in method_fields:
            fail(path + ".method", "unknown method")
        target = day(required(item, "target_date", path), path + ".target_date")
        if target <= valuation_date:
            fail(path + ".target_date", "target must be after valuation date")
        if required(item, "interim_distributions", path) != "excluded":
            fail(path + ".interim_distributions", "P0 supports 'excluded' only; no dividends or buyback cash added separately")
        input_data = mapping(required(item, "inputs", path), path + ".inputs")
        expected = method_fields[method]
        fields(input_data, expected, path + ".inputs")
        if set(input_data) != expected:
            fail(path + ".inputs", "missing fields: " + ", ".join(sorted(expected - set(input_data))))
        x = {key: fact(input_data[key], path + ".inputs." + key, valuation_date)[0] for key in expected}
        if x["revenue_m"] <= 0:
            fail(path + ".inputs.revenue_m", "must be > 0")
        margin = x["net_margin" if method == "equity_pe" else "ebit_margin"]
        if not 0 < margin <= 1:
            fail(path + ".inputs.*margin", "P/E and EBIT multiple require positive, <=100% profitability; use another model for losses")
        multiple = x["exit_pe" if method == "equity_pe" else "exit_ev_ebit"]
        if multiple <= 0:
            fail(path + ".inputs.*multiple", "must be > 0")
        rate = x["wacc" if method == "enterprise_ebit" else "cost_of_equity"]
        if not 0 <= rate <= 1:
            fail(path + ".inputs.*rate", "discount rate must be in [0,1]")
        years = (target - valuation_date).days / 365.25
        discount_factor = (1 + rate) ** years
        if method == "equity_pe":
            if x["forecast_shares_m"] <= 0:
                fail(path + ".inputs.forecast_shares_m", "must be > 0")
            terminal_equity_m = x["revenue_m"] * margin * multiple
            terminal_price = terminal_equity_m / x["forecast_shares_m"]
            value = terminal_price / discount_factor
            bridge = "future after-interest equity income; no debt/cash bridge"
        elif method == "enterprise_ebit":
            if capital is None:
                fail(path, "enterprise_ebit requires an as-of valuation-date capital bridge")
            # WACC discounts enterprise (not shareholder) value. Current net claims are deducted ONCE.
            pv_enterprise_m = x["revenue_m"] * margin * multiple / discount_factor
            equity_today_m = pv_enterprise_m + capital["cash_m"] - capital["debt_m"] - capital["other_claims_m"]
            if equity_today_m <= 0:
                fail(path, "EV bridge yields nonpositive equity value; do not turn a negative residual into a target")
            value = equity_today_m / capital["shares_m"]
            terminal_price = None
            bridge = "discount enterprise at WACC; apply valuation-date claims; use valuation-date shares"
        else:
            if x["forecast_shares_m"] <= 0:
                fail(path + ".inputs.forecast_shares_m", "must be > 0")
            # Same target date for terminal net cash, EBIT multiple and future diluted shares.
            terminal_equity_m = x["revenue_m"] * margin * multiple + x["terminal_net_cash_m"]
            if terminal_equity_m <= 0:
                fail(path, "terminal equity value must be > 0")
            terminal_price = terminal_equity_m / x["forecast_shares_m"]
            value = terminal_price / discount_factor
            bridge = "terminal EV plus signed terminal net cash; discount equity at cost of equity"
        results.append({
            "name": name, "method": method, "target_date": str(target),
            "years": round(years, 8), "discount_factor": round(discount_factor, 8),
            "terminal_price_usd": None if terminal_price is None else round(terminal_price, 6),
            "present_value_per_share_usd": round(value, 6),
            "upside_vs_reference": round(value / price - 1, 8),
            "bridge_method": bridge,
            "inputs": x,
            "provenance": input_data,
        })
    warnings.append("Terminal-multiple stress tests, NOT full FCFF/FCFE DCF; no interim cash flows or shareholder distributions valued.")
    warnings.append("HTTPS sources and analyst rationales are required but NOT independently verified by this offline calculator.")
    return {
        "schema_version": 1, "ticker": ticker, "valuation_date": str(valuation_date),
        "currency": "USD", "units": "USD millions and million shares; per-share USD",
        "price": price, "price_as_of": str(quoted_on),
        "capital": capital, "capital_status": "provisional" if any(w.startswith("Capital bridge") for w in warnings) else ("as_of_declared" if capital else "not_needed"),
        "results": results, "warnings": warnings,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Version 1 audited scenario JSON")
    parser.add_argument("-o", "--output", type=Path, help="Write JSON output to file")
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as handle:
            payload = json.load(handle, parse_constant=lambda v: fail("json", f"invalid {v}"))
        result = validated_input(payload)
    except (OSError, ValueError) as error:
        print(f"VALUATION BLOCKED: {error}", file=sys.stderr)
        return 2
    serialized = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
