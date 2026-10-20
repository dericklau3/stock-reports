"""P2 snapshot immutability, point-in-time guardrails and mathematical review tests."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from valuation_engine import ValidationError
from valuation_p2 import freeze, verify, compare_vintages, evaluate_history, shapley

CAPTURE="2026-10-20T09:00:00+00:00"
URL="https://example.org/dated-market-or-official-filing"

def f(value,basis="analyst",as_of="2025-01-01"):
    if basis=="analyst":
        return {"value":value,"basis":basis,"as_of":as_of,
                "rationale":"Illustrative retrospective research hypothesis; NOT a historical recommendation."}
    return {"value":value,"basis":basis,"as_of":as_of,"source_url":URL}

def base(day="2025-01-01",target="2027-01-01", revenue=1000, rate=.12, price=15, method="equity_pe"):
    price_day=day
    ins={"revenue_m":f(revenue,as_of=day)}
    if method=="equity_pe":
        ins.update(net_margin=f(.2,as_of=day),forecast_shares_m=f(100,as_of=day),
                   exit_pe=f(12,as_of=day),cost_of_equity=f(rate,as_of=day))
    elif method=="enterprise_ebit":
        ins.update(ebit_margin=f(.2,as_of=day),exit_ev_ebit=f(12,as_of=day),
                   wacc=f(rate,as_of=day))
    else:
        ins.update(ebit_margin=f(.2,as_of=day),exit_ev_ebit=f(12,as_of=day),
                   terminal_net_cash_m=f(-100,as_of=day),
                   forecast_shares_m=f(100,as_of=day),cost_of_equity=f(rate,as_of=day))
    out={"schema_version":1,"ticker":"DEMO","valuation_date":day,"currency":"USD",
        "price":f(price,"market",price_day),
        "cases":[{"name":"base","method":method,"target_date":target,
                  "interim_distributions":"excluded","inputs":ins}]}
    if method=="enterprise_ebit":
        out["capital"]={"bridge_as_of":day, "shares_m":f(100,as_of=day),
                        "cash_m":f(50,as_of=day),"debt_m":f(20,as_of=day),
                        "other_claims_m":f(5,as_of=day)}
    return out

def p1(day="2025-01-01", margin=.2):
    ends=["2026-01-01","2027-01-01","2028-01-01","2029-01-01","2030-01-01"]
    years=[{"end_date":d,"revenue_m":f(1000+200*i,as_of=day),
            "ebit_margin":f(margin,as_of=day),"cash_tax_rate":f(.21,as_of=day),
            "d_and_a_m":f(20,as_of=day),"capex_m":f(30,as_of=day),
            "delta_nwc_m":f(10,as_of=day)} for i,d in enumerate(ends)]
    return {"schema_version":2,"ticker":"DEMO","valuation_date":day,"currency":"USD",
            "price":f(15,"market",day),
            "capital":{"bridge_as_of":day,"shares_m":f(100,as_of=day),
                       "cash_m":f(50,as_of=day),"debt_m":f(20,as_of=day),
                       "other_claims_m":f(5,as_of=day)},
            "analyses":[{"name":"base-dcf","scenario":"base","method":"fcff_dcf",
                         "justification":"This is an illustrative five-year synthetic scenario only; all numbers are fictional.",
                         "wacc":f(.1,as_of=day),"years":years,
                         "terminal":{"method":"perpetuity","growth":f(.02,as_of=day)}}]}

def observations(cutoff="2027-03-01"):
    return {"schema_version":3,"ticker":"DEMO","evaluation_date":cutoff,
            "prices":[{"observed_on":"2027-01-03","price":f(21,"market","2027-01-03")}],
            "actuals":[{"period_end":"2027-01-01","published_on":"2027-02-15",
                         "metrics":{"revenue_m":f(1100,"filing","2027-02-15"),
                                    "net_income_m":f(180,"filing","2027-02-15"),
                                    "diluted_shares_m":f(105,"filing","2027-02-15")}}]}

class P2Tests(unittest.TestCase):
    def test_p0_snapshot_is_replayed_and_sealed(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        self.assertEqual(snap["record_class"],"retrospective_reconstruction")
        self.assertEqual(verify(snap)["snapshot_sha256"],snap["snapshot_sha256"])
        self.assertEqual(snap["forecast_metrics"]["net_income_m"],200)

    def test_snapshot_mutation_detected(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        snap["intrinsic_price_usd"]+=1
        with self.assertRaisesRegex(ValidationError,"changed after freeze"):
            verify(snap)

    def test_snapshot_input_lookahead_blocked(self):
        doc=base()
        doc["cases"][0]["inputs"]["revenue_m"]["as_of"]="2025-01-02"
        with self.assertRaisesRegex(ValidationError,"look-ahead"):
            freeze(doc,"base",captured_at=CAPTURE)

    def test_freeze_refuses_fake_earlier_capture(self):
        with self.assertRaisesRegex(ValidationError,"cannot precede"):
            freeze(base(),"base",captured_at="2024-12-31T10:00:00+00:00")

    def test_price_backtest_and_fundamental_metrics_are_separate(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        result=evaluate_history([snap],observations())
        v=result["vintages"][0]
        self.assertEqual(v["status"],"matured_scored")
        self.assertAlmostEqual(v["price_diagnostic"]["observed_price_return"],21/15-1)
        self.assertAlmostEqual(v["fundamental_diagnostics"]["revenue_m"]["signed_error"],-100)
        self.assertEqual(result["fundamental_calibration"]["revenue_m"]["sample_size"],1)
        self.assertAlmostEqual(result["fundamental_calibration"]["revenue_m"]["wape"],100/1100)
        self.assertIn("diagnostic",v["price_diagnostic"]["note"])

    def test_maturity_and_no_actuals_are_not_silent_success(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        doc={"schema_version":3,"ticker":"DEMO","evaluation_date":"2026-10-20",
             "prices":[],"actuals":[]}
        result=evaluate_history([snap],doc)
        self.assertEqual(result["statuses"],{"open":1})
        doc["evaluation_date"]="2027-03-01"
        self.assertEqual(evaluate_history([snap],doc)["statuses"],{"matured_missing_evidence":1})

    def test_price_timing_not_future_leaked(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        doc=observations()
        doc["evaluation_date"]="2027-01-02"
        with self.assertRaisesRegex(ValidationError,"future"):
            evaluate_history([snap],doc)

    def test_actual_publication_lag_is_guarded(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        doc=observations()
        doc["evaluation_date"]="2027-02-01"
        doc["prices"]=[]
        with self.assertRaisesRegex(ValidationError,"published"):
            evaluate_history([snap],doc)
        doc=observations()
        doc["actuals"][0]["metrics"]["revenue_m"]["as_of"]="2027-03-01"
        with self.assertRaisesRegex(ValidationError,"publication"):
            evaluate_history([snap],doc)

    def test_duplicate_dates_or_mixed_ticker_rejected(self):
        snap=freeze(base(),"base",captured_at=CAPTURE)
        with self.assertRaisesRegex(ValidationError,"duplicate model snapshot"):
            evaluate_history([snap,snap],observations())
        doc=observations()
        doc["ticker"]="OTHER"
        with self.assertRaisesRegex(ValidationError,"match"):
            evaluate_history([snap],doc)

    def test_equity_pe_shapley_exact_and_market_gap_distinct(self):
        old=freeze(base(),"base",captured_at=CAPTURE)
        new=freeze(base(day="2025-02-01",revenue=1200,rate=.1,price=17),"base",captured_at=CAPTURE)
        result=compare_vintages(old,new)
        self.assertAlmostEqual(sum(result["factors_usd_per_share"].values()),
                               result["delta_model_value"],places=9)
        self.assertGreater(result["factors_usd_per_share"]["revenue"],0)
        self.assertEqual(result["reference_price_change_usd"],2)
        self.assertAlmostEqual(result["market_change_minus_model_revision_usd"],
                               2-result["delta_model_value"])

    def test_shapley_order_symmetry(self):
        a={"x":1.,"y":2.}
        b={"x":3.,"y":5.}
        r=shapley(a,b,lambda k:k["x"]*k["y"])
        self.assertAlmostEqual(sum(r["factors_usd_per_share"].values()),13.)

    def test_changed_target_horizon_refused(self):
        old=freeze(base(),"base",captured_at=CAPTURE)
        new=freeze(base(day="2025-02-01",target="2028-01-01"),"base",captured_at=CAPTURE)
        with self.assertRaisesRegex(ValidationError,"not comparable"):
            compare_vintages(old,new)

    def test_p1_dcf_replay_and_aggregate_attribution(self):
        old=freeze(p1(),"base-dcf",captured_at=CAPTURE)
        new=freeze(p1(day="2025-02-01",margin=.22),"base-dcf",captured_at=CAPTURE)
        self.assertEqual(verify(old)["method"],"fcff_dcf")
        result=compare_vintages(old,new)
        self.assertAlmostEqual(sum(result["factors_usd_per_share"].values()),
                               result["delta_model_value"],places=8)
        self.assertIn("terminal_pv",result["factors_usd_per_share"])

    def test_unscored_p1_dcf_future(self):
        snap=freeze(p1(),"base-dcf",captured_at=CAPTURE)
        result=evaluate_history([snap],observations(cutoff="2027-03-01"))
        self.assertEqual(result["statuses"],{"open":1})

    def test_nonfinite_actual_disallowed(self):
        doc=observations()
        doc["actuals"][0]["metrics"]["revenue_m"]["value"]=float("nan")
        snap=freeze(base(),"base",captured_at=CAPTURE)
        with self.assertRaisesRegex(ValidationError,"finite"):
            evaluate_history([snap],doc)

    def test_cli_freeze_and_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            basepath=Path(tmp)
            model=base()
            (basepath/"model.json").write_text(json.dumps(model))
            (basepath/"observations.json").write_text(json.dumps(observations()))
            command=[sys.executable,str(ROOT/"valuation_p2.py"),"freeze",
                     str(basepath/"model.json"),"--name","base","-o",str(basepath/"snapshot.json")]
            run=subprocess.run(command,capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            second=[sys.executable,str(ROOT/"valuation_p2.py"),"review",
                    "--observations",str(basepath/"observations.json"),
                    str(basepath/"snapshot.json"),"-o",str(basepath/"review.json")]
            done=subprocess.run(second,capture_output=True,text=True)
            self.assertEqual(done.returncode,0,done.stderr)
            review=json.loads((basepath/"review.json").read_text())
            self.assertEqual(review["statuses"],{"matured_scored":1})


if __name__=="__main__":
    unittest.main(verbosity=2)
