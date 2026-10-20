#!/usr/bin/env python3
"""Recompute LMND valuation. Inputs contain dated facts and explicit hypotheses.

Use equity P/S, so no second cash addback or financing-debt deduction is made.
Capital intensity and mature-margin outputs are stress tests, not issuer guidance.
"""
from pathlib import Path
from datetime import date
from statistics import mean
import json
import math

BASE = Path(__file__).resolve().parent
INPUT = BASE / "2026-10-20-valuation-inputs.json"
OUTPUT = BASE / "2026-10-20-valuation-results.json"

def calculate(d):
    start = date.fromisoformat(d["valuation_date"])
    end = date.fromisoformat(d["target_date"])
    years = (end - start).days / 365.25
    discount = (1 + d["equity_discount_rate"]) ** years
    price = d["quote"]["price"]
    shares = d["shares"]["latest_cover_actual_millions"]
    a = d["actual_financials"]
    guide = d["management_guidance_July29"]
    cap = price * shares
    base = d["scenarios"]["base"]
    mid_ps = mean(base["equity_price_to_revenue"])
    mid_target = base["revenue"] * mid_ps / base["future_economic_shares_millions"]
    result = {
        "valuation_date": d["valuation_date"],
        "quote": d["quote"],
        "target_date": d["target_date"],
        "years": years,
        "discount_factor": discount,
        "reference_market_cap_USD_millions": cap,
        "share_denominator_date": d["shares"]["latest_cover_date"],
        "P_TTM_revenue": cap / a["TTM_revenue"],
        "P_FY2026_guidance_mid_revenue": cap / mean(guide["FY2026_revenue"]),
        "P_current_IFP": cap / a["Q2_IFP"],
        "P_FY2026_end_guidance_mid_IFP": cap / mean(guide["FY2026_end_IFP"]),
        "P_book": cap / a["equity"],
        "book_value_per_reference_share": a["equity"] / shares,
        "H1_SBC_to_revenue": a["H1_SBC"] / 552.4,
        "FY2026_SBC_to_guidance_revenue": guide["FY2026_SBC"] / mean(guide["FY2026_revenue"]),
        "H1_ordinary_FCF": a["H1_OCF"] - a["H1_cash_capex_PPE"],
        "H1_net_financing": a["H1_financing_draws"] - a["H1_financing_repayments"],
        "Q2_GLR_sum": sum(a[k] for k in ["Q2_attritional_ratio", "Q2_CAT_exPPD_ratio", "Q2_LAE_exPPD_ratio", "Q2_favorable_PPD_ratio"]),
        "Q2_GLR_without_PPD_proxy": a["Q2_gross_loss_ratio"] - a["Q2_favorable_PPD_ratio"],
        "Q2_2025_GLR_without_PPD_proxy": a["Q2_2025_gross_loss_ratio"] - a["Q2_2025_favorable_PPD_ratio"],
        "scenarios": {},
    }
    intensity = a["required_regulatory_surplus_approximately"] / a["Q2_IFP"]
    for name, s in d["scenarios"].items():
        terminal = [s["revenue"] * x / s["future_economic_shares_millions"] for x in s["equity_price_to_revenue"]]
        present = [x / discount for x in terminal]
        pe = [x / margin for x in s["equity_price_to_revenue"] for margin in s["assumed_mature_net_margin_for_crosscheck"]]
        result["scenarios"][name] = {
            "future_equity_value_USD_millions": [s["revenue"] * x for x in s["equity_price_to_revenue"]],
            "future_economic_shares_millions": s["future_economic_shares_millions"],
            "terminal_per_share_USD": terminal,
            "present_per_share_USD": present,
            "present_price_difference": [x / price - 1 for x in present],
            "implied_PE_given_assumed_after_SBC_net_margin_range": [min(pe), max(pe)],
            "illustrative_IFP_2026_to_2028_CAGR": (s["illustrative_end_IFP"] / mean(guide["FY2026_end_IFP"])) ** 0.5 - 1,
            "illustrative_required_capital_if_unchanged_current_intensity": intensity * s["illustrative_end_IFP"],
            "increment_to_current_required_capital_under_that_stress": intensity * s["illustrative_end_IFP"] - a["required_regulatory_surplus_approximately"],
            "capital_warning": d["capital_stress"],
        }
    reverse_target_equity = price * discount * base["future_economic_shares_millions"]
    result["base_midpoint_present_USD"] = mid_target / discount
    result["reverse"] = {
        "FY2028_revenue_at_base_mid_PS": reverse_target_equity / mid_ps,
        "FY2028_equity_at_current_price_and_base_share_discount_assumptions": reverse_target_equity,
        "net_income_required_at_terminal_PE25": reverse_target_equity / 25,
        "required_net_margin_at_revenue2100_PE25": reverse_target_equity / 25 / base["revenue"],
        "warning": "At a different terminal multiple, shares, horizon or required return, the reverse requirement changes. Not a current EPS consensus or probability.",
    }
    result["sensitivities"] = {
        "base_revenue_minus20pct": base["revenue"] * 0.8 * mid_ps / base["future_economic_shares_millions"] / discount,
        "base_mid_PS_to2x": base["revenue"] * 2 / base["future_economic_shares_millions"] / discount,
        "base_shares95M": base["revenue"] * mid_ps / 95 / discount,
        "base_shares100M": base["revenue"] * mid_ps / 100 / discount,
        "bear_shares110M_low_PS": d["scenarios"]["bear"]["revenue"] * d["scenarios"]["bear"]["equity_price_to_revenue"][0] / 110 / discount,
        "base_discount18pct": mid_target / (1.18 ** years),
    }
    previous = d["previous_baseline"]
    result["previous_bridge"] = {
        "price_change_fraction": price / previous["price"] - 1,
        "reference_actual_share_change_millions": shares - previous["actual_shares_proxy_millions"],
        "hypothesis_changes": previous["hypothesis_bridge"],
    }
    checks = {
        "GLR_components_equal_reported": math.isclose(result["Q2_GLR_sum"], a["Q2_gross_loss_ratio"], abs_tol=1e-10),
        "adjusted_FCF_equals_ordinary_plus_borrowing": math.isclose(result["H1_ordinary_FCF"] + result["H1_net_financing"], a["H1_adjusted_FCF"], abs_tol=1e-9),
        "cash_investments_including_restricted": math.isclose(a["cash_unrestricted_label"] + a["cash_restricted"] + a["investments_balance_sheet"], a["cash_and_investments_including_restricted"], abs_tol=1e-8),
        "excluded_nominal_awards_sum": math.isclose(d["shares"]["excluded_options_millions"] + d["shares"]["excluded_unvested_restricted_millions"], d["shares"]["excluded_total_nominal_millions"], abs_tol=1e-9),
        "discount_is_future_and_positive": years > 0 and discount > 1,
        "all_present_values_discounted_once": all(math.isclose(p * discount, t) for s in result["scenarios"].values() for p, t in zip(s["present_per_share_USD"], s["terminal_per_share_USD"])),
    }
    assert all(checks.values()), checks
    result["checks"] = checks
    return result

if __name__ == "__main__":
    output = calculate(json.loads(INPUT.read_text()))
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(output, ensure_ascii=False, indent=2))
