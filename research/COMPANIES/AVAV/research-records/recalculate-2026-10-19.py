"""AVAV equity scenarios, reconciled GAAP financial history and sensitivities.

USD million / shares million except prices. Main model uses company-defined
adjusted EBITDA, retains cash-settled convertible principal, leaves operating
rent in operating costs, allows future dilution, and discounts future EQUITY.
All FY2028 scenario parameters are researcher assumptions, not company guidance.
"""
from pathlib import Path
from datetime import date
import json, math

ROOT=Path(__file__).resolve().parent

def calculate(d):
    q=d['quote']['close_USD'];c=d['capital'];g=d['guidance_FY2027']
    shares=c['latest_disclosed_common_shares_m'];netdebt=c['convertible_principal_m']-c['cash_m']-c['short_term_investments_m']+c.get('known_subsequent_cash_uses_m',0)
    cap=q*shares;ev=cap+netdebt
    years=(date.fromisoformat(d['target_date'])-date.fromisoformat(d['as_of'])).days/365.25
    factor=(1+d['discount_rate'])**years
    out={}
    for name,a in d['scenarios'].items():
        endpoints=[]
        for ebitda,mult in zip(a['EBITDA_m'],a['EV_EBITDA']):
            future=(ebitda*mult-a['target_net_debt_m'])/a['future_shares_m']
            pv=future/factor
            endpoints.append({'EBITDA_m':ebitda,'EV_EBITDA':mult,'future_equity_value_m':ebitda*mult-a['target_net_debt_m'],
                              'future_USD_per_share':future,'present_USD_per_share':pv,'gap_vs_quote':pv/q-1,
                              'convertible_above_initial_conversion_price':future>c['initial_conversion_price_USD']})
        assert endpoints[0]['present_USD_per_share']<endpoints[1]['present_USD_per_share']
        assert not any(x['convertible_above_initial_conversion_price'] for x in endpoints),'Rebuild conversion excess/capped-call treatment above conversion price'
        out[name]=endpoints
    f=d['financials']
    for name,x in f.items():
        assert math.isclose(x['FCF_m'],x['CFO_m']-x['PPE_cash_m']-x['software_cash_m'],abs_tol=1e-6),name
    for key in f['FY2026']:
        if key=='period_end':continue
        if isinstance(f['FY2026'][key],(int,float)):
            assert math.isclose(f['TTM'][key],f['FY2026'][key]+f['Q1FY2027'][key]-f['Q1FY2026'][key],abs_tol=1e-6),key
    s=d['segments_Q1FY2027'];old=d['segments_Q1FY2026']
    assert math.isclose(s['AxS_revenue_m']+s['SCDE_revenue_m'],f['Q1FY2027']['revenue_m'],abs_tol=1e-6)
    assert math.isclose(s['AxS_adj_EBITDA_m']+s['SCDE_adj_EBITDA_m'],g['Q1_actual_adj_EBITDA_m'],abs_tol=1e-6)
    a=d['scenarios']['base'];ebitda=sum(a['EBITDA_m'])/2;mult=sum(a['EV_EBITDA'])/2
    center=(ebitda*mult-a['target_net_debt_m'])/a['future_shares_m']/factor
    reverse=(q*factor*a['future_shares_m']+a['target_net_debt_m'])/mult
    base_sens={}
    for label,eb,m,n,sh,r in [
        ('EBITDA_minus_20pct',ebitda*.8,mult,a['target_net_debt_m'],a['future_shares_m'],d['discount_rate']),
        ('multiple_18x',ebitda,18,a['target_net_debt_m'],a['future_shares_m'],d['discount_rate']),
        ('net_debt_plus_200m',ebitda,mult,a['target_net_debt_m']+200,a['future_shares_m'],d['discount_rate']),
        ('shares_55m',ebitda,mult,a['target_net_debt_m'],55,d['discount_rate']),
        ('discount_10pct',ebitda,mult,a['target_net_debt_m'],a['future_shares_m'],.10),
        ('discount_15pct',ebitda,mult,a['target_net_debt_m'],a['future_shares_m'],.15)]:
        base_sens[label]=(eb*m-n)/sh/(1+r)**years
    prior=d['prior']
    return {'as_of':d['as_of'],'quote':d['quote'],'target_date':d['target_date'],'discount_years':years,'discount_factor':factor,
            'reference_marketcap_m':cap,'reference_EV_m':ev,'net_debt_ex_operating_leases_m':netdebt,
            'EV_FY27_guidance_adj_EBITDA_mid':ev/(sum(g['adj_EBITDA_m'])/2),
            'quote_FY27_guidance_adj_EPS_mid':q/(sum(g['adj_EPS'])/2),
            'quote_FY27_guidance_adj_EPS_range':[q/max(g['adj_EPS']),q/min(g['adj_EPS'])],
            'EV_FY27_guidance_EBITDA_less_SBC_mid_context_only':ev/(sum(g['adj_EBITDA_m'])/2-g['SBC_addback_m']),
            'reported_Q1_revenue_growth':f['Q1FY2027']['revenue_m']/f['Q1FY2026']['revenue_m']-1,
            'AxS_growth':s['AxS_revenue_m']/old['AxS_revenue_m']-1,
            'group_ex_ESAero_growth_proxy':(f['Q1FY2027']['revenue_m']-s['ESAero_contribution_m'])/f['Q1FY2026']['revenue_m']-1,
            'AxS_ex_ESAero_growth_proxy':(s['AxS_revenue_m']-s['ESAero_contribution_m'])/old['AxS_revenue_m']-1,
            'group_adj_EBITDA_growth':g['Q1_actual_adj_EBITDA_m']/g['prior_Q1_adj_EBITDA_m']-1,
            'scenarios':out,'base_midpoint_present_USD':center,'required_FY28_EBITDA_at_base_multiple_m':reverse,
            'required_margin_at_base_revenue_mid':reverse/(sum(a['revenue_m'])/2),
            'sensitivities':base_sens,'price_change_from_prior':q/prior['quote_USD']-1,
            'prior_present_value_ranges_USD':prior['present_value_ranges_USD'],
            'assumption_change':'FY2028 revenue/EBITDA/multiples retained; target net debt increases by100m in bear/base to reserve slower cash recovery and continuing campus construction. Quote/date/share proxy and known subsequent cash uses refreshed. No speculative MOU revenue added.',
            'SBC_treatment':d['SBC_treatment'],'limits':d['limits']}

if __name__=='__main__':
    data=json.loads((ROOT/'2026-10-19-valuation-inputs.json').read_text())
    result=calculate(data)
    (ROOT/'2026-10-19-valuation-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
