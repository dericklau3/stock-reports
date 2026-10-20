"""P0 numerical and accounting-identity regression tests; no network or third-party deps."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("valuation_engine", ROOT / "valuation_engine.py")
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)

ASOF = "2026-10-20"
URL = "https://example.org/original-report"


def source(value, basis="analyst", as_of=ASOF):
    item = {"value": value, "basis": basis, "as_of": as_of}
    if basis == "analyst":
        item["rationale"] = "Illustrative research scenario, not a fact or market forecast."
    else:
        item["source_url"] = URL
    return item


def scenario(method, **inputs):
    return {"name": "base", "method": method, "target_date": "2027-10-20",
            "interim_distributions": "excluded", "inputs": {k: source(v) for k, v in inputs.items()}}


def base(case):
    return {"schema_version": 1, "ticker": "DEMO", "valuation_date": ASOF,
            "currency": "USD", "price": source(100, "market", "2026-10-19"), "cases": [case]}


def capital(shares=100, cash=50, debt=20, claims=5, as_of=ASOF):
    return {"bridge_as_of": ASOF, "shares_m": source(shares, as_of=as_of),
            "cash_m": source(cash, as_of=as_of), "debt_m": source(debt, as_of=as_of),
            "other_claims_m": source(claims, as_of=as_of)}


class ValuationTests(unittest.TestCase):
    def test_equity_pe_uses_equity_discount_and_forecast_shares(self):
        data = base(scenario("equity_pe", revenue_m=1000, net_margin=.20,
                             forecast_shares_m=100, exit_pe=20, cost_of_equity=.1))
        result = engine.validated_input(data)["results"][0]
        self.assertAlmostEqual(result["present_value_per_share_usd"],
                               40 / (1.1 ** (365 / 365.25)), places=5)
        self.assertEqual(result["terminal_price_usd"], 40)

    def test_enterprise_wacc_bridge_before_current_shares(self):
        data = base(scenario("enterprise_ebit", revenue_m=1000, ebit_margin=.20,
                             exit_ev_ebit=10, wacc=.1))
        data["capital"] = capital()
        r = engine.validated_input(data)["results"][0]
        expected = (2000 / (1.1 ** (365 / 365.25)) + 50 - 20 - 5) / 100
        self.assertAlmostEqual(r["present_value_per_share_usd"], expected, places=5)
        self.assertIsNone(r["terminal_price_usd"])

    def test_future_equity_bridge_discounted_together(self):
        data = base(scenario("equity_exit_ebit", revenue_m=1000, ebit_margin=.2,
                             exit_ev_ebit=10, terminal_net_cash_m=-200,
                             forecast_shares_m=100, cost_of_equity=.1))
        r = engine.validated_input(data)["results"][0]
        self.assertAlmostEqual(r["present_value_per_share_usd"],
                               18 / (1.1 ** (365 / 365.25)), places=5)
        self.assertEqual(r["terminal_price_usd"], 18)

    def test_enterprise_rejects_equity_rate_or_future_shares(self):
        data = base(scenario("enterprise_ebit", revenue_m=1000, ebit_margin=.2,
                             exit_ev_ebit=10, cost_of_equity=.1))
        data["capital"] = capital()
        with self.assertRaisesRegex(engine.ValidationError, "unknown fields"):
            engine.validated_input(data)
        data["cases"][0]["inputs"].pop("cost_of_equity")
        data["cases"][0]["inputs"]["wacc"] = source(.1)
        data["cases"][0]["inputs"]["forecast_shares_m"] = source(120)
        with self.assertRaisesRegex(engine.ValidationError, "unknown fields"):
            engine.validated_input(data)

    def test_bridge_requires_same_date_and_stale_disclosure(self):
        data = base(scenario("enterprise_ebit", revenue_m=1000, ebit_margin=.2,
                             exit_ev_ebit=10, wacc=.1))
        data["capital"] = capital()
        data["capital"]["bridge_as_of"] = "2026-06-30"
        with self.assertRaisesRegex(engine.ValidationError, "MUST use the valuation date"):
            engine.validated_input(data)
        data["capital"] = capital(as_of="2026-06-30")
        with self.assertRaisesRegex(engine.ValidationError, "reconciliation_note"):
            engine.validated_input(data)
        data["capital"]["reconciliation_note"] = "Interim cash and shares unverified, use only as a provisional stress-test bridge."
        result = engine.validated_input(data)
        self.assertEqual(result["capital_status"], "provisional")

    def test_no_unsourced_market_data_or_undocumented_analyst_guesses(self):
        data = base(scenario("equity_pe", revenue_m=1000, net_margin=.2,
                             forecast_shares_m=100, exit_pe=20, cost_of_equity=.1))
        data["cases"][0]["inputs"]["exit_pe"].pop("rationale")
        with self.assertRaisesRegex(engine.ValidationError, "rationale"):
            engine.validated_input(data)
        data["cases"][0]["inputs"]["exit_pe"] = source(20, "consensus")
        data["cases"][0]["inputs"]["exit_pe"].pop("source_url")
        with self.assertRaisesRegex(engine.ValidationError, "source_url"):
            engine.validated_input(data)

    def test_stale_price_look_ahead_and_wrong_units_rejected(self):
        data = base(scenario("equity_pe", revenue_m=1000, net_margin=.2,
                             forecast_shares_m=100, exit_pe=20, cost_of_equity=.1))
        data["price"]["as_of"] = "2026-10-01"
        with self.assertRaisesRegex(engine.ValidationError, "older than 7"):
            engine.validated_input(data)
        data["price"]["as_of"] = "2026-10-21"
        with self.assertRaisesRegex(engine.ValidationError, "look-ahead"):
            engine.validated_input(data)
        data["price"]["as_of"] = "2026-10-19"
        data["currency"] = "JPY"
        with self.assertRaisesRegex(engine.ValidationError, "USD only"):
            engine.validated_input(data)

    def test_negative_earnings_cannot_have_positive_pe_target(self):
        data = base(scenario("equity_pe", revenue_m=1000, net_margin=-.1,
                             forecast_shares_m=100, exit_pe=20, cost_of_equity=.1))
        with self.assertRaisesRegex(engine.ValidationError, "positive"):
            engine.validated_input(data)

    def test_nonfinite_booleans_and_negative_bridge_rejected(self):
        data = base(scenario("equity_pe", revenue_m=1000, net_margin=.2,
                             forecast_shares_m=100, exit_pe=20, cost_of_equity=.1))
        data["cases"][0]["inputs"]["exit_pe"]["value"] = True
        with self.assertRaisesRegex(engine.ValidationError, "JSON number"):
            engine.validated_input(data)
        data["cases"][0]["inputs"]["exit_pe"]["value"] = float("inf")
        with self.assertRaisesRegex(engine.ValidationError, "finite"):
            engine.validated_input(data)
        data["cases"][0]["inputs"]["exit_pe"]["value"] = 20
        data["capital"] = capital(debt=-1)
        with self.assertRaisesRegex(engine.ValidationError, "nonnegative"):
            engine.validated_input(data)

    def test_cli_fixture_roundtrip(self):
        fixture = ROOT / "examples" / "valuation-input.example.json"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            cmd = [sys.executable, str(ROOT / "valuation_engine.py"), str(fixture), "--output", str(output)]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(len(result["results"]), 3)
            self.assertEqual(result["ticker"], "DEMO")
            self.assertEqual(result["capital_status"], "provisional")


if __name__ == "__main__":
    unittest.main(verbosity=2)
