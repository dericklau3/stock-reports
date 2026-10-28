# Alphabet（GOOG）Tracker

Last updated: 2026-10-29

## Current Research View｜Q3 2026 披露后完整深研

**投资观点：中性偏建设性、现金流与资本结构须继续验证。** 2026Q3 Cloud收入$30.709bn同比+103%、分部经营利润$11.121bn，搜索和广告稳定；但Q3自由现金流**−$9.065bn**、Q2**−$5.855bn**，全年2026 CapEx仍计划$195–205bn且2027预计显著增加；2026Q3财报后盘后股价回撤并不自动证明内在价值便宜。

**核心逻辑：** 2026Q3收入**$127.577bn +25%**、经营利润**$40.576bn +30%**。Q3 Search$63.350bn+12%，AI查询确实增加；Cloud TPU系统收入强劲，但必须在计算外购、设备折旧、电力、研发和资本现金之后才能确认股东回报。Gemini App10亿用户、模型API 320亿 tokens/分钟与YouTube 1.5亿订阅（含试用）是使用采用证据，**不是独立归属净利**。

**主要风险：** 搜索/广告技术反垄断救济、AI推理每次查询成本、2027高资本投入和GPU/电力采购合同、2026Q3股权证券价格造成报表盈利波动、Q3增发股票与债券及2029强制可转优先股、Waymo债权人和少数股东的价值索偿。

**最新财务及市价时点：** Q3/9M期末2026-09-30；**2026-10-28美东16:04公布的SEC Exhibit 99.1**，**Q3 10-Q完整附注暂未核实**。[Q3原始文件](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)。GOOG 2026-10-28**常规收盘$321.89**（当日财报公布前），GOOGL常规收盘$324.89；财报后GOOG 17:11 EDT盘后单次约$289.74。旧基线10/19 GOOG收盘$340.16，当前报告不将盘后报价混入常规收盘估值。

**2026Q3 TTM**：收入**$471.098bn**、毛利**$286.698bn**、GAAP经营利润**$156.976bn**、归属普通股GAAP净利**$235.310bn**（严重受Q2投资浮盈抬高、Q3证券损失−$8.664bn），OCF**$179.551bn**、现金CapEx**$159.804bn**、TTM FCF**$19.747bn**。9M2026 FCF**−$4.804bn**。9/30实际普通A5888m+B828m+C5578m=**12294m**，与Q3 EPS加权稀释股12368m不是同一分母；现金及市场证券$265.098bn、债务$125.102bn、2029强制可转优先股清算面额约$19.25bn；证券资产含非现金股权投资，不能等同完全可分配现金。

**最新2028条件估值**：2026-10-29至2028-12-31折现2.17385年、研究者股权资本必要回报率12%、归属普通股**正常化税后净利润**（剔非经常投资证券估值变动，含SBC/税/利息/优先股息）×2028退出P/E÷未来经济股。保守**$113.22–164.92**、基础**$210.64–318.91**（独立中枢**$250.43**）、乐观**$393.56–619.06**。基准为321.89 regular close，见财报后盘后289.74属于不同交易时段；三档情景**不是公司指引、分析师目标价或完整现金流贴现结果**。旧2026-10-20估值使用Enterprise EV/EBIT（基础$275.60–368.86），本次使用equity_pe并根据Q3新财报、股份和资本成本重设，**不能把估值差异归因于仅仅股价**。计算按公开P0公式由独立程序复算，原仓库Python引擎和P2 freeze在本次会话未运行，已列为验收缺口；不能假装已认证。

**本次交付**：
- [2026-10-29完整九章研究](deep-research/2026-10-29-deep-research.md)
- [2026-10-29原始资料、全部事件候选/缺口和估值复算底稿](research-records/2026-10-29-research.md)
- [2026-10-29估值条件JSON](research-records/2026-10-29-valuation-input.json)
- [2026-10-29程序数值输出JSON](research-records/2026-10-29-valuation-output.json)
- [2026-10-20历史报告](deep-research/2026-10-20-deep-research.md)（旧报告原文未改）

## 2026-10-29 相对2026-10-20研究的变化记录

