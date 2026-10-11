# Space Exploration Technologies（SPCX / SpaceX）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**中性等待，资本回报证据仍不足：Starlink利润和AI收入明显扩张，但现金资本投入远超经营现金；不把世界级工程能力等同股票便宜。

## Current Main Thesis

**核心逻辑：**发射能力支撑全球卫星通信，Connectivity已提供经营利润；AI计算与软件可以扩大收入，但也扩大现金需求和治理复杂度。

## Key Risks

**主要风险：**AI资本开支、客户集中与并购稀释压过通信利润；Cursor闭合8-K未取得，不能拿第三方摘要里的股份数字冒充原件。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker2026-07-09、deep-research/2026-07-09-deep-research-v2.md；旧价148.30，首财报待验证，Cursor预计Q3完成，基础110–230美元。
- 当前观点：中性等待，资本回报证据仍不足：Starlink利润和AI收入明显扩张，但现金资本投入远超经营现金；不把世界级工程能力等同股票便宜。
- 报价桥：{"price": 162.57, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/SPCX/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 旧2026-07-09只有招股书/Q1 → 本次正式Q2报告：收入7814百万、AI收入2561百万、合并经营亏损143百万。
- 旧桥贷计划偿还 → Note9明确已全额偿还，债券票息仍约1464百万/年；不是多加250亿净现金。
- 旧现金1008亿六月19日快照 → 六月30日现金+证券100009百万；H1严重负FCF改变资本风险。
- Cursor旧预计Q3完成 → 供应方官方8月声明称收购后拟取消模型合同；不以第三方成交股数摘要充当SEC原文。
- 旧股价148.30 → 新收盘162.57；原基础价格区间暂停，观点维持中性但更重资本与股本闭合。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "reverse earnings and scenario conditions; reliable SOTP unavailable",
    "status": "unable_to_reliably_value",
    "target_year": null,
    "discount_years": null,
    "calculations": [
      {
        "name": "Q2 revenue growth",
        "expression": "7814/4071-1",
        "result": 0.9194301154507492
      },
      {
        "name": "Q2 gross profit",
        "expression": "7814-3495",
        "result": 4319
      },
      {
        "name": "H1 gross profit",
        "expression": "12508-5883",
        "result": 6625
      },
      {
        "name": "H125 gross profit",
        "expression": "8138-4244",
        "result": 3894
      },
      {
        "name": "H125 gross FCF",
        "expression": "351-6965",
        "result": -6614
      },
      {
        "name": "H126 gross FCF",
        "expression": "3466-28476",
        "result": -25010
      },
      {
        "name": "H126 rebate-adjusted cash gap",
        "expression": "3466-28476+1195",
        "result": -23815
      },
      {
        "name": "common H126 loss numerator",
        "expression": "-4817-671",
        "result": -5488
      },
      {
        "name": "AplusB million",
        "expression": "(7696293669+5485486276)/1000000",
        "result": 13181.779945
      },
      {
        "name": "legal snapshot cap million",
        "expression": "162.57*(7696293669+5485486276)/1000000",
        "result": 2142961.96565865
      },
      {
        "name": "30PE implied NI million",
        "expression": "162.57*(7696293669+5485486276)/1000000/30",
        "result": 71432.065521955
      },
      {
        "name": "notes annual coupon million",
        "expression": "25000*.05855",
        "result": 1463.75
      }
    ],
    "current_forward_PE": "当前亏损不适合简单PE；预测快照未取得",
    "historical_forward_PE": "未取得历史预测序列；不沿用旧298x",
    "scenario_conditions": {
      "bear": "AI investment fails, communication weakens",
      "base": "communications growth + AI contracts sustainable but capex remains high",
      "bull": "repeatable AI/Starship/software profits and lower capex intensity"
    },
    "capital_policy": "期末preferred converted already embedded A/B, not deducted again; full debt principal39512 inclusive finance leases and other financing; no extra IPO cash addition on top ofJune30 cash; Cursor indexed third-party shares excluded until original read"
  },
  "capital_structure": {
    "date": "2026-06-30, cover July28",
    "A_cover": 7696293669,
    "B_cover": 5485486276,
    "C_issued": 0,
    "preferred_outstanding": 0,
    "weighted_H1_basic_diluted_million": 4879,
    "cash_million": 93522,
    "securities_million": 6487,
    "restricted_cash_implied_million": 830,
    "debt_principal_million": 38433,
    "finance_leases_million": 1079,
    "debt_and_lease_carrying_million": 39364,
    "other_financing_million": 13406,
    "operating_lease_current_million": 344,
    "operating_lease_noncurrent": "not separately closed",
    "SBC_H1_PandL_million": 1470,
    "SBC_capitalized_million": 110,
    "ordinary_awards_excluded_antidilutive_million": 564,
    "conditional_performance_awards_million": 1331,
    "Cursor_closing_share_numbers": "search lead only, not original; excluded precise denominator",
    "current_actual_economic_shares": "not closed after acquisition"
  }
}
```

### 改判条件与最强反证
加强：Connectivity收入/利润维持、AI新增收入可持续且资本开支/CFO差额实质缩小，Cursor成交和稀释原件闭合。削弱：计算客户退租或高资本投入不带来盈利，供应中断影响付费使用。最强反证：Starlink规模与新云合同可能把集团带入盈利拐点；但Q2调整后EBITDA转正单独不足证明。

### 决定性局限
- Cursor8-K访问403，Capedge替代返回空文；精确成交股份、承担奖励与当前经济股数未原件闭合
- Q2原PDF缓存未保存精确取回URL，已验证PDF发行人/期间并读表，但远端来源定位仍需父代理补齐
- 本期原年度完整表未复核，未把旧中文转述数字当FY财务原件
- OpenAI仅官方搜索索引原文片段，不是正文取回；实际合同及双方回应未闭合
- 当前非流动经营租赁、10月现金/债务与未来盈利/历史Forward P/E无法完整闭合
- Q2财报及公告缓存原件完整并已读，但旧下载精确远端URL未在当前文件留存；不能用新拼接SEC路径伪补来源。

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。

父代理补充：提供Q2原缓存的公开短摘录、财务事实及内容哈希；原下载URL仍缺失。移除未读供应商完整公告所涉及的具体终止日期，不把索引线索作为确定合同事件。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Space Exploration Technologies（SPCX / SpaceX）Tracker

Last updated: 2026-07-09

## Current Research View

**中性 / 等待确认，接近“可研究但仍需安全边际”**，中低置信度，12-36 个月视角。

SPCX 是 Space Exploration Technologies Corp. / SpaceX 的 Class A 普通股，不是旧的 SPAC ETF。股价从 2026-06-16 的 201.80 美元回落到 2026-07-08 收盘 148.30 美元，市值从约 2.66 万亿美元降至约 1.95 万亿美元。估值压力明显缓解，但以约 98x pro forma EV/Sales、整体亏损和负 FCF 看，仍不是强安全边际。

## Current Main Thesis

- SpaceX 是 Space + Starlink Connectivity + AI/xAI/Grok/X + Cursor 选择权组合。
- 目前真正证明高质量利润的是 Connectivity/Starlink：2025 revenue 113.87 亿美元，operating income 44.23 亿美元，Segment Adjusted EBITDA 71.68 亿美元。
- Space/Falcon/Starship 是战略底座，但 Space segment 2025 operating loss 6.57 亿美元，Q1 2026 operating loss 6.62 亿美元。
- AI 是最大上行和最大现金流风险：2025 AI operating loss 63.55 亿美元，Q1 2026 AI capex 77.23 亿美元。
- 2026-06-16 与 Anysphere/Cursor 签署 600 亿美元股票并购协议，预计 2026 Q3 完成，增加 AI 分发选择权和稀释/整合风险。
- 2026-06-22 8-K 披露截至 2026-06-19 cash and cash equivalents 约 1008 亿美元。
- 2026-06-26 完成 250 亿美元 senior unsecured notes 发行，计划偿还 bridge loan；年票息约 14.64 亿美元。
- Elon Musk IPO 后约拥有 82% 投票权，公司为 Nasdaq controlled company。

## Key Risks

- 当前估值仍高：2026-07-08 market cap 约 1.95 万亿美元，TTM revenue 193.0 亿美元；粗略 pro forma EV/Sales 约 98x。
- TTM net loss 约 93.6 亿美元，TTM FCF 仍大幅为负。
- AI segment 亏损和 capex 是最大现金流风险。
- Anthropic compute agreement 可由任一方提前 90 天通知终止。
- Starship 商业化仍未验证，payload delivery to orbit 目标需要跟踪。
- Cursor 交易带来稀释和整合风险。
- Musk 控制权极强，Class A 股东治理权弱。
- Float 较低、期权和指数资金流可能放大波动。
- X/Grok 法律、内容安全、GDPR、版权和环保诉讼风险较高。
- Mission drift：从航天/通信扩张到 AI、X、Cursor，战略复杂度和管理层注意力风险上升。

## Latest Earnings or Company Update

- 最新财务披露：2026-06-12 424B4 prospectus，含 2025 全年和 Q1 2026 财务。
- 2026-06-15 8-K：underwriters 全额行使 83,333,333 股超额配售，IPO 最终发行 638,888,888 股 Class A，发行价 135 美元，gross proceeds 约 862.5 亿美元。
- 2026-06-16 8-K：SpaceX 与 Anysphere/Cursor 签署 merger agreement，implied equity value 600 亿美元，预计 2026 Q3 完成。
- 2026-06-17 8-K：Roelof Botha 被任命为独立 Common Stock Director，并加入 Audit Committee。
- 2026-06-22 8-K：截至 2026-06-19，公司 cash and cash equivalents 约 1008 亿美元；宣布 senior notes offering。
- 2026-06-23 8-K：定价 250 亿美元 senior notes。
- 2026-06-26 8-K：完成发行 250 亿美元 senior notes：2031/2033/2036/2046/2056 到期，票息 5.350%-6.650%。
- StockAnalysis 2026-07-09 accessed：2026-07-08 close 148.30 美元；after-hours 148.88 美元；market cap 约 1.95 万亿美元；shares out 约 131.7 亿；TTM revenue 193.0 亿美元；forward P/E 约 298x；earnings date shown as 2026-08-17。

## What Changed Since Prior View

- 股价从 201.80 美元回落到 148.30 美元，风险回报比改善。
- 市值从约 2.66 万亿美元降至约 1.95 万亿美元。
- 6月下旬完成 250 亿美元 senior notes 发行，缓解 bridge loan 短期压力，但增加长期利息负担。
- 现金更新显示 6月19日现金约 1008 亿美元，短期流动性强。
- 观点维持 **中性 / 等待确认**，但从“估值极端过热”调整为“可研究但仍需财报确认和安全边际”。

## Valuation Snapshot

- Current price used: 148.30 美元，2026-07-08 close。
- Market cap: 约 1.95 万亿美元。
- TTM revenue: 193.0 亿美元。
- Pro forma EV estimate: 约 1.89 万亿美元，使用 6月19日 cash 1008 亿美元和债券发行后粗略 debt/leases 估算。
- Pro forma EV/Sales: 约 98x。

Practical zones:

- 强安全边际区：低于 110 美元，尤其 80-100 美元。
- 可观察 / 小仓分批区：110-150 美元。
- 合理但仍需兑现区：150-200 美元。
- 偏贵 / 不宜追高区：200-250 美元。
- 过热区：250 美元以上，除非 AI/Starship/FCF 同时显著超预期。

## Core Thesis Assumptions That Must Remain True

- Starlink/Connectivity revenue 和 operating income 持续增长。
- AI segment 外部收入增长，亏损率和 capex intensity 下降。
- Starship 达成商业 payload delivery 和更低单位发射成本。
- Cursor 能增强企业 AI 分发，而不是造成战略漂移或超预期稀释。
- Capex/revenue 开始回落，FCF 路径在未来数年内清晰。
- 法律、监管、关联交易和治理风险不造成重大估值折价。

## Red-line Conditions

- AI capex 继续扩大但收入和 margin 不改善。
- Anthropic 或其他 compute 客户合同缩减、终止或重谈。
- Starship 重大延期或事故。
- Starlink 增速、ARPU 或 operating margin 明显放缓。
- Cursor 交易造成超预期稀释或整合失败。
- Lock-up 解禁后持续大量卖出压制股价。
- 股价重回 200+ 但 FCF/AI亏损/Starship里程碑没有同步改善。

## Management Promises / Milestones to Follow

- Q2 2026 首份上市后财报。
- Cursor 交易是否 2026 Q3 完成。
- Anthropic compute agreement 收入确认和稳定性。
- Starship payload delivery to orbit。
- Senior notes proceeds 是否按计划偿还 bridge loan。
- Roelof Botha 加入董事会/Audit Committee 后治理透明度是否改善。

## Metrics or Events to Monitor Next

- Connectivity revenue、operating income、service lines、ARPU。
- AI revenue、external customer revenue、operating loss、capex。
- Consolidated capex / revenue、OCF、FCF。
- Cash balance、debt、interest expense、finance leases。
- Starship milestones、launch cadence、mission success rate。
- Cursor integration、Grok paid conversion、enterprise AI adoption。
- Share count、SBC、performance awards、insider selling。
- Legal accruals and new X/Grok/AI/environment claims。

## What Would Change the Research View

Upgrade to **建设性** if Q2/Q3 show Starlink remains high-growth/high-margin, AI loss and capex intensity decline, FCF path becomes clearer, Starship hits commercial milestones, Cursor dilution is controlled, and price stays near or below the 110-150 watch range.

Downgrade to **Negative / thesis weakening** if AI capex remains uncontrolled, compute customer contracts weaken, Starship is delayed or has a major incident, Starlink growth slows, legal/regulatory risks expand, or price returns above 200 without matching fundamental improvement.

## Research Files

- `deep-research/2026-06-17-deep-research.md`
- `deep-research/2026-07-09-deep-research-v2.md`
