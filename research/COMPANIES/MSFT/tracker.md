# Microsoft（MSFT）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**中性等待：生意质量保持强，但股价较7月明显上升，资本开支与非经营投资收益使“增长等于股东现金回报”不能成立。

## Current Main Thesis

**核心逻辑：**办公订阅提供持续利润，Azure云服务扩张，付费Copilot席位给AI商业化提供证据；估值应依赖可持续盈利和资本回报，而不是把投资公允价值收益永久化。

## Key Risks

**主要风险：**AI基础设施资本投入可能长期吞噬现金；最新完整10-K附注未取得，租赁负债、投资权益和承诺不能假设为零。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker 2026-07-08；deep-research/2026-07-08-deep-research.md；旧价388.84、FY2026E EPS16.82、FCF64600百万，旧2030基础折现441美元。
- 当前观点：中性等待：生意质量保持强，但股价较7月明显上升，资本开支与非经营投资收益使“增长等于股东现金回报”不能成立。
- 报价桥：{"price": 535.07, "currency": "USD", "date": "2026-10-09", "session": "regular-close", "url": "https://api.nasdaq.com/api/quote/MSFT/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 2026-07-08基线388.84美元、FY2026 Q3 → 2026-10-09收盘535.07及FY2026全年公告；报价变化不自动归因某事件。
- 旧FY2026E收入329500百万/EPS16.82 → 实际331839百万/17.95；投资收益贡献必须剥离，不能全当经营超额。
- 旧FY2026E FCF64600百万 → 实际66987百万；仍低于FY2025的71611，AI资本开支主线未解除。
- 旧2030折现中枢441美元不直接挪用：改为明确的一年条件EPS情景；从积极/谨慎转中性等待，主要因价格与现金回报要求提高。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "conditional forward earnings scenarios; no audited-10K closure",
    "target": "FY2027 / approximately one year after research date",
    "discount_rate": 0.1,
    "discount_years": 1,
    "assumptions": {
      "bear": {
        "EPS": 18,
        "PE": 24
      },
      "base": {
        "EPS": 20,
        "PE": 28
      },
      "bull": {
        "EPS": 22,
        "PE": 32
      }
    },
    "calculations": [
      {
        "name": "FY2026 FCF",
        "expression": "182935-115948",
        "result": 66987
      },
      {
        "name": "FY2025 FCF",
        "expression": "136162-64551",
        "result": 71611
      },
      {
        "name": "Q4FY26 FCF",
        "expression": "55441-35802",
        "result": 19639
      },
      {
        "name": "Q4FY25 FCF",
        "expression": "42647-17079",
        "result": 25568
      },
      {
        "name": "revenue growth",
        "expression": "331839/281724-1",
        "result": 0.17788686799846665
      },
      {
        "name": "operating growth",
        "expression": "155237/128528-1",
        "result": 0.20780685920577624
      },
      {
        "name": "share-proxy market-cap million",
        "expression": "535.07*7427",
        "result": 3973964.8900000006
      },
      {
        "name": "historical GAAP PE",
        "expression": "535.07/17.95",
        "result": 29.808913649025072
      },
      {
        "name": "OpenAI-adjusted historical PE",
        "expression": "535.07/17.28",
        "result": 30.964699074074076
      },
      {
        "name": "bear present-value",
        "expression": "18*24/1.1",
        "result": 392.7272727272727
      },
      {
        "name": "base present-value",
        "expression": "20*28/1.1",
        "result": 509.09090909090907
      },
      {
        "name": "bull present-value",
        "expression": "22*32/1.1",
        "result": 640.0
      }
    ],
    "current_forward_PE": "未取得有效同口径预测快照；历史实际EPS倍数不是forward PE",
    "historical_forward_PE": "未取得历史当时EPS日频序列，不以今日EPS倒填历史价格",
    "precision_limit": "使用期末股本代理；EPS倍数包含经济股权激励成本，但不能校正缺失租赁资本负担；不额外加投资NAV避免重复。",
    "status": "conditional_scenarios_not_reliable_complete_current_value",
    "interpretation": "可复算的研究条件情景，不是已证实预测或精确NAV/DCF；最新股本或其他缺口见gaps。"
  },
  "capital_structure": {
    "actual_shares_million": 7427,
    "actual_shares_date": "2026-06-30",
    "weighted_diluted_FY2026_million": 7453,
    "cash_short_term_investments_million": 76843,
    "funded_debt_million": 40294,
    "operating_lease_long_term_million": 16532,
    "operating_lease_current": "公告未单列",
    "finance_leases": "完整附注未取得",
    "preferred_convertibles": "未据完整10-K验证；不可假定全部为零",
    "SBC_million": 12405,
    "buybacks_cash_million": 22271,
    "future_dilution": "情景EPS已按研究假设；10月实际股本未取得"
  }
}
```

### 改判条件与最强反证
加强判断：云增长与Copilot付费维持，且FCF增长重新快于股本/资本承诺增长；弱化判断：连续披露资本开支快于CFO且现金回报无改善。最强反证：Azure43%及3000万付费席位可能推高盈利超出基础EPS20；相反公司投资收益和租赁负担可能让EPS倍数虚高。

### 决定性局限
- 完整FY2026 10-K与租赁/承诺/权益附注未取得，不能作闭合DCF或精确EV
- 10月最新实际股数未核验，仅使用6月期末代理市值
- 当前与历史Forward P/E预测快照缺失；共识超预期未核验
- 下载公告为Fast-EDGAR原公告镜像，与搜索确认的Microsoft公告同源，非独立交叉验证
- 一项SEC及镜像URL未由已取回索引验证且访问失败，不作为已阅读证据

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Microsoft（MSFT）Tracker

Last updated: 2026-07-08

## Current Research View

**Positive / Constructive**，中高置信度，12-36 个月视角。

MSFT 仍是 AI 时代最完整的企业软件 + 云 + 开发者平台之一，但当前研究重点从“AI 需求是否真实”转向“AI capex 能否转化为高 ROIC 和可恢复的 FCF margin”。2026-07-07 收盘价 388.84 美元，相比 2026-05-20 报告时约 417 美元估值更合理；按 FY2026E EPS 16.82 美元，当前约 23.1x FY2026E P/E。问题是 FY2026E FCF 受 AI capex 高峰压制，P/FCF 约 44.7x，仍不算便宜。

## Current Main Thesis

- FY2026 Q3 revenue 828.86 亿美元，同比增长 18%。
- FY2026 Q3 operating income 383.98 亿美元，同比增长 20%。
- FY2026 Q3 net income 317.78 亿美元，同比增长 23%；diluted EPS 4.26 美元，同比增长 24%。
- Azure and other cloud services revenue +40%。
- Microsoft Cloud revenue 545 亿美元，同比增长 29%。
- Commercial RPO 6270 亿美元，同比增长 99%；约 25% 预计未来 12 个月确认。
- TTM revenue 3182.7 亿美元，TTM net income 1252.2 亿美元，TTM operating margin 46.8%。
- TTM FCF 729.2 亿美元，FCF margin 22.9%，显示 AI/cloud capex 正在压低自由现金流。
- Microsoft 与 OpenAI 长期合作延展；MSFT 持有 OpenAI 约 27% as-converted 权益，承诺资金 130 亿美元，截至 2026-03-31 已出资 118 亿美元。

## Current Practical Price Zones

- **强安全边际区**：300 美元以下。
- **较有吸引力区**：300-350 美元。
- **合理观察/小幅配置区**：350-400 美元。当前 388.84 美元位于此区间。
- **合理偏贵区**：400-475 美元，需要 FY2027 指引、Cloud margin 和 FCF 改善支持。
- **高预期区**：475 美元以上，需要 bull case：Azure/Copilot/OpenAI/GitHub AI 高 ROI 且 FCF margin 回升。

## Latest Valuation Snapshot — 2026-07-08

- Price：388.84 美元（2026-07-07 close）；383.06 美元（2026-07-08 pre-market quote）
- Market cap：约 2.89 万亿美元
- Enterprise value：约 2.94 万亿美元
- Shares outstanding：约 74.3 亿股
- TTM revenue：3182.7 亿美元
- TTM net income：1252.2 亿美元
- TTM EPS：16.79 美元
- TTM gross margin：68.31%
- TTM operating margin：46.80%
- TTM profit margin：39.34%
- TTM free cash flow：729.2 亿美元
- PE：23.16x
- Forward PE：21.00x；按 FY2026E EPS 16.82 美元约 23.1x
- EV/Sales：约 9.22x TTM；约 8.9x FY2026E sales
- P/FCF：约 39.6x TTM；约 44.7x FY2026E FCF
- Dividend yield：0.94%
- Beta：1.13
- 52-week range：349.20 - 555.45 美元
- Next estimated earnings：2026-07-29 after market close

## Scenario Valuation Summary

基于 FY2026E revenue 3295 亿美元、EPS 16.82 美元、FCF 646 亿美元，假设 FY2026-2030 不同增长/利润率/终值倍数，用 10% 折现率：

- **Bear**：收入 CAGR 8%，净利率 34%，FCF margin 24%，20x P/E / 24x FCF，折现中枢约 257 美元。
- **Base-low**：收入 CAGR 11%，净利率 36%，FCF margin 26%，22x P/E / 26x FCF，折现中枢约 335 美元。
- **Base**：收入 CAGR 14%，净利率 38%，FCF margin 28%，25x P/E / 28x FCF，折现中枢约 441 美元。
- **Bull**：收入 CAGR 17%，净利率 40%，FCF margin 31%，28x P/E / 30x FCF，折现中枢约 580 美元。

## Key Risks

- AI capex ROI 不足，导致 FCF margin 长期低于历史软件平台水平。
- Microsoft Cloud gross margin 被 AI infrastructure 折旧、电力和组件成本持续压低。
- Copilot seat 增长无法转化为高 usage、renewal 和 ARPU。
- OpenAI 关系和经济权利存在治理、竞争、监管不确定性。
- AWS、Google Cloud、Oracle、OpenAI direct、Anthropic、Meta 等竞争。
- Teams/cloud/AI partnerships/gaming 相关反垄断风险。
- 股价再次上行后，如果估值依赖 bull case，安全边际会下降。

## Latest Earnings or Company Update

- 最新季度：FY2026 Q3，季度结束 2026-03-31，财报和 10-Q 发布于 2026-04-29。
- Productivity and Business Processes revenue：350.13 亿美元，operating income 209.73 亿美元。
- Intelligent Cloud revenue：346.81 亿美元，operating income 137.53 亿美元。
- More Personal Computing revenue：131.92 亿美元，operating income 36.72 亿美元。
- Operating cash flow：466.79 亿美元。
- Additions to property and equipment：308.76 亿美元。
- Q3 rough FCF：约 158 亿美元。
- Stock-based compensation：30.81 亿美元。
- Cash + short-term investments：782.72 亿美元。
- Current portion of long-term debt：88.39 亿美元；long-term debt：314.23 亿美元。
- Q3 share repurchases：46.27 亿美元；dividends paid：67.56 亿美元。
- Q4 FY2026 guidance：total revenue 867-878 亿美元；Azure constant currency growth 39%-40%；Microsoft Cloud gross margin 约 64%。

## What Changed Since Prior View

- 2026-05-20 view 为 **Positive**，当时股价约 417.42 美元、市值约 3.10 万亿美元、forward PE 约 22.5x。
- 2026-07-08 更新后，股价回落到 388.84 美元，估值更合理；但 TTM / FY2026E FCF multiple 仍偏高，说明报告将观点调整为 **Positive / Constructive**，强调分批和价格纪律。
- 新报告补充了 OpenAI 10-Q 披露：约 27% as-converted 权益、130 亿美元承诺资金、118 亿美元已出资。
- 新报告补充了 bear/base/bull 明确估值区间和实用价格带。

## Metrics or Events to Monitor Next

- FY2026 Q4 earnings：预计 2026-07-29 盘后。
- Azure and other cloud services growth, especially Q4 39%-40% CC guidance。
- Microsoft Cloud revenue and gross margin percentage，重点看是否接近 64% 指引。
- Commercial RPO, OpenAI-adjusted demand quality, bookings。
- Microsoft 365 Copilot paid seats, net adds, ARPU, usage, renewal。
- GitHub Copilot usage/value-based pricing transition after 2026-06-01。
- Capex, finance leases, depreciation, FCF margin。
- OpenAI investment gains/losses, governance, economic rights, related-party disclosures。
- Operating expense growth and headcount trend。
- Search advertising ex-TAC and Bing/Edge/Copilot share gains。
- Gaming revenue, Xbox content cycle, Activision integration。
- Share repurchases, dividend, share count。

## What Would Change the Research View

- **Upgrade / stronger Positive**：股价进入 300-350 美元区间且基本面无恶化；或 Q4/FY2027 显示 Azure/Copilot 增长强、Cloud margin 稳定、FCF margin 回升路径清晰。
- **Maintain**：股价 350-400 美元，Azure 接近 35%-40%，FY2027 double-digit revenue/operating income growth 兑现，但 capex/FCF 仍需验证。
- **Downgrade**：Azure 增速明显放缓、Cloud gross margin 跌破预期、AI capex 继续大幅上修但收入/EPS 不同步上修、Copilot ROI 争议加剧、OpenAI 关系恶化，或股价跑赢 EPS/FCF revisions。

## Research Files

- `deep-research/2026-05-20-deep-research.md`
- `deep-research/2026-07-08-deep-research.md`