| 项目 | 10月20日旧已知/假设 | 新证据与日期 | 估值与下一验证 |
|---|---|---|---|
| 报价 | GOOG 10/19 $340.16 regular close | GOOG 10/28 **$321.89 regular close**；财报后盘后17:11约289.74 | 市场时段/日期需一致，不能用盘后盘价与旧regular价算纯模型差 |
| Q3财务 | 旧Q2 TTM收入$445.866bn、经营利$147.628bn、FCF$53.273bn | 2026-10-28公告Q3后TTM**收入471.098bn /营业156.976bn/FCF19.747bn** | 经营增长，现金回报恶化；2027 CapEx风险更显著 |
| Search/Cloud | Q2 Search收入+17%、Cloud+82%，分部EBIT8.814bn | Q3 Search同比**+12%**、Cloud**+103%**，EBIT**$11.121bn** | 搜索广告同比增速回落；Cloud高成长需确认包含TPU系统/并购贡献、总部AI支出及后续回款 |
| 普通股与融资 | 2026-07-15实际12230m普通股；截至6/30 ATM $40bn未用，债务100.164bn | **9/30实际12294m**，Q3卖A12m+C24m净现金12.4bn，ATM剩**$27.6bn**，债125.102bn，Q3新无抵押债净发28.7bn | 股票与债券不是免费资本；未来稀释需调和股权激励/2029强制可转优先股 |
| 资产证券和优先 | 6月现金+市价证券242.474bn、其中可交易股票87.063bn，优先清算19.25bn | 9月现金及市价证券265.098bn、Q3股权证券公允价值净亏8.664bn；9M GAAP其他收入127.478bn | Q3股票/债券市场证券具体拆分未完整10-Q复核；不能用GAAP NI直接当稳定税后净利 |
| 投资现金 | H1 CapEx80.598bn、FCF4.261bn；FY26目标195–205bn | 9M CapEx131.953bn，Q3 CapEx51.355bn、FCF−9.065bn；Q3电话会维持FY26范围、预计27继续升 | 2026Q4为达旧指引还需CapEx约63.047–73.047bn（推算不是发生事实），2027需核可用资金与ROIC |
| 估值 | 2026-10-20 P0 enterprise_ebit Base275.60–368.86 | 2026-10-29 P0 equity_pe Base210.64–318.91，终期2028、方法变更，正常化净利率23–27%，PE24–28、未来股12.60–12.70bn | 不能平均不同口径模型；Q3 10-Q+多期FCF/FCFE及非经营股权NAV是尚缺主导敏感性 |
| 历史目标 | 2028预测未到期 | 2026-10-29依然未到期 | P2真实模型命中率不能凭行情倒推创造 |

**下一验证与反证：** Q3正式10-Q、美国/欧洲司法救济执行、TPU真实交付与Wiz有机/收购贡献、Q4 FY26现金资本开支、2027具体新指引、2026Q4 ATM新增股份与偿债、AI计算使用云分部整体股权现金贡献、Waymo对外借款后少数/母公司收益桥。完整近12个月SEC/合作方/司法发现**有披露缺口**，报告和底稿已标注；继续研究不得声明已穷尽。

---

## Historical research archived verbatim as of 2026-10-20



## Current Research View

- **投资观点：中性偏建设性、仍无厚安全边际。** Search和Cloud有真实利润且Gemini4已面向付费应用发布；价格从10/9的$347.86降至10/19的$340.16，但最新正式capex指引已达$195–205bn/年，GAAP EPS高受股权证券未实现盈利影响，资本/股本索偿仍需核验。

## Current Main Thesis

- **核心逻辑：** 广告商与Google Cloud客户确实持续付费，Cloud季度$24.768bn+82%、EBIT$8.814bn；Gemini4、TPU、Waymo增加增长机会。最终长期价值在AI推理、外购SpaceX算力、电力合同/固定供应、折旧、优先股及经营现金之后。

## Key Risks

- **主要风险：** 2026Q2 GAAP其他收入约$98bn并非稳定营业收入；H1 FCF仅$4.261bn，截止6/30全部重大采购合同义务$811bn（固定供应/能源$707bn为相关子集而非额外可加）；9月AdX/DFP被法院下令开放竞价，2029优先股可能转股、未来ATM可能稀释。

