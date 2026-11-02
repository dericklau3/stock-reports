// Run: node 2026-11-02-current-valuation.js 2026-11-02-current-valuation-input.json
// Present-day actuals only. No projected revenues, terminal values or discount rates.
const fs=require("node:fs");
const input=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));
const a=input.actuals;
const rev=a.FY2026.revenue_m+a.FY2027_H1.revenue_m-a.FY2026_H1.revenue_m;
const gp=a.FY2026.gross_profit_m+a.FY2027_H1.gross_profit_m-a.FY2026_H1.gross_profit_m;
const op=a.FY2026.operating_income_m+a.FY2027_H1.operating_income_m-a.FY2026_H1.operating_income_m;
const cap=input.price_usd*input.economic_shares_m;
const netCash=input.cash_and_short_investments_m-input.convertible_principal_m;
const ev=cap-netCash;
const peer=input.comparison.BKSY.ev_ttm_sales;
const result={market_cap_m:cap,net_cash_m:netCash,enterprise_value_m:ev,realized_ttm_revenue_m:rev,realized_ttm_gross_profit_m:gp,realized_ttm_operating_income_m:op,realized_ttm_gross_margin:gp/rev,trailing_price_to_sales:cap/rev,trailing_ev_to_sales:ev/rev,trailing_ev_to_gross_profit:ev/gp,price_to_book:cap/input.latest_stockholders_equity_m,approx_ttm_fcf_yield:a.TTM_cashflow_estimates_from_prior_research.free_cashflow_m/cap,peer_BKSY_ev_ttm_sales:peer,PL_EV_sales_premium_vs_BKSY_multiple:ev/rev/peer-1,mechanical_peer_multiple_price_usd:(peer*rev+netCash)/input.economic_shares_m,disclaimer:"The peer-price mapping is a single market multiple reference, NOT an intrinsic value or price target. Balance sheet and shares are from different dates."};
if(!(result.trailing_ev_to_sales>0)) throw Error("invalid observed EV multiple");
console.log(JSON.stringify(result,null,2));
