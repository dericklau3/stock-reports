# SKHY / SK hynix Inc. Tracker

Last updated: 2026-10-15（定向修订估值及相关财务，非全篇新研究）

## Current Research View

**投资观点：**建设性但需观察；正式半年报已取得，正常化盈利估值基础情景约$110–185/ADS，中枢约$143；10月14日常规收盘$147.55接近中枢，非明显低估。ADS只是换算，不是拒绝估值的理由。

## Current Main Thesis

**核心逻辑：**高带宽内存让AI加速器更有效读取数据；客户认证、先进工艺与封装能力支持需求，但扩产和定价仍受存储周期影响。

## Key Risks

**主要风险：**行业扩产或客户需求转弱可使超高利润率迅速回落；ADS比例、发行后股本、融资及非经营收益口径会直接改变每ADS价值。

## Latest Research

[原2026-10-11深研，10月15日已修订估值](deep-research/2026-10-11-deep-research-update.md)；[当前估值输入及来源](https://github.com/dericklau3/stock-reports/blob/main/research/COMPANIES/SKHY/research-records/2026-10-15-valuation-inputs.json)；[真实复算结果](https://github.com/dericklau3/stock-reports/blob/main/research/COMPANIES/SKHY/research-records/2026-10-15-valuation-results.json)；[复算脚本](https://github.com/dericklau3/stock-reports/blob/main/research/COMPANIES/SKHY/research-records/recalculate-2026-10-15.py)。10月11日JSON/validation只代表当时研究，不再是当前估值状态。

## 2026-10-15：用户要求具体ADS价格后的估值修订

### 旧判断 → 新证据 → 改动

- 旧文无法可靠给每ADS值 → 已读取SEC正式半年报全文及合并财务附注，不再沿用受阻状态；ADS结构本身不阻止估值。保留参数不确定性，建立明示假设而不是制造精确保证价。
- 旧价$169.03（10月9日）→ Nasdaq 10月14日纽约常规收盘$147.55；两者是不同日期，不是ADS换算差异。直接交易ADS价无需汇率才能算代理市值；韩元盈利转美元EPS才用汇率。
- 原始SEC官网本次仍403，已通过Yahoo托管的同份SEC半年报全文取回，核对公司、期间及KPMG审阅日期2026-08-14。不是把搜索摘要当财报。最终IPO说明书此次官网403、镜像404，但此次正式半年报期后事项重新确认17790000股普通股、177900000份ADR、每普通股10份ADR及每普通股1490美元发行价，并以股数桥交叉核对。424B4预计净募资仍沿用先前核验记录，不能声称本次重读424B4成功。
- H1归母净利134.150412万亿韩元，但净金融收益76.250778万亿；Q2金融工具估值收益53.237425万亿、股息收入10.027945万亿。新模型从经营利润构造正常化税后归母盈利，排除上述估值变动和异常投资股息，绝不把单季净利乘四。
- H1经营现金流91.742501万亿，现金资本开支18.994016万亿，简式FCF72.748485万亿；扣除计入CFO的投资股息13.983648万亿只余58.764837万亿，仍不是完全正常化FCF。H1账面税费40.056711万亿、实付所得税7.704636万亿，不能直接永久外推现金转化。
- 6月底现金及等价物26.835986万亿、短期金融工具22.397559万亿、短期投资38.724378万亿，加总87.957923万亿不是全部现金；借款18.586634万亿，另租赁负债2.526505万亿。当前税负31.958025万亿及长期投资85.309524万亿说明净现金/投资资产NAV必须另作税后、可用性核查，不能直接把账面资产全加在股权利润法上。
- 附注14确认2023年可交换债H1已全数交换、6月底余额USD0，不能继续作为未偿债和额外未来股数重复扣除。半年报发行股数712702365减库存股1626865=711075500；再加IPO新增普通股17790000=728865500。未来模型取750000000股，额外约2.9%为研究者稀释预留而非当前已验证股本；SBC不加回经营利润。
- 10月14日最新6-K只确认第三季度电话会：10月28日09:00首尔/08:00北京；没有把尚未披露的Q3财务数字作为模型事实。

### 估值模型与假设边界

- 估值基准日2026-10-15；目标2028-12-31，期限808天/365.25=2.212183436年；折现率12%，折现因子1.284929484。
- 每ADS=0.1普通股；预测摊薄普通股7.50亿，对应75亿ADS等值经济份额，不是声称75亿ADS已实际发行。汇率采用10月14日ECB参考值1USD=1336.79KRW，经Frankfurter取回；不是未来汇率预测或成交汇率。
- 算式：正常化归母净利=(预测年收入×经营利润率+正常净利息收入0.35万亿KRW)×(1−税率)×99.9%；每ADS美元EPS=归母净利KRW÷预测普通股×0.1÷KRW/USD；今日每ADS价值=EPS×情景P/E÷折现因子。净利息0.35近似H1利息收入减费用年化0.343960万亿，不资本化估值收益、汇兑/衍生品收益或异常股息。
- 保守：2028正常化收入240–270万亿、经营利润率25–30%、税28%、P/E12–14；精确现值40.4346–63.5887，展示约$40–65/ADS。
- 基础：收入300–360万亿、经营利润率40–45%、税27%、P/E16–20；精确现值109.0061–183.8091，展示约$110–185，中间经营假设/P-E18得143.2658。基础收入围绕Q2单季年化317.275万亿上下，利润率明显低于Q2的76.3%；因此不是把高峰直接永久化。倍数为研究判断，对HBM领先给予溢价，不冒充市场一致预测或历史估值分位。
- 乐观：收入400–440万亿、经营利润率50–55%、税27%、P/E20–22；精确现值226.8318–301.8216，展示约$225–305。要求扩量、领先份额和现金回报同时成立，不能仅凭长期协议新闻上调。
- 未折现的2028年底价格情景分别约$52–82、$140–236、$291–388，与今天的价值严格区分。价格差不含股息/费用/税，不是保证收益；没有人为设定发生概率或概率加权目标价。
- 这是股权正常化盈利能力法，不是完整资产分拆NAV/DCF；不再额外加净现金、预计IPO募资或投资持仓价值。独立投资资产税后可变现NAV有可能改变更完整SOTP结果，不能暗中把它塞进上沿。
- 基础中枢143.2658对比147.55低约2.90%；反向看，P/E18、同一折现/股数/汇率下，支持现价需要正常化归母年净利约105.602万亿KRW，略高于基础中间假设102.535万亿。
- 敏感性：KRW/USD上升10%（韩元走弱）时基础中枢约130.24，下降10%时约159.18；股数8亿时约134.31；折现10%约149.09、15%约135.13；P/E每变动1倍影响约7.96美元。由此可见ADS换算可准确处理，盈利、倍数、现金转化和外汇才是真正不确定项。
- 现金检验：P/E隐含盈利可转为股东现金。基础年收入每额外1%长期再投资/营运资金占用即约3.3万亿KRW年度现金需求；如果资本开支持续远超折旧、现金转化恶化或需要超出预留的新股融资，应下调倍数/利润或加大股数，而非维持价格不动。资本建设募资不能无条件当可分配现金。
- 当前/一年历史市场NTM Forward P/E未独立闭合；现价÷自建2028正常化EPS12.5–16.9倍只是模型比值，不能拿它冒充市场Forward P/E，更不能用今天预测回填历史。

复算命令：`python research/COMPANIES/SKHY/research-records/recalculate-2026-10-15.py`；原始输入、来源URL/实际读取镜像、保存原件与SHA256清单均见10月15日研究记录。旧价格带未直接复用，只保留在下方历史档案。

**以下2026-10-11及7月记录均为历史，已由上述10月15日修订替代；保留原文以追踪变更。**

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
