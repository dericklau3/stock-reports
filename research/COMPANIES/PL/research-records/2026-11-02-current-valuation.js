// Run: node 2026-11-02-current-valuation.js 2026-11-02-current-valuation-input.json
// Only current, issuer-specific actual TTM metrics; no peer multiples or future cash-flow forecasts.
const fs=require("node:fs");
const x=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
const a=x.actuals;
const rev=a.FY2026.revenue_m+a.FY2027_H1.revenue_m-a.FY2026_H1.revenue_m;
const gp=a.FY2026.gross_profit_m+a.FY2027_H1.gross_profit_m-a.FY2026_H1.gross_profit_m;
const op=a.FY2026.operating_income_m+a.FY2027_H1.operating_income_m-a.FY2026_H1.operating_income_m;
const cap=x.price_usd*x.economic_shares_m;
const netCash=x.cash_and_short_investments_m-x.convertible_principal_m;
const ev=cap-netCash;
const output={market_cap_m:cap,net_cash_m:netCash,enterprise_value_m:ev,realized_ttm_revenue_m:rev,realized_ttm_gross_profit_m:gp,realized_ttm_operating_income_m:op,realized_ttm_gross_margin:gp/rev,trailing_price_to_sales:cap/rev,trailing_ev_to_sales:ev/rev,trailing_ev_to_gross_profit:ev/gp,price_to_book:cap/x.latest_stockholders_equity_m,approx_ttm_fcf_yield:a.TTM_cashflow_estimates_from_prior_research.free_cashflow_m/cap,disclaimer:"Trading multiples reflect only the stock's observed price relative to already-reported company financials. They do not establish an intrinsic fair value. Cash, share count and price dates are not perfectly aligned."};
if(!Number.isFinite(output.trailing_ev_to_sales)||output.trailing_ev_to_sales<=0)throw Error("invalid EV/TTM Sales");
console.log(JSON.stringify(output,null,2));
