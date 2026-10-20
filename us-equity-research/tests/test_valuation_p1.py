"""P1 methodological and numerical regression tests. Standard library only."""
from __future__ import annotations
import copy
from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import valuation_p1 as model

ASOF='2026-10-20'


def x(value, basis='analyst', when=ASOF):
    r={'value':value,'basis':basis,'as_of':when}
    if basis=='analyst':
        r['rationale']='DEMO research assumption, not a market forecast; based on illustrative financial bridge.'
    else:
        r['source_url']='https://example.org/illustrative-report'
    return r


def meta(analyses=None,cap=True):
    doc={'schema_version':2,'ticker':'DEMO','currency':'USD','valuation_date':ASOF,
         'price':x(25,'market','2026-10-19'),'analyses':analyses or []}
    if cap:
        doc['capital']={'bridge_as_of':ASOF,'shares_m':x(100),
                        'cash_m':x(20),'debt_m':x(80),'other_claims_m':x(10)}
    return doc


def year(ending,margin=.2,capex=25, revenue=200):
    return {'end_date':ending,'revenue_m':x(revenue),'ebit_margin':x(margin),
            'cash_tax_rate':x(.25),'d_and_a_m':x(10),'capex_m':x(capex),'delta_nwc_m':x(5)}


def dcf():
    return {'name':'dcf_base','scenario':'base','method':'fcff_dcf','wacc':x(.1),
            'justification':'Five annual projection periods allow capital expenditures and reinvestment to be modeled explicitly.',
            'years':[year(f'{y}-10-20') for y in range(2027,2032)],
            'terminal':{'method':'perpetuity','growth':x(.02)}}


def fpe():
    return {'name':'pe_base','scenario':'base','method':'forward_pe','basis':'gaap','horizon':'FY1',
            'period_start':'2026-10-01','period_end':'2027-09-30','eps':x(2,'consensus','2026-10-19'),
            'peers':[{'ticker':'AAA','basis':'gaap','horizon':'FY1',
                       'period_start':'2026-10-01','period_end':'2027-09-30','price':x(30,'market','2026-10-19'),
                       'eps':x(2,'consensus','2026-10-19'),'comparable_reason':'Comparable growth and cash conversion, only a fixture.'},
                     {'ticker':'BBB','basis':'gaap','horizon':'FY1',
                       'period_start':'2026-10-01','period_end':'2027-09-30','price':x(60,'market','2026-10-19'),
                       'eps':x(3,'consensus','2026-10-19'),'comparable_reason':'Similar reinvestment intensity, only a fixture.'}]}


def sotp():
    return {'name':'sotp_base','scenario':'base','method':'sotp',
            'overlap_reconciliation':'Client and manufacturing segment contributions exclude all intercompany transfers; parent cash, claims and minority interests are only bridged once.',
            'corporate_cost_pv_m':x(40),'nonoperating_assets_m':x(5),
            'segments':[{'name':'legacy','kind':'current_ev','ownership':x(1),
                         'boundary_note':'Operating enterprise value does not include corporate assets or intercompany revenue.',
                         'enterprise_value_m':x(500)},
                        {'name':'growth','kind':'milestone_ev','ownership':x(1),
                         'boundary_note':'Independent future program; excludes legacy operations and corporate funding.',
                         'target_date':'2027-10-20','wacc':x(.1),'success_probability':x(.25),
                         'success_ev_m':x(600),'failure_ev_m':x(100)}]}


