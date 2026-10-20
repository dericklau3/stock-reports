# NVIDIA Corporation（NVDA）完整中文深度研究｜2026-10-20

**投资观点：谨慎看好。** 现有数据中心平台显示强劲且已入账的营业利润、收入增长及自由现金流，股价从上一研究下跌约5.3%而FY2027 Q3正式增长指引仍强。相比单纯硬件龙头估值，必须给客户信用支持、未来大型承诺及AI项目融资困难更高权重，不能将全部增长不加区分当独立客户需求。

**核心逻辑：** GPU、CPU、网络与CUDA软件形成互补的“整个AI工厂”采购方案，客户同时买性能、互联、部署效率和软件兼容。Blackwell已规模确认收入，Rubin正在生产与交付链条，但未来需求要经过客户实际部署、终端算力收费及回款后才能保持可持续经营利润；Cloud/Financing的支持承诺使公司承担新的风险。

**主要风险：** 云客户和AI模型服务商债务及AI资本开支回报、2800亿美元级供应承诺、360亿美元第三方云容量协议及1085亿美元最高信用担保敞口，与应收/库存上升互相关联；ASIC/AMD竞争、出口限制以及市值巨大下的估值倍数下修风险。

研究截止**2026-10-20（亚洲日期）**，证券：NVIDIA Corporation（NASDAQ：NVDA普通股，美元；SEC CIK 0001045810，非ADR），最新完整季报：**FY2027 Q2截至2026-07-26，SEC10-Q于2026-08-26提交**，全年FY2026截至2026-01-25。报价：**2026-10-19 16:00 EDT美国常规时段$217.09**，非10月20日盘中价或10月19日盘后价；[StockAnalysis历史](https://stockanalysis.com/stocks/nvda/history/)、[ChartExchange](https://chartexchange.com/symbol/nasdaq-nvda/historical/)、[Investing](https://www.investing.com/equities/nvidia-corp-historical-data?symbol=NVDA)同价。原件：[FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)、[FY2027 Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

## 1. 公司到底是做什么生意的？

NVIDIA卖**芯片及整套计算与网络设备**，主要包括数据中心用GPU并行计算芯片、Vera CPU、机架系统、NVLink/InfiniBand/Ethernet网络及相关软件（CUDA、推理部署组件）；也有PC游戏GeForce、创作者/工作站、汽车、机器人和科学计算相关设备与开发平台。**客户的实际问题**：运行大模型需高吞吐计算、快速GPU互联、成熟开发和调度工具、能源利用效率及持续升级；用NVIDIA计算+交换机+软件整套系统能减少跨品牌整合风险和部署时间。

**谁买谁付**：微软Azure、Google Cloud等大型云商、AI专用云厂商（例如CoreWeave、Nebius）、服务器/整机渠道、企业、科研和主权AI项目采购计算设备；渠道商可能是直接NVIDIA付费客户，最终使用者向云商租计算、按小时或token付费，而不一定直接向NVIDIA付款。客户购买硬件/系统按履约交付确认收入，软件授权、企业服务及长期支持按合同确认。生产主要外包晶圆、HBM内存、先进封装及组件供应商；公司仍要承担研发、采购和容量承诺、物流、库存、保修、销售与资本支持成本。[2026 Q2 10-Q经营模式及财务](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

**举例假设：**某AI专用云商为提高企业推理吞吐量采购NVIDIA Rubin机架与网络，先向NVIDIA或其渠道支付硬件款，随后向自己的企业租户收取推理使用费。若租户实际支付不足，云商仍需还设备或建设债务；若NVIDIA事先承诺回购闲置容量/提供部分场地担保，NVIDIA会从设备商部分变成经济风险承接方。任何云商向终端用户收多少钱，不自动等于NVIDIA同额新增收入。

**竞争和利润来源：**重要替代方案是AMD Instinct、Google TPU、AWS Trainium、Broadcom参与设计的大客户自研ASIC以及CPU/软件工具迁移。NVIDIA有超大规模真实收入的硬证据：FY2027 Q2数据中心收入约**$89.0bn、同比+117%**、合并GAAP毛利率75%；CUDA生态、计算与网络联合优化和平台支持是竞争优势，但这些是结构性解释，**没有可靠当前可比单位成本及每位客户留存原始数据**，不能仅凭品牌自称永久垄断。已有业务利润主要来自Compute & Networking；显卡/边缘AI仍有现金收入，未来新CPU和机器人平台不应全部当成已兑现利润。[Q2公司原始结果](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/)；[10-Q segment](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

## 2. 近期已公布的重大事件

核心时间窗：**2025-10-20—2026-10-20**。检查过NVIDIA原始Newsroom公告、2025Q3/2025FY财报与2026Q1/Q2公告、2026Q2 SEC 8-K/10-Q，及部分合作伙伴/媒体对照；详细日期和纳排见[当日研究底稿](../research-records/2026-10-20-research.md)。**尚未穷尽**2025年10—12月及2026年逐月所有NVIDIA、各云商、监管法定文件与项目建设许可，未可证声称全年所有事件无遗漏。

| 公告日期与事件 | 公布了什么 | 对公司的实际意义 |
|---|---|---|
| **2026-10-19 · [Modal采用Vera CPU](https://www.reuters.com/business/nvidia-wins-fast-growing-ai-startup-modal-new-central-processors-2026-10-19/)**（Reuters报道，原厂客户未独立取得正式金额合同） | Modal云平台拟采用Vera CPU处理AI Agent任务，试用反馈有性能改善但仍保留AMD、Intel混合部署。 | 新CPU进入真实客户采购评估；试用性能不等于FY2027确认收入或声称所有云厂商全面替换其他CPU。 |
| **2026-10-19 · [Jülich量子容错仿真](https://nvidianews.nvidia.com/news/nvidia-runs-record-simulation-of-fault-tolerant-quantum-computing-at-julich-supercomputing-centre)** | NVIDIA披露在JUPITER超算运行104-qubit容错系统模拟。 | 证明科研计算平台能力，尚无可独立计价的新增云收入或商业量子硬件销售合同；不是财务指引。 |
| **2026-10-15 · [Adobe扩大合作](https://nvidianews.nvidia.com/news/adobe-and-nvidia-expand-collaboration-to-speed-agentic-creation)** | Photoshop、Premiere、Substance、Brand Concierge整合RTX Spark及Nemotron开发/加速能力。 | 客户产品实际适配，是软件生态增加采用的证据；未披露独立最低采购或增量利润，不能当大订单。 |
| **2026-10-13 · [英国AI安全算力支持](https://nvidianews.nvidia.com/news/nvidia-commits-250-million-to-advance-uk-agentic-safety-and-security-research-over-the-next-five-years)** | 宣布未来五年提供价值**$250m**算力捐赠，每年约$50m，通过英国NVIDIA Cloud Partners交付。 | 扩张模型生态，但属有成本的算力捐赠，不是政府采购已付NVDA现金订单。 |
| **2026-10-12 · [Cisco联合USFP光模块计划](https://nvidianews.nvidia.com/news/nvidia-and-cisco-introduce-new-pluggable-optics-form-factor-to-scale-ai-factories)** | 两家公司联合推进高密度400Gbps/lane USFP光模块，形成多家供应生态。 | 有望提高系统光互联效率，公告是技术计划/标准生态，不是已确认销售。 |
| **2026-09-16 · [Vera Rubin MLPerf推理测试](https://nvidianews.nvidia.com/news/latest?c=21926&page=12)** | 公司披露Rubin NVL72在MLPerf Inference v6.1公开结果。 | 有对照测试证据，但不同模型/系统成本与真实运行条件需辨析，不能把基准分数等同云用户付费或份额。 |
| **2026-08-26 · [FY2027 Q2业绩及10-Q](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/)**，8-K和10-Q同日 | 单季收入**$96.221bn**、数据中心**$89.0bn**、GAAP毛利率75.0%，Q3收入指引**$108.0bn±2%**及GAAP毛利率**74.0%±0.5个百分点**；10-Q披露大规模供货、云购买及信用承诺。 | 既验证高速增长，也揭示风险转为采购/信用系统性负担。指引**不包括中国Data Center compute收入**，不可将未批准中国销售加入预测。 |
| **2026-08-24 · [Groq 3 LPX进入量产](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)** | 新低延迟推理加速产品与Vera Rubin组合，Nebius被披露为首批采用者。 | GPU之外争取推理工作负载的商业路线有产品进度；实际客户交付收入和毛利未独立披露。 |
| **2026-08-10 · [与六大资管/银行讨论超过$500bn第三方算力融资平台](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital)** | 与Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR签MOU，希望长期动员超$500bn第三方资本。 | **MOU不是已募集/已签贷款/由NVIDIA承担的$500bn债务**；可促进销售，也扩大行业对杠杆和AI算力收费的依赖。 |
| **2026-07-16 · [日本Noetra国家AI工厂项目](https://nvidianews.nvidia.com/news/japan-government-industrial-leaders-and-nvidia-launch-the-worlds-first-national-ai-infrastructure)** | 公司宣布为Noetra支持的140MW设施，目标包含13,750 Vera CPUs与27,500 Rubin GPUs，有日本METI产业协同。 | 真实合作和配置目标，**尚未证实全部芯片已交付或收款**，不乘单价当当前销量。 |
| **2026-05-20 · [FY2027 Q1与股东分配改变](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)** | Q1收入**$81.615bn**同比+85%；董事会5月18日批准增加**$80bn**回购授权，季度普通股股息从$0.01上调为**$0.25**。 | 高现金利润与大规模股东分配变成实际现金义务，授权额不是全部立即执行的回购。 |
| **2026-02-25 · [FY2026年度财报](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026/)** | FY2026总收入**$215.938bn**、GAAP经营利润**$130.387bn**，Blackwell成为AI系统核心销售。 | 两年间由FY2025约$130.497bn增至$215.938bn，增长真实；周期、库存和云财务质量影响长期倍数。 |
| **2025-12-01 · [Synopsys扩大战略合作](https://nvidianews.nvidia.com/news/latest?c=21926&page=11)** | 双方宣布扩大AI工程设计和EDA领域合作。 | 新分行业需求开拓；软件集成/投资与实际增量收入不可混为一谈。 |
| **2025-11-19 · [FY2026 Q3财报](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026)** | 截至2025-10-26季度收入$57.0bn，数据中心$51.2bn，GAAP毛利73.4%。 | 确立本次FY2027 Q2营收高速增长之前的经营基线。 |

**重要期后资金与负面风险线索**：2026-08 NVIDIA SEC 10-Q披露为SB Energy/OpenAI Ohio 4.25GW设施分阶段提供总上限**$105bn**信用担保，加上其他云伙伴租赁约$3.5bn上限**$108.5bn**，以及$279bn采购承诺和$36bn云容量采购安排（详第3、4、8节）；它们是发行人法定文件确认的经济约束，而不是几篇营销新闻。2026-10-15 [Reuters分析CoreWeave融资/债券](https://www.reuters.com/legal/transactional/coreweaves-ai-contracts-lenders-financing-its-build-out-2026-10-15/)及10/19 [FT关于新云商数据中心建设延迟](https://www.ft.com/content/9ea5a37d-15c9-4d5b-94d6-719048c9cd3c)属于**现实行业负面信号**，但不能由媒体推断NVDA的具体坏账已经实现。资料缺口：未完成2025年10—12月全部官方公告、各大云客户2026Q3全部资本开支指引与原始财报、全部许可/场地阶段逐月核验。

## 3. 公司正在做什么、做到哪一步？

| 重点项目 | 为什么做？希望达到什么结果？ | 当前进展与下一步 |
|---|---|---|
| **Blackwell→Vera Rubin平台升级** | 降低每单位推理计算成本、提升训练和网络吞吐，让客户愿意持续扩建整套AI工厂。 | Q2 Blackwell仍是大部分设备出货，Vera Rubin已在量产/从FY2027 Q3开始生产出货，伙伴CoreWeave、Google、Microsoft、Oracle和Nebius报告有运行机架；下一关Q3实际Rubin收入、稳定运行和74%毛利指引兑现。[2026Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| **推理系统、Vera CPU及网络光互联** | 除GPU外增加CPU/低延迟推理/交换机在同一机房的价值，扩大系统方案份额。 | 8/24 Groq3 LPX宣布量产，10/19 Modal准备采用Vera CPU，10/12 Cisco光模块为联合标准计划；下一关需要客户付费部署收入、可靠的不同平台每token总成本证据而不只是跑分。[Groq公告](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai) |
| **制造/HBM供应与库存约束** | 为高需求产品提前取得内存、封装和产能，防止无法交付，同时维持售价和良率。 | Q2供应/产能承诺从上季$119bn增至**$279bn**；库存从FY2026末$21.403bn升至$31.575bn，应收从$38.466bn升至$63.059bn。下一关是Q3新承诺与真正供货消耗、库存减值及客户收款。[10-Q Note10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| **AI云采购/第三方资本支持** | 帮缺资金客户取得机房、电力和采购GPU的融资能力，推动产品需求变成可运行算力。 | 7/26云容量**$36bn**（约六年合约）、8月SB Energy/OpenAI担保上限$105bn、平台伙伴MOU称可动员>$500bn资金；**$500bn非已融资实额，$108.5bn担保非已支付债务**。下一关终端付费、融资真实交割、云容量消化、担保逐阶段实际敞口及损失。[10-Q Notes](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| **CUDA软件、实体AI及区域产业部署** | 提高开发者转换成本，并在科研、工程、工业和自动驾驶领域扩大GPU之外的软件入口。 | 7月日本140MW合作目标、10月Adobe工具集成、10月Jülich量子仿真均有公告；尚缺这些项目可拆分增量收入、真实外部软件续费及利润。[Adobe公告](https://nvidianews.nvidia.com/news/adobe-and-nvidia-expand-collaboration-to-speed-agentic-creation) |

## 4. 财务状况：收入、利润和现金

全部单位**十亿美元**，美国GAAP，FY2025截至2025-01-26；FY2026截至2026-01-25；H1 FY2027截至2026-07-26；**TTM=FY2026＋H1 FY2027−H1 FY2026**，同长度比较。原始[2026 FY10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)和[Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

| 指标 | FY2025 | FY2026 | H1 FY2026 | H1 FY2027 | TTM至Q2 FY2027 |
|---|---:|---:|---:|---:|---:|
| GAAP收入 | 130.497 | 215.938 | 90.805 | 177.837 | **302.970** |
| GAAP毛利 | 97.858 | 153.463 | 60.521 | 133.299 | **226.241** |
| GAAP经营利润 | 81.453 | 130.387 | 50.078 | 117.270 | **197.579** |
| GAAP净利润 | 72.880 | 120.067 | 45.197 | 118.010 | **192.880** |
| 经营现金流 | 64.089 | 102.718 | 42.779 | 74.421 | **134.360** |
| 现金资本开支 | 3.236 | 6.042 | 3.122 | 4.434 | **7.354** |
| 简化自由现金流 | 60.853 | 96.676 | 39.657 | 69.987 | **127.006** |

<small class="financial-glossary">GAAP指美国会计准则；经营利润不含通常记在非营业收益中的投资浮盈；经营现金流是经营收付；本表简化FCF＝CFO−购买长期设备及无形资产的现金，不扣另列的设备付款本金（FY2027 H1另有$0.092bn）；公司披露的调整FCF口径可能不同。</small>

**资金说明：**2026-07-26现金$22.443bn及可交易债券$34.143bn，共**$56.586bn**，账面债务短期$1.000bn＋长期$32.366bn＝**$33.366bn**；此外持有可交易股票$42.783bn及非上市证券$51.157bn，**它们不是等价于无限制可用现金**，部分仍有锁定期，且波动损益已进入净利。Q2 10-Q资产负债表列长期经营租赁负债$4.985bn（短期相关额另列），H1融资净发行债券约$24.896bn。H1买入股权证券$42.404bn、现金回购普通股约$39.044bn及股息支付$6.290bn；回购与股息不等于经营支出或capex。采购、云租赁、设备投资和担保均有未来不同触发及有效期，**不能将合同总额机械当作已到期的有息负债、也不能用现有现金一笔抵销**。[Q2 10-Q现金流及Note10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

**总结：**截至FY2027 H1收入同比约**+95.85%**、经营利润同比**+134.17%**，增长确有营业利润兑现；同期GAAP净利润$118.01bn包含**$23.707bn证券净收益**（税影响及其他项目不能直接机械扣作为正式调整净利），H1 CFO $74.421bn明显小于净利，部分因为应收账款现金减少$24.590bn、库存现金减少$10.204bn。同期应收账面从$38.466bn增至$63.059bn、库存从$21.403bn升到$31.575bn；高增长解释了部分营运资本占用，但供需错配或客户融资若恶化，将影响现金转化。H1现金资本开支$4.434bn不足以代表广义总资本风险：未来供应承诺$279bn、云容量和设施担保应分别作为条件敞口持续追踪。

## 5. 管理层与资本分配

CEO Jensen Huang领导的平台技术与多代系统升级使FY2027 Q2同比业绩显著超越FY2026，管理层以Q1指引$91bn、Q2实际$96.221bn的同一GAAP收入口径完成超过前述财务指引的交付，这里只比较**公司指导**，不假称超过华尔街财报前共识。Q2新的Q3 $108bn±2%收入指引同样不能当已实现收入。[2026Q1公司指引](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)｜[Q2实际](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027/)。

资本分配的变化更重要：2026H1回购现金约$39.044bn、股息$6.29bn，FY2027 Q1上调季度每股股息为$0.25并增加$80bn回购授权；与此同时7/26资产负债表债务$33.366bn、上半年净发行债券约$24.896bn、H1 SBC损益$3.954bn。**法定在外股本**：2026-08-21 10-Q封面约**24.1bn**股，2026-07-26实际权益表**24.147bn**股，Q2 GAAP稀释加权平均**24.285bn**股，供EPS计算的分母不代表当前实际股数；数据商2026-10-19估算在外约**24.15bn**，与7月权益表吻合但不等于来自发行人的10月更新。研发与销售体系转为支持客户云和融资，$99bn股权投资、$25bn新增股权投资承诺及最大担保$108.5bn意味着公司已不是完全没有下游资本风险的传统芯片IP许可商。[Q2 10-Q Note10和权益表](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)｜[StockAnalysis](https://stockanalysis.com/stocks/nvda/statistics/)。

## 6. 估值分析：当前股价贵不贵？

| 关键指标 | 估算结果 |
|---|---|
| 参考股价及报价日 | **$217.09**，2026-10-19 16:00 EDT常规收盘；较2026-10-09 $229.28下降**5.32%** |
| 法定股份代理市值 | **约$5.232万亿美元**，按2026-08-21封面**24.1bn**实股作近似；数据商约24.15bn→$5.243万亿美元，10月精确经济股本未独立调和 |
| 当期适用估值 | 自算TTM GAAP **P/E约27.12×**（GAAP净利包含证券收益）、股权市值/TTM简化FCF **约41.19×**、市销 **17.27×**；StockAnalysis当前提供Forward P/E **17.95×**，但未明示NTM还是FY1及调整EPS口径，不能严格与旧报告同口径比较 |
| 保守情景（FY2028结束） | **折现到2026-10-20现值约$127–156/股**。假设FY2028收入$450bn、归一化扣SBC净利率45%、未来24.5bn稀释股、目标市盈率18–22×、年折现13% |
| 基础情景（FY2028结束） | **现值约$316–369/股**。假设FY2028收入$700bn、净利率52%、24.2bn股、24–28×、年折现11%；FY2028收入接近**10月9日的数据商FY2028平均收入预测$692.21bn**，但不是精确共识利润预测 |
| 乐观情景（FY2028结束） | **现值约$502–569/股**。假设FY2028收入$825bn、净利率55%、24.0bn股、30–34×、年折现10%，需要增长/平台定价和回购共同兑现 |

估值基准日**2026-10-20**；目标期**FY2028财年末约2028-01-30**，相距约**1.2786年**（第三方预测数据库将结束日标作1月31日，约一天标签差异不改条件结论）。上述为**研究假设条件现值，不是未来FY2028未折现股价**。采用股权净利估值`FY2028正常化GAAP净利（含持续SBC经济成本）/未来稀释经济股数×目标P/E÷(1+股权折现率)^1.2786`；**不再额外加账面现金或全部股权投资、也不第二次扣现有债**，避免在含投资/利息影响的净利模型中双算。股权投资非经常性市值收益没有被加进正常化毛利/利润率，模型也没有将$108.5bn担保一定发生损失。条件压力/完整计算、情景敏感性与未来SBC股数路径不足的限制记录见[研究底稿](../research-records/2026-10-20-research.md)。估值财务预测来自研究者，不是假定市场共识；[10/09预测快照](https://stockanalysis.com/stocks/nvda/forecast/)FY2027 non-GAAP EPS $9.31、FY2028 non-GAAP EPS $15.91，两个年度的指标分别与本页模型的**GAAP归一化税后利润口径不同**，不能把$15.91拿来直接证明模型的净利率。

**总结：**相比价格，**现金业务强但估值的敏感源是增长变现质量与信用支持风险**。保守模型仍显示约28%–41%下行，而基础模型给出明显上行，说明业绩兑现已强、但模型非常依赖FY2028 7000亿美元收入及52%净利润率和高倍数同时成立；若第三方融资无法为客户提供足够建设现金，产品订单和采购承诺可能同步调整。即使目前静态Forward P/E看起来较低，也不能只凭“17.95倍”下定论；更稳妥应同时验证Q3 1080亿美元指引、库存和应收转现金、阶段性最大担保未实际扩大为损失、客户终端算力利用率。

## 7. 未来值得关注的事件

| 重要事件 | 为什么值得关注 |
|---|---|
| **FY2027 Q3业绩（数据商预计2026-11-18，发行人正式日期未核实）** | 对照公司8/26 **$108bn±2%收入、GAAP毛利74.0%±0.5个百分点**指引，观察数据中心计算/网络、Rubin量产实际经营杠杆、净利的证券收益分拆与真实OCF。 |
| **大型客户10–11月财报及2027年AI capex说明**（不同客户日期核实程度不同） | Microsoft、Google、Amazon、Meta、Oracle与私有AI云需要公布可融资的建设项目、利用率、云收入及债务；若转向自研ASIC或减少采购，会改变FY2028预期。 |
| **FY2027 Q3供应/云容量与担保净敞口更新**（随财报） | 7/26 $279bn供应、$36bn云容量及最高$108.5bn担保是已披露基线，下一关是实际未履约余额、有效敞口、生效项目与终端客户是否承担费用。 |
| **SB Energy/OpenAI首批大型设施交付（公司预计FY2029，尚无确定日）** | 按九期/建设批准逐期生效担保，不是2026年一次性1085亿美元全额债务；需用项目竣工、正式租约和客户真实付款验证。 |
| **Rubin与Vera/Groq3及Cisco光互联规模收入节点**（未披露确定日期） | 产品宣布量产和客户采用后，分别验证产出良率、毛利、延迟/功耗成本、软件收入和竞争对手替代节奏。 |

**总结：**下一份正式财报的收入与毛利如果超前改善，同时应收、库存和云信用责任下降，将比单纯跑分更加强化谨慎看好。若实际项目融资受压而承诺增长显著快于客户使用及收现，应降低对FY2028基础模型的信心。

## 8. 主要投资风险

| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |
|---|---|---|
| **客户融资与循环采购** | NVDA的投资/云购买/担保可能支撑部分原有客户对NVIDIA芯片采购，遇到融资困难时设备销售和股权资产同时受损。 | CoreWeave/Nscale/SB Energy项目资本市场利差走阔、客户资本开支项目取消或推迟、云容量无法转由第三方收费使用。 |
| **供应与HBM/封装承诺过度** | 订单低于提前锁定的采购量会导致库存跌价、解约成本及73%–75%高毛利下行。 | 期末库存$31.575bn、后续供应承诺$279bn仍增长却无匹配收款、存货拨备提高。 |
| **大客户/自研ASIC替代** | 云巨头把更多训练/推理迁移到TPU、Trainium等，整体平台毛利率和份额可能下降。 | 主要采购商减少份额、不同任务下更便宜可用的替代方案、硬件系统价格下降。 |
| **资本市场和监管出口限制** | 禁售中国某些芯片、HBM或关税措施，以及AI项目债券压力，可能削弱地区收入和客户采购预算。 | H20/H200许可收紧、中国实际计算出货未改善、利率和数据中心融资成本持续攀升。 |
| **投资收益与高估值失配** | GAAP归属净利润若由证券浮盈抬高、OCF却落后，正常化EPS和股票合理倍数可能同时下降。 | FY2027 H1 $23.707bn股权证券收益不再出现、应收与库存增长快于营收、客户付款周期延长。 |

**总结：**最大反证不是“GPU忽然没人买”，而是NVIDIA、核心AI云客户和模型商共同押注同一算力资产与终端需求，导致硬件销量、股票投资和保证敞口高度相关。下行情景应考虑客户建设延误与市场估值降档同时发生，而不能把高账面投资收益当成缓冲。

## 9. 四种投资视角：怎么看这家公司？

| 投资视角 | 最关注什么 | 对公司的判断 |
|---|---|---|
| **巴菲特式** | 平台客户持续采购与企业可分配现金 | FY2027 H1经营利润$117bn和OCF$74bn证明商业利润真实，但云承诺/担保可能使未来股东现金与现有轻资产盈利路径不一样，价格仍需风险折扣。 |
| **芒格式** | 最脆弱的投资叙事以及永久损失路径 | 最应避免的是把被公司共同投资和提供担保的AI云采购，误算成完全独立、不相关的终端市场需求；应持续反推融资链违约造成的二次风险。 |
| **段永平式** | 客户是不是为有用的技术持续付费 | 运行中的Blackwell系统、Rubin合作与Adobe等产品集成是有用价值的证据，但真实每token成本和云租户复购、收款质量比新闻发布更能支持长期价格。 |
| **李录式** | AI计算基础设施的长期位置与下行保护 | 供应链、CUDA生态和现金回报可理解，但$5.2万亿美元以上的估值对持续增长和信用风险较敏感，保守情景所示下行保护未必充分。 |

**总结：**以上仅是四种投资方法，不是四位投资者本人发表的观点。NVIDIA在AI商业化获益方面的财务证据比大量尚亏损的算力企业更强，关键是能否保持高毛利与经营现金，同时不把自己变成过度承担客户融资与建设风险的最终兜底方。
