# SKHY / SK hynix Inc. Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**建设性但需观察：HBM及高端存储的商业进展较7月更扎实，但不能用异常高单季净利润证明现价便宜；最新半年度附注受阻使精确估值暂缓。

## Current Main Thesis

**核心逻辑：**高带宽内存让AI加速器更有效读取数据；客户认证、先进工艺与封装能力支持需求，但扩产和定价仍受存储周期影响。

## Key Risks

**主要风险：**行业扩产或客户需求转弱可使超高利润率迅速回落；ADS比例、发行后股本、融资及非经营收益口径会直接改变每ADS价值。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker/deep-research2026-07-09；IPO前折算144.6美元、F-1/A和Q1基线。
- 当前观点：建设性但需观察：HBM及高端存储的商业进展较7月更扎实，但不能用异常高单季净利润证明现价便宜；最新半年度附注受阻使精确估值暂缓。
- 报价桥：{"price": 169.03, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/SKHY/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 2026-07-09 F-1/A未交易ADS → 最终424B4每ADS0.1、$149发行价、728865500普通股及10/09真实收盘169.03；“尚无交易史”旧状态失效。
- 旧Q1生产/样品阶段 → 公司Q2明确HBM4批量出货，下半年增产为目标，HBM4E仍样品阶段。
- 旧Q1收入52576.3、经营37610.3十亿KRW → Q2 79318.7/60542.6；承认实际经营进展。
- 旧价格带暂停精确定价，因净利润高于收入而最新附注/现金流未取回；建设性但需观察维持。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "cyclical normalized earnings pending; reverse earnings only",
    "status": "unable_to_reliably_value",
    "target_year": null,
    "discount_years": null,
    "current_forward_PE": "未取得；不年化异常净利润",
    "historical_forward_PE": "未取得历史当时预测；ADS新上市历史短",
    "calculations": [
      {
        "name": "FY24 operating income",
        "expression": "31828-3924-4436",
        "result": 23468
      },
      {
        "name": "FY25 operating income",
        "expression": "58691-5019-6466",
        "result": 47206
      },
      {
        "name": "FY24FCF",
        "expression": "29796-15946",
        "result": 13850
      },
      {
        "name": "FY25FCF",
        "expression": "53373-27519",
        "result": 25854
      },
      {
        "name": "Q126FCF",
        "expression": "26330-7657",
        "result": 18673
      },
      {
        "name": "Q226 revenue growth",
        "expression": "79318.7/22232-1",
        "result": 2.5677716804605972
      },
      {
        "name": "Q226 operating margin",
        "expression": "60542.6/79318.7",
        "result": 0.7632828072068756
      },
      {
        "name": "new ordinary issue",
        "expression": "177900000*.1",
        "result": 17790000.0
      },
      {
        "name": "ADS equivalent denominator",
        "expression": "728865500/.1",
        "result": 7288655000.0
      },
      {
        "name": "proxy marketcap millionUSD",
        "expression": "169.03*(728865500/.1)/1000000",
        "result": 1232001.35465
      },
      {
        "name": "30PE NI millionUSD",
        "expression": "169.03*(728865500/.1)/1000000/30",
        "result": 41066.71182166667
      }
    ],
    "capital_policy": "no FX used for direct ADS marketcap; latest profits KRW and marketcapUSD not divided without contemporaneous FX; final share count includesIPO already; no IPO cash double-add; shares-dilution/leases/exchangeables pending",
    "scenario_conditions": {
      "bear": "ASP down and high capex",
      "base": "normalize HBM/DRAM earnings with cash bridge",
      "bull": "long-duration tight HBM market and repeatable contracts"
    }
  },
  "capital_structure": {
    "postoffering_ordinary_shares": 728865500,
    "prospectus_date": "2026-07-09",
    "treasury_2026June29": 1626865,
    "IPO_ADS": 177900000,
    "IPO_ordinary": 17790000,
    "IPO_price": 149,
    "IPO_net_proceeds_estimated_USD_billion": 26.2,
    "Q2_cash_statement_KRW_trillion": 88,
    "Q2_debt_statement_KRW_trillion": 18.6,
    "Q2_net_cash_statement_KRW_trillion": 69.4,
    "Q1cash_equivalent_KRW_billion": 21167,
    "Q1shortterm_instruments_KRW_billion": 18220,
    "Q1shortterm_investment_assets_KRW_billion": 14943,
    "Q1borrowings_KRW_billion": 19318,
    "Q1lease_current_noncurrent_KRW_billion": [
      526,
      1988
    ],
    "restricted_assets": "本期未独立闭合",
    "exchangeable_bonds": "半年度附注未取得；旧债/库藏股兑付不能忽略",
    "preferred_or_hybrid": "本期完整索偿未核验",
    "SBC": "库存股员工报酬计划及期权会稀释；完整半年度金额未取",
    "October_actual_shares": "未核验；使用最终IPO代理"
  }
}
```

### 改判条件与最强反证
加强：HBM认证/量产持续、跨周期合同与正常经营现金回报足以覆盖扩产，补齐正式半年度附注；弱化：客户砍单、HBM/DRAM价格下降伴库存上升或扩产失控。最强反证：Q2经营利润76%及HBM4量产说明长期稀缺可能比传统存储周期更强；不是将118%净利率当永久事实。

### 决定性局限
- 正式半年度6-K正文访问403，StockTitan替代DNS失败；搜索摘要不作财务原件输入
- Q2净利润金融收益/税项桥、毛利/现金流/资本开支未取得，无法可靠正常化估值
- Q2现金定义、受限项及IPO结算后的最新净索偿不闭合；不叠加预计募集资金
- 10月当前股本、完整员工奖励/可交换债/优先索偿与当前/历史Forward P/E未核验
- 直接ADS报价已闭合；需要KRW盈利转USD模型时仍缺当期汇率，不能用3月方便换算率冒充

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# SKHY / SK hynix Inc. Tracker

Last updated: 2026-07-09

## Current research view

Constructive but watchful. SK hynix 是AI/HBM内存周期的核心受益者，业务质量在存储厂中很突出；但当前折算价约144-145美元/ADS已反映较强乐观预期，安全边际一般。

## Current main thesis

- 公司在2026年Q1 HBM收入份额约56.4%，全球第一；DRAM收入份额约29.1%，全球第二；NAND收入份额约18.5%，全球第二。
- AI训练/推理和数据中心扩张提升对HBM、服务器DRAM、eSSD的需求。
- 与NVIDIA路线图合作、M15X/Yongin/P&T7/Indiana扩产封装计划强化长期供给能力。
- 但存储行业仍是资本密集强周期行业，必须用正常化利润而非单季高峰利润估值。

## Latest update

2026-07-09 deep research completed using SK hynix F-1/A filed 2026-07-06 and Yahoo Chart data for 000660.KS/KRW=X/SKHY metadata. SKHY ADS had metadata but no trading price history at retrieval time, so valuation uses Korean common share 000660.KS折算。每ADS代表0.1普通股。

## Valuation snapshot

- 000660.KS price used: about KRW 2,175,000.
- USD/KRW used: about 1504.48.
- Implied ADS equivalent: about USD 144.6.
- Post-offering common shares: about 728.8655 million per F-1/A.
- Current view: price is in fair-to-slightly-expensive zone, not a strong margin-of-safety entry.

Practical zones:

- Strong margin of safety: below about USD 105/ADS.
- Watch/small starter range: about USD 105-125/ADS.
- Fair but limited margin of safety: about USD 125-155/ADS.
- Expensive/no-add unless bull evidence strengthens: above about USD 170/ADS.

## Key risks

- HBM ASP or demand peaks earlier than expected.
- Samsung/Micron catch up in HBM quality, yield, or customer certification.
- AI capex slows or NVIDIA/cloud customer roadmap changes.
- High capex creates future oversupply.
- Customer concentration: F-1/A says top two customers were 14.8% and 12.4% of Q1 2026 revenue; largest customer was 23.9% of 2025 revenue.
- Geopolitics/export controls involving Korea, U.S., China, and advanced semiconductors.
- ADS newly listed/no trading history at research date may create liquidity and pricing uncertainty.

## Core thesis assumptions that must remain true

- SK hynix remains a top HBM supplier through HBM4/HBM4E.
- HBM demand remains structurally strong beyond one inventory/capex cycle.
- Capex discipline remains rational and does not destroy future pricing.
- Operating cash flow can fund a meaningful part of capex through the cycle.
- Customer relationships with NVIDIA and major cloud/AI infrastructure buyers remain strong.

## Red-line conditions

- HBM share loss or major customer qualification failure.
- DRAM/HBM ASP decline while inventories rise.
- Capex materially increases without matching long-term order visibility.
- Free cash flow turns structurally negative outside planned investment periods.
- ADS trades materially above USD 170 without stronger evidence of sustained bull-case EBITDA.

## Management promises / milestones to follow

- M15X ramp after wafer input began in Q1 2026.
- Yongin phase 1 cleanroom expected Q1 2027.
- P&T7 advanced packaging plant expected by end-2027.
- Indiana advanced packaging plant expected to start operations in H2 2028.
- HBM4E/future DRAM development and NVIDIA collaboration progress.

## Metrics/events to monitor next

- SKHY ADS pricing, first trading, and premium/discount versus 000660.KS.
- Quarterly DRAM/HBM/NAND revenue growth and ASP indicators.
- Gross margin and operating margin after Q1 2026 surge.
- CFO, capex, and FCF.
- Customer concentration and commentary on AI demand.
- Samsung/Micron HBM progress.

## What would change the research view

Upgrade if: follow-on quarters confirm HBM-driven margins, customer commitments strengthen, and price enters a better margin-of-safety zone.

Downgrade if: HBM demand/ASP softens, competitors catch up faster than expected, capex rises into weakening demand, or ADS price rerates far above fundamentals.

## Report links

- deep-research/2026-07-09-deep-research.md
