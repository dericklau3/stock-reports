// INTC cash-flow scenarios, 2026-10-30. Pure Node 18+; no packages or API calls.
// Usage: node 2026-10-30-valuation-scenarios-engine.js 2026-10-30-valuation-scenarios-input.json
// Output is JSON written to stdout. Values in USD billions except price/shares.
const fs=require("fs"), path=require("path");
const spec=JSON.parse(fs.readFileSync(process.argv[2]||path.join(__dirname,"2026-10-30-valuation-scenarios-input.json"),"utf8"));
const elapsed=(Date.parse(spec.valuation_date+"T00:00:00Z")-Date.parse(spec.balance_sheet_date+"T00:00:00Z"))/86400000/365.25;
const round=(n,d=4)=>Number(n.toFixed(d));
function valueCase(s,shock={}){
  s={...s,...shock};
  if(!(s.wacc>s.terminal_g && s.incremental_roic>s.terminal_g && s.economic_shares_b>0))throw Error("Invalid discount, reinvestment or shares");
  const hist=spec.historic_baseline, q=spec.q4_2026_analyst_projection, f=spec.forecast;
  const tax=f.cash_tax_rate, bridge=spec.balance.cash+spec.balance.short_term_investments-spec.balance.short_term_debt-spec.balance.long_term_debt-spec.balance.non_controlling_interests_book_value;
  const q4fcff=q.ebit*(1-q.cash_tax_rate)+q.da-q.capex-q.delta_nwc;
  let pvflows=q4fcff/Math.pow(1+s.wacc,q.period_fraction_years-elapsed), prev=hist.fy2026_revenue_implied;
  const rows=[];
  const revenueAt=i=>s.rev2027*Math.pow(s.rev2036/s.rev2027,i/9);
  const rev2035=revenueAt(8), nwc2036=f.nwc_incremental_sales_pct*(s.rev2036-rev2035);
  const nopat2036=s.rev2036*s.ebit_margin2036*(1-tax);
  // Stable growth reinvestment rate = g / incremental ROIC; ensures terminal FCFF is economically consistent.
  const capex2036=s.da2036 + nopat2036*s.terminal_g/s.incremental_roic - nwc2036;
  for(let i=0;i<10;i++){
    const year=2027+i, weight=i/9, revenue=revenueAt(i), margin=s.ebit_margin2027+(s.ebit_margin2036-s.ebit_margin2027)*weight;
    const ebit=revenue*margin, da=s.da2027+(s.da2036-s.da2027)*weight, capex=s.capex2027+(capex2036-s.capex2027)*weight;
    const deltaNwc=f.nwc_incremental_sales_pct*(revenue-prev), fcff=ebit*(1-tax)+da-capex-deltaNwc;
    const t=q.period_fraction_years+1+i-elapsed;
    pvflows+=fcff/Math.pow(1+s.wacc,t);
    rows.push({year,revenue_b:round(revenue),ebit_margin:round(margin,6),ebit_b:round(ebit),da_b:round(da),capex_b:round(capex),delta_nwc_b:round(deltaNwc),fcff_b:round(fcff),year_fraction:round(t,6)});
    prev=revenue;
  }
  const last=rows[9], terminalFCFF=nopat2036*(1-s.terminal_g/s.incremental_roic), expectedFinalFCFF=last.ebit_b*(1-tax)+last.da_b-last.capex_b-last.delta_nwc_b;
  if(Math.abs(terminalFCFF-expectedFinalFCFF)>0.005)throw Error("2036 terminal cashflow mismatch");
  const terminalEnterpriseValue=terminalFCFF*(1+s.terminal_g)/(s.wacc-s.terminal_g);
  const terminalPV=terminalEnterpriseValue/Math.pow(1+s.wacc,last.year_fraction);
  const enterpriseValue=pvflows+terminalPV, equityValue=enterpriseValue+bridge;
  return {per_share_usd:round(equityValue/s.economic_shares_b,4),equity_value_b:round(equityValue),enterprise_value_b:round(enterpriseValue),bridge_b:round(bridge),pv_explicit_fcff_b:round(pvflows),pv_terminal_b:round(terminalPV),terminal_pct_of_ev:round(terminalPV/enterpriseValue,5),q4_2026_fcff_b:round(q4fcff),capex2036_b:round(capex2036),normalized_terminal_fcff2036_b:round(terminalFCFF),yearly:rows};
}
const outputs=Object.fromEntries(Object.entries(spec.scenario_endpoints).map(([name,s])=>[name,{inputs:s,results:valueCase(s),sensitivity_wacc_plus_1pp:valueCase(s,{wacc:s.wacc+0.01}).per_share_usd,sensitivity_capex2027_plus_4b:valueCase(s,{capex2027:s.capex2027+4}).per_share_usd}]));
for(const prefix of ["bear","base","bull"])if(outputs[prefix+"_low"].results.per_share_usd>outputs[prefix+"_high"].results.per_share_usd)throw Error("Scenario bounds reversed");
if(Object.entries(outputs).some(([k,v])=>v.results.yearly[0].fcff_b>=0))throw Error("2027 FCF must reflect management's expected 2027 negative FCF");
console.log(JSON.stringify({model:spec.model,as_of:spec.valuation_date,usd_bn_unless_noted:true,reference_after_hours_price_usd:spec.price_reference.post_earnings_after_hours_usd,baseline:spec.historic_baseline,capital_bridge_2026_09_26_b:round(spec.balance.cash+spec.balance.short_term_investments-spec.balance.short_term_debt-spec.balance.long_term_debt-spec.balance.non_controlling_interests_book_value),scenario_outputs:outputs,interpretation:"Conditional discounted present-value ranges, not guaranteed future prices. Full legal claims and unclosed Classiq transaction remain materially uncertain."},null,2));
