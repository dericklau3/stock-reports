# INTC Tracker — Intel Corporation

Last updated: 2026-10-30

## Current Research View

- **投资观点：**中性偏谨慎。Q3 DCAI恢复而Foundry亏损仍大，2027年CapEx现金支出上行；**本次补充可复算的截至2026-10-30每股条件价值：保守$1–10、基础$15–36、乐观$55–88**，不是未来12个月保证成交价。**Q3财报发布于10-29常规收盘后：当日常规收盘$92.07（财报前），20:00 EDT盘后$70.90（财报后），两者不能混作一个时点。**
- **研究截止：**2026-10-30 08:12（UTC+8；美东2026-10-29 20:12 EDT）；Q3会计期间截至2026-09-26，10-29已发布8-K附件EX99.1，独立Q3 10-Q截至研究时点尚未核实。

## Current Main Thesis

- **核心逻辑：**Q3 Intel Products经营利润$5.324bn，Foundry分部经营亏$1.853bn，对外Foundry收入仅$0.411bn且环比+$0.118bn主要来自非经常性项目。Q3经营现金流$5.082bn、毛现金CapEx$4.219bn，公司调整FCF$1.639bn。2027资本支出预计明显增加；外部代工真实毛利与普通股每股FCF是决定性的下次验证。
- **业务判断：**DCAI收入同比+78%；CCPG收入同比-5%。Oracle 2026-10-27合作属未来协作规划、最低新增订单未披露；2026-10-26 Classiq为尚未交割的量子软件收购，交易对价未知。

## Key Risks

- **主要风险：**PC需求弱、Q4 Fab28事故影响、先进工艺外部客户未商业化、2027高资本支出、收购对价和经济股数/托管权证索偿的不完整调和。此前“8月公开发行净募资未知”的缺口**已解决**：2026Q3现金流正式确认公开发行净收益**$22.617bn**；2026-09-26实际在外股数约**5.310bn**，现金+短投$54.005bn、债务$50.134bn、NCI$16.642bn。

## Latest Research

[2026-10-30完整深研](deep-research/2026-10-30-deep-research.md)；[2026-10-30来源、覆盖、财务与估值底稿](research-records/2026-10-30-research.md)；[反向估值可复算JS](research-records/2026-10-30-reverse-valuation.js)和[机算输出](research-records/2026-10-30-reverse-valuation-output.json)。上一版完整报告：[2026-10-23](deep-research/2026-10-23-deep-research.md)；更早报告见下方历史记录。

## 2026-10-30 条件每股估值区间补充（同日原报告修订）

