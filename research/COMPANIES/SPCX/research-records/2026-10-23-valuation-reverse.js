"use strict";
// SPCX 2026-10-23 no-forward-look reverse valuation check.
// Recalculate: node research/COMPANIES/SPCX/research-records/2026-10-23-valuation-reverse.js
function calculate(){
  const facts={
    ticker:"SPCX",issuer:"Space Exploration Technologies Corp.",cutoff:"2026-10-23 09:00 UTC+8",
    quote:{usd:144.75,date:"2026-10-22",session:"16:00 America/New_York, regular close",url:"https://stockanalysis.com/stocks/spcx/transcripts/723936-q3-2026/"},
    shares:{class_a:8246541218,class_b:5334522491,as_of:"2026-10-15",url:"https://d18rn0p25nwr6d.cloudfront.net/CIK-0001181412/b47786db-efbf-4d78-a475-cf153ee82f29.pdf"},
    capital:{as_of:"2026-09-30",cash_m:51294,marketable_securities_m:38561,debt_and_finance_leases_current_m:2698,debt_and_finance_leases_long_term_m:36146,capital_status:"historical_snapshot_not_comprehensive_fully_diluted_bridge"},
    financials_usd_m:{fy2024:{revenue:14015,gross:6019,operating:466,net:791,cfo:5776,capex:11163},
      fy2025:{revenue:18674,gross:9223,operating:-2589,net:-4937,cfo:6785,capex:20737},
      m9_2025:{revenue:13714,gross:6765,operating:-1216,net:-2590,cfo:4120,capex:13846},
      m9_2026:{revenue:27083,gross:15722,operating:705,net:-413,cfo:13097,capex:48069},
      q3_2026:{revenue:14575,operating:2791,net:4404,cfo:9631,capex:19593}},
    source_financial:"https://d18rn0p25nwr6d.cloudfront.net/CIK-0001181412/b47786db-efbf-4d78-a475-cf153ee82f29.pdf",
    source_q3:"https://www.sec.gov/Archives/edgar/data/1181412/000162828026066482/spaceexplorationtechnologi.htm",
    q4_2026_capex_guidance_bn:[35,40],
    expected_echoStar_equity_shares_m:261.8,
    material_scope_omissions:["not fully diluted economic shares / future SBC","EchoStar and Grain spectrum closing cash and share obligations","possible Tesla transaction under only special committee review","unverified 2027-2032 capex after AI compute scale-up","cancellable cloud contract renewal and unit economics","Starship reuse / satellites replacement capex"],
    valuation_status:"INCOMPLETE: reverse-normalization market hurdle, NOT independent fair value"
  };
  const f=facts.financials_usd_m;
  const ttm=Object.fromEntries(Object.keys(f.fy2025).map(k=>[k,f.fy2025[k]-f.m9_2025[k]+f.m9_2026[k]]));
  const shares=facts.shares.class_a+facts.shares.class_b;
  const equity_bn=shares*facts.quote.usd/1e9;
  const net_cash_bn=(facts.capital.cash_m+facts.capital.marketable_securities_m-facts.capital.debt_and_finance_leases_current_m-facts.capital.debt_and_finance_leases_long_term_m)/1000;
  const ev_bn=equity_bn-net_cash_bn;
  const reverse={multiple_30x_normalized_common_earnings_bn:equity_bn/30,multiple_40x_normalized_common_earnings_bn:equity_bn/40,multiple_25x_normalized_owner_fcf_bn:equity_bn/25};
  const result={...facts,computed:{economic_shares:shares,market_equity_bn:equity_bn,net_cash_simple_bn:net_cash_bn,ev_simple_bn:ev_bn,ttm_fy2025_minus_9m2025_plus_9m2026_usd_m:ttm,ttm_fcf_usd_m:ttm.cfo-ttm.capex,q3_fcf_usd_m:f.q3_2026.cfo-f.q3_2026.capex,ev_over_ttm_revenue:ev_bn/(ttm.revenue/1000),eq_over_ttm_revenue:equity_bn/(ttm.revenue/1000),reverse_market_earnings_cash_hurdles:reverse,fy2026_capex_if_q4_guidance_met_bn:[48.069+35,48.069+40]}};
  // Strict arithmetic invariants; do not infer fair-value endpoints from the market.
  if(shares!==13581063709 || ttm.revenue!==32043 || ttm.cfo-ttm.capex!==-39198 || f.q3_2026.cfo-f.q3_2026.capex!==-9962)throw Error("accounting identity did not match filing");
  if(Math.abs(ev_bn+net_cash_bn-equity_bn)>1e-6)throw Error("enterprise/equity bridge mismatch");
  return result;
}
if (typeof module!=="undefined" && require.main===module)process.stdout.write(JSON.stringify(calculate(),null,2)+"\n");
module.exports={calculate};
