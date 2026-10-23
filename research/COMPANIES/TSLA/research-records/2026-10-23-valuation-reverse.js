"use strict";
// TSLA 2026-10-23 independent reversal of observed market equity valuation.
// Run: node research/COMPANIES/TSLA/research-records/2026-10-23-valuation-reverse.js
function calculate(){
 const financials_m={
  FY2024:{revenue:97690,gross_profit:17450,operating_profit:7076,net_income_to_common:7091,cfo:14923,capex:11342},
  FY2025:{revenue:94827,gross_profit:17094,operating_profit:4355,net_income_to_common:3794,cfo:14747,capex:8527},
  NineMonths2025:{revenue:69926,gross_profit:12085,operating_profit:2946,net_income_to_common:2954,cfo:10934,capex:6134},
  NineMonths2026:{revenue:78669,gross_profit:14965,operating_profit:2057,net_income_to_common:2378,cfo:14897,capex:13014},
  Q32026:{revenue:28046,gross_profit:5494,operating_profit:718,net_income_to_common:787,cfo:6263,capex:4732}
 };
 const ttm=Object.fromEntries(Object.keys(financials_m.FY2025).map(k=>[k,financials_m.FY2025[k]-financials_m.NineMonths2025[k]+financials_m.NineMonths2026[k]]));
 for(const [k,v] of Object.entries(financials_m))v.fcf=v.cfo-v.capex;
 ttm.fcf=ttm.cfo-ttm.capex;
 const shares=3952757946,price=374.58,cash=17853+27594,debtAndFinance=1387+8136,noncontrolling=546+54,netCash=cash-debtAndFinance;
 const mktcap=price*shares/1e9,evSimple=mktcap-netCash/1000;
 const reverse=[25,40,60,100].map(pe=>({hypothetical_stable_pe:pe,required_yearly_common_profit_bn:mktcap/pe,required_net_margin_if_revenue_200bn:mktcap/pe/200}));
 const ownerFCF=[20,25,40].map(pfcf=>({hypothetical_stable_pfcf:pfcf,required_yearly_owner_fcf_bn:mktcap/pfcf}));
 const result={
  ticker:"TSLA",valuation_date:"2026-10-23",valuation_cutoff:"2026-10-23 22:15 China Standard Time (UTC+8)",latest_regular_close_date:"2026-10-22",
  market_price_usd:price,market_source:"https://stockanalysis.com/stocks/tsla/history/",
  financial_statement_end:"2026-09-30",filing_date:"2026-10-21",
  filing_10q:"https://ir.tesla.com/_flysystem/s3/sec/000162828026066775/tsla-20260930-gen.pdf",
  filing_8k:"https://www.sec.gov/Archives/edgar/data/1318605/000162828026066738/exhibit9914.htm",
  shares_outstanding_asof:"2026-10-15",shares,capital_m:{cash_and_equivalents:17853,short_term_investments:27594,debt_and_finance_lease_current:1387,debt_and_finance_lease_noncurrent:8136,noncontrolling_regular:546,noncontrolling_redeemable:54,restricted_cash_separate_estimate:19006-17853,operating_lease_current:1075,operating_lease_longterm:5847},
  financials_m,ttm_m:ttm,valuation_scope:"current consolidated market implied earnings only; excludes explicit scenario valuation of robotaxi, Optimus, potential SpaceX combination, future equity dilution and major planned capex",
  full_company_fair_value_status:"incomplete_due_to_material_operating_cash_and_dilution_omissions",
  economics:{mktcap_bn:mktcap,simple_net_cash_bn:netCash/1000,simple_ev_bn:evSimple,ttm_pe:mktcap/(ttm.net_income_to_common/1000),ttm_pfcf:mktcap/(ttm.fcf/1000),ttm_price_sales:mktcap/(ttm.revenue/1000),ttm_ev_sales:evSimple/(ttm.revenue/1000),reverse_required_common_income:reverse,reverse_required_fcf:ownerFCF,q3_fcf_m:financials_m.Q32026.fcf,consensus_q3_fcf_m:-4506,fcf_surprise_m:financials_m.Q32026.fcf+4506,annual_capex_if_management_guidance_m:20000},
  warnings:["Reverse market implied thresholds are not a valuation target or probability-weighted fair value.","No full SOTP or DCF: missing verified recurring autonomous ride revenues and marginal costs, Optimus commercial economics, 2027+ capex and fully diluted equity capital.","Do not add CEO 2025 performance restricted shares on top of legal current shares without reconciling economic denominator; stock-based compensation has continued future vesting contingencies.","The SpaceX special committee is considering possible combination, not a signed acquisition; no Tesla/SpaceX asset/price or financing included.","New $30bn credit commitments are not cash or borrowings; no double-count.","Cash flow Q3 partially driven by working-capital release and deferred revenue; not sustainable CFO normalized without further evidence.","No P0/P1 native engine executed and P2 not available for reverse market hurdle."]};
 if(ttm.revenue!==103570||ttm.net_income_to_common!==3218||ttm.fcf!==3303||financials_m.Q32026.fcf!==1531)throw Error("filing-period reconciliation mismatch");
 return result;
}
if(typeof module!=="undefined" && require.main===module)console.log(JSON.stringify(calculate(),null,2));
module.exports={calculate};
