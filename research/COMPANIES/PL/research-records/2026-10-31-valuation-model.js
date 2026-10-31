// PL illustrative 15-year explicit FCFF DCF, USD millions. Run: node 2026-10-31-valuation-model.js 2026-10-31-valuation-input.json
// Explicit horizon beyond P1 v4's 5-10 years; P2 does not automatically freeze this model.
// No unverified future equity funding; GAAP EBIT includes recurring share compensation economics.
const fs = require("node:fs");
const arg = process.argv[2];
if (!arg) throw Error("Input JSON path required");
const x=JSON.parse(fs.readFileSync(arg,"utf8"));
function compute(s,wacc=s.wacc,g=s.terminal_growth) {
 let rev=x.fy27_revenue_guidance_midpoint_usd_m, pv=0, rows=[];
 for(let i=0;i<15;i++){
  const prior=rev;rev*=1+s.revenue_growth[i];
  const ebit=rev*s.ebit_margin[i],tax=Math.max(0,ebit)*.22;
  const da=rev*s.da_to_revenue[i],capex=rev*s.capex_to_revenue[i];
  const nwc=(rev-prior)*.03,fcff=ebit-tax+da-capex-nwc;
  const years=1.25+i; pv+=fcff/(1+wacc)**years;
  rows.push({fy:2028+i,revenue_m:rev,ebit_m:ebit,fcff_m:fcff,present_value_m:fcff/(1+wacc)**years});
 }
 const terminal=rows.at(-1).fcff_m*(1+g)/(wacc-g);
 const terminalPV=terminal/(1+wacc)**15.25;
 const stubPV=x.short_stub_fy27_q4_fcff_usd_m/(1+wacc)**x.stub_years;
 const ev=pv+terminalPV+stubPV;
 const netcash=x.cash_and_short_term_investments_usd_m-x.convertible_principal_usd_m;
 return {enterprise_value_m:ev,explicit_pv_m:pv,terminal_pv_m:terminalPV,stub_pv_m:stubPV,net_cash_m:netcash,estimated_equity_m:ev+netcash,price_usd:(ev+netcash)/x.share_count_m,terminal_value_share:terminalPV/ev,rows};
}
const output={model:"15y_fcff_dcf_conditional_not_P1",date:x.valuation_date,assumptions:"FY2028-2042 annual, 22% cash tax on positive EBIT, change in operating net working capital=3% revenue increment, Jan31 FY dates, 2027Q4 -$10m stub. Cash is as of July31 (provisional); debt principal assumed cash settled. No extra equity financing in base. No P2.",scenario_results:{}};
for(const [name,s] of Object.entries(x.scenarios)){
 const central=compute(s);
 const samples=[compute(s,s.wacc+.01,s.terminal_growth-.003),compute(s,s.wacc-.01,s.terminal_growth+.003)];
 output.scenario_results[name]={...central,low_price_usd:Math.min(...samples.map(y=>y.price_usd)),high_price_usd:Math.max(...samples.map(y=>y.price_usd)),sensitivities:{downside_discount_plus_100bps_terminal_growth_minus_30bps:samples[0].price_usd,upside_discount_minus_100bps_terminal_growth_plus_30bps:samples[1].price_usd},dilution_10pct_illustration:central.estimated_equity_m/(x.share_count_m*1.1)};
}
console.log(JSON.stringify(output,null,2));
