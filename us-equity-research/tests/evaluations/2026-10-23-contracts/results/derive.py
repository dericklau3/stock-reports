import json,pathlib,datetime
r=pathlib.Path(__file__).resolve().parent
rows={}
for timing in ['normal','delay']:
 d=json.loads((r/f'inputs/counterfactual_{timing}.json').read_text()); o=json.loads((r/f'outputs/counterfactual_{timing}.json').read_text()); a=d['analyses'][0]; x=o['results'][0]; p=a['segments'][1]; asof=datetime.date.fromisoformat(d['valuation_date']); df=lambda on:(1+p['wacc']['value'])**((datetime.date.fromisoformat(on)-asof).days/365.25)
 success_cost=sum(c['success_cost_m']['value']/df(c['on']) for c in p['costs']); failure_cost=sum(c['failure_cost_m']['value']/df(c['on']) for c in p['costs']); success_pv=p['success_ev_m']['value']/df(p['target_date'])-success_cost; failure_pv=p['failure_ev_m']['value']/df(p['target_date'])-failure_cost
 required_project=25*100-(500-40+5+120-80-10)
 rows[timing]={'source':'synthetic 材料A/B/C/D/E，非真实估值','discount_years':(datetime.date.fromisoformat(p['target_date'])-asof).days/365.25,'expected_terminal_ev_m':112.5,'expected_first_cost_m':50,'expected_additional_cost_m':30 if timing=='delay' else 0,'project_pv_m':x['segments'][1]['owned_enterprise_pv_m'],'preterminal_cost_pv_m':x['segments'][1]['owned_preterminal_cost_pv_m'],'equity_m':x['equity_value_m'],'conditional_per_share_usd':x['present_value_per_share_usd'],'counterfactual_gap':x['upside_vs_reference'],'market_gap_review_required':x['market_gap_review_required'],'required_project_pv_m_at_reference':required_project,'implied_success_probability_unchanged_evs_costs':(required_project-failure_pv)/(success_pv-failure_pv),'implied_success_terminal_ev_m_at_probability_25pct':((required_project+x['segments'][1]['owned_preterminal_cost_pv_m'])*df(p['target_date'])-.75*(-50))/.25,'success_path_total_cost_m':sum(c['success_cost_m']['value'] for c in p['costs'])}
(r/'outputs/derivation.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(rows,ensure_ascii=False,indent=2))
