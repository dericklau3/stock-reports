// INTC 2026-10-30 conditional reverse-valuation research calculator.
// This is NOT an intrinsic price target / P0-P1 whole-equity result.
// All currency inputs in USD billion, shares in billion, prices USD/share.
// The forecast capital structure, 2028 EBIT multiple and return are analyst assumptions.
const asOf = "2026-10-30", exitDate = "2028-12-31";
const years = (Date.parse(exitDate+"T00:00:00Z")-Date.parse(asOf+"T00:00:00Z"))/86400000/365.25;
const shares2028B=5.8, netCashLessClaims2028B=-15, costOfEquity=0.12, assumedRevenue2028B=80;
const snapshots = [
 {price:92.07, phase:"2026-10-29 16:00 EDT regular close, before earnings"},
 {price:70.90, phase:"2026-10-29 19:59 EDT after-hours indicative"}
];
function neededEbit(p, multiple){
  return (p*shares2028B*Math.pow(1+costOfEquity,years)-netCashLessClaims2028B)/multiple;
}
const out = {
  model:"reverse_exit_ebit_only_not_whole_equity",
  as_of:asOf,target:exitDate,year_fraction:years,
  assumptions:{shares2028B,netCashLessClaims2028B,costOfEquity,assumedRevenue2028B},
  source_urls:[
   "https://stockanalysis.com/stocks/intc/transcripts/714242-q3-2026/",
   "https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/q326earningsrelease.htm"
  ],
  snapshots:snapshots.map(s=>({...s,requirements:[20,25,30].map(multiple=>({
    exitMultipleEVtoEBIT:multiple,
    required2028EbitB:+neededEbit(s.price,multiple).toFixed(6),
    requiredMarginOnAssumedRevenue:+(neededEbit(s.price,multiple)/assumedRevenue2028B).toFixed(6)
  }))}))
};
console.log(JSON.stringify(out,null,2));