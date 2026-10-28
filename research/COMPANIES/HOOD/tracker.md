# Robinhood Markets（HOOD）Tracker

Last updated: 2026-10-28

## Current Research View（2026-10-28，美国Q3财报后）

**投资观点：中性偏谨慎。** Gold、净入金与事件合约增长真实，但Q3加密收入同比−55%，归属净利润同比−16%，信用准备同比+173%，估值对盈利修复有较高要求。使用2026-10-27常规收盘价**$94.56**（美东16:00），不混用10/28盘前报价。

**核心逻辑：** 2026-10-27公告2026Q3收入**$1,424m**、归属净利**$468m**、Gold **5.2m**、有资客户**28.7m**、Q3净入金**$15.7bn**，事件合约收入**$173m**、期权**$399m**，加密**$120m**。实际每股价值取决于正常化税后归属利润、信用风险及未来经济稀释，而非托管资产或名义交易量。

**主要风险：** 预测市场SEC/CFTC及各州/部落法律规则、Q3信用损失准备**$71m**、加密/利息周期、RVI非经营公允价值损益、2029年**$2.2bn**可转债本金、SBC和未来稀释。账面客户隔离现金不属于普通股自由现金。

**最新完整财务：** 2026Q3（9/30期末、10/27披露）。TTM收入**$5,082m**、归属净利**$1,984m**、经营现金流**$3,046m**，设备/资本化软件现金投资**$76m**，差额$2,970m **不是金融机构可分配自由现金流**。9/30现金5829m、segregated cash/securities 13443m、restricted42m、长期借款2660m；9/30法定经济股A793m+B108m=901m，不能当作10/27完全稀释的实时股数。

**2026-10-28估值（2027-12-31目标、12%股权折现的P0股权归属正常化净利退出PE条件现值）：** 保守**$19.16–34.55**、基础**$48.57–72.37**（中枢研究假设**$61.11**）、乐观**$89.35–133.97**。不是公司指导价、市场共识或完整多阶段DCF；当前参考价94.56美元高于基础情景上限。按2027收入7.0bn、950m经济股和33倍市盈率反推，该市价要求约3.11bn税后归属利润或44.4%净利率。数值由程序实现原P0公式复算，但**原仓库Python估值引擎和P2冻结未在本次会话运行**。

**当前报告**：[2026-10-28完整九章研究](deep-research/2026-10-28-deep-research.md) | [核验、事件覆盖及复算底稿](research-records/2026-10-28-research.md) | [估值输入](research-records/2026-10-28-valuation-input.json) | [估值输出](research-records/2026-10-28-valuation-output.json)。旧报告保留：[2026-10-20完整研究](deep-research/2026-10-20-deep-research.md)。

## 2026-10-28 新事实与 2026-10-20 基线变化

