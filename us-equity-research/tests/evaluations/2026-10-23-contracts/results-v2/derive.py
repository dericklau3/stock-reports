import json,pathlib,datetime
r=pathlib.Path(__file__).resolve().parent
d=json.loads((r/'inputs/counterfactual_normal.json').read_text());o=json.loads((r/'outputs/counterfactual_normal.json').read_text());p=d['analyses'][0]['segments'][1];asof=datetime.date.fromisoformat(d['valuation_date']);df=lambda on:1.1**((datetime.date.fromisoformat(on)-asof).days/365.25)
s=600/df(p['target_date'])-sum(c['success_cost_m']['value']/df(c['on']) for c in p['costs']);f=-50/df(p['target_date'])-sum(c['failure_cost_m']['value']/df(c['on']) for c in p['costs']);need=25*100-495
x={'source':'synthetic A/B/C/E; mechanical counterfactual only','required_project_pv_m':need,'implied_success_probability':(need-f)/(s-f),'implied_success_ev_m':((need+o['results'][0]['segments'][1]['owned_preterminal_cost_pv_m'])*df(p['target_date'])+.75*50)/.25}
(r/'outputs/normal-reverse.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');print(json.dumps(x))