## Latest Research

[2026-10-20完整深研](deep-research/2026-10-20-deep-research.md)；[当日证据来源、资本结构与估值计算](research-records/2026-10-20-research.md)。历史：[2026-10-11深研](deep-research/2026-10-11-deep-research-update.md)及[旧复算JSON](research-records/2026-10-11-research.json)。

## 2026-10-20 新完整深度研究（保留2026-10-11及更早原文）

**完整新报告**：[2026-10-20](deep-research/2026-10-20-deep-research.md)，**研究核验与可复算底稿**：[2026-10-20研究原始记录](research-records/2026-10-20-research.md)。

### 旧论点/时间 → 新事实/日期 → 当前判断变化

| 项目 | 旧2026-10-11研究基线 | 2026-10-20最新证据 | 影响 |
|---|---|---|---|
| GOOG报价与股本 | 10/9常规收盘$347.86；7/15 A5868m+B835m+C5527m总12230m经济股；旧市值代理$4.254T | 10/19 16:00 EDT常规收盘**GOOG $340.16**、**GOOGL $344.18**，C价-2.2135%；ChartExchange有$340.07差9美分 | 新按三类报价A×344.18、B/C×340.16市值代理**$4.183746T**；比全用C价$4.160157T多$23.589bn。10月真实全部在外股数/ATM尚未独立核实 |
| 观点 | 中性等待；业务强但FCF吃紧 | Gemini4真实发布，Google Search/Q2Cloud正增长、Waymo新贷为经营扩展提供资金；近期股价降2.2% | **中性偏建设性、并非完全看多**：新产品和现金投放带来机会，但资本承诺与估值仍缺厚安全边际 |
| Search/广告救济 | 旧10/11研究对9/16广告技术法院最新救济未取原文 | 2026-09-16 [美国DOJ](https://www.justice.gov/index.php/opa/pr/department-justice-again-wins-substantial-relief-against-google)确认法院命令AdX/DFP集成Prebid、非歧视AdWords竞价、开放数据、六年监督，**未要求资产整体拆分**；10/13 [DOJ搜索案件](https://www.justice.gov/atr/case/us-and-plaintiff-states-v-google-llc)新增授权模板 | 不再写成等待判决，也不称全面胜诉；未来TAC、广告技术竞争和分发收入真实受救济影响 |
| Gemini4与模型业务 | Q2模型升级需要实证 | 2026-10-13 Google发布[Gemini 4 Argon](https://blog.google/intl/en-mena/product-updates/explore-get-answers/gemini-4-argon-built-to-solve-your-hardest-problems/)，API收费初始输入$2/million tokens、输出$10/million；Gemini Pro/Ultra与Search AI Mode可用 | 技术产品上线+明确付费路径；尚无独立该模型收入、净现金、留存，不仅凭benchmarks上调2028利润率 |
| GoogleCloud/TPU | Q2 Cloud$24.768bn+82%、营业利润$8.814bn、backlog$519.5bn，旧研究已取得 | 再核10-Q：总RPO$519.5bn、Cloud$513.9bn；Q2 TPU系统开始交付客户自有机房，7/22电话会称大部分现有协议收入2027才确认，Q3用第三方cloud capacity会带来短期margin压力 | 真实增长不等于完整回款；必须跟踪2027交付、折旧、合同收入与Fcf |
| 外购算力 | 旧报告“能源扩容”但未列实际巨大SpaceX算力采购 | 2026-06-05 [SpaceX SEC Rule433](https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm)：2026-10起**Google付SpaceX $920m每月**至2029-06（110,000 GPU），有供货不达标下调条款与2026-12-31后提前终止权 | 是**Google支出**，不是销售收入；需内部或转租实际回收，且GOOG持有SpaceX权益浮盈与供应商风险相关 |
| 电力供应 | Q2新增长期能源和供应承诺 | 2026-10-14 [AEP公告](https://www.aep.com/news/stories/view/12314/)拟投资约$4bn、702MW产能，Google采购20年PPA，2028年底目标正式供电 | 4bn为**AEP的**资本开支，不可写GOOG capex；2028之前不是已投运容量，Google有未来购电成本 |
| Waymo资本结构 | Q2已披露城市运营和Waymo业务，其他赌注未有稳定利润 | 2026-02 [Waymo外部16bn equity](https://waymo.com/blog/2026/02/waymo-raises-usd16-billion-investment-round/)、投后估值约$126bn；2026-10-08 [首次5bn贷款](https://waymo.com/blog/2026/10/waymo-closes-5-billion-debt-financing/)，9月15个美国城市；10/19 Semafor“20k车队”仅匿名来源Waymo未确认 | 债权人及Waymo少数股东有索偿，扩张计划不等于2027利润；10月新贷不得谎称已体现在6/30报表中，也不把Waymo整体估值再加上市母公司全价 |
| FY2026CapEx与营运现金 | 旧报告认为2026旧范围$180–190bn未核最新 | Q2 2026 CFO在7/22财报电话会正式**调高为$195–205bn**，2027仍预期显著增加；H1 capex$80.598bn、FCF$4.261bn，Q2单季约**−$5.9bn** | 旧指引作废，新模型须留经营再投资缓冲及现金支出，H1 GAAP盈利不是自由现金 |
| 承诺、担保与现金 | 老版现金marketables$242.474bn、供应/能源fixed$707bn、债务$100.164bn和preferred清算$19.25bn | Q2 10-Q同时给出**全类重大采购及其他合同义务$811.0bn**，含短期$200.7bn，$707bn为**其中固定/保证供应及电力子集**；金融担保/信用衍生潜在最高$7.6bn/$43.8bn；可变现证券含marketable equity$87.063bn | 不能把811+707相加，也不把全部担保当债或股权证券浮盈当固定现金；本次估值现金桥保守只采用现金及可交易债券$155.411bn |
| 2028估值模型 | 2026-10-11现值bear$129–186/base$282–375/bull$462–603，企业价值模型采用$242.474bn含股权投资作为现金基础 | 截止2026-10-20，剩余至2028-12-31 **2.198494年**，相同研究者营收/EBIT率/退出倍数/未来股份假设，剔出$87.063bn股权市值并重新贴现（见研究底稿） | bear现值**$122.89–179.59**、base**$275.60–368.86**、bull**$455.67–596.97**；当前$340.16在基础区间上部，安全边际不厚，财务股本/资本责任未全封闭 |

### 新财务、现金、融资及每股索偿备查（USD million）

- 2026FY latest reporting **2026Q2 10-Q 6/30**，[官方10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm)，[2025年10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm)；截至2026-10-20 Q3正式利润未公布，市场日历10/28，不称已兑现。
- FY2024 / FY2025 / H12025 / H12026 / TTM（USDm）：
  - 营收**350018 / 402836 / 186662 / 229692 / 445866**；
  - 毛利**203712 / 240301 / 111262 / 142478 / 271517**；
  - GAAP经营**112390 / 129039 / 61877 / 80466 / 147628**；
  - GAAP普通股应占净利润**100118 / 132170 / 62736 / 174685 / 244119**；
  - 经营现金流**125299 / 164713 / 63897 / 84859 / 185675**；
  - 现金资本开支**52535 / 91447 / 39643 / 80598 / 132402**；
  - 简化FCF **72764 / 73266 / 24254 / 4261 / 53273**。
- **GAAP收益污染**：Q2其他收益净额约$98000m，主要来自投资证券未实现收益；Q2 total NI $112193m/归属普通股$112107m高于集团operating $40770m，**TTM普通利润$244119m不代表正常化主营持续盈利**。TTM历史PE按三类市值约17.14×，P/简化FCF约78.53×，不是同一概念。
- **股本**：7/15 A5868m B835m C5527m 合12230m经济股；C无投票、A有投票、B强化投票；普通股Q2 EPS稀释平均12309m不是同日股本。优先存托385m对应19.25m强制可转优先（清算$19250m、6.25%年累积$1203.125m），2029约转普通43.56275–54.45825m；2028模型既扣未转优先索偿又不纳同批转股分母，适当处理封顶看涨合同。H1 SBC$14708m纳入GAAP EBIT，未来经济股数变化另外预估。
- **资产负债及或有义务**：6/30现金+市场证券$242474m，但含上市股权证券$87063m、保守安全现金及债券155411m；借款$100164m、finance leases$2590m、operating leases$18037m、未起租未来$85200m和短期约$5800m。全类未来采购承诺$811000m（其中短期$200700m），固定/担保长期能源供应$707000m为子集；或有信用背书$7600m+衍生风险max$43800m，不应一次性当已到期借款。2026H1没有普通股回购，6月净新募$49600m（普通股含Berkshire$10bn和强制转preferred）；新ATM最多$40000m，截至6/30未用**不能假定10月未用**。2026-10 Waymo新借$5000m、未来更高资本要求须Q3复核。
- **保守同一时点企业资本桥**：`155411-80000(研究保留金)-100164-2590-19250-2386.325(PV优先股股息)≈-48979.325m`；2028企业终值先用10% 2.198494年折现，再加同日可分配现金扣债及preferred索偿、除2028经济股数，不计额外市场股票/Waymo公司整体投后价值，不将$811bn承诺全部作为债务重复扣除。
- **反向估值**：GOOG $340.16、基础高端2028 12500m股份、退出EV/EBIT26、10%折现2.198494年及上述净−48979.325m bridge，要求2028退出企业价值**$5303.578bn**、营业利润**$203.984bn**，对应2028营收650bn下EBIT率**31.382%**；若margin34%则收入约**$599.952bn**。退出倍数降至20、相同收入条件下则需要40.797% EBIT率。具体来源、全部端点和计算见research-records/2026-10-20-research.md。
- **改判**：升级=Search每次查询扣AI推理成本后的盈利更好、Cloud RPO 变成可复算EBIT/OCF、2026Q3 FCF同比修复并支撑下年资本开支、DOJ救济没有严重冲击广告TAC、稀释被经营毛利吸收。降级=更多资本开支和第三方租费、广告监管导致结构性利润下降、股票持仓重新估值转负、Waymo营运借款持续扩大且无外部单位利润。
- **研究明确缺口**：截至10/20并无2026Q3完整季报；公司当日精准股数、ATM actual issued、优先/Waymo借款股东索偿、SpaceX算力实际开始交付、欧洲/美国所有逐月法庭文件/法定补救细则、过去一年真实同口径forward PE高低不能独立核实；已按原始文书建立近12个月候选台账但**未穷尽全部月份全部声明**，不能称完全核验。

## 2026-10-11关键变化
{
  "facts": [
    "Cloud63%→82%增长，Search19%→17%仍正增长",
    "从回购叙事转向普通股/强制可转优先股/ATM融资，并且H1无回购",
    "TTM利润被进一步投资收益放大，Q2总利润不等普通股利润",
    "旧FY2025收入402843m本次官方402836m；不得静默沿用旧数字",
    "新增大额承诺和租赁、并购与股本桥"
  ],
  "price": {
    "old": 384.9,
    "new": 347.86,
    "change": -0.09623278773707444
  },
  "model": [
    "取消原始EPS与未折现未来P/E锚，采用含SBC与折旧EBIT并扣优先索偿",
    "不对同一mandatorypreferred既扣清算又加转股；2028未转，2029敏感性另列"
  ]
}


### 父代理复核补充：报价缺口已解决

Nasdaq历史原页核验2026-10-09常规收盘 347.86 美元；本次采用该交易所记录。初稿中的报价未核验限制已解决，其余股数、合同和来源缺口继续保留。详见可复算记录中的 `resolved_during_parent_review`。

## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Alphabet（GOOG）Tracker

Last updated: 2026-05-20

## Current Research View

**建设性但需观察**，中等偏高置信度，12-24 个月视角。

GOOG 的 2026Q1 证明 AI 正在增强 Search、Cloud 和订阅业务，而不是立刻破坏核心广告模型。Search & other 同比 +19%，Google Cloud 同比 +63% 且 operating margin 32.9%，整体 operating margin 36.1%。但当前约 4.68 万亿美元市值、29x TTM P/E、1800-1900 亿美元 FY2026 capex 指引，使风险回报从“便宜修复”转向“高质量但需兑现”。

## Current Main Thesis

- Q1 2026 total revenue 为 1098.96 亿美元，同比增长 22%，constant currency 增长 19%。
- Q1 2026 Google Search & other revenue 为 603.99 亿美元，同比增长 19%。
- Q1 2026 YouTube ads revenue 为 98.83 亿美元，同比增长 11%。
- Q1 2026 Google subscriptions, platforms, and devices revenue 为 123.84 亿美元，同比增长 19%。
- Q1 2026 Google Cloud revenue 为 200.28 亿美元，同比增长 63%。
- Q1 2026 Google Cloud operating income 为 65.98 亿美元，operating margin 32.9%。
- Q1 2026 consolidated operating income 为 396.96 亿美元，operating margin 36.1%。
- Q1 2026 net income 为 625.78 亿美元，EPS 5.11 美元，但 equity securities gain 对 EPS 贡献约 2.35 美元，不能简单年化。
- Q1 2026 operating cash flow 约 457.9 亿美元，capex 约 356.7 亿美元，FCF 约 101 亿美元。
- FY2026 capex 指引上调至 1800-1900 亿美元。

## Key Risks

- AI Overviews / agentic search 改变 traditional search click and ad economics。
- 默认搜索、广告技术、Android/Play 相关反垄断 remedies。
- FY2026 capex 1800-1900 亿美元导致 FCF 持续承压。
- Google Cloud 高增长但 margin 被 depreciation、infrastructure cost 或 pricing pressure 压缩。
- OpenAI、Anthropic、Microsoft、Meta、xAI 等模型和应用竞争。
- Google Network 继续下滑，开放网页广告生态承压。
- Q1 EPS 受 equity securities gain 放大，未来投资收益可能反向波动。
- 当前估值已修复到 base case 中部，容错率低于此前。

## Latest Earnings or Company Update

- 最新季度：2026 Q1，季度结束 2026-03-31，财报和 10-Q 发布于 2026-04-29。
- Total revenue：1098.96 亿美元，Q1 2025 为 902.34 亿美元。
- Google Services revenue：896.37 亿美元，Q1 2025 为 772.64 亿美元。
- Google Cloud revenue：200.28 亿美元，Q1 2025 为 122.60 亿美元。
- Other Bets revenue：4.11 亿美元，Q1 2025 为 4.50 亿美元。
- Operating income：396.96 亿美元，Q1 2025 为 306.06 亿美元。
- Net income：625.78 亿美元，Q1 2025 为 345.40 亿美元。
- Diluted EPS：5.11 美元，Q1 2025 为 2.81 美元。
- Cloud backlog：超过 4600 亿美元。
- Paid subscriptions：3.5 亿。
- Waymo：超过每周 50 万次 fully autonomous rides。
- Quarterly dividend：提高至 0.22 美元/股，2026-06-15 支付，record date 2026-06-08。

## What Changed Since Prior View

这是本 workspace 中第一份 GOOG 研究观点。

## Metrics or Events to Monitor Next

- Search & other revenue growth and AI Overview monetization。
- Paid clicks, CPC, commercial query trends。
- YouTube ads, Shorts monetization, CTV revenue。
- Google Cloud revenue growth, operating margin, backlog conversion。
- Capex run-rate versus 1800-1900 亿美元 FY2026 guidance。
- Operating cash flow, FCF, FCF margin。
- Gemini consumer plans, Google One, Workspace AI attach。
- Gemini Enterprise paid MAU and API token usage。
- DOJ / EU / UK antitrust developments。
- Waymo rides, city launches, unit economics。
- Share repurchases, SBC, share count。

## What Would Change the Research View

- 若 Search & other 连续几个季度保持 mid/high-teens 增长、Cloud 继续 40%+ 增长且 margin 维持 25%-30%+、capex 不再持续上修、FCF margin 恢复、Gemini/Workspace AI 收入更清晰，可上调至 **Positive**。
- 若基本面强但估值和 capex 已反映大量好消息，维持 **建设性但需观察**。
- 若 Search 增长明显放缓、AI Overviews 压低广告经济性、Cloud margin 被 capex/depreciation 吞噬、capex 再度大幅上修、监管 remedies 改变商业模式，或股价继续上涨但 EPS/FCF revisions 跟不上，下调至 **Neutral / Negative**。

## Research Files

- `deep-research/2026-05-20-deep-research.md`