| 项目 | 旧假设/已知（2026-10-20） | 新事实及公告 | 对当前研究影响 |
|---|---|---|---|
| 股价 | 2026-10-19常规收盘$96.52 | 2026-10-27常规收盘$94.56（[价格来源](https://stockanalysis.com/stocks/hood/history/)） | −$1.96/约−2.03%，盘后披露Q3业绩不可视作已反映于常规收盘 |
| 盈利 | 以Q2为最新，TTM收入4932m/归属净利润2072m | [2026-10-27 Q3财报](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-third-quarter-2026-results)：TTM收入5082m/归属净利1984m | 收入增长但归属利润更弱，重新审视RVI、坏账、税和交易组合 |
| Gold与业务 | Q2 Gold4.84m、事件Q2收入156m、8月crypto交易量偏弱 | Q3 Gold5.2m、事件173m、期权399m、crypto收入120m同比−55% | 真实用户采用不等于利润每股稳定增长 |
| 信贷融资 | Q2坏账准备56m、可转本金2200m/2029 | Q3坏账准备71m，同比+173%；9/30 long-term borrowing 2660m | Q3完整融资附注/信用净核销与客户隔离资本待核 |
| 估值 | 2027基础条件现值54.98–78.75 | 重新计算基础48.57–72.37，基准日10/28 | 价格、Q3利润与假设都变，不能把差异归于行情 alone |
| 预测复盘 | 2027目标尚未到来 | 2026-10-28仍未到目标 | 不编造命中率、未来市盈率历史区间和上市/监管成效 |

**未完成的实证检查：** 近12个月IR/SEC全部公告与伙伴官方资料、SEC/Cboe最终KPI许可批文、州和部落docket、Q3 10-Q信托/证券融资资本桥、当日真实经济股和分部归属利润尚未全面核实。正式估值复核应运行仓库原 valuation_engine.py 与 P2 freeze、审查历史当时有效的Forward PE，不能把独立数值输出当全部技能自动验收。

---

## 历史归档：2026-10-20及更早研究（以下保留原文）



## Historical Research View (2026-10-20)

**投资观点：中性偏谨慎（2026-10-20）。** 客户净入金/Gold/专业产品扩张仍有真实增长；但股价即使从10/09 $109.02降至10/19 $96.52（−11.47%），仍高于本次FY2027基础情景折现现值上沿约$79，不能将降价直接等同安全边际。

## Historical Main Thesis (2026-10-20)

**核心逻辑：** 有证据的客户增长是Q2 Gold4.84m、8月客户资产$384bn及LTM净入金$74.1bn；但交易收入容易受加密/事件合约成交周期影响，银行和信用卡资金有不同风险。以风险调整后的**归属正常化净利润/每股资本**而非客户AUC衡量价值。

## Historical Risks (2026-10-20)

**主要风险：** 8月事件合约量MoM−23%、加密量YoY−38%；Cboe KPI推出许可监管与各州/部落博彩法诉讼；H1信用准备$92m vs $52m；母公司2029 $2.2bn零息可转债、信用卡信托$959m融资及SBC/权证股份，不能把所有客户资产当自由现金。

## Historical Research Links (2026-10-20)

[2026-10-20九章完整深研](deep-research/2026-10-20-deep-research.md)；[2026-10-20来源、重大事件及情景复算底稿](research-records/2026-10-20-research.md)。历史：[2026-10-11研究](deep-research/2026-10-11-deep-research-update.md)、[旧计算JSON](research-records/2026-10-11-research.json)、[旧验收](research-records/2026-10-11-validation.json)。

## 2026-10-20 全新完整深研及变化记录（保留10/11、5/12旧版）

**完整版**：[2026-10-20九章深度研究](deep-research/2026-10-20-deep-research.md)；**完整底稿**：[2026-10-20原始文书核验、事件时间线、GAAP现金和估值计算](research-records/2026-10-20-research.md)。

| 稳定项目 | 上版2026-10-11研究基线/旧承诺 | 2026-10-20新事实与发生/公告日期 | 投资观点/估值影响 |
|---|---|---|---|
| 股票报价 | 10/09 Nasdaq regular close**$109.02**、Q2 A790m/B109m=899m旧市值$98.009bn | 10/19 16:00 EDT **$96.52** StockAnalysis/Investing/Yahoo，ChartExchange $96.50于15:59:56，差$0.02；A790m+B109m=899m取6/30快照 | 价格**−11.465786%**，代理市值**$86.77148bn**。10/19最新股数未核对，不把Q2 diluted weighted912m当现时股数，也不只计算交易A类 |
| Q2财报和现金 | 2026Q2 $1308m revenue、$561m归属公司利润、H1收入$2375m，旧全文10-Q未完整取得 | 本轮读取**[2026Q2 SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000114/hood-20260630.htm)**财务、Notes4/7/11–15。TTM revenue**$4932m**、operating-diff**$2270m**、attributable NI**$2072m**、CFO**$245m**、cash PPE+software**$67m** | TTM CFO−设备$178m受用户应收/证券融资剧变，**不是制造业可派FCF**；Q2 other income net$135m包括RVI退出并表$106m和股票$23m，税前不得粗暴减除称adjusted net |
| Gold与客户资金 | Q2 Gold4.8m、资产$369bn，旧8月月报引用缓存、未查9月更新 | Q2真实Gold**4.84m**同比+39%、ARPU$187、资产$368.7bn、净入金$21.7bn；[9/10正式8月月报](https://investors.robinhood.com/news-releases/news-release-details/robinhood-markets-inc-reports-august-2026-operating-data)8月funded28.6m、AUC$384bn、单月净入金$4.0bn、LTM净入金$74.1bn。9/28 [月内交易color](https://investors.robinhood.com/events/event-details/robinhood-shares-selected-september-month-date-trading-color)不是完整9月报 | 真实客户留存/资金投入，但客户资产不能当集团现金；下次Q3净入金扣市价收益、Gold续费和真实净收入 |
| 期权/crypto/event周期 | Q2 event revenue$156m，权益和期权交易活跃 | 8月权益$335.4bn同比+68%，期权292.5m份同比+50%；crypto **$17.5bn同比−38%**（App$7.4bn+Bitstamp$10.1bn，总和不能再叠加），events**4.7bn份环比−23%**仍同比约15x | 交易热度波动与盈利倍数同时风险增加，不从单月成交名义乘交易手续费猜Q3 GAAP利润 |
| Rothera/SIG合营与监管 | 旧研究仅泛说事件合约增长、州法/联邦监管 | [10-Q业务和法务](https://www.sec.gov/Archives/edgar/data/1783879/000178387926000114/hood-20260630.htm)2025-11成立SIG合营Rothera，2026-01-20控股MIAXdx 90%；公司卷入NV、NJ、MA、MI、WA和部落诉讼，监管结果并非全面豁免 | 增加vertical infrastructure有价值，但最终利润和合规资本未知；不能不计少数股权/合规责任 |
| HOOD Summit和Cboe新KPI | 旧10/11未将9月大会分阶段新产品原文核查 | 2026-09-29 [Robinhood官方](https://robinhood.com/newsroom/hood-summit-2026/)Agents/Apps/Social、合格用户crypto perpetual分阶段rollout、24/7周末美股为未来计划；2026-09-30 [Cboe](https://ir.cboe.com/news/news-details/2026/Cboe-and-Robinhood-Announce-Planned-Launch-of-New-KPI-Contracts-Further-Expanding-Prediction-Market-Offerings/default.aspx)23家公司KPI二元期权在SEC框架拟10月上线，**9/30明确subject to approval**；10/16媒体称已核准但无SEC原令 | 产品发布/开放用户和产生收费三个阶段不能混。下次验证正式监管批文、合约首成交/清算和风险成本 |
| 客户信用卡与银行融资 | 旧仅知“Credit Card Funding Trust/经营设施”未读全注 | 2026Q2 Note11：**六条循环借款承诺$1.55bn**、卡应收净$1.1bn、截至6/30信用信托借款本金利息**$959m**、SOFR+130–150bp、利率加权5.06%；7/23信托$500m ABS、4.86%固定加权票息；Coastal Bank表外214m应收 | 信托债权通常限于信托资产，并非母公司通用无抵押贷款；也不是无成本资金。H1坏账准备$92m同比+77%是净利率风险 |
| 零息可转债/稀释 | 6月发$2.2bn 2029、旧缓存资本公式信息未完全闭合 | **10-Q Note11**确认2029-10-01到期、本金$2.2bn/账面$2.170bn、转股价$174.42、理论12.6m股、capped-call花$123.2m/保护上限$237.85、当次募资$290m现金买回约2.7m Class A；Note14操作租赁现值**$219m**，**无财务租赁**；另8.74m历史warrant行权$26.60、RSU未归属9m | $96.52转价以下本期不急迫，但仍要归还现金本金，且未来股/期权和SBC导致完全稀释不应只用法律899m。10月经济股、治理Form4未完整审计 |
| 海外/私募及政府服务 | Q2已列部分新业务，但各交易阶段需要区分 | 2026-06-01 [WonderFi已交割](https://robinhood.com/newsroom/robinhood-enters-canada-completes-acquisition-wonderfi/)，2026-03-06 RVI封闭基金IPO并Q2退出并表，2026-04宣布Trump Accounts并2026-07-04正式上线 | 真实产品扩张不是传统经纪手续费增量全归HOOD的证明；RVI收益不能持续年化 |
| 2027模型与市场预期 | 旧2027假设Bear/Base/Bull收入4.8/5.8/7.5bn、归属净利率25/35/40%、PE25/35/40、股920/950/980m；旧PV约28.39/65.12/106.62，旧股价109.02 | 2026-10-14 [第三方FY2027 revenue约$6.85bn、nonGAAP EPS $3.43](https://stockanalysis.com/stocks/hood/forecast/)，将其作为更新基础收入锚；新2027压力端点Bear收入5.4–5.8bn/净利率22–26%/PE22–26/940–950m→PV**$24.02–36.42**，Base6.5–7.2bn/31–35%/PE30–34/950–960m→**$54.98–78.75**，Bull8–9bn/37–40%/PE38–43/960–975m→**$100.74–140.80** | **中性偏谨慎**，现价$96.52高于基础情景上限，接近乐观下限；公司实际总利润高增长但RVI及市场周期不能支持无限倍数 |

### 更新的财务时间和估值纪律

- **财务表单位USDm GAAP**：FY2024/FY2025/H12025/H12026/TTM净收入**2951/4473/1916/2375/4932**，费用**1897/2379/1107/1390/2662**，经营差额**1054/2094/809/985/2270**，归属净利**1411/1883/722/911/2072**，经营现金**−157/1638/4151/2758/245**，毛设备+资本化软件现金**50/54/29/42/67**，简化现金差额**−207/1584/4122/2716/178**。TTM=FY2025+H12026−H12025。金融经纪信托业务的现金流剧烈受客户应付与证券借贷影响，最后一行不能当自由可分配FCF。
- **Q2业绩**：[公司公告](https://investors.robinhood.com/news-releases/news-release-details/robinhood-reports-second-quarter-2026-results)Q2总收入1308、transaction776、netinterest389、other143、attrNI561、nonGAAP adjustedEBITDA741；单季gain106m deconsolidation+23m equity gains税前属于非经营，不做利润率前瞻的常态。
- **债务隔离/现金**：6/30 cash**$5362m**、segregated cash+securities**$12023m**、restricted**$62m**；客户AUC不是母公司现金；RHM note持有2029可转$2200m本金、账面$2170m；信用卡Trust借款与承诺和ABS融资不是母公司同一债券的第二份；经营租赁PV219m，无fin leases。10月不同来源资产负债的完整发行变动未闭合。
- **稀释与治理**：法定A790m B109m C0，10/19价96.52代理市值$86.77148bn；Q2 diluted weighted912m非当日股本；公司8.74m权证/9m RSUs已未归属、2029可转潜在12.6m股属于不同价格/触发，未来预计股940–975m为**经济稀释缓冲研究者假设**，不是只把这些数全加或直接承认“0稀释”。
- **估值年份与数学**：研究10/20至2027-12-31剩余**1.196440794年**、折现**1.12^t≈1.145213477**、所有端点采用`2027正常化归属净利润×exit PE÷未来经济股数÷1.145213477`。情景估值Bear24.02–36.42/Base54.98–78.75/Bull100.74–140.80（USD/share现值）。公司保守稳态净利需同时覆盖信用卡坏账、监管、员工报酬与合理税/资金成本，预测净利率22–40%是模型假设，不是管理层指引。
- **反向估值**：以2027 BaseHigh，未来股950m、PE34与discount 1.145213477，现价96.52需2027归属正常化净利润**$3088.506m**（7.2bn收入的**42.896%**）；净利率只有35%则需收入**$8.824bn**，明显超2026-10-14时FY2027分析师平均$6.85bn。BaseHigh归属净利率变化1百分点⇒现值每股约**$2.25**，股数额外多5%⇒价值跌4.76%。
- **历史Forward PE**：数据商10/14 FY2026 adjusted EPS2.55、FY2027 adjusted EPS3.43，按10/19 price静态分母约37.85×/28.14×，但不是同日完全对齐或GAAP。**过去一年日频当时有效同口径Forward PE高低未核实**，不可编/按今天EPS回算历史峰谷。
- **下次触发**：10/27美东17:00 Q3（[官方确认](https://investors.robinhood.com/events/event-details/robinhood-q3-2026-earnings)）、KPI二元合同SEC核准/上市日期和单项收入、秋季/选举事件合约监管、下一完整月报、信用风险、真实A+B净股数。上修须客户净入金即使市场行情下行仍正增长且Gold/投顾对归属正常化利润持续贡献、坏账趋稳、规则稳定；下修为期权/crypto和事件合约收入长期衰退、监管限制、信用损失吞噬毛收入或经济股数快于盈利增加。
- **未完成核验**：近12月所有SEC8-K及州/部落docket、9/28月内摘要全文数字、SEC对Cboe新KPI产品的最终审批原件、2026-10-19所有真实流通股及2029完整转换场景/税后资本分配、完整360日日频时点有效Forward PE预测，不能宣称已经全部覆盖。旧版原文下方保留。

---

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