- **用户要求与交付修正：**2026-10-30原报告估值部分曾因2027以后CapEx、Classiq价格与政府托管/权证权益未核而**没有给具体目标价格**，不符合用户希望得到可衡量区间的完整深研目标。本次直接**原位改写同日完整报告第6节**，其余章节与旧版本历史报告保留；同时冻结六组新估值输入/计算输出，旧反向EBIT脚本仅作辅助不覆盖。
- **本次明确目标估值（当前2026-10-30折现条件价值，不是未来保证成交价）：保守1–10美元、基础15–36美元、乐观55–88美元/股。** 精确条件端点：1.3134/9.9542、15.3092/35.6409、54.9281/87.5787美元。2026-10-29财报后20:00 EDT参考盘后70.90美元，高于基础区间，位于乐观区间；此前10-29常规92.07美元是**财报前**价格不能混用。
- **详细模型：**[可复算输入](research-records/2026-10-30-valuation-scenarios-input.json)、[模型引擎](research-records/2026-10-30-valuation-scenarios-engine.js)、[全部逐年与敏感性结果](research-records/2026-10-30-valuation-scenarios-output.json)及[解释/假设/来源核对](research-records/2026-10-30-research.md#6-2026-10-30-同日估值补充与精确区间替代本底稿前文无价格区间的表达)。
- **范围方法：**2026Q4+2027–2036逐年FCFF、20%常态现金税率、2036年增长率/ROIC相容的长期再投资、已核现金54.005bn和债50.134bn及非控股权益16.642bn桥接；条件经济股数5.65—6.20bn，2027 CapEx研究假设24—32bn、各情景FCFF为负。2036合并营收路径115—225bn，EBIT率19%—36%；乐观路径非常激进。预测经营数据非管理层公开预算，不得当成市场共识。
- **核心弱点及敏感性：**基础终值占EV现值约81%—94%，保守可超过100%；基础端点WACC+1pp变为12.02/28.94美元，若只增加2027毛CapEx4bn变为12.98/33.19美元。政府托管/权证等法定权益、公允NCI、Classiq未公布交易对价均尚未完整核对；这些区间是**可复算条件估值，不能标为已完成P1 v4 whole-equity门禁或P2冻结。**
- **原始事实仍有效：**Q3营收16.513bn、Foundry亏1.853bn、2026-08公开发行净融资22.617bn、09-26实际股数5.310bn、Q4收入指引15—16bn。继续检验2027 CapEx、外部Foundry经常毛利、稀释和2027后的现金流。今日新增模型输入输出后不追溯改写2026-10-23旧报告。

## 2026-10-30 完整深研更新（追加历史）

- **Q3财报：**[10-29正式8-K附件EX99.1](https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/q326earningsrelease.htm)，单季GAAP收入$16.513bn、经营利润$2.522bn、归属母公司净利润$3.320bn，调整后EPS$0.52；Q4营收指引$15bn–$16bn，GAAP毛利率37.1%。
- **关键分部：**DCAI营收$7.318bn、经营利润$3.039bn；CCPG营收$8.097bn、经营利润$2.285bn；Foundry分部收入$6.697bn，经营亏$1.853bn，**对外**收入$0.411bn（约6.1%，环比增量主要非经常性）；内部收入不能重复计入合并销售。[10-29管理层电话会](https://stockanalysis.com/stocks/intc/transcripts/714242-q3-2026/)。
- **融资与现金核验：**2026Q3披露公开普通股增发实际净筹**$22.617bn**、2026-09-26现金及短投**$54.005bn**、有息债**$50.134bn**、非控股权益**$16.642bn**、当前实际普通股约**5.310bn股**（不等于2026Q4预计平均稀释5.44bn）。关闭旧2026-10-23档案关于增发最终净到款不明的事实缺口，**保留**权益托管/条件warrants/租赁和未来FD桥接缺口。
- **现金流：**Q3 GAAP OCF $5.082bn，现金毛CapEx $4.219bn，简单FCF $0.863bn；公司口径调整FCF $1.639bn（包括政府/伙伴现金流及租赁调节），不可混淆。自算TTM 2026Q3 revenue $59.892bn、OCF $17.472bn、现金PP&E $15.855bn、简单FCF $1.617bn；2027 CapEx将增加，不能将Q3正现金流机械年化为稳态。
- **已公布变化：**2026-10-29 [Fab28事故对Q4预计约$0.3bn收入影响](https://stockanalysis.com/stocks/intc/transcripts/714242-q3-2026/)；2026-10-27 [Oracle Xeon/OCI规划合作](https://www.intc.com/news-events/press-releases/detail/1785/intel-and-oracle-plan-expanded-collaboration-to-support)（采购条款未公开）；2026-10-26 [Classiq拟收购](https://www.intc.com/news-events/press-releases/detail/1784/intel-to-acquire-classiq-to-create-a-full-stack-quantum)（2027H1目标交割、对价未披露）。核查了Intel IR新闻2025-10至2026-10归档，但全年全部SEC/监管/伙伴来源仍**未完成覆盖**；10-22 FCC媒体线索未取得行政原文。
- **当前报价、估值边界：**10-29常规收盘$92.07（财报**之前**），10-29 19:59 EDT盘后$70.90（发布后）。以09-26 5.310bn在外股数做市值代理为$488.89bn/$376.48bn，TTM P/S约8.16x/6.29x；这不等于完全稀释经济权益。未来2027–2030逐年CapEx、外部Foundry长期现金边际、Classiq价格、政府托管/权证与未来融资仍不可精确估计，故**未完成可靠whole-equity保守/基础/乐观内在价**；不沿用10-23条件P0/P1价格与时点比较。只保留可复算的2028 **反向EBIT门槛**：假设2028经济股份5.8bn、有符号净现金及其他索偿-$15bn、12%股权要求回报，现价盘后$70.90在25x退出EV/EBIT下，要求2028正常化EBIT约$21.637bn；所有假设明确标为分析师假设，不是正式价值目标。未运行仓库P0/P1 CLI，也不伪造P2冻结。
- **下一验证：**正式Q3 10-Q（独立申报未核实取得）、2026Q4业绩/PC库存、Fab28产线恢复、2027 gross CapEx与FCF、14A商业客户合同、Classiq审批交割价、资本结构稀释；逐项与历史不可回改的2026-10-23预测对照。历史2028预测未到期，不报告命中率。

## 2026-10-23 完整深研更新（追加历史）

- **本次研究：**[完整报告](deep-research/2026-10-23-deep-research.md)、[详细底稿及范围缺口](research-records/2026-10-23-research.md)、[独立程序复算源码](research-records/2026-10-23-valuation-replay.js)、[输入/输出存档](research-records/2026-10-23-valuation-replay-output.json)。报告和底稿均以2026-10-23 09:00 UTC+8为知识截止；没有覆盖2026Q3未来财报。
- **与上次估值差异：**上次2026-10-21报告报价参考2026-10-20 $91.69，本次已核2026-10-22常规收盘$85.49（相比10/21 $92.96为-8.04%）。并无经确认的新季度GAAP利润或真实期后现金数据支持改变长期收入/利润路径。
- **新的重大事件：**2026-10-21 [JobsOhio披露](https://www.jobsohio.com/newsroom/news-press/intel-foundry-provides-us-manufacturing-capacity-update) Ohio One第一大型结构桁架已吊装安装，仍是厂房施工非开始晶圆量产；2026-10-22 [Reuters报道](https://www.reuters.com/technology/fcc-grants-intel-waiver-foreign-made-robotic-devices-2026-10-22/) FCC给Intel特定老旧外国产AGV设备一年豁免，**未获取FCC最终裁决原文，保留待核实**。正反消息均不代表可直接确认更高外部Foundry收入。
- **财务未变：**最近正式文件2026Q2 10-Q，Foundry外部付费相关Q2收入$0.293bn/分部收入$5.765bn、Foundry单季经营亏损$2.089bn；资本现金与7月实际股数依然是8月大额发行前时点。预计2026-10-29盘后Q3财报方能开始重建资本索偿桥。
- **独立P0条件价（估值日10/23、2028-12-31退出并折现）**：保守$7.10–10.98、基础$32.98–41.89、强乐观$72.49–87.12。采用旧研究尚未新证据改变的2028经营假设；未完整反映未来CapEx与后续融资。
- **独立P1五年逐年FCFF条件复算（旧v2财务假设、尚未调和临时资本代理）**：基础$20.08、强乐观$62.25，终值约占EV 75.7%/79.8%；与P0显著不一致，不机械平均。以$85.49反推在30x、12%股权回报、2028预期经济股60亿与净现金索偿-50亿美元的极有利假设下，仍需2028 EBIT约$22.08bn，即以$90bn销售测算24.54%正常化经营利润率。
- **不确定性/模型验收状态：**该轮实际计算为独立JS公式复算，并未运行仓库P0/P1 Python CLI，也没有P2密封冻结。2026年8月发行实际净到款、Q3资金耗用与股数、政府托管/权证、租赁、未来14A/Ohio/Arizona现金CapEx和第三方Foundry现金毛利均不完整，因此严格的whole-equity估值仍未完成；不得以任何条件价格对整股宣称已量化精确折价%。将来若有足够材料再以P1 v4 whole scope完整重算并冻结P2。
- **下一验证：**2026-10-29 Q3收入/Foundry外部付费及亏损、Q3 10-Q发行到账和股本、未来工厂资本开支及采购合同；补齐近12个月SEC 8-K、美国DOC及FCC原始披露、主要伙伴定点与整段时间的覆盖证据。

## 2026-10-21 完整深研更新（追加历史）

- **本次完整报告：**[2026-10-21-deep-research.md](deep-research/2026-10-21-deep-research.md)；[本次证据/计算/缺口研究底稿](research-records/2026-10-21-research.md)；[P0输入](research-records/2026-10-21-valuation-input.json)、[P0结果](research-records/2026-10-21-valuation-output.json)、[P1输入](research-records/2026-10-21-valuation-p1-input.json)、[P1结果](research-records/2026-10-21-valuation-p1-output.json)。保留10月20日与历史报告不覆盖。
- **实际新增事实与时点：**2026-10-20 INTC常规收盘**$91.69**，较2026-10-19 **$92.03**下降0.37%；2026-10-21时最新仍为2026-06-27截止Q2 10-Q，Q3财报官方日程**2026-10-29美股盘后**。没有将未发布的Q3真实业绩、期后资产负债表或新14A外部客户收费认定为事实。
- **继续成立的核心经济事实：**Q2 Products营业利润$4.817bn、Foundry亏$2.089bn；外部代工及封测收入仅$0.293bn，占Foundry总分部$5.765bn约5.1%；2026 H1调整FCF−$10.435bn但含Apollo大额回购。必须分别判断财务会计利润、FCF、实际外部客户付费和经济股份分母。
- **P0 2028股权退出EBIT条件现值，基准$91.69：**保守$7.10–10.97、基础$32.96–41.86、乐观$72.45–87.07；2028末EBIT目标日与净现金代理同日，按15%/13%/12%股权回报要求折现2.196年。模型不是逐年现金流；2028盈利与净现金、退出倍数均为分析师假设。
- **P1逐年FCFF DCF：**基础$20.08、强乐观$62.25（滚动未来5年2027–2031），终值占比约75.7%和79.8%；明显低于P0，主要因为逐年资本开支。不得简单平均模型；逆推现价需异常积极的长期FCF假设。Bear DCF因长期现金流难以界定未提供正价；Forward P/E同比同行和SOTP缺关键同口径证据未硬编。
- **资本和稀释的优先核验：**2026Q2现金+短投$29.727bn、债$50.537bn、NCI$15.601bn，7月17日报告股数约5.044bn；8月10/11公开发行210.526m股+$31.579m超额配售，**合计242.105m股、总价$23bn**。最终实际净现金、Q3现金消耗、政府143m escrow股份及241m条件warrants经济口径未充分调和；不得把全部托管股份既作为新增股数又当衍生负债重复索偿。P1采用5.286bn股及现金49.427bn等**未审计临时代理**，不应作为精确已验证市值或公允价值。
- **重要日期与来源：**2026-10-12 D-series送样（[Intel原文](https://www.intc.com/news-events/press-releases/detail/1783/intel-accelerates-open-infrastructure-for-the-agentic-ai-era)）；09-08 High-NA（[Intel](https://www.intc.com/news-events/press-releases/detail/1781/intel-foundry-and-asml-collaborate-to-accelerate-industry)、[ASML](https://investor.asml.com/news-releases/news-release-details/intel-foundry-and-asml-collaborate-accelerate-industry-readiness-high-na-euv)）；08-10/11发行及全额配售（[8-K](https://www.intc.com/filings-reports/all-sec-filings/content/0001193125-26-346806/d117670d8k.htm)）；07-21 Fortinet（[双方新闻](https://www.intc.com/news-events/press-releases/detail/1775/intel-and-fortinet-collaborate-to-advance-cybersecurity)）；04-09 Google（[Intel](https://www.intc.com/news-events/press-releases/detail/1766/intel-and-google-deepen-collaboration-to-advance-ai)）；04-01/04-08 Apollo Fab34回购协议/交割（[Intel](https://www.intc.com/news-events/press-releases/detail/1764/intel-to-repurchase-49-equity-interest-in-ireland-fab)）；2025-12-26完成NVIDIA投资，12-29披露（[8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086325000204/intc-20251226.htm)）。它们对工程/资金有不同影响，但无证据证明均已形成外部利润。
- **研究限制/下一关：**本次近12个月事件IR新闻归档及已知主要SEC/伙伴定点查阅，不是全量8-K、全部DOC/伙伴原始披露逐项覆盖；P0/P1输入输出已记录数学复算，尚缺在仓库工作目录实际调用原Python CLI的执行日志和P2 SHA256密封快照，故不宣称全部计算脚本验收已通过。下次优先在2026-10-29财报后重建最新股权/净索偿、外部Foundry付费和现金CAPEX、14A客户商业合同，并完成CLI/P2冻结，比较历史时点预测（尚无到期回测）。
- **观点保持：**中性偏谨慎。只有长期客户付费、Foundry亏损收窄、未来融资和股本稳定且FCF改善并存才增加信心；若相反则下调。

## 2026-10-20 深研更新（追加历史）

- 本次研究：[2026-10-20完整深研](deep-research/2026-10-20-deep-research.md)，[研究与估值底稿](research-records/2026-10-20-research.md)。不覆盖2026-10-11版本。
- 研究/行情基准：2026-10-20；2026-10-19常规收盘92.03美元（EDT），较旧报价104.70美元下跌12.10%，未有Q3财报；最新财务仍为2026-06-27 Q2 10-Q。官方下一财报2026-10-29盘后。
- 观点演变：2026-10-11中性等待→2026-10-20中性等待。主要改变是报价显著下降、2026-10-12 GPU D-series采样及2026-09-08 ASML High-NA工艺公开证据得到补充；不代表已经有新收入、外部14A确定订单或资产负债表更新。
- 核心经济事实重新突出：Q2 Foundry总分部收入$5.765bn、外部foundry及封测仅$0.293bn，约5.1%（2025Q2 $0.022bn）；Foundry经营亏损$2.089bn。H1外部foundry及封测$0.467bn（2025H1 $0.053bn）。产品分部Q2 EBIT$4.817bn但不分配部分SBC/总部费用。来源[2026 Q2 10-Q Note 2](https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000157/intc-20260627.htm)。
- 资本与资金：6月27日现金及短投$29.727bn、债务$50.537bn、NCI$15.601bn；8月10/11/12发行定价$95、基础210,526,315股+已行使31,578,947股全额超配，总新增约0.242105bn股，融资总价$23bn；最新实际到账、发行费用与股票数仍待Q3验证。143m剩余政府托管股和241m有条件权证不能重复按股票与负债索偿扣除。
- 2028压力估值（**2026-10-20现值**，不是真实目标价）：保守$8.9–12.9、基础$33.5–42.7、乐观$72.7–87.9；使用FV EBIT与2028年退出倍数折现2.188年，扣除净索偿代理$17.184bn（**含未经验证$19.7bn初始发行净现金假设**），未来股数5.50/5.65/5.80bn；原始计算、核验缺口和概念性贴现限制见研究底稿。报价隐含即使按30x、12%折现、58亿未来股仍需2028 EBIT约$23.53bn；研究假设非预测。
- 关键事件日期：2026-10-12 AI推理GPU D-series客户送样；2026-09-08 Intel-ASML逾100万片High-NA流程处理（含认证、研发及选定层次生产）；2026-08-11大额增发全额超配行权；2026-07-21 Fortinet SP6合作无金额；2026-04-09 Google多代Xeon/IPU合作；2026-04-01协议/04-08回购Apollo爱尔兰合资49%约$14.2bn；2025-12-26 NVIDIA $5bn股权私募已交割（2025-12-29 8-K）。原始公告与候选取舍见本次研究底稿。
- 下一验证：10月29日Q3财报的Foundry外部收入和亏损、Q3增发实际净资金与股本及托管、2027资本开支与自由现金流、14A重大外部签约、D-series从送样至量产获客；不得把意向/送样直接计入估值。
- 保留缺口：未逐页完整审计整个2025-10-20至2026-10-20所有SEC 8-K与政府DOC公告；Google同日独立合同金额、所有期后资本/租赁更新、历史每日Forward P/E区间无法核实；影响准确估值及重大合同完整性。

## 2026-10-11 深研更新（追加历史）

- 观点：中性等待；业务恢复承接8月，但报价104.70高于92.80，没有新季报验证现金改善。历史 [2026-08-20](https://github.com/dericklau3/stock-reports/blob/7c05fd1d8c3401e619e0441e49c48edc1fa8bac0/research/COMPANIES/INTC/deep-research/2026-08-20-deep-research-update.md)；新稿 [2026-10-11](deep-research/2026-10-11-deep-research-update.md)。
- 重要修正：此前遗漏8月公开发行；Aug12 8K显示210,526,315股@$95、额外31,578,947全行使，合计242,105,262股、gross23bn。最终现金到账未获得，不能当已证实现金。
- 股数：July17 actual5.044bn；机械发行后5.286bn+剩余escrow143m≈5.429bn，vendor5.25bn冲突不取平均。Escrow衍生负债不再与同一股份重复扣；DOC241m warrants条件触发。
- 现金口径：投资+融资栏H1 PP&E7.615bn，非仅6.192bn；adjustedFCF -10.435bn，自算与FY24/FY25官方调节公式一致。买回Ireland权益一次性支出非永久烧钱率。
- 估值：折现正常化EBIT、NCI扣除、资本投入及稀释；只有附条件情景，最终现金/股份/租赁需要Q3调和。
- 下一验收：官方2026-10-29盘后财报；Foundry外部客户收入、亏损收窄、资本回报；若持续约2bn季亏且capex上升/融资扩大，下调；客户及现金回报兑现后再增强。
- 底稿 research-records/2026-10-11-research.json；决定性原件 /home/ubuntu/.hermes/cache/scratch/stock-reports-batch-research/INTC/aug-8k.txt、/home/ubuntu/.hermes/cache/scratch/stock-reports-batch-research/INTC/q2-10q.txt；脚本 /home/ubuntu/.hermes/cache/scratch/stock-reports-batch-research/INTC/build.py；验证 /home/ubuntu/.hermes/cache/scratch/stock-reports-batch-research/INTC/validation.json。
- 未解决：发行最终到账、报价日股数、最新租赁、完整Q&A、历史日频ForwardPE。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# INTC Tracker — Intel Corporation

- **Ticker**: INTC
- **Company**: Intel Corporation
- **Exchange**: NASDAQ
- **CIK**: `0000050863`
- **Sector**: Semiconductors / Integrated device manufacturer / Foundry / AI infrastructure
- **Last updated**: 2026-08-20
- **Current research view**: Neutral / wait for confirmation（中性 / 等待确认）
- **Confidence**: Medium
- **Latest memo**: `deep-research/2026-08-20-deep-research-update.md`
- **Prior memo**: `deep-research/2026-07-24-deep-research.md`

## Current Research View

**Neutral / wait for confirmation（中性 / 等待确认）**。

Intel 的业务反转是真实的：Q2 2026 revenue **$16.1B**，同比 **+25%**；DCAI **+59%**；CCPG **+13%**；Foundry **+31%**；non-GAAP EPS **$0.42**；Q3 revenue guide **$15.8B-$16.8B**。但当前 $92.80 仍约对应 **EV/Sales 8.91x**、**Forward PE 55.86x**、**P/FCF 172x**，市场仍按“AI compute + 美国本土先进制造 + Foundry 成功”而不是传统低估半导体来定价。

价格从 2026-07-24 旧报告锚点 **$102.62** 回落到 2026-08-19 收盘 **$92.80**，研究吸引力提高，但还不是强安全边际区。

## Current Main Thesis

- 产品业务恢复明显：Q2 Total Intel Products revenue **$15.139B**，同比 **+28%**，operating income **$4.817B**。
- DCAI 是最大亮点：Q2 revenue **$6.262B**，同比 **+59%**，operating income **$2.474B**，margin 约 **40%**。
- CCPG 是利润底座：Q2 revenue **$8.877B**，同比 **+13%**，operating income **$2.343B**。
- Foundry 是最大变量：Q2 revenue **$5.765B**，同比 **+31%**，但 operating loss 仍为 **-$2.089B**。
- 18A 已 ramp；18A-P 于 2026 年 6 月进入 risk production；Intel 继续承诺 14A 开发并以 2028 HVM 为目标。
- 普通股价值仍受 adjusted FCF、DOC escrow shares、warrants、政府持股、SoftBank/NVIDIA 私募和股数增长影响。

## Latest Financial Snapshot

StockAnalysis accessed 2026-08-20; market data as of 2026-08-19 close.

| Metric | Value |
|---|---:|
| Price | $92.80 |
| Market cap | $487.62B |
| Enterprise value | $508.18B |
| Shares outstanding | 5.25B |
| Shares change YoY | +13.28% |
| TTM revenue | $57.03B |
| TTM net income | -$11.29B |
| TTM EPS | -$2.30 |
| Cash | $29.73B |
| Total debt | $50.54B |
| Net debt | $20.56B |
| Book equity | $103.14B |
| Forward PE | 55.86x |
| EV/Sales | 8.91x |
| EV/EBITDA | 30.18x |
| P/FCF | 172.24x |
| P/OCF | 32.65x |
| Beta | 2.24 |
| Analyst consensus | Hold |
| Analyst target | $114.88 |
| 52-week range | $22.78-$142.35 |

## Q2 2026 Earnings Snapshot

Intel reported Q2 2026 results on 2026-07-23; Q2 10-Q filed/published 2026-07-24.

| Metric | Q2 2026 | Q2 2025 | YoY / Change |
|---|---:|---:|---:|
| Revenue | $16.1B | $12.9B | +25% |
| GAAP gross margin | 40.4% | 27.5% | +12.9 ppts |
| Non-GAAP gross margin | 41.8% | 29.7% | +12.1 ppts |
| GAAP operating margin | 11.1% | -24.7% | +35.8 ppts |
| Non-GAAP operating margin | 17.2% | -3.9% | +21.1 ppts |
| GAAP EPS | -$2.16 | -$0.67 | n/m |
| Non-GAAP EPS | $0.42 | -$0.10 | n/m |
| Operating cash flow | $7.0B | $2.1B | Improved |
| Adjusted FCF | -$8.4B | -$1.1B | Worse |

## Segment Tracking

| Segment | Q2 2026 revenue | YoY | Q2 2026 operating income/loss | Watch item |
|---|---:|---:|---:|---|
| CCPG | $8.877B | +13% | $2.343B | AI PC / PC refresh sustainability |
| DCAI | $6.262B | +59% | $2.474B | AI compute demand and CPU/ASIC competitiveness |
| Total Intel Products | $15.139B | +28% | $4.817B | Product business profit durability |
| Intel Foundry | $5.765B | +31% | -$2.089B | External customer revenue, 18A/14A, loss narrowing |
| All Other | $701M | -33% | $230M | Mobileye/IMS/divested Altera effects |

## Q3 2026 Guidance

| Metric | GAAP | Non-GAAP |
|---|---:|---:|
| Revenue | $15.8B-$16.8B | same |
| Gross margin | 41.0% | 42.0% |
| EPS attributable to Intel | $0.31 | $0.38 |

## Valuation Snapshot

| Metric | Value |
|---|---:|
| EV/Sales | 8.91x |
| P/S | 8.55x |
| EV/EBITDA | 30.18x |
| Forward PE | 55.86x |
| P/OCF | 32.65x |
| P/FCF | 172.24x |
| TTM FCF yield | 0.6% |
| P/B | 4.73x |
| Net debt/share | $3.92 |

### Scenario Price Ranges

| Scenario | Revenue | EV/Sales | Net debt | Diluted shares | Implied price | vs $92.80 |
|---|---:|---:|---:|---:|---:|---:|
| Bear foundry cash burn | $58B | 4.5x | $25B | 5.4B | $43.7 | -52.9% |
| Downside reset | $62B | 6.0x | $23B | 5.35B | $65.2 | -29.7% |
| Base products recover | $68B | 7.0x | $21B | 5.35B | $85.0 | -8.4% |
| Base plus foundry better | $75B | 8.0x | $18B | 5.4B | $107.8 | +16.1% |
| Bull AI foundry | $85B | 9.0x | $15B | 5.5B | $136.4 | +46.9% |
| Hyper-bull U.S. foundry | $100B | 10.0x | $10B | 5.7B | $173.7 | +87.2% |

## Practical Price Zones

| Price Zone | Action Framework |
|---|---|
| <$50 | Strong research zone if liquidity and 14A/foundry risk have not worsened. |
| $50-$65 | Contrarian phased-entry zone; more room for execution volatility. |
| $65-$80 | Attractive but still evidence-dependent; needs FCF and Foundry loss improvement. |
| $80-$95 | Current zone; cheaper than July but still not a strong margin of safety. |
| $95-$110 | Fair-to-expensive; requires Q3/Q4 beats and Foundry evidence. |
| $110-$135 | Bull-case zone; requires DCAI + Foundry + FCF proof. |
| >$135 | Hyper-bull zone; avoid chasing AI/government-support narrative alone. |

## Key Investment Questions

1. Can DCAI sustain strong growth after Q2's +59% YoY?
2. Can CCPG maintain profit contribution as AI PC / Windows refresh cycles mature?
3. Can Intel Foundry reduce quarterly operating loss from roughly -$2B?
4. Will Intel 18A/18A-P ramp without yield/cost surprises?
5. Can Intel 14A secure significant external customers or committed demand?
6. Can adjusted FCF turn positive despite equipment, clean room, substrate and fab investments?
7. Will government/strategic investor shares, warrants, escrow shares and future financing dilute ordinary shareholders further?

## Evidence Required to Upgrade

- Q3/Q4 revenue beats guide midpoint with gross margin stability.
- DCAI continues high growth with healthy margin.
- Intel Foundry operating loss narrows materially.
- External foundry customer revenue becomes large and recurring.
- Intel 14A secures significant external customer/design commitment.
- Adjusted FCF improves from Q2 -$8.4B toward breakeven/positive.
- Share count / warrants / escrow shares / government ownership complexity stops worsening.

## Evidence Required to Downgrade

- 14A paused, delayed materially, discontinued, or fails to secure external customers.
- Foundry loss remains around -$2B/quarter or worsens.
- DCAI growth slows sharply.
- Adjusted FCF remains deeply negative despite revenue growth.
- Additional large equity issuance or government/partner dilution.
- Gross margin stalls or declines as new nodes enter production.

## Major Events Timeline

| Date | Event | Investment relevance |
|---|---|---|
| 2025-08-22 / 2025-08-27 | U.S. Government Agreement / DOC equity and escrow shares | Government support but dilution and mark-to-market complexity |
| 2025-09-12 | Altera deconsolidated after sale of 51% | Improves comparability but reduces consolidated exposure |
| 2025-09-26 | SoftBank $2B private placement completed | Strategic capital, dilution |
| 2025-12 | NVIDIA $5B private placement completed | Strategic AI validation, dilution |
| 2026-01-23 | FY2025 10-K filed | Full-year baseline and risk factors |
| 2026-04-24 | Q1 2026 10-Q filed | Warned about 14A committed-demand risk |
| 2026-07-23 | Q2 2026 earnings release/slides | Revenue +25%, DCAI +59%, Foundry +31%, non-GAAP EPS $0.42 |
| 2026-07-24 | Q2 2026 10-Q | Confirms 18A/18A-P/14A, escrow/warrants and FCF details |
| 2026-08-19 | StockAnalysis close $92.80 | Price down from prior $102.62, valuation still high vs FCF |

## What Changed Since Prior View

- Price fell from **$102.62** in the 2026-07-24 memo to **$92.80** on 2026-08-19 close.
- Market cap moved from about **$503.76B** to **$487.62B**; EV now about **$508.18B**.
- Shares outstanding increased in third-party data to **5.25B**, YoY change **+13.28%**.
- Q2 10-Q confirms 18A high-volume production start, 18A-P risk production in June 2026, and Intel commitment to completing 14A development / 2028 HVM path.
- Q2 adjusted FCF remains a major red flag at **-$8.4B**.
- Research view remains Neutral / wait for confirmation: lower price improves research attractiveness, but not enough for high-conviction upgrade.

## Core Thesis Assumptions That Must Remain True

1. DCAI revenue and margin remain strong.
2. CCPG keeps a profitable PC/AI PC refresh base.
3. Foundry operating loss narrows from roughly -$2B/quarter.
4. 18A/18A-P yield, cost and production ramp remain on schedule.
5. 14A obtains significant external customer / committed demand.
6. Adjusted FCF improves materially.
7. Dilution and government/strategic investor complexity do not keep worsening.

## Red-Line Conditions

- 14A lacks significant customer demand or is paused/discontinued.
- Foundry loss does not narrow by coming quarters.
- DCAI growth slows materially after Q2 spike.
- Adjusted FCF remains deeply negative through revenue recovery.
- Share count continues rising sharply.
- Additional large government/partner/common equity issuance at unfavorable economics.
- Gross margin weakens as 18A/18A-P/14A production ramps.

## Metrics to Monitor Next

- Q3 2026 revenue vs $15.8B-$16.8B guide.
- Q3 non-GAAP gross margin vs 42.0% guide.
- DCAI revenue growth and operating margin.
- CCPG revenue and margin.
- Intel Foundry revenue split: external vs internal/intersegment.
- Foundry operating loss and utilization.
- 18A/18A-P yield/cycle-time/cost commentary.
- 14A customer/design commitments.
- Adjusted FCF bridge: OCF, gross capex, government incentives, partner contributions/distributions, finance leases.
- Shares outstanding, escrow share release, DOC warrant exposure and any new private placements.

## Research Files

- `deep-research/2026-07-24-deep-research.md` — prior full deep research report.
- `deep-research/2026-08-20-deep-research-update.md` — latest Q2 10-Q and valuation update.

## Sources

- Intel Q2 2026 earnings release / Exhibit 99.1, published 2026-07-23, via StockAnalysis/Quartr filing mirror.
- Intel Q2 2026 Form 10-Q, published 2026-07-24, via StockAnalysis/Quartr filing mirror.
- Intel Q2 2026 earnings slides, published 2026-07-23, via StockAnalysis/Quartr filing mirror.
- StockAnalysis INTC overview/statistics/financials/filings pages, accessed 2026-08-20.
