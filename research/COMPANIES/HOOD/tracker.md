# Robinhood Markets（HOOD）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**中性等待：客户资产与产品渗透改善，但股价已超出旧基础情景，交易周期、一次性收益和可转债需要重新定价。

## Current Main Thesis

**核心逻辑：**经纪入口、Gold订阅与现金/融资服务相互导流；新业务只有带来持续净收入、受控信用成本，才足以支持金融平台溢价。

## Key Risks

**主要风险：**事件合约与加密交易的监管及周期风险，加上可转债与客户资金口径，可能使高盈利倍数缺乏下行保护。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker 2026-05-12、deep-research/2026-05-12-deep-research.md；旧价格76.28、2027收入48/58/75亿美元，基础未来价75–80但未完整折现。
- 当前观点：中性等待：客户资产与产品渗透改善，但股价已超出旧基础情景，交易周期、一次性收益和可转债需要重新定价。
- 报价桥：{"price": 109.02, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/HOOD/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 2026-05-12 Q1基线 → Q2正式公告：净收入1067→1308百万，Gold430万→480万，资产3073亿→3690亿美元。
- 旧股价76.28→109.02；旧2027基础净收入58亿美元沿用为研究假设，不偷改为指引；纳入950百万预测稀释股数及12%折现。
- 新增6月可转债22亿美元与RVI收益，旧“无传统长期债务”描述不再可用。
- 旧建设性但需观察→中性等待；盈利可持续性和价格要求均要重新验证。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "conditional net-income multiple; financial-company client-fund exclusion",
    "discount_rate": 0.12,
    "discount_years": 1.2210814510609171,
    "target": "2027-12-31",
    "assumptions": {
      "bear": {
        "revenue_million": 4800,
        "net_margin": 0.25,
        "PE": 25,
        "shares_million": 920
      },
      "base": {
        "revenue_million": 5800,
        "net_margin": 0.35,
        "PE": 35,
        "shares_million": 950
      },
      "bull": {
        "revenue_million": 7500,
        "net_margin": 0.4,
        "PE": 40,
        "shares_million": 980
      }
    },
    "calculations": [
      {
        "name": "TTM net revenues",
        "expression": "4473+2375-1916",
        "result": 4932
      },
      {
        "name": "H1 revenue growth",
        "expression": "2375/1916-1",
        "result": 0.23956158663883098
      },
      {
        "name": "proxy capitalization",
        "expression": "109.02*(790+109)",
        "result": 98008.98
      },
      {
        "name": "revenue multiple",
        "expression": "109.02*899/(4473+2375-1916)",
        "result": 19.872055961070558
      },
      {
        "name": "FY24 cash difference",
        "expression": "-157-13-37",
        "result": -207
      },
      {
        "name": "FY25 cash difference",
        "expression": "1638-15-39",
        "result": 1584
      },
      {
        "name": "H125 cash difference",
        "expression": "4151-10-19",
        "result": 4122
      },
      {
        "name": "H126 cash difference",
        "expression": "2758-21-21",
        "result": 2716
      },
      {
        "name": "bear future",
        "expression": "4800*.25*25/920",
        "result": 32.608695652173914
      },
      {
        "name": "base future",
        "expression": "5800*.35*35/950",
        "result": 74.7894736842105
      },
      {
        "name": "bull future",
        "expression": "7500*.4*40/980",
        "result": 122.44897959183673
      },
      {
        "name": "bear present",
        "expression": "4800*.25*25/920/pow(1.12,1.2210814510609171)",
        "result": 28.39449916688484
      },
      {
        "name": "base present",
        "expression": "5800*.35*35/950/pow(1.12,1.2210814510609171)",
        "result": 65.12402921202084
      },
      {
        "name": "bull present",
        "expression": "7500*.4*40/980/pow(1.12,1.2210814510609171)",
        "result": 106.62424176952675
      }
    ],
    "current_forward_PE": "unavailable",
    "historical_forward_PE": "unavailable; no backfilled EPS",
    "capital_treatment": "EPS net-income assumes normal after-tax interest/SBC/credit losses; no customer cash add-on; gross debt not deducted again from equity earnings value; scenario shares are researcher diluted estimates, not audited full dilution.",
    "status": "conditional_scenarios_not_reliable_complete_current_value",
    "target_date": "2027-12-31"
  },
  "capital_structure": {
    "date": "2026-06-30",
    "A_million": 790,
    "B_million": 109,
    "C_million": 0,
    "preferred_issued": 0,
    "cash_million": 5362,
    "segregated_cash_securities_million": 12023,
    "restricted_cash_million": 62,
    "convertible_face_million": 2200,
    "convertible_carrying_million": 2170,
    "coupon": 0,
    "maturity": "2029",
    "capped_call_cost_million": 123.2,
    "capped_call_cap_USD": 237.85,
    "conversion_price_USD_company_statement": 174.42,
    "SBC_H1_million": 197,
    "leases": "not separately closed; other liabilities cannot be treated as zero",
    "other_borrowings": "Credit Card Funding Trust and working credit facilities require complete 10-Q notes",
    "actual_current_shares": "未核验，仅期末约数",
    "full_dilution": "完整契约、期权/RSU及结算选择未闭合"
  }
}
```

### 改判条件与最强反证
加强：在交易收入正常化时仍有净入金、订阅和服务增长，归属正常化净利润覆盖信用成本，股本变化落在假设内。弱化：连续净入金转负、监管直接限制核心交易渠道，或信用准备增长快于相关收入。最强反证：Q2平台采用和新业务收入可能使2027超过75亿美元；不应用一次性RVI收益证明该反证。

### 决定性局限
- 完整Q2 10-Q可转债/租赁/信用融资附注未取得，不能作精确EV及完全稀释估值
- 9月经营月报最新性未闭合，8月只能称本次已读缓存月报
- 可转债缓存正文精确来源URL缺失，契约正文未取得；FY2025和8月公告URL已由本次搜索定位但未重新取回正文
- 10月经济股数与当前/历史Forward P/E未取得；发布前共识未核验
- 可转债公告精确远端URL未在继承缓存中留存；本地正文在，契约全文和当前FD桥未闭合。

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。

父代理补充：融资公告精确URL已定位；新取正文403，财务数字仍取完整缓存。可转债契约与最新完全稀释桥仍未闭合。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Robinhood Markets（HOOD）Tracker

Last updated: 2026-05-12

## Current Research View

**建设性但需观察**，中等置信度，12-24 个月视角。

HOOD 已经从单一零售交易 App 转向更广义的个人金融平台，盈利能力、净存款和产品扩展都明显改善。当前主要问题是估值已经接近 base case，需要公司继续证明交易收入之外的 Gold、Retirement、Banking、Strategies、interest 和 prediction markets 能提升收入耐久性。

## Current Main Thesis

- Q1 2026 Total Platform Assets 为 3073 亿美元，同比增长 39%。
- Q1 2026 Net Deposits 为 177 亿美元，相当于 2025 Q4 期末平台资产的 22% 年化增长率；过去 12 个月 Net Deposits 为 678 亿美元。
- Q1 2026 revenue 为 10.67 亿美元，同比增长 15%；adjusted EBITDA 为 5.34 亿美元，margin 50%。
- Gold subscribers 达 430 万，同比增长 36%，Gold revenue 5000 万美元，同比增长 32%。
- Retirement AUC 达 274 亿美元，同比增长 90%；margin book 达 170 亿美元，同比增长 93%。
- Event contracts 交易量创纪录，Other transaction revenue 同比 +320%，但监管风险高。
- 公司已刷新 15 亿美元回购授权，资本回报能力增强。

## Key Risks

- Options/crypto/event contracts 交易量周期性回落。
- Prediction markets、crypto、PFOF 和 market structure 监管风险。
- 利率下行压缩 net interest revenue。
- Credit card、margin、banking 扩张带来信用和欺诈风险。
- 产品线扩张过快导致执行和合规复杂度上升。
- 当前估值较高，若增长或利润率放缓，倍数可能压缩。

## Latest Earnings or Company Update

- 最新季度：2026 Q1，财报发布于 2026-04-28。
- Total net revenues 10.67 亿美元，+15% YoY。
- Transaction-based revenues 6.23 亿美元，+7% YoY。
- Net interest revenues 3.59 亿美元，+24% YoY。
- Other revenues 8500 万美元，+57% YoY。
- Net income attributable to Robinhood 3.50 亿美元，+4% YoY。
- Diluted EPS 0.38 美元。
- Adjusted EBITDA 5.34 亿美元，+14% YoY，margin 50%。
- Funded Customers 2740 万，+6% YoY；Investment Accounts 2910 万，+8% YoY。
- Total Platform Assets 3073 亿美元，+39% YoY。
- Robinhood Gold subscribers 430 万，+36% YoY。

## What Changed Since Prior View

这是本 workspace 中第一份 HOOD 研究观点。

## Metrics or Events to Monitor Next

- Monthly/quarterly Net Deposits 和 Total Platform Assets。
- Gold subscribers、Gold revenue、ARPU。
- Options/equity/crypto/event contracts volumes。
- Other transaction revenue 是否可持续。
- Net interest revenue、margin book、cash/deposits、cash sweep。
- Robinhood Strategies AUM 和 funded customers。
- Banking/Gold Card/Platinum Card adoption。
- Regulatory developments around prediction markets、crypto、PFOF。
- Adjusted EBITDA margin、SBC、credit losses、回购执行。

## What Would Change the Research View

- 若 HOOD 在交易量正常化下仍能维持 20%+ revenue 增长、50% 左右 adjusted EBITDA margin，并证明 Gold/Strategies/Banking 等非交易业务复利，观点可上调至 **Positive**。
- 若平台指标继续强劲但估值需要消化，维持 **建设性但需观察**。
- 若 Net Deposits 放缓、transaction revenue 下滑且非交易收入补不上，或监管改变核心盈利模式，观点下调至 **Neutral/Negative**。

## Research Files

- `deep-research/2026-05-12-deep-research.md`
