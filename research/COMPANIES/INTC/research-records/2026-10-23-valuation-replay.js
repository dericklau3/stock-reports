/* Independent 2026-10-23 INTC scenario replay using public repository valuation formulas; run `node 2026-10-23-valuation-replay.js` */
function replay(){
  const valuationDate="2026-10-23",priceDate="2026-10-22",referencePrice=85.49;
  const years=(a,b)=>(Date.parse(b+"T00:00:00Z")-Date.parse(a+"T00:00:00Z"))/86400000/365.25;
  const expiry="2028-12-31",t=years(valuationDate,expiry);
  const p0=[
    {scenario:"bear",revenue_bn:60,ebit_margin:.1,multiples:[15,20],terminal_net_cash_claims_bn:-35,terminal_shares_bn:5.7,discount_rate:.15},
    {scenario:"base",revenue_bn:75,ebit_margin:.18,multiples:[20,25],terminal_net_cash_claims_bn:-20,terminal_shares_bn:5.8,discount_rate:.13},
    {scenario:"bull",revenue_bn:90,ebit_margin:.25,multiples:[25,30],terminal_net_cash_claims_bn:-5,terminal_shares_bn:6,discount_rate:.12}
  ].map(c=>({...c,discount_years:t,present_value_per_share_usd:c.multiples.map(m=>(c.revenue_bn*c.ebit_margin*m+c.terminal_net_cash_claims_bn)/c.terminal_shares_bn/(1+c.discount_rate)**t)}));
  const capital={economic_shares_m:5286.105262,cash_m:49427,debt_m:50537,other_claims_m:16074,status:"provisional; unreconciled future financing/dilution and government escrow"};
  const yearsEnds=[2027,2028,2029,2030,2031].map(y=>`${y}-10-23`);
  const p1params=[
    {scenario:"base",revenues_bn:[65,75,83,91,98],ebit_margins:[.12,.18,.2,.22,.23],tax_rate:.20,da_bn:[13.5,14.3,15,15.3,15.5],capex_bn:[17,17.5,18,18,18.2],nwc_bn:[.8,.9,1,1.1,1.2],wacc:.115,perpetual_g:.025},
    {scenario:"bull",revenues_bn:[72,90,105,119,132],ebit_margins:[.16,.25,.29,.32,.34],tax_rate:.21,da_bn:[14,15,16.2,17.4,18.5],capex_bn:[16,17,18,20,22],nwc_bn:[.9,1.3,1.4,1.5,1.7],wacc:.10,perpetual_g:.03}
  ];
  const p1=p1params.map(q=>{
    const periods=yearsEnds.map((end,i)=>{
      const ebit_bn=q.revenues_bn[i]*q.ebit_margins[i];
      const fcff_bn=ebit_bn-Math.max(ebit_bn,0)*q.tax_rate+q.da_bn[i]-q.capex_bn[i]-q.nwc_bn[i];
      const tf=years(valuationDate,end);
      return {end,t_years:tf,revenue_bn:q.revenues_bn[i],ebit_bn,fcff_bn,pv_fcff_bn:fcff_bn/(1+q.wacc)**tf};
    });
    const pv_explicit_bn=periods.reduce((x,p)=>x+p.pv_fcff_bn,0);
    const last=periods[periods.length-1];
    const pv_terminal_bn=last.fcff_bn*(1+q.perpetual_g)/(q.wacc-q.perpetual_g)/(1+q.wacc)**last.t_years;
    const ev_bn=pv_explicit_bn+pv_terminal_bn;
    const equity_bn=ev_bn+(capital.cash_m-capital.debt_m-capital.other_claims_m)/1000;
    return {scenario:q.scenario,params:q,periods,pv_explicit_bn,pv_terminal_bn,ev_bn,terminal_ev_fraction:pv_terminal_bn/ev_bn,present_value_per_share_usd:equity_bn/(capital.economic_shares_m/1000)};
  });
  const bullish=p0.find(p=>p.scenario==="bull");
  const implied_ebit_bn=(referencePrice*bullish.terminal_shares_bn*(1+bullish.discount_rate)**t-bullish.terminal_net_cash_claims_bn)/Math.max(...bullish.multiples);
  return {
    ticker:"INTC",valuation_date:valuationDate,price:{usd:referencePrice,as_of:priceDate,session:"US regular close"},
    valuation_status:"conditional stress tests; NOT verified full-equity fair value",models:{
      p0_equity_exit_ebit:{scope:"economic whole-company proxy with material unverified funding, share and claim assumptions",target_date:expiry,scenarios:p0},
      p1_fcff_dcf:{scope:"legacy v2 assumption replay, material omissions: Q3 funding and share dilution",capital,scenarios:p1}
    },
    reverse_price:{assumptions:"bull case net cash, diluted future shares, discount rate, upper 30x multiple",required_2028_ebit_bn:implied_ebit_bn,required_margin_on_90bn_revenue:implied_ebit_bn/90},
    model_execution:"Independent JavaScript implementation of repository documented P0/P1 formulas; original Python P0/P1 CLI NOT executed; P2 sealed snapshot NOT created.",
    limitations:[
      "Forward P/E peer quote/EPS same timestamp and basis unavailable.",
      "SOTP cannot separate internal foundry transfers, unassigned HQ, future fab capex or noncontrolling claims without unverifiable assumptions.",
      "Potential government escrow/conditional warrants overlap with debt and share counts.",
      "Q3 reported actual shares, offering net proceeds and capital expenditures not yet available.",
      "P1 DCF terminal value >75% EV and 2031 steady-state re-investment unproven; mathematical calculations are not investment forecasts."
    ]
  };
}
console.log(JSON.stringify(replay(),null,2));
