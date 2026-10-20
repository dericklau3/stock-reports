# Cerebras Systems（CBRS）完整深度研究 — 2026-10-20

- **投资观点：**中性偏建设性，等待经营现金回报与核心客户部署验证。股价较10月9日下降26.5%显著改善价格条件，已低于本研究的2028基础情景现值下沿，但基础情景自身仍依赖快速扩张和高退出倍数，不能称有可靠安全边际。
- **核心逻辑：**Cerebras向外部客户销售专用AI计算系统、提供极低延迟推理算力；OpenAI的长期容量合同、AWS和AMD集成及渠道伙伴带来商业化可能，关键是已签容量转成真实交付、持续付费、单位经济和稀释后每股现金。
- **主要风险：**OpenAI/G42等客户集中、设备和机房现金投入先于利润、高增长退出倍数与客户/员工权证摊薄；媒体关于新模型改用GPU的说法未经客户完整架构核实，不能认定合同取消，也不能忽略集中风险。

研究截止2026-10-20（亚洲日期）；最新可核实常规收盘为2026-10-19 16:00 EDT **$120.66**（StockAnalysis；ChartExchange日表$120.67，取前者；不是10月20日盘中价）；Cerebras Systems Inc.，CIK 0002021728，Nasdaq A类普通股CBRS，以美元交易。最新已披露完整财报是截至2026-06-30的2026Q2/上半年，2026-08-12公布并申报10-Q；研究日尚未核实有更新的10-Q或重大8-K。 [价格](https://stockanalysis.com/stocks/cbrs/history/)｜[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[SEC清单](https://data.sec.gov/submissions/CIK0002021728.json)。

## 1. 公司到底是做什么生意的？

**卖什么：** Cerebras销售整套AI计算设备（包含晶圆级WSE处理器、系统、配套软件和交付支持），也可以由自己或渠道伙伴部署系统，把AI模型运行所需的高速推理算力卖给应用开发者、研究机构、云平台和模型企业。**解决什么问题：** 代码智能体或长文本分析需要连续生成大量文字，等待每一步输出会拖慢总任务；专用架构把大量计算与高速存储集成在接近一整片晶圆的处理器上，主打降低逐token生成延迟，而不是销售应用本身。**谁付款：** 买服务器的企业/云运营商直接采购硬件；采购算力的模型开发商、应用公司或平台伙伴通过容量、云使用量或商业合同支付Cerebras，最终应用用户通常是向应用/云公司付费，不是直接向Cerebras付设备款。**怎么收费：** 硬件以合同交付、验收和收入确认；算力按承诺容量或消费式使用/服务合同记收入，签约与确认收入、现金到账三者不同。**什么决定利润：** 晶圆/服务器制造、折旧、研发、机房、电力、网络、运维、融资及股权激励能否被售价和系统利用率覆盖。[S-1最终招股书商业模式](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)；[Q2 10-Q业务与风险](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

**举例假设：** 某代码助手公司希望减少编程代理每次生成修改建议的等待，把部分推理调用接到Cerebras云；它向算力提供商支付费用，用户向代码助手付订阅费。真实客户验证与假设区分：OpenAI在2026-01-14确认了**750MW**分批部署计划，Gimlet 2026-09-28确认联合方案已服务部分私有流量、General Compute 09-29确认将自费购入系统后向最终用户出售推理容量；但这些主体的未来规划不等于全部已使用、收入或Cerebras股东利润。[OpenAI原文](https://openai.com/index/cerebras-partnership/)｜[Gimlet](https://gimletlabs.ai/blog/cerebras-announcement)｜[General Compute](https://www.generalcompute.com/blog/general-compute-cerebras-multi-year-agreement)。

**竞争和护城河：** WSE及系统软件适配能为对响应速度敏感的工作负载创造价值，Q2 GAAP云收入同比增281%是采用的间接证据；但对手是NVIDIA GPU生态、AMD GPU、其他定制芯片及拥有自研算力的云商。Cerebras与AMD及AWS合作意味着其未来或更多承担生成阶段（decode），但为读取输入的prefill增加其他硬件，也可能改变全系统成本和利润分配。尚未披露跨客户同口径全生命周期毛利、留存及成本优劣；不要由单模型30倍速度宣称广泛市场份额或定价权。[AMD共同公告与测试脚注](https://ir.amd.com/news-events/press-releases/detail/1293/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference-solution)。

## 2. 近期已公布的重大事件

**发现窗口：2025-10-20—2026-10-20。**本次重读2026年10月10日旧报告与tracker；核查发行人2026年新闻归档、2025年末重要事项、最终424B4、8月12日10-Q及部分SEC后续申报，同时逐项复核OpenAI、AMD、AWS、Gimlet、General Compute、Compute Nordic等关键客户/伙伴公开原文。未逐份覆盖全期SEC 8-K及各主体所有月度新闻、Cerebras的X/LinkedIn即时披露；2025年10–11月部分伙伴和政府原件亦未全面核实，**不能称完成12个月无遗漏核查**。下列只列可找到原始披露且影响投资逻辑的事件，按公告日倒序：

| 公告日期与事件 | 公布了什么 | 对公司的实际意义 |
|---|---|---|
| **2026-09-29 · [General Compute多年采购与部署](https://www.generalcompute.com/blog/general-compute-cerebras-multi-year-agreement)** | 伙伴确认将融资采购系统并向客户出售推理容量，首个应用为编码智能体，计划2027Q1开放；提到其已有4亿美元信贷工具。 | 是独立采购/融资方的明确承诺；融资额度不等于Cerebras销售额，采购金额、验收及生产收入未知。 |
| **2026-09-28 · [Gimlet 100MW合作](https://gimletlabs.ai/blog/cerebras-announcement)** | 伙伴计划部署100MW；联合服务已在私有流量运行，预计2026年稍后开放首个公开节点、2027向客户开放CS-4。 | 已有使用证据，但100MW目标不可全部按已上电计，也不可与公司其他总容量简单相加。 |
| **2026-09-01 · [芬兰Mikkeli 165MW项目](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-and-compute-nordic-finland-announce-new-165-mw-ai-data)** | 与Compute Nordic Finland按50→80→165MW分阶段建设；每笔服务订单七年期，首期50MW已动工；地方投资估算约10亿–17亿欧元。 | 锁定长期机房能力和费用约束；地方区域投资总额不是Cerebras收入，已施工不等于已上电。 |
| **2026-08-20 · [Callosum欧洲异构推理合作](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-and-callosum-partner-deliver-ultra-low-latency)** | 双方计划将异构AI推理服务推向欧洲客户。 | 增加渠道与工作负载可能；合作金额/最低购买和重复性收入未披露。 |
| **2026-08-18 · [CS-4发布](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)** | 公布新系统；对CS-3的每瓦吞吐声称最高10x、对特定GPU测试单用户生成速度最高30x，原计划Q3开始发货。 | 有工程/效率突破潜力；本次未核实Q3发货与客户验收，不能把参数直接折算成毛利。 |
| **2026-08-13 · [GPT-5.6 Sol Ultrafast模型服务](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-powers-ultrafast-mode-openais-gpt-56-sol)** | Cerebras披露其硬件为OpenAI GPT-5.6 Sol Ultrafast有限预览提供推理，最高750输出token/秒为指定产品/条件宣传。 | 有具体生产应用而非纯意向，但无法据此推断后续所有新模型都采用同一硬件或长期利润；需检查最新用户流量和合同兑现。 |
| **2026-08-12 · [Q2财报](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples)** | GAAP收入1.801亿美元、core收入2.099亿美元；云GAAP同比+281%，GAAP毛利率14.2%、core毛利率40.6%，上半年资本支出很高。 | 商业增长是真实的，但大幅调整及资本需求需要与“核心”成绩分开评估。 |
| **2026-08-05 · [Lovable AI编码合作](https://investors.cerebras.ai/news-releases/news-release-details/lovable-and-cerebras-partner-power-ai-software-creation-worlds)** | 双方宣布将Cerebras推理接入软件生成工作流；具体付款金额及规模化盈利未披露。 | 有真实应用需求方向，但新闻稿不能证明规模化客户收入。 |
| **2026-07-23 · [AMD联合推理架构](https://ir.amd.com/news-events/press-releases/detail/1293/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference-solution)** | 用AMD Helios处理高吞吐阶段，WSE处理低延迟生成；7月公告预计2026H2上线，后续Q2电话材料将生产目标表述为Q4。 | 扩大应用范围但需增加整套硬件；5倍性能等结果为指定基准模型，不是可确认客户盈利。 |
| **2026-07-22 · [CrowdStrike安全AI合作](https://investors.cerebras.ai/news-releases/news-release-details/crowdstrike-and-cerebras-partner-power-ai-detection-and-response)** | CrowdStrike计划使用Cerebras推理来加强Falcon AIDR，Cerebras反向采用Falcon安全产品。 | 是双向产品集成，未知是否存在可计量长期净采购。 |
| **2026-07-09 · [欧洲200MW扩张规划](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-accelerates-european-expansion-200mw-ai-compute)** | 计划2026年底首批欧洲机房上线、2027年底地区容量合计200MW；芬兰9月新项目属后续节点。 | 将本地响应速度和供给同长期合同连接；规划MW与验收使用MW不可混同或重复加算。 |
| **2026-05-13/15 · [IPO定价与交割](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-closing-initial-public-offering)** | 05-13定价每股185美元；05-14开始交易；05-15完成出售3,450万股，约63.8亿美元发行总价，约62亿美元净募集。 | 解决部分近期融资需求，带来A/B/N三类股与股权激励/客户权证复杂性；融资不是运营获利。 |
| **2026-03-13 · [AWS Bedrock合作](https://press.aboutamazon.com/aws/2026/3/aws-and-cerebras-collaboration-aims-to-set-a-new-standard-for-ai-inference-speed-and-performance-in-the-cloud)** | AWS确认Trainium前处理与Cerebras CS-3生成的方案面向Bedrock；AWS最初称未来数月上市，Cerebras后续目标2027Q1。 | 云渠道极具重要性，原相对时间描述与修订目标需继续确认；截至本研究未证实Bedrock正式GA或真实付费收入。 |
| **2026-01-14 · [OpenAI 750MW合作正式公布](https://openai.com/index/cerebras-partnership/)**（**2025-12协议签订**，见[Q2 10-Q注3](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)） | OpenAI确认750MW低延迟计算容量计划按批次至2028上线；另有1.25GW选择权非确定采购。 | 是估值最重要的真实长期合同，却增加客户集中、部署及融资约束；容量合同并不保证所有新模型继续只用Cerebras。 |
| **2025-12-18 · [美国能源部Genesis MOU](https://www.cerebras.ai/press-release/cerebras-systems-and-u-s-department-of-energy-sign-mou-to-accelerate-the-genesis-mission-and-u-s)** | 宣布与DOE签谅解备忘录探索AI/HPC合作。 | 政策与技术渠道机会；MOU不是政府已拨款订单或必然收入。 |
| **2025-12-09 · [G42/MBZUAI Jais 2](https://www.cerebras.ai/press-release/cerebras-delivers-end-to-end-training-and-inference-for-jais-2-the-world-s-leading-open-arabic)** | Cerebras设备用于Jais 2训练和推理的合作展示。 | 强化实际应用场景，但不能忽略招股书及10-Q披露的G42相关客户集中与历史关联关系。 |

近期显著的**不利新线索**来自市场而非发行人公告：2026-10-19媒体报道TD Cowen将12个月目标价从275美元降到175美元但维持Buy；媒体亦称OpenAI某新“Ultrafast”模型使用NVIDIA硬件。评级不是合同证据，且尚未取得OpenAI原始完整硬件路由或终止披露，不能直接写作客户取消合同。[2026-10-19媒体报道](https://www.investing.com/news/stock-market-news/why-is-cerebras-systems-stock-sliding-today-93CH-4957923)。另据[424B4解禁说明](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)，10月14日一批约1,940万股可售资格已生效，不等于新增发行或全部实际出售。新公司公告方面未发现10月10日至本研究日足以证实新增收入/解约的同等级原件；投资者社交账号及完整SEC逐项覆盖仍有缺口。

## 3. 公司正在做什么、做到哪一步？

| 重点项目 | 为什么做？希望达到什么结果？ | 当前进展与下一步 |
|---|---|---|
| **OpenAI承诺容量持续交付** | 让OpenAI的复杂模型以低延迟生成，提高长期持续使用收入。 | 2026Q2已有合同相关收入，公司10-Q披露Q2对应OpenAI收入5,680万美元、H1 7,440万美元；原750MW按批次至2028，下一关是各阶段上线、实际利用率、模型持续采用和现金/服务抵偿。[10-Q注3/10](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) |
| **CS-4产品交付** | 在相同电力预算下增加生成吞吐，并扩大设备/云服务毛利空间。 | 8月已发布，原计划Q3首次发货；Q3已结束，但截止本次未取得可确认发货/验收或延期公告，记为“原目标到期、状态未核实”，不是完成。[CS-4公告](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions) |
| **AMD异构推理 + AWS Bedrock** | 将读入输入与生成拆分，扩大效率，并借大云分发给企业客户。 | AMD 7月原称2026H2、公司Q2材料给Q4生产目标；AWS 3月曾表示未来数月、后续公司给2027Q1目标。两者目前仍待独立正式商用及真实客户收费数据。[AMD](https://ir.amd.com/news-events/press-releases/detail/1293/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference-solution)｜[AWS](https://press.aboutamazon.com/aws/2026/3/aws-and-cerebras-collaboration-aims-to-set-a-new-standard-for-ai-inference-speed-and-performance-in-the-cloud) |
| **Gimlet/General Compute渠道** | 由伙伴采购或运营系统，吸收部分资本负担并带来新付费应用。 | Gimlet私有流量在使用，100MW目标尚未全部交付；General Compute计划2027Q1开放，采购金额未披露。下一关是系统验收、伙伴现金采购及Cerebras确认销售。[两伙伴公告](https://gimletlabs.ai/blog/cerebras-announcement) |
| **欧洲及其他机房产能建设** | 为承诺容量提供上电地点，降低跨区域延迟并支持长期业务。 | 2026-09-01芬兰首期50MW开工，165MW为分阶段计划；欧洲合计200MW是此前2027规划；下一关是上电、利用率、机房租金及资本回报。[芬兰原文](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-and-compute-nordic-finland-announce-new-165-mw-ai-data) |

## 4. 财务状况：收入、利润和现金

单位：**百万美元**，美国GAAP；FY为截至12月31日完整财年，H1为截至6月30日六个月，TTM为FY2025 + H1 2026 − H1 2025。年度出自[最终招股书经审计财务表](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)；半年与余额出自[Q2 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

| 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2 |
|---|---:|---:|---:|---:|
| GAAP收入 | 290.252 | 509.991 | 373.516 | 680.673 |
| GAAP毛利 | 122.738 | 199.071 | 111.735 | 237.103 |
| GAAP经营损益 | −101.438 | −145.862 | −492.270 | −552.480 |
| GAAP合并净损益 | −481.602 | +237.827 | −464.534 | −512.352 |
| 经营现金流 | +451.978 | −10.050 | −47.488 | +66.305 |
| 现金资本开支 | 23.435 | 382.739 | 548.873 | 746.518 |
| 简化自由现金流 | +428.543 | −392.789 | −596.361 | −680.213 |

<small class="financial-glossary">GAAP：美国会计准则；毛利＝收入减直接成本；经营损益＝扣研发、销售、管理后的主营盈亏；合并净损益还包含利息、税及金融项目。</small>
<small class="financial-glossary">经营现金流＝经营收支净现金；资本开支＝现金买设备及资本项目；简化自由现金流＝经营现金流−现金资本开支；TTM＝最近12个月。</small>

**资金约束：**2026-06-30现金67.42157亿美元、短期投资11.79390亿美元，约79.22亿美元可动用；受限现金6.84680亿美元**排除**；OpenAI营运贷款9.18244亿美元、已入表租赁负债5.68827亿美元，得到调整后净现金代理约64.34476亿美元。另有未开始及期后租约约23亿美元**最低未折现未来付款**，不可按已入表债再扣一次。公司在8月10-Q称现有流动性预计至少支撑未来12个月，属管理层判断而不是保证；客户贷款的偿付部分可通过服务抵偿，尚需结合新现金预算与到期条款评估，不将H1支出简单年化推断资金寿命。[10-Q资产负债表、注10/15/17和流动性](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

**总结：** FY2025收入同比增长约75.7%，H1 2026同比约84.1%，但营业亏损依旧且资本开支持续增加。FY2025合并正净利润含约3.63亿美元一次性远期负债终止收益，不能解释为稳定经营盈利；2024正经营现金流受预收款影响，也不能年化。Q2 GAAP收入1.801亿美元、core（公司调整口径）2.099亿美元；GAAP毛利率14.2%、core毛利率40.6%，两者差异包括客户权证抵减与成本分类，不能把core当股东净现金。[Q2正式对账](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples)。Q2股权激励3.770亿美元含IPO条件触发追认约2.736亿美元，不能将整个季度费用全部视作永久常态，也不能因“非现金”忽略未来股本；H1简化FCF **−5.964亿美元**确实反映扩建现金消耗，TTM简化FCF −6.802亿美元。2026-06-30尚未履约收入254亿美元（RPO）包含OpenAI大额合同与部分机房成本转付，约22%预计2028-06-30之前确认，**并非**可直接用于高倍数估值的净新增利润。[Q2 10-Q注3](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

## 5. 管理层与资本分配

管理层通过2026-05 IPO募集约62亿美元净额，成功储备扩张资金；但这个资本缓冲来自发行股票而非业务自由现金。2026年全年**core收入指引8.80–8.90亿美元**、core毛利率41%–43%、core经营利润率−19%至−17%；Q3 core收入2.14–2.16亿美元、毛利率38%–40%、经营利润率−25%至−23%。2027收入“超过三倍”属于管理层战略展望，尚未附完整设备投入、股权/客户权证与现金计划，不能当统一财务指引。[Q2结果/指引](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples)。

普通股A/B/N三类经济权利相同、投票权不同（B20票，N无票）；2026-08-05实际A112,247,109 + B111,601,424 + N13,715,508 = **237,564,041股**，不是仅A类，也不是2026-10-19的实时完全稀释股数。OpenAI最高33,445,026股、AWS最高2,696,678股权证存在阶段触发、行使与未归属限制；其中OpenAI已于7月行使部分并计入8月5日已发行股数，不能再次全部相加。[Q2 10-Q封面/注12](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。10月14日起约1,940万股阶段解禁带来潜在流通供给而**非新增股本**；10月19日报导CEO/CTO过去交易计划下售股，未逐笔重核所有Form 4/144，不能据媒体金额臆断内幕动机。[424B4可售股份](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)。

## 6. 估值分析：当前股价贵不贵？

| 关键指标 | 估算结果 |
|---|---|
| 当前参考股价 | **$120.66**（2026-10-19 16:00 EDT常规收盘，较10月9日$164.17下跌26.5%） |
| 公司整体经济市值 | **约286.64亿美元（代理）**：$120.66 × 8月5日全部三类已发行2.37564041亿股；未计期后变化/未来稀释，非实时完全稀释市值 |
| 适用当前估值指标 | **调整企业价值约222.30亿美元**，对FY2026 core收入指引中点8.85亿美元约**25.1× EV/core Sales**；GAAP过去12个月仍亏损，可靠Forward P/E无解释意义，历史有效EPS预期序列未取得 |
| 保守情景估值 | **$25.8–39.7/股现值**；2028 core收入18亿美元、EV/收入5–8倍、调整净现金10亿美元、预测经济股数2.80亿 |
| 基础情景估值 | **$136.3–179.1/股现值**；2028 core收入40亿美元、EV/收入12–16倍、调整净现金30亿美元、预测经济股数2.70亿 |
| 乐观情景估值 | **$264.6–322.3/股现值**；2028 core收入60亿美元、EV/收入18–22倍、调整净现金20亿美元、预测经济股数3.00亿 |

**方法及时点：** 本次完整重算了2026-10-20研究基准到2028-12-31 **2.1985年**、16%假设股权回报率的现值：`[(2028 core收入×假设退出EV/收入倍数＋2028时点调整净现金) / 2028预测经济股数] / (1.16^2.1985)`。三个情景由2026-10-10旧假设作为**仍待未来验证的条件输入**，而不是新增公开盈利预测；净现金均为**2028时点研究预测**，不是拿6月现金重复加回，未来股数尝试反映持续激励和融资。现金预算、真实全部潜在稀释及完整可比同行估值不可得，因此不是可审计DCF/精确目标价。详细折现端点、敏感性、条件和来源见[同日底稿](../research-records/2026-10-20-research.md)；报价与财务来源见[报价](https://stockanalysis.com/stocks/cbrs/history/)、[10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

**总结：** 价格相比旧版大跌后落在本研究基础情景下沿以下，但**基础情景本身需要2028 core收入达到2026年指引中点约4.52倍，且仍能享有12–16倍的2028收入估值**；按假设可持续FCF率10%–15%，退出倍数隐含的EV/FCF仍可达80–160倍。以基础情景2028股数2.70亿、未来净现金30亿美元、16%折现倒推当前价，对2028年40亿美元core收入要求约**10.54倍EV/收入**；若坚持14倍，则要求收入至少约**30.1亿美元**（约2026指引3.4倍），其他条件不变。市场重估和TD Cowen目标价下修不能证明已失去客户，也不能保证反弹；最决定安全边际的仍是2028收入转现金质量、需求兑现、估值倍数及最终稀释股数。

## 7. 未来值得关注的事件

| 重要事件 | 为什么值得关注 |
|---|---|
| **2026Q3财报与Q4展望（官方日期尚未核实）** | 比较Q3 core收入指引2.14–2.16亿美元，以及GAAP/core毛利、现金capex与经济股数；按照FY指引中点8.85亿美元和H1 core4.012亿美元，Q3中点2.15亿美元对应Q4需约**2.69亿美元**，这是研究者倒算门槛，不是官方Q4指引。 |
| **2026-10-28下一批约1,940万股解禁资格** | 根据424B4的分批条款，潜在流通供给变化；不能把取得售股资格说成已出售或新增稀释。 |
| **AMD Q4 2026生产与CS-4原Q3交付核对** | 同时验证异构方案整机效率和2026Q3交付旧承诺，查真实验收、客户采购与回收期，不把模拟测试当量产。 |
| **AWS Bedrock / General Compute 2027Q1目标、Gimlet公开云目标** | 渠道从合作公告进入真正客户付费和双方收入分成；正式GA与发布时间仍需各方后续核验。 |
| **OpenAI 750MW各阶段交付、贷款结算与新模型路由** | 观察实上电、持续采购和每期服务收入，排查某类模型被GPU替代是否影响容量实际兑现。 |

**总结：** Q3是重新验证全年指引与未来现金投入的关键时刻。若新模型与伙伴渠道持续收费、核心毛利改善且未来股数控制良好，可以支持更高情景；反之，若容量合同只是增加账面RPO却持续吞噬现金，应该下修盈利和退出倍数，而非仅因为股价便宜就上调结论。

## 8. 主要投资风险

| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |
|---|---|---|
| OpenAI/G42集中与需求切换 | 大客户规模或模型路由改变将影响收入、设备利用率和合同风险；贷款还有非现金抵偿与特定契约。 | OpenAI扩容量不及计划、客户独立确认降低使用、Q3收入集中仍未改善、贷款抵偿进度逆转。 |
| 数据中心长期现金承诺 | 设备、租金、网络与电力先支出，若上线滞后会破坏自由现金流并可能要求筹资。 | capex/租约增长超过实际付费容量、系统验收延期和现金消耗持续扩大。 |
| 新架构的单位经济不可量化 | 单用户速度领先但额外GPU/内存网络成本让利润偏低，客户压价则难覆盖资本回报。 | core毛利低于指引、无法提供完整TCO/归属利润、外部渠道反复推迟GA。 |
| 股本与解禁/权证 | 员工权益及客户权证可能削弱每股增长，分批解禁造成流通供给波动；多投票权限制公众控制。 | 三类经济股份及净完全稀释股数明显超模型、现金筹资条款不利。 |
| 高倍数下修 | 即使增长兑现，只要估值由高收入倍数回归利润/FCF指标，现价仍可跌很多。 | 2028收入和毛利达不到基础假设、预测退出倍数低于10倍、全成本FCF率迟迟不提升。 |

**总结：** 最强的反方路径是“合同很多、设备上了、收入增长，但高资本投入、客户让利及低倍数最终吞噬股东价值”。对大幅下跌的股票尤其要区分**估值下跌已经发生**与**业务坏消息是否真的发生**：前者清楚，后者仍须原始客户、财报和生产记录证明。

## 9. 四种投资视角：怎么看这家公司？

| 投资视角 | 最关注什么 | 对公司的判断 |
|---|---|---|
| 巴菲特式 | 稳定利润、资本回报与价格安全余地 | AI推理生意可理解且客户需求存在，但无法按目前数据预测稳定现金分红或高投入回报；价格改善不等于护城河已稳固。 |
| 芒格式 | 倒推最可能造成永久损失的认知错误 | 把254亿美元RPO、MW和模型测试都当可分配利润、忽略未来股数及高退出倍数，是潜在主要错误。 |
| 段永平式 | 真实客户价值、重复付费与执行 | OpenAI、Gimlet、General Compute多方确认比宣传重要；观察各客户由试用/计划转持续付费及实际毛利。 |
| 李录式 | 产业长期位置、理解边界与下行保护 | 晶圆级加速是长期AI架构的可选路径，但高资本强度及客户集中的最坏情景仍缺可靠每股资产保护。 |

**总结：** 四种视角是分析方法，不代表四位投资者本人意见。CBRS的长期投资价值取决于把快速推理做成可规模化、真实收款和可再投资的生意；本次价格下跌让可选性更有吸引力，但在下一轮经营现金、客户部署和稀释验证之前，仍不应把有条件的基础估值当作保证回报。
