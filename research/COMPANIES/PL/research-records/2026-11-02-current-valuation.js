// Run: node 2026-11-02-current-valuation.js 2026-11-02-current-valuation-input.json
// PL own-history market valuation anchor; realized TTM inputs only; no peers or future DCF.
const fs=require("node:fs");
const x=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
const h=x.own_historical_ev_to_revenue.map(v=>v.ev_to_actual_revenue).sort((a,b)=>a-b);
if(h.length<3||!h.every(v=>Number.isFinite(v)&&v>=0))throw Error("Invalid own historical EV/revenue observations");
const med=h.length%2?h[(h.length-1)/2]:(h[h.length/2-1]+h[h.length/2])/2;
const a=x.actuals;
const rev=a.FY2026.revenue_m+a.FY2027_H1.revenue_m-a.FY2026_H1.revenue_m;
const gp=a.FY2026.gross_profit_m+a.FY2027_H1.gross_profit_m-a.FY2026_H1.gross_profit_m;
const op=a.FY2026.operating_income_m+a.FY2027_H1.operating_income_m-a.FY2026_H1.operating_income_m;
const cap=x.price_usd*x.economic_shares_m;
const netCash=x.cash_and_short_investments_m-x.convertible_principal_m;
const EV=cap-netCash;
const fairEV=med*rev, fairEquity=fairEV+netCash;
const fair=fairEquity/x.economic_shares_m;
const output={model:"issuer_own_4fiscal_year_historical_EV_to_actual_sales_median",valuation_date:x.as_of_date,quote_date:x.quote_date,historical_valuation_source:x.historical_valuation_source,own_historical_ev_to_revenue:x.own_historical_ev_to_revenue,own_history_median_ev_to_revenue:med,market_cap_m:cap,net_cash_m:netCash,enterprise_value_m:EV,realized_ttm_revenue_m:rev,realized_ttm_gross_profit_m:gp,realized_ttm_operating_income_m:op,realized_ttm_gross_margin:gp/rev,trailing_price_to_sales:cap/rev,trailing_ev_to_sales:EV/rev,trailing_ev_to_gross_profit:EV/gp,price_to_book:cap/x.latest_stockholders_equity_m,approx_ttm_fcf_yield:a.TTM_cashflow_estimates_from_prior_research.free_cashflow_m/cap,reference_enterprise_value_m:fairEV,reference_equity_value_m:fairEquity,fair_price_reference_usd:fair,model_gap_vs_quote_pct:(fair/x.price_usd-1)*100,history_window_sensitivity:{if_FY2023_through_FY2025_median:(4.91*rev+netCash)/x.economic_shares_m,if_FY2022_through_FY2026_median:(6.57*rev+netCash)/x.economic_shares_m},caveat:"Fair-price reference reflects PL's own historical market-multiple median, not a provable unique intrinsic value. Historic company fundamentals/capital structure vary; cash, shares and price are not strictly contemporaneous. No peers or future cash-flow forecasts."};
if(!Number.isFinite(fair)||fair<=0)throw Error("Invalid fair-price estimate");
console.log(JSON.stringify(output,null,2));
