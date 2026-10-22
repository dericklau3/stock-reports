"""Economic-contract regressions using synthetic data only."""
import copy
import unittest
from datetime import date
from test_valuation_p1 import model, meta, dcf, sotp, fpe, x


def scope(kind='whole', omissions=None):
    return {'kind': kind, 'description': 'All operating businesses and corporate claims reconciled.',
            'material_omissions': omissions or []}


def modern(analyses):
    doc = meta(analyses)
    doc['schema_version'] = 4
    for a in analyses:
        if a['method'] != 'forward_pe':
            a['scope'] = scope()
        if a['method'] == 'sotp':
            for s in a['segments']:
                if s['kind'] == 'milestone_ev':
                    s.update(cost_treatment='separate', costs=[],
                             cost_note='No additional pre-commercial spending in this synthetic fixture.')
    return doc


class ContractTests(unittest.TestCase):
    def test_peer_future_eps_rejected(self):
        a=fpe(); a['peers'][0]['price']['as_of']='2026-10-13'
        with self.assertRaises(model.ValidationError): model.evaluate(meta([a]))

    def test_history_future_eps_relative_to_actual_quote_rejected(self):
        a=fpe(); a['history']=[{'observed_on':'2026-01-20','basis':'gaap',
            'period_start':'2026-01-01','period_end':'2026-12-31',
            'price':x(30,'market','2026-01-14'),'eps':x(2,'consensus','2026-01-20')}]
        with self.assertRaises(model.ValidationError): model.evaluate(meta([a]))

    def test_far_future_fy1_history_rejected(self):
        a=fpe(); a['history']=[{'observed_on':'2026-01-20','basis':'gaap',
            'period_start':'2029-01-01','period_end':'2029-12-31',
            'price':x(30,'market','2026-01-20'),'eps':x(2,'consensus','2026-01-20')}]
        with self.assertRaises(model.ValidationError): model.evaluate(meta([a]))

    def test_scope_controls_market_comparison_and_reverse(self):
        a=dcf(); doc=modern([a]); a['scope']=scope('partial',['new program'])
        out=model.evaluate(doc)
        r=out['results'][0]
        self.assertNotIn('upside_vs_reference',r)
        self.assertNotIn('reverse',r)
        self.assertIsNone(r['market_gap_review_required'])
        self.assertGreater(r['present_value_per_share_usd'],0)
        a['scope']=scope()
        r=model.evaluate(doc)['results'][0]
        self.assertTrue(r['market_gap_review_required'])
        self.assertIn('reverse',r)

    def test_omissions_prevent_whole_comparison(self):
        doc=modern([dcf()]); doc['analyses'][0]['scope']=scope('whole',['unfunded expansion'])
        r=model.evaluate(doc)['results'][0]
        self.assertNotIn('upside_vs_reference',r)

    def test_new_format_requires_scope(self):
        doc=modern([dcf()]); del doc['analyses'][0]['scope']
        with self.assertRaises(model.ValidationError): model.evaluate(doc)

    def test_partial_not_crosschecked_against_whole(self):
        doc=modern([dcf(),sotp()]); doc['analyses'][0]['scope']=scope('partial')
        self.assertEqual(model.evaluate(doc)['crosschecks'],[])

    def test_outcome_costs_and_negative_failure_value(self):
        a=sotp(); doc=modern([a]); s=a['segments'][1]
        s['failure_ev_m']=x(-50)
        s['costs']=[{'on':'2027-04-20','success_cost_m':x(80),'failure_cost_m':x(40)}]
        r=model.evaluate(doc)['results'][0]
        t=(date(2027,10,20)-date(2026,10,20)).days/365.25
        c=(date(2027,4,20)-date(2026,10,20)).days/365.25
        pv=(600*.25-50*.75)/1.1**t-(80*.25+40*.75)/1.1**c
        self.assertAlmostEqual(r['segments'][1]['owned_enterprise_pv_m'],pv)
        self.assertAlmostEqual(r['present_value_per_share_usd'],(500+pv-40+5-70)/100)

    def test_cost_double_count_and_out_of_period_rejected(self):
        for treatment, when in [('included','2027-04-20'),('separate','2028-01-01')]:
            doc=modern([sotp()]); s=doc['analyses'][0]['segments'][1]
            s['cost_treatment']=treatment
            s['costs']=[{'on':when,'success_cost_m':x(10),'failure_cost_m':x(10)}]
            with self.assertRaises(model.ValidationError): model.evaluate(doc)

    def test_current_period_horizon_and_anchor(self):
        a=fpe(); doc=modern([a]); a['fy1_end_date']='2027-09-30'
        for p in a['peers']: p['fy1_end_date']='2027-09-30'
        r=model.evaluate(doc)['results'][0]
        self.assertAlmostEqual(r['current_forward_pe'],12.5)
        a['fy1_end_date']='2026-09-30'
        with self.assertRaises(model.ValidationError): model.evaluate(doc)

    def test_legacy_numerical_result_unchanged(self):
        old=model.evaluate(meta([sotp()]))['results'][0]['present_value_per_share_usd']
        new=model.evaluate(modern([sotp()]))['results'][0]['present_value_per_share_usd']
        self.assertAlmostEqual(old,new)

    def test_new_snapshot_replay_and_partial_rejection(self):
        from valuation_p2 import freeze, verify
        doc=modern([dcf()])
        snap=freeze(doc,'dcf_base',captured_at='2026-10-20T12:00:00+00:00')
        self.assertEqual(verify(snap)['model_version'],4)
        doc['analyses'][0]['scope']=scope('partial')
        with self.assertRaises(model.ValidationError): freeze(doc,'dcf_base')

    def test_fy2_and_ntm_valid_and_mismatched_history(self):
        a=fpe(); a['horizon']='FY2'; a['period_start']='2027-10-01'; a['period_end']='2028-09-30'
        a['fy1_end_date']='2027-09-30'
        for peer in a['peers']:
            peer.update(horizon='FY2',period_start='2027-10-01',period_end='2028-09-30',fy1_end_date='2027-09-30')
        doc=modern([a]); self.assertGreater(model.evaluate(doc)['results'][0]['current_forward_pe'],0)
        a['history']=[{'observed_on':'2026-01-20','horizon':'FY1','fy1_end_date':'2026-12-31','basis':'gaap',
            'period_start':'2026-01-01','period_end':'2026-12-31',
            'price':x(30,'market','2026-01-20'),'eps':x(2,'consensus','2026-01-20')}]
        with self.assertRaises(model.ValidationError): model.evaluate(doc)
        a=fpe(); a['horizon']='NTM'
        for peer in a['peers']: peer['horizon']='NTM'
        self.assertGreater(model.evaluate(modern([a]))['results'][0]['current_forward_pe'],0)

    def test_missing_cost_declaration_rejected(self):
        doc=modern([sotp()]); del doc['analyses'][0]['segments'][1]['cost_treatment']
        with self.assertRaises(model.ValidationError): model.evaluate(doc)

    def test_financing_delay_cli_and_snapshot_roundtrip(self):
        import json, subprocess, sys, tempfile
        from pathlib import Path
        from valuation_p2 import freeze, verify
        a=sotp(); doc=modern([a])
        # 原始资料：80百万老股，新增20百万股，每股5美元；现金20百万，无其他流出。
        doc['capital']['shares_m']=x(80+20)
        doc['capital']['cash_m']=x(20+20*5)
        g=a['segments'][1];g['target_date']='2028-10-20';g['failure_ev_m']=x(-50)
        g['costs']=[{'on':'2027-10-20','success_cost_m':x(80),'failure_cost_m':x(40)}]
        delayed=copy.deepcopy(a);delayed['name']='delay';delayed['scenario']='bear'
        dg=delayed['segments'][1];dg['target_date']='2029-10-20'
        dg['costs'].append({'on':'2028-10-20','success_cost_m':x(60),'failure_cost_m':x(20)})
        doc['analyses'].append(delayed)
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp);inp=path/'input.json';out=path/'output.json'
            inp.write_text(json.dumps(doc))
            run=subprocess.run([sys.executable,'-B',str(Path(model.__file__)),str(inp),'--output',str(out)],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            rows=json.loads(out.read_text())['results']
            t=lambda y:(date(y,10,20)-date(2026,10,20)).days/365.25
            project=112.5/1.1**t(2028)-50/1.1**t(2027)
            self.assertAlmostEqual(rows[0]['present_value_per_share_usd'],(495+project)/100)
            self.assertLess(rows[1]['present_value_per_share_usd'],rows[0]['present_value_per_share_usd'])
            self.assertTrue(rows[0]['market_gap_review_required'])
            snap=freeze(json.loads(inp.read_text()),'sotp_base',captured_at='2026-10-20T12:00:00+00:00')
            self.assertAlmostEqual(verify(snap)['intrinsic_price_usd'],rows[0]['present_value_per_share_usd'])
