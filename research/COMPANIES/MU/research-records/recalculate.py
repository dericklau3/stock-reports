import json,math
from pathlib import Path
P=Path(__file__).parent;f=P/'2026-10-14-research.json';r=json.loads(f.read_text());v=r['valuation'];c=r['capital_structure'];checks=[]
def eq(name,a,b):
 assert math.isclose(a,b,rel_tol=1e-9,abs_tol=1e-7),(name,a,b)
 checks.append({'name':name,'calculated':a,'expected':b,'passed':True})
for name,p in r['financial_periods'].items():
 eq(name+' grossprofit',p['revenue']-p['cogs'],p['gross_profit']);eq(name+' FCF',p['ocf']-p['gross_cash_capex'],p['gross_FCF'])
eq('debt already includes finance leases',c['notes_carrying']+c['finance_leases_already_inside_debt'],c['debt_includes_finance_leases'])
eq('cash and securities',c['cash_equivalents']+c['short_term_investments']+c['long_term_marketable_investments'],c['cash_and_marketable_investments'])
eq('economic surpluscash',c['cash_and_marketable_investments']-c['debt_includes_finance_leases']-c['noncurrent_customer_contract_liabilities_proxy']-c['noncurrent_income_taxes_payable']-c['operating_cash_buffer_assumption'],c['valuation_surplus_cash'])
eq('marketcap',r['quote']['price']*r['identity']['actual_common_shares']/1e6,v['market_cap_m'])
eq('FY26PE',r['quote']['price']/r['financial_periods']['FY2026']['GAAP_diluted_EPS'],v['current_FY2026_GAAP_PE'])
for name,s in v['scenarios'].items():
 discounted=[]
 for i,t in enumerate(v['ACT365_25_years']):
  e=s['revenue'][i]*s['EBIT_margin_after_SBC'][i];cf=e*(1-s['tax'])+s['depreciation'][i]-s['gross_cash_capex'][i]-s['delta_NWC'][i];eq(name+' EBIT'+str(i),e,s['EBIT'][i]);eq(name+' FCFF'+str(i),cf,s['FCFF'][i]);discounted.append(cf/(1+v['WACC'])**t)
 for i,m in enumerate(s['terminal_EV_EBIT']):
  terminal=s['EBIT'][-1]*m/(1+v['WACC'])**v['ACT365_25_years'][-1];pv=(sum(discounted)+terminal+c['valuation_surplus_cash'])/r['identity']['forecast_economic_diluted_shares_m'];eq(name+' PV endpoint'+str(i),pv,s['present_equity_per_share'][i])
  eq(name+' price change'+str(i),pv/r['quote']['price']-1,s['price_change_vs_close'][i])
for s in v['base_sensitivity']:
 base=v['scenarios']['base'];ev=sum(cf/(1+s['WACC'])**t for cf,t in zip(base['FCFF'],v['ACT365_25_years']))+base['EBIT'][-1]*s['EV_EBIT']/(1+s['WACC'])**v['ACT365_25_years'][-1];eq('sensitivity', (ev+c['valuation_surplus_cash'])/r['identity']['forecast_economic_diluted_shares_m'],s['PV_per_share'])
reverse=v['reverse_valuation'];eq('reverseprice',(v['scenarios']['base']['PV_interim_FCFF']+reverse['required_FY2029_EBIT_m']*reverse['exit_multiple']/(1+v['WACC'])**v['ACT365_25_years'][-1]+c['valuation_surplus_cash'])/r['identity']['forecast_economic_diluted_shares_m'],r['quote']['price'])
output={'independent_math_checks':len(checks),'checks':checks,'scope':'Recomputes saved arithmetic only, not independent proof of forecast facts, customer contracts or source completeness.'};(P/'2026-10-14-validation.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n');print('INDEPENDENT RECALCULATION',len(checks),'PASS')
