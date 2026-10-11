# BitMine Immersion Technologies（BMNR）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**谨慎观望：最新完整季度原件已补齐，真实质押收入和历史每股ETH改善值得承认，但10月完全摊薄股数与全部索偿尚未闭合，不能沿用7月NAV折价结论。

## Current Main Thesis

**核心逻辑：**BMNR现在主要是ETH财库及验证服务平台，质押产生代币奖励、融资可以增加资产；股东回报取决于每股ETH和扣优先负担后的净资产，而不是持币总量。

## Key Risks

**主要风险：**ETH下跌、折价增发、固定费用和优先股负担可同时损害每股价值；重大内控缺陷及使命从挖矿转向金库仍须认真对待。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker/2026-07-10深研：谨慎观望、旧14.69、静态0.81x NAV、5.742METH和Q2基线；旧缓存在report三稿不冒充原件。
- 当前观点：谨慎观望：最新完整季度原件已补齐，真实质押收入和历史每股ETH改善值得承认，但10月完全摊薄股数与全部索偿尚未闭合，不能沿用7月NAV折价结论。
- 报价桥：{"price": 24.03, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/BMNR/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "source_policy": "继承父代理Nasdaq原JSON，拒绝15:55的24.05旧非收盘快照", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 7月基线财务到2/28→本次实际取回7/14提交5/31 Q3全文；收入46.535M/净亏83.595M，9M OCF−287.592M，不再写“季度全文受阻未读”。
- 旧569.577M普通股与588.6M FD→正式7/9actual603.226394M及5/31奖励/期权/权证19.264829M；622.491223M保守跨日代理非10月FD。
- 旧ETH5742237→10/4声明6016414、staked5067309；仅总量增长4.77%已核验，10月每股增长未确认。
- 旧回购只有授权→公司10/5明确2026购21M股；这是声明进步，不自动抵消未知同期增发。
- 旧股价14.69/0.81xNAV→10/09正式24.03已闭合；废止精确当前0.81x及19%折价，NAV待最新资本桥。
- Q3正式披露5/31内控仍无效、十年固定服务费40–50M及违约终止85%，风险未随KPMG更换自然消失。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "common NAV and ETH per economically FD share",
    "status": "unable_to_reliably_value_current",
    "target_year": null,
    "discount_years": null,
    "current_forward_PE": "不适用财库重估利润，无当前有效预测",
    "historical_forward_PE": "未取得完整当时预测序列，不用今日估算回填历史",
    "formula": "(ETH*spotETH+BTC*spotBTC+unrestrictedcash+realizableinvestments-totaldebtandotherliabilities-preferredseniorclaims-NCI)/economicallyFDshares*assumedmNAV",
    "current_inputs_missing": [
      "October actual/FDshares;not current marketcap implied shares",
      "aligned cryptoquotes/security valuations",
      "current preferredcounts/cumulative unpaid dividends",
      "ATM netissuance/buyback and current restrictedcash/liabilitychanges"
    ],
    "historical_capital_reconciliation": {
      "Julyactualshares": 603226394,
      "Mayawards_total": 19264829,
      "Julyactual_plusMayawards_conservative_notcurrent_FD": 622491223,
      "warning": "可能含归属/行权重叠；全加价外CVI未加行权现金是保守代理，不是当前NAV分母；ATM余量非有限上界。"
    },
    "same_date_ETHper_share_history": {
      "FY2025_0831": 0.008067244317044048,
      "20260531": 0.009345160480582612,
      "source": "Q3 Note4 and balance shares;both exact date periods"
    },
    "scenario_conditions": {
      "bear": "ETH lower/ATM belowNAV/higherclaims",
      "base": "fullalignedNAVbridge required",
      "bull": "ETHhigher and per-share accretivefinance/externalnetfees"
    },
    "calculations": [
      {
        "name": "FY24gross",
        "expression": "3310-3473",
        "result": -163
      },
      {
        "name": "FY25gross",
        "expression": "6095-5785",
        "result": 310
      },
      {
        "name": "Q326gross",
        "expression": "46535-5726",
        "result": 40809
      },
      {
        "name": "9M26gross",
        "expression": "59870-8177",
        "result": 51693
      },
      {
        "name": "FY24FCF",
        "expression": "-30-76",
        "result": -106
      },
      {
        "name": "FY25FCF",
        "expression": "-4149-1065",
        "result": -5214
      },
      {
        "name": "9M25FCF",
        "expression": "1366-18",
        "result": 1348
      },
      {
        "name": "9M26FCF",
        "expression": "-287592-406",
        "result": -287998
      },
      {
        "name": "Q326op",
        "expression": "46535-5726-37270-15404",
        "result": -11865
      },
      {
        "name": "9M26op",
        "expression": "59870-8177-335662-9038538",
        "result": -9322507
      },
      {
        "name": "leaseLiability",
        "expression": "104+1216",
        "result": 1320
      },
      {
        "name": "FY25ETHpershare",
        "expression": "1874927/232412324",
        "result": 0.008067244317044048
      },
      {
        "name": "May31ETHpershare",
        "expression": "5416945/579652432",
        "result": 0.009345160480582612
      },
      {
        "name": "same-date ETH/share growth",
        "expression": "(5416945/579652432)/(1874927/232412324)-1",
        "result": 0.15840801558949313
      },
      {
        "name": "treasuryETHgrowth vsJuly snapshot",
        "expression": "6016414/5742237-1",
        "result": 0.04774741969027052
      },
      {
        "name": "stakedfraction",
        "expression": "5067309/6016414",
        "result": 0.8422473918849335
      },
      {
        "name": "grossannualrewardETH",
        "expression": "5067309*.0263",
        "result": 133270.2267
      },
      {
        "name": "grossannualrewardUSDatAnnouncement",
        "expression": "5067309*.0263*2726",
        "result": 363294637.9842
      },
      {
        "name": "June preferred baseline dividendUSD",
        "expression": "3500000*100*.095",
        "result": 33250000.0
      },
      {
        "name": "Mayawards_potential",
        "expression": "2872929+10435430+1097346+4500000+359124",
        "result": 19264829
      },
      {
        "name": "conservativeJulyplusMay_awards_notcurrentFD",
        "expression": "603226394+2872929+10435430+1097346+4500000+359124",
        "result": 622491223
      },
      {
        "name": "conditionalJulyshares_marketcap_M",
        "expression": "24.03*603226394/1000000",
        "result": 14495.530247820001
      },
      {
        "name": "Q3noncashSBCsum_thousand",
        "expression": "36689+1162+506",
        "result": 38357
      },
      {
        "name": "Q3GAAPnoncashreweight",
        "expression": "264121-133275-9381-6793+9917-480",
        "result": 124109
      },
      {
        "name": "simple9MCFOcashbridge",
        "expression": "-287592-12102446+12218362",
        "result": -171676
      },
      {
        "name": "Q3historicalCommonBookUSDpershare",
        "expression": "11599577000/579652432",
        "result": 20.01126254224014
      }
    ],
    "capital_policy": "May total liabilities already contain leases/warrant liability, do not double-deduct; preferred afterMay separate; cannot combine FD dilution of liabilitywarrant with liabilityvalue without adjustment; token purchases not equipmentcapex; rewards notFCF; historical treasuryshares exclude; IPO proceedsnotdoubleadded"
  },
  "capital_structure": {
    "balance_date": "2026-05-31",
    "cash_M": 340.289,
    "collateral_derivative_cash_M": 100.125,
    "crypto_M": 10871.934,
    "ETH": 5416945,
    "BTC": 203,
    "total_liabilities_M": 30.128,
    "lease_total_M": 1.32,
    "lease_current_M": 0.104,
    "lease_noncurrent_M": 1.216,
    "finance_lease": "明确无finance leases见Note7",
    "warrant_liability_M": 2.087,
    "other_noncurrent_M": 14.687,
    "traditional_debt": "5/31公司明确无债；非10月无索偿承诺",
    "NCI_M": 0.548,
    "actualshares_20260531": 579652432,
    "actualshares_20260709": 603226394,
    "weighted_basicdiluted_Q3": 551788656,
    "warrants_equity_May": 2872929,
    "CVI_May": 10435430,
    "CVI_strike": 87.5,
    "CVI_expiry": "2027-03-22",
    "timeRSU_May": 1097346,
    "performanceRSU_May": 4500000,
    "options_May": 359124,
    "options_weighted_strike": 21.1,
    "SBC9M_M": 38.357,
    "common_authorized": 50000000000,
    "preferred_authorized": 20000000,
    "ATM_ceiling_USD_B": 24.5,
    "ATM9Mshares": 340748312,
    "ATM9Mnet_M": 11869.401,
    "October_remainingATM": "未核验，旧6.713B不是当前容量",
    "JunePreferredissued": 3500000,
    "JunePreferredprice": 80,
    "JunePreferrednet_M": 273.8,
    "historical_liquidation_per_preferred": 100,
    "historical_preferredClaim_M": 350,
    "preferred_current_quantity_and_unpaid": "未全核验，不宣称当前恰好350M",
    "preferred_annualrate": 0.095,
    "oldconvertible_preferred": "正式Q3明确FY25已转换且5/31不在外；与6月新BMNP不同",
    "MAVANownership": 0.98,
    "MAVAN_NCI": 0.02,
    "EthTowerfixedfee_M_peryear": [
      40,
      50
    ],
    "termination_fee": "remainingfees85%contractbaseline",
    "latest_assets_statement_date": "2026-10-04",
    "latest_ETH_statement": 6016414,
    "latest_staked_statement": 5067309,
    "latest_BTC_statement": 214,
    "latest_cash_securities_statement_M": 643,
    "latest_Beast_statement_M": 180,
    "latest_ORBS_statement_M": 117,
    "latest_crypto_price_basis_ETH": 2726,
    "weeklyannualized_yield": 0.0263,
    "buyback_statement_2026shares": 21000000,
    "current_completeFDshares": null
  }
}
```

### 改判条件与最强反证
加强：同日期完全摊薄每股ETH/NAV持续上升、折价不继续有害ATM、优先/现金桥与内控闭合，外部平台付费利润证实；弱化：折价增发、每股ETH下降、托管/衍生重大损失、重述及非核心资本扩张。最强反证：Q3真实质押收入提升，FY25末→5/31同日期每股ETH有改善且公司新声明实际回购，不可把所有融资一概定为摊薄；但不能由这几项外推10月NAV。

### 决定性局限
- 最新完整财务已补齐Q3；FY2026年度8/31已结束，但官方IR及申报缓存未读到已发布新10-K，不作年度猜测
- 10月实际/FD股本、ATM发行/回购净额、优先在外量与递延清算/股息未完全对齐；当前NAV/mNAV无法可靠估值
- 同期ETH/BTC与非核心投资可变现值/现金可用性未闭合；10/4公告价不是10/11现货价
- 独立MAVAN外部AUM/付费客户/费率/盈利分拆和内控正式有效性未证实
- FY25初版股数后来修订，采用Q3重列232412324普通股而非初版234712324；正式财务镜像与主站仍同源非独立审计

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# BitMine Immersion Technologies（BMNR）Tracker

Last updated: 2026-07-10

## Current Research View

**谨慎观望 / 不建议直接建仓**，中高置信度，6-18个月视角。

BMNR是高beta ETH财库股，不是传统经营型成长公司。按2026-07-09收盘价$14.69与2026-07-10现货价格估算，当前约为0.81x保守完全摊薄NAV，资产层面已有折价；但使命漂移、内部控制重大缺陷、巨额ATM剩余额度、管理层激励和非核心投资使折价具有合理性。

## Current Main Thesis

- 截至2026-06-28，公司披露持有5,742,237 ETH、206 BTC、$527M现金及有价证券、$180M Beast和$71M ORBS，总持有资产约$11.1B。
- 4,879,157 ETH已质押，披露年化收益率2.68%；静态年化奖励约130,761 ETH。
- 当前估算基本NAV约$18.76/股，保守完全摊薄NAV约$18.16/股；股价$14.69对应约19% FD NAV折价。
- 从2026-02-28至当前，ETH总量增长28.4%、基本股数增长15.3%，ETH/基本股增长约11.3%，近期融资仍实现每股增厚。
- 当前最重要变量不是总ETH，而是完全摊薄每股ETH、每股NAV、mNAV和折价状态下是否继续增发。
- BMNR已从BTC挖矿/浸没式冷却根本转向ETH金库、质押和生态股权配置，按用户“不得偏离原始使命”的纪律不属于新增购买候选。

## Key Risks

- ETH价格下降及mNAV折价扩大。
- 截至2026-02-28，$24.5B普通股ATM仍有约$6.713B销售容量；折价增发会摊薄每股NAV。
- 3.5M股BMNP拥有$350M清算优先权及约$33.25M年度累计现金股息。
- 保守完全摊薄股数约588.6M，包括权证、未归属RSU和绩效RSU。
- Tom Lee的450万份绩效RSU与股价、市值、总ETH等目标挂钩，可能偏向做大总量而非每股价值。
- 截至2026-02-28披露控制与程序无效；KPMG刚接任审计师。
- 质押、托管、slashing、退出队列、监管和期权策略风险。
- Beast/ORBS等moonshot投资降低NAV纯度与透明度。

## Latest Earnings or Company Update

- 最新完整SEC季报：截至2026-02-28的2026 Q2 Form 10-Q，2026-04-14 filed。
- 2026 Q2收入约$11.0M，其中质押收入$10.201M；六个月经营现金流约-$316.6M。
- 2026-02-28总资产$9.894B、数字资产$8.806B、现金$879.6M、总负债$36.2M、无传统债务。
- 2026-06发行3.5M股9.50%永久优先股BMNP，净募资约$273.8M。
- 2026-07-06公告披露ETH持仓5.742M、已质押4.879M，总持有资产约$11.1B。
- 2026-07-09 BMNR收盘$14.69，基本市值约$8.37B。

## What Changed Since Prior View

- ETH持仓从2026-05-10的5.207M增至2026-06-28的5.742M。
- ETH现货和BMNR股价均显著下跌，BMNR从接近NAV转为约0.81x FD NAV。
- 新增BMNP优先股：$350M清算优先权与固定股息负担。
- 每股ETH仍增长，但管理层稀释激励、内部控制和使命漂移权重上升，评级由“中性/等待确认”调整为“谨慎观望/不建议直接建仓”。

## Metrics or Events to Monitor Next

- 截至2026-05-31季度10-Q：最新基本股数、现金、ETH、G&A、期权及KPMG审阅结果。
- ETH/基本股与ETH/完全摊薄股是否继续增长。
- BMNR对普通股NAV的折溢价；mNAV低于1时是否暂停ATM。
- $6.713B ATM剩余容量的实际使用与发行均价。
- MAVAN外部第三方AUM、客户数、费率、毛利和留存率。
- 质押收益率、slashing/退出队列和托管对手方。
- 内部控制重大缺陷是否正式整改。
- Beast/ORBS等非核心投资占比是否继续扩大。

## What Would Change the Research View

- 若KPMG审阅无重大问题、每股ETH继续增长、mNAV低于1时停止增发并改善内控，可上调至**中性/可观察**。
- 若MAVAN出现可验证的第三方平台收入、完全摊薄每股NAV持续上升且资本配置KPI改为每股指标，可上调至**建设性**。
- 若公司在折价状态大规模ATM、每股ETH下降、出现重述/托管/期权损失或非核心投资扩张，观点下调至**负面/回避**。

## Research Files

- `deep-research/2026-07-10-deep-research.md`
- `deep-research/2026-05-12-deep-research.md`
