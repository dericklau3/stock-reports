# Tesla（TSLA）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**中性等待：Q3交付和储能部署有实际改善，但车量不能回答利润和现金问题；不沿用未闭合AI期权的旧目标价。

## Current Main Thesis

**核心逻辑：**汽车与储能形成制造、服务和现金基础；驾驶软件及无人运营可能提升附加价值，必须分别证明监管、安全、客户付费与单位经济。

## Key Risks

**主要风险：**高市值已前置AI商业化，而汽车经营利润率薄、资本开支高、CEO奖励和限制性股份使每股价值与GAAP EPS分母显著不同。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：deep-research/2026-06-23-deep-research.md；tracker于2026-07-23更新、earnings-tracking/2026-Q2-earnings-tracking.md。
- 当前观点：中性等待：Q3交付和储能部署有实际改善，但车量不能回答利润和现金问题；不沿用未闭合AI期权的旧目标价。
- 报价桥：{"price": 382.7, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/TSLA/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 旧2026-07-23 tracker“Q2 10-Q尚未取得” → 本次读取43页原10-Q，财务与CEO奖励核验明显完善。
- 旧Q2交付480126 → Q3 486532，储能13.5→13.7GWh；未来事件改为已确认10月21日财报。
- 旧6月深研股价405.05/7月跟踪378.93 → 10月9日382.70；股本代理换为7月16日实际法律在外3949.547百万，不能说只因价格变化市值下降。
- 中性等待维持，但暂停旧未闭合Robotaxi/Optimus目标区间，改反向盈利要求及明确验证条件。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "reverse normalized earnings; no reliable full optionality valuation",
    "status": "unable_to_reliably_value",
    "current_forward_PE": "未取得同口径预测快照",
    "historical_forward_PE": "未取得历史当时预测日频序列",
    "discount_years": null,
    "target_year": null,
    "calculations": [
      {
        "name": "FY24 FCF",
        "expression": "14923-11342",
        "result": 3581
      },
      {
        "name": "FY25 FCF",
        "expression": "14747-8527",
        "result": 6220
      },
      {
        "name": "H125 FCF",
        "expression": "4696-3886",
        "result": 810
      },
      {
        "name": "H126 FCF",
        "expression": "8634-8282",
        "result": 352
      },
      {
        "name": "H1 revenue growth",
        "expression": "50623/41831-1",
        "result": 0.2101790538117665
      },
      {
        "name": "Q3 delivery sequential growth",
        "expression": "486532/480126-1",
        "result": 0.01334233097145332
      },
      {
        "name": "Q3 production delivery gap",
        "expression": "486532-464391",
        "result": 22141
      },
      {
        "name": "legal-share proxy market cap million",
        "expression": "382.7*3949.547394",
        "result": 1511491.7876838
      },
      {
        "name": "30PE implied NI million",
        "expression": "382.7*3949.547394/30",
        "result": 50383.059589460005
      },
      {
        "name": "60PE implied NI million",
        "expression": "382.7*3949.547394/60",
        "result": 25191.529794730002
      }
    ],
    "scenario_conditions": {
      "bear": "auto margin/FCF deteriorate; AI option no cash",
      "base": "auto margin repair and energy cash profit, but robotaxi units missing",
      "bull": "repeatable paid autonomous trips and robot units produce net profit; not numerically inferred"
    },
    "capital_policy": "restricted award shares already in legal count not readded; future SBC and unissued awards need separate current audit; no option value added to core cash flows; EV not supplied while lease/NCI timing incomplete",
    "interpretation": "可复算的研究条件情景，不是已证实预测或精确NAV/DCF；最新股本或其他缺口见gaps。"
  },
  "capital_structure": {
    "date": "2026-06-30 except legal shares July16",
    "legal_shares": 3949547394,
    "H1_weighted_basic_million": 3235,
    "H1_weighted_diluted_million": 3538,
    "cash_investments_million": 43524,
    "cash_equivalent_million": 15219,
    "restricted_cash_implied_million": 1206,
    "debt_principal_million": 9080,
    "finance_lease_carrying_million": 281,
    "debt_finance_lease_carrying_million": 9342,
    "nonrecourse_debt_principal_million": 9078,
    "recourse_debt_principal_million": 2,
    "redeemable_NCI_million": 54,
    "NCI_million": 607,
    "preferred_issued": 0,
    "operating_leases": "ROU 6386; latest full liability bridge not extracted; cannot set zero",
    "SBC_H1_PandL_million": 2181,
    "CEO_2025_performance_restricted_shares_million": 423.7,
    "CEO_2025_interim_cancelled_million": 96,
    "2018_award_exercised_million": 304,
    "net_settlement_exercise_price_million_shares": 17.5,
    "current_october_shares": "not verified"
  }
}
```

### 改判条件与最强反证
加强：连续2–3季汽车不含积分毛利回升到旧目标18%–20%、FCF转正，并有无人运营真实收入/成本数据；不是保证阈值。削弱：交付靠降价、资本开支持续压过CFO，或正式安全/监管限制。最强反证：软件及无人平台规模化可能使现有制造盈利倍数失效；缺经济数据不能把其概率当100%。

### 决定性局限
- Q3正式利润和现金流尚未披露，不能从交付量推算EPS
- Robotaxi/Optimus外部付费单位经济与资本需求未闭合，拒绝精确期权/DCF目标价
- 10月股本、奖励归属及完整当前租赁负债桥未闭合，市值只用法律股数代理
- 当前与历史Forward P/E以及财报前共识未取得
- Q3 BusinessWire本次访问超时；使用保存的公司公告Yahoo转载原文，非独立确认

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Tesla（TSLA）Tracker

Last updated: 2026-07-23

## Current Research View

**中性 / 等待确认**，中等置信度，12-24 个月视角。

TSLA 仍是“EV/制造 + 能源储能 + FSD/Robotaxi/Cybercab/Optimus/real-world AI 期权”的稀缺组合。2026 Q2 财报强化了多头叙事：交付恢复、库存改善、FSD subscriptions 增长、Robotaxi 多城市上线、Cybercab 开始生产、储能部署恢复。但财务质量也更让人谨慎：operating margin 只有 1.4%，auto gross margin ex credits 降至 16.3%，capex 跳升到 57.89 亿美元并导致 FCF 转负。

当前研究重点不是证明 Tesla “有没有长期上限”，而是确认这个上限能否足够快转成可量化收入、毛利和自由现金流。Q2 后，观点维持 **中性 / 等待确认**，但监控重点从“交付是否恢复”进一步切换到“利润率/FCF 能否跟上 AI 与 Robotaxi 投资”。

## Current Main Thesis

- Q2 2026 total revenues 为 **282.36 亿美元**，同比 **+26%**。
- Q2 total deliveries 为 **480,126** 辆，同比 **+25%**；production 为 **451,758** 辆，同比 **+10%**，交付大于生产，Q1 库存压力得到缓解。
- Global vehicle inventory days 从 Q1 的 27 天降至 **15 天**。
- Automotive revenues 为 **205.16 亿美元**，同比 **+23%**；但 automotive gross margin ex regulatory credits 只有 **16.3%**，低于 Q1 的 19.2%。
- Energy revenue 为 **31.39 亿美元**，同比 **+13%**；storage deployed **13.5 GWh**，同比 **+41%**，但 energy gross margin 降至约 **20.4%**，受 vendor cell issue 相关 warranty charges 影响。
- Services and Other revenue 为 **45.81 亿美元**，同比 **+50%**；gross profit 达 **6.48 亿美元**，gross margin **14.1%**，为本季质量较好的亮点。
- GAAP operating income 为 **3.98 亿美元**，同比 **-57%**；operating margin 仅 **1.4%**。
- GAAP net income attributable to common 为 **11.14 亿美元**，同比 **-5%**；Q2 有 **10.05 亿美元 SpaceX equity investment unrealized gain**，主业经营利润需要打折看。
- Operating cash flow 为 **46.97 亿美元**，但 capex 为 **57.89 亿美元**，导致 free cash flow 为 **-10.92 亿美元**。
- Cash + short-term investments 为 **435.24 亿美元**，资产负债表仍强。
- Active FSD subscriptions 为 **1.48M**，同比 **+56%**；North America 新交付 FSD subscription attach rate 超过 **55%**。
- Robotaxi 已在美国 **seven major metros** live；Florida 三个城市在 2026 年 7 月 launched Robotaxi；Cybercab 已在 Gigafactory Texas 开始生产。
- StockAnalysis 2026-07-23 数据显示：previous close **378.93 美元**，market cap **1.40 万亿美元**，enterprise value **1.38 万亿美元**，TTM revenue **978.8 亿美元**，TTM net income **38.6 亿美元**，TTM FCF **70.0 亿美元**，PE **363.72x**，P/FCF **200.67x**。

## Key Risks

- 当前估值仍前置 Robotaxi/FSD/Optimus 成功，容错率低。
- Q2 revenue +26%，但 operating income -57%，说明增长没有转化为经营杠杆。
- Automotive ASP 和 regulatory credits 压力仍在；auto gross margin ex credits 从 Q1 19.2% 降至 Q2 16.3%。
- 2026 AI/Robotaxi/Cybercab/Optimus/垂直整合投资强度上升，Q2 capex 占 revenue 约 20.5%，FCF 转负。
- Energy warranty-related charges due to vendor cell issue 暴露供应商/电芯保修风险。
- Robotaxi/FSD 监管、安全事件、责任归属和公众接受度风险。
- SBC 和 CEO performance award 相关费用带来稀释压力；Q2 SBC expense 为 **11.51 亿美元**。
- 中国竞争、欧洲/中国市占率、关税、供应链和能源项目执行风险。
- 管理层关键人风险和治理折价。

## Latest Earnings or Company Update

- 最新季度：**2026 Q2**，财报发布时间 / 8-K 日期为 **2026-07-22**。
- SEC filings：2026-07-22 Form 8-K，Exhibit 99.1 为 Second Quarter 2026 Update；截至 2026-07-23 检查，最新 10-Q 仍为 2026-04-23 filed 的 Q1 10-Q，Q2 10-Q 尚未出现在 SEC recent filings 中。
- Total revenues：**282.36 亿美元**，同比 +26%。
- Total gross profit：**47.51 亿美元**，gross margin **16.8%**。
- Operating expenses：**43.53 亿美元**，同比 +47%。
- Income from operations：**3.98 亿美元**，operating margin **1.4%**。
- Adjusted EBITDA：**32.73 亿美元**，同比 -4%，margin **11.6%**。
- GAAP diluted EPS：**$0.32**；non-GAAP diluted EPS：**$0.33**。
- Operating cash flow：**46.97 亿美元**；capex：**57.89 亿美元**；FCF：**-10.92 亿美元**。
- Deliveries：**480,126** 辆；production：**451,758** 辆。
- Active FSD subscriptions：**1.48M**。
- Storage deployed：**13.5 GWh**。
- Robotaxi：美国 7 个 major metros live；部分城市 ramping unsupervised；Bay Area operations 使用 FSD Supervised 并有 CA TCP permit。
- Cybercab：Gigafactory Texas 开始生产；production Cybercab 公路 engineering test drives 已开始；7 月开始员工 rides。
- Optimus：Fremont Model S/X lines decommissioned，正在安装 first-generation Optimus lines，预计 2026 年生产。

## What Changed Since Prior View

较 2026-06-23 深度研究，观点仍为 **中性 / 等待确认**，但证据结构发生变化：

- **改善**：Q2 交付恢复显著，deliveries 超过 production，inventory days 从 27 降至 15，缓解 Q1 的库存/产交差担忧。
- **改善**：FSD subscription、Robotaxi 城市上线、Cybercab 生产、Optimus 生产线等 AI/自动驾驶叙事更具体。
- **改善**：Services and Other profitability 创纪录，说明车队生态后市场收入质量在提高。
- **恶化**：auto gross margin ex credits 环比明显下降，ASP 压力仍在。
- **恶化**：operating margin 只有 1.4%，收入增长没有转化为利润杠杆。
- **恶化**：capex 大幅跳升，FCF 转负，市场必须更认真审视 AI/Cybercab/Robotaxi 投资回报周期。
- **恶化**：energy gross margin 从 Q1 的 39.5% 降至 Q2 约 20.4%，且有 vendor cell warranty charge。
- **估值变化**：股价从 2026-06-22 的 405.05 美元降至 2026-07-23 抓取时 previous close 378.93 美元，market cap 从约 1.52T 降至约 1.40T，但 P/FCF 仍约 200x，不能算便宜。

## Current Price Discipline

| TSLA 股价区间 | 研究判断 |
|---|---|
| **<$250** | 开始有明显安全边际，前提是现金流和交付没有恶化。 |
| **$250-320** | 可积极研究 / 分批观察区，对应 base case 中下部。 |
| **$320-380** | 当前附近下沿；需要 Q3 毛利率和 FCF 修复确认。 |
| **$380-450** | bull case 预期区，不宜因单季 Robotaxi headline 追高。 |
| **>$450** | 需要 Robotaxi/FSD 收入、paid miles、单位经济和 FCF 共同证明。 |
| **>$600** | 基本需要 bull case 兑现，不能只靠汽车/能源当前利润支撑。 |

## Metrics or Events to Monitor Next

- Q2 2026 10-Q：debt、commitments、SBC、CEO award、RPO、capex details、warranty accruals。
- Q3/Q4 deliveries、production、inventory days。
- Automotive ASP、auto gross margin ex regulatory credits、discount/incentive trend。
- FSD subscriptions、attach rate、recognized software/service revenue。
- Robotaxi paid miles、revenue、事故率、保险/remote operation cost、城市扩张节奏。
- Cybercab 产能、成本、法规、fleet deployment。
- Energy storage deployments、Megapack 3 / Megafactory Texas ramp、energy gross margin、vendor cell warranty issue 是否一次性。
- Services and Other gross margin 是否维持两位数。
- Capex run-rate，尤其 Q3 是否继续 >$5B。
- Operating cash flow、free cash flow、cash + investments。
- Optimus production 是否进入可验证外部客户或真实工厂应用，而不只是内部 training data collection。
- China and Europe market share、pricing、competition。

## What Would Change the Research View

- 若 TSLA 连续 2-3 个季度交付恢复增长、inventory days 保持低位、auto gross margin ex credits 回升到 18%-20%、FCF 转正且 Robotaxi/FSD 有可量化收入扩张，可上调至 **建设性 / 正面**。
- 若基本面仍强但 AI/Robotaxi 兑现节奏慢、估值继续消化，维持 **中性 / 等待确认**。
- 若交付恢复靠降价换来、毛利率继续下滑、capex 长期压低 FCF、FSD/Robotaxi 出现重大监管或安全挫折、energy warranty issue 扩大，或 SBC/稀释继续恶化，下调至 **负面 / thesis weakening**。

## Research Files

- `deep-research/2026-05-13-deep-research.md`
- `deep-research/2026-06-23-deep-research.md`
- `earnings-tracking/2026-Q2-earnings-tracking.md`
- `tracker.md` updated 2026-07-23 with Q2 2026 earnings tracking.

## Sources

- Tesla Form 8-K filed 2026-07-22, Exhibit 99.1: Second Quarter 2026 Update.
- Tesla SEC submissions JSON, CIK `0001318605`.
- StockAnalysis TSLA quote/statistics/financials/forecast pages, accessed 2026-07-23.