class P1ValuationTests(unittest.TestCase):
    def test_dcf_accounts_for_cash_taxes_and_reinvestment(self):
        r=model.evaluate(meta([dcf()]))['results'][0]
        self.assertAlmostEqual(r['years'][0]['ebit_m'],40)
        self.assertAlmostEqual(r['years'][0]['cash_taxes_m'],10)
        self.assertAlmostEqual(r['years'][0]['fcff_m'],10)
        # 5 equal cash flows of $10m, Gordon 2% WACC 10%, bridge net -$70m / 100m shares
        spans=[(date(y,10,20)-date(2026,10,20)).days/365.25 for y in range(2027,2032)]
        ev=sum(10/1.1**t for t in spans)+(10*1.02/.08)/1.1**spans[-1]
        self.assertAlmostEqual(r['present_value_per_share_usd'],(ev-70)/100)
        self.assertAlmostEqual(r['sensitivity'][1]['cells'][1]['per_share_usd'],r['present_value_per_share_usd'])
        self.assertAlmostEqual(r['reverse']['implied_market_ev_m'],2570)

    def test_negative_ebit_does_not_create_tax_refund(self):
        d=dcf();d['years'][0]['ebit_margin']=x(-.2)
        sample=meta([d]);sample['capital']['debt_m']=x(0)
        r=model.evaluate(sample)['results'][0]
        self.assertEqual(r['years'][0]['cash_taxes_m'],0)
        self.assertEqual(r['years'][0]['fcff_m'],-60)

    def test_bad_gordon_spread_and_negative_terminal_fcff_blocked(self):
        d=dcf();d['terminal']['growth']=x(.1)
        with self.assertRaisesRegex(model.ValidationError,'below WACC'):
            model.evaluate(meta([d]))
        d=dcf();d['years'][-1]['capex_m']=x(1000)
        with self.assertRaisesRegex(model.ValidationError,'positive final-year'):
            model.evaluate(meta([d]))

    def test_future_years_must_be_consecutive_full_years(self):
        d=dcf();d['years'][1]['end_date']='2030-10-20'
        with self.assertRaisesRegex(model.ValidationError,'no gaps'):
            model.evaluate(meta([d]))

    def test_exit_multiple_reverse_and_sensitivity(self):
        d=dcf();d['terminal']={'method':'exit_ev_ebit','exit_ev_ebit':x(8)}
        r=model.evaluate(meta([d]))['results'][0]
        self.assertAlmostEqual(r['pv_terminal_m'], 320/1.1**((date(2031,10,20)-date(2026,10,20)).days/365.25))
        self.assertEqual(r['reverse']['type'],'required_exit_ev_ebit')
        self.assertGreater(r['reverse']['value'],8)
        self.assertLess(r['sensitivity'][1]['cells'][0]['per_share_usd'],r['present_value_per_share_usd'])

    def test_forward_pe_median_and_no_blind_full_year_claim(self):
        p=fpe()
        p['history']=[{'observed_on':'2026-01-20','price':x(30,'market','2026-01-20'),
                       'eps':x(1.5,'consensus','2026-01-20'),'basis':'gaap',
                       'period_start':'2026-01-01','period_end':'2026-12-31'}]
        r=model.evaluate(meta([p],cap=False))['results'][0]
        self.assertAlmostEqual(r['current_forward_pe'],12.5)
        self.assertAlmostEqual(r['peer_median_forward_pe'],17.5)
        self.assertAlmostEqual(r['peer_implied_price_usd'],35)
        self.assertEqual(r['history_sample_extrema']['coverage'],'sample_extrema_not_full_year')
        self.assertNotIn('present_value_per_share_usd',r)

    def test_peer_basis_mismatch_rejected(self):
        p=fpe();p['peers'][0]['basis']='adjusted'
        with self.assertRaisesRegex(model.ValidationError,'mismatches'):
            model.evaluate(meta([p],False))

    def test_future_eps_and_historical_lookahead_rejected(self):
        p=fpe();p['eps']['as_of']='2026-10-20'
        with self.assertRaisesRegex(model.ValidationError,'point-in-time'):
            model.evaluate(meta([p],False))
        p=fpe();p['history']=[{'observed_on':'2026-01-20','price':x(30,'market','2026-01-20'),
                              'eps':x(1.5,'consensus','2026-10-19'),'basis':'gaap',
                              'period_start':'2026-01-01','period_end':'2026-12-31'}]
        with self.assertRaisesRegex(model.ValidationError,'no look-ahead'):
            model.evaluate(meta([p],False))

    def test_sotp_bridge_ownership_and_corporate_cost(self):
        r=model.evaluate(meta([sotp()]))['results'][0]
        expected=(500+(600*.25+100*.75)/(1.1**(365/365.25))-40+5+20-80-10)/100
        self.assertAlmostEqual(r['present_value_per_share_usd'], expected)
        self.assertEqual(len(r['segments']),2)

    def test_sotp_includes_independent_dcf_segment(self):
        s=sotp()
        d=dcf();d['name']='divisional'
        s['segments'][1]={'name':'future_foundry','kind':'fcff_dcf','ownership':x(1),
                           'boundary_note':'Standalone cash flows exclude internal and parent cost transfers.',
                           'wacc':d['wacc'],'years':d['years'],'terminal':d['terminal'],
                           'justification':d['justification']}
        r=model.evaluate(meta([s]))['results'][0]
        self.assertGreater(r['segments'][1]['owned_enterprise_pv_m'],0)

    def test_sotp_requires_explicit_overlap_and_disallows_duplicate_names(self):
        s=sotp();s.pop('overlap_reconciliation')
        with self.assertRaisesRegex(model.ValidationError,'overlap_reconciliation'):
            model.evaluate(meta([s]))
        s=sotp();s['segments'][1]['name']='legacy'
        with self.assertRaisesRegex(model.ValidationError,'duplicate segment'):
            model.evaluate(meta([s]))

    def test_capital_dated_provisional_vs_fresh(self):
        d=meta([dcf()]);d['capital']['cash_m']['as_of']='2026-07-01'
        with self.assertRaisesRegex(model.ValidationError,'reconciliation_note'):
            model.evaluate(d)
        d['capital']['reconciliation_note']='Outdated quarter cash: net cash flows and any equity issuance after fiscal quarter require a reconciliation.'
        self.assertEqual(model.evaluate(d)['capital_status'],'provisional')

    def test_crosscheck_warns_on_divergence_without_average(self):
        r=model.evaluate(meta([dcf(),sotp(),fpe()]))
        self.assertEqual(len(r['results']),3)
        self.assertEqual(len(r['crosschecks']),1)
        self.assertEqual(r['crosschecks'][0]['scenario'],'base')
        self.assertTrue(r['crosschecks'][0]['material_disagreement'])
        self.assertNotIn('blended_price_usd',r)

    def test_json_cli_roundtrip_and_rejects_bad_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            inp=Path(tmp)/'valuation.json';out=Path(tmp)/'result.json'
            inp.write_text(json.dumps(meta([dcf(),sotp(),fpe()])),encoding='utf-8')
            result=subprocess.run([sys.executable,str(ROOT/'valuation_p1.py'),str(inp),'--output',str(out)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(len(json.loads(out.read_text())['results']),3)
            inp.write_text(json.dumps({'schema_version':99}),encoding='utf-8')
            bad=subprocess.run([sys.executable,str(ROOT/'valuation_p1.py'),str(inp)],capture_output=True,text=True)
            self.assertEqual(bad.returncode,2)
            self.assertIn('VALUATION BLOCKED',bad.stderr)


if __name__=='__main__':
    unittest.main(verbosity=2)
