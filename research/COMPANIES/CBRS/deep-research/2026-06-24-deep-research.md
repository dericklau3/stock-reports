# Cerebras Systems（CBRS）深度研究 - 2026-06-24

- **Research view**: 中性 / 等待确认
- **Confidence**: 中等偏低
- **Time horizon**: 12-24 个月
- **Main thesis**: Cerebras 是 AI 推理基础设施中少数有明确差异化硬件路线、顶级客户背书和高增长收入的上市标的；但 2026-06-23 收盘市值约 497.9 亿美元、盘后仍约 442 亿美元，已经把“成为 Nvidia 之外重要 AI 推理平台”的成功路径提前折现。当前更适合跟踪第一年上市后的执行质量，而不是用一季增长直接给高确定性正面观点。
- **Key risk**: 最大风险是客户集中和重资本扩张叠加高估值：OpenAI、AWS、G42/MBZUAI 等关键客户驱动增长，但公司 2026 年仍指引核心 operating margin 为 -28% 至 -32%，数据中心扩张、客户权证、OpenAI working capital loan 和 IPO 后股本结构会让真实股东回报更复杂。

> 说明：本文是研究支持与决策框架，不构成个性化投资建议。CBRS 于 2026-05-14 IPO，交易历史很短，估值与财务口径仍有较高不确定性。

## 1. Executive View

**研究观点：中性 / 等待确认。** Cerebras 的业务故事很强：它不是又一家普通 AI 软件公司，而是用整片硅晶圆做成超大 AI 芯片和整机系统，目标是在 AI 推理场景中用速度差异化挑战 GPU 集群。2026Q1 财报显示需求确实旺盛：GAAP revenue 1.934 亿美元，同比增长 94%；core revenue 1.913 亿美元，同比增长 92%；公司还披露 OpenAI 750MW、超过 200 亿美元的多年合作，以及 AWS 分发合作。

但投资结论不能只看“AI + OpenAI + 高增长”。截至 2026-06-23，CBRS 收盘价 226.72 美元，市值约 497.9 亿美元；财报后盘后跌至 201.27 美元，盘后隐含市值仍约 442 亿美元。以公司 FY2026 core revenue 指引 8.55-8.65 亿美元中点计，收盘市值约为 57.9x FY2026 core revenue；即使按盘后价格估算，仍约 51x。这个估值要求公司未来数年持续高速增长，并把高速推理需求转成可持续毛利和现金流。

核心判断：

- **业务质量有真实亮点。** 2026Q1 GAAP revenue 同比 +94%，GAAP gross margin 45%，core gross margin 47%；cloud and other services revenue 同比 +178%，说明公司不只卖硬件，也在把能力云化。
- **OpenAI 和 AWS 是强背书，也是集中风险。** 公司自己的 8-K 风险提示明确点名依赖 OpenAI、G42、MBZUAI 和 AWS 等重要客户；任何合同节奏、资本安排、模型需求或竞争格局变化都会放大波动。
- **现金看似充足，但增长消耗也重。** 2026Q1 末 cash、restricted cash 和 short-term investments 合计约 33 亿美元；随后 Q2 IPO gross proceeds 64 亿美元。但 Q1 capex 1.32 亿美元，FCF 约 -1.20 亿美元，且公司为了数据中心扩张还使用 OpenAI 10 亿美元 working capital loan 和最高 8.5 亿美元 revolving credit facility。
- **估值高度依赖 2027-2028 扩张。** 2026 年公司指引 core revenue 8.55-8.65 亿美元、core gross margin 38%-41%、core operating margin -28% 至 -32%。也就是说，收入增长强，但当前仍是亏损扩张阶段。

最强反方理由：如果 Cerebras 的 wafer-scale 架构在低延迟推理中持续领先，并且 OpenAI/AWS 合作把它变成大型 AI 应用的标准推理后端之一，今天的高 EV/Sales 可能是早期平台溢价，而不是泡沫。但这需要后续财报证明：客户不止少数大客户、毛利率不会被数据中心租赁/扩容吞噬、资本开支能转化为高利用率收入。

## 2. Business Model and Industry Structure

### 初学者版：Cerebras 到底卖什么，谁付钱

Cerebras 卖的是 AI 计算能力。客户通常是大模型公司、云厂商、AI 原生企业、政府或主权 AI 项目。客户想要的不是“芯片本身”，而是更快地训练、部署和运行 AI 模型。

把它拆成普通话：

- **硬件销售**：Cerebras 设计并制造大型 AI 计算系统，客户买设备放到自己的数据中心或大型计算集群里使用。收入来自设备和相关系统销售。
- **云与服务**：客户不买设备，而是通过 Cerebras 或合作云平台调用推理算力，按合同或使用量付费。这更像云计算服务，收入可能更持续，但需要 Cerebras 自己先投入数据中心、设备和运营成本。
- **客户合作与权证**：Cerebras 会和大客户签大额长期合同，有时也给客户股权/权证激励。这样可以锁定需求，但会带来收入抵减、稀释和客户议价问题。

核心经济问题是：Cerebras 能否把“很快的 AI 推理速度”变成客户愿意长期付费、毛利率可维持、资本开支可回收的规模化平台。

### 关键术语翻译

| 术语 | 通俗解释 |
|---|---|
| Wafer-Scale Engine（WSE） | 把一整片硅晶圆做成一个超大处理器，而不是把很多小芯片连在一起。目标是减少芯片之间通信瓶颈。 |
| Inference（推理） | AI 模型训练好以后，真正回答用户问题、生成代码、生成图片或处理任务的过程。比如你问模型一个问题，模型输出答案，就是推理。 |
| Training（训练） | 用海量数据训练模型，让模型学会规律。训练通常更重，推理则是日常使用中不断发生的计算。 |
| Prefill / Decode | 大模型推理的两个阶段。prefill 处理输入上下文，decode 逐字生成输出。Cerebras 与 AWS 的策略是让 AWS Trainium 3 处理 prefill，Cerebras CS-3 负责高速 decode。 |
| Core revenue | 公司使用的非 GAAP 收入口径，排除了客户权证摊销、数据中心 pass-through 收入/成本等影响。适合观察核心业务趋势，但不能替代 GAAP。 |
| Customer warrants | 给客户的权证或股权相关权益。商业上可能帮助拿订单，会计上可能作为 contra-revenue 抵减收入，也会带来稀释复杂性。 |

### 行业结构

Cerebras 的竞争不是单一维度，而是同时和芯片、系统、云和自研 ASIC 竞争。

| 竞争层级 | 主要对手 | Cerebras 优势 | Cerebras 短板 |
|---|---|---|---|
| AI GPU/加速器 | Nvidia、AMD、Intel、Groq、TPU/自研芯片 | wafer-scale 架构、高速推理、片上内存和低延迟定位 | 软件生态、供应链规模、客户迁移成本弱于 Nvidia |
| 云推理服务 | AWS、Azure、Google Cloud、CoreWeave、Oracle Cloud | 可通过 AWS/OpenAI 等合作快速放大分发 | 需要自己投入或租用数据中心能力，资本密集 |
| 大客户自研 | OpenAI、Google、Amazon、Meta、Microsoft 自研 ASIC | 可作为专用高速推理补充 | 大客户可能长期内化算力，供应商议价能力有限 |
| 主权 AI / 企业 AI | 各类 AI 基础设施供应商 | 高性能、差异化硬件、可本地部署 | 项目型收入波动，销售周期和政治/合规风险 |

公司类型判断：CBRS 是 **高增长、早期上市、资本密集型 AI 基础设施公司**，更接近 CoreWeave + AI 芯片硬件的混合体，而不是轻资产软件公司。因此估值应重点看 EV/Sales、收入增长、毛利率、capex 强度、客户集中和路径到 FCF。

## 3. Segment and Product Analysis

### Hardware：卖系统和机架，是当前基础业务

硬件业务收入来自 Cerebras 的 AI 计算平台，包括 proprietary systems、software 和 racks，用于数据中心到超算级部署。2026Q1 hardware revenue 为 1.106 亿美元，同比增长 59%；GAAP hardware gross margin 41%，core hardware gross margin 42%。

硬件业务的优点是收入确认清晰、客户可以直接部署；缺点是项目型、资本密集、毛利率可能受供应链和大型客户议价影响。对投资者来说，硬件增长需要和 backlog、交付周期、库存、客户集中一起看。

### Cloud and Other Services：更像长期平台化方向

云和服务业务让客户不一定买设备，而是使用 Cerebras 的 AI 推理能力。2026Q1 cloud and other services revenue 为 8,281 万美元，同比增长 178%；GAAP gross margin 49%，core cloud and other services gross margin 53%。

这部分更像未来的高质量收入来源，因为如果客户持续调用推理服务，收入会比一次性硬件销售更经常性。但它的代价也明显：公司需要数据中心容量、设备、租赁、网络、电力和运营团队。2026 年 core operating margin 指引为 -28% 至 -32%，说明云化扩张短期会消耗利润。

### OpenAI / AWS 合作：最大亮点，也是最大检验点

公司在 2026Q1 材料中披露：

- 与 OpenAI 达成超过 200 亿美元的多年合作，OpenAI 将部署 750MW 的 Cerebras 高速推理算力。
- 与 AWS 开始多年合作，把 Cerebras fast inference 通过 AWS 的全球分发能力带给更多客户。
- 与 AWS 的技术方案中，AWS Trainium 3 处理 prefill，Cerebras CS-3 负责高速 decode。

专业判断：这两个合作显著提高 Cerebras 的可信度。如果 OpenAI 和 AWS 真的把它用于关键推理负载，Cerebras 可以成为 AI 基础设施链条中有地位的供应商。但商业风险在于：这些合同可能伴随融资、贷款、权证、容量承诺和客户议价；收入确认节奏与现金流回收不一定同步。

## 4. Financial Deep Dive

### 2026Q1 财务表现

| 指标 | 2026Q1 | 2025Q1 | 变化 |
|---|---:|---:|---:|
| GAAP revenue | 1.934 亿美元 | 9,951 万美元 | +94% |
| Hardware revenue | 1.106 亿美元 | 6,967 万美元 | +59% |
| Cloud and other services revenue | 8,281 万美元 | 2,984 万美元 | +178% |
| GAAP gross profit | 8,618 万美元 | 4,160 万美元 | +107% |
| GAAP gross margin | 44.6% | 41.8% | +280 bps |
| GAAP operating loss | -1,504 万美元 | -2,847 万美元 | 改善 |
| GAAP net loss | -1,401 万美元 | -2,387 万美元 | 改善 |
| Operating cash flow | 1,234 万美元 | -5,494 万美元 | 改善 |
| Capex | 1.320 亿美元 | 9,824 万美元 | +34% |
| 粗略 FCF | -1.196 亿美元 | -1.532 亿美元 | 改善但仍为负 |
| SBC | 959 万美元 | 915 万美元 | +5% |

增长质量：收入增长非常强，毛利率也有改善，核心经营亏损从 2025Q1 的 -1,932 万美元收窄到 2026Q1 的 -351 万美元。但自由现金流仍为负，且后续全年 operating margin 指引显示公司会继续为增长投入。

### 2026 全年指引

公司给出的 core non-GAAP 指引：

| 指标 | Q2 2026 指引 | FY2026 指引 |
|---|---:|---:|
| Core revenue | 约 1.94 亿美元，同比增长 88% | 8.55-8.65 亿美元，同比增长约 69% |
| Core gross margin | 36%-38% | 38%-41% |
| Core operating margin | -30% 至 -32% | -28% 至 -32% |

这个指引的含义很清楚：收入高增长，但公司选择继续亏损扩张。研究重点应从“收入能不能增长”推进到“增长能不能带来规模经济”。

### 资产负债表和融资结构

截至 2026-03-31：

- Cash and cash equivalents：17.16 亿美元。
- Restricted cash：10.29 亿美元。
- Investments：5.16 亿美元。
- Cash + restricted cash + short-term investments：约 33 亿美元。
- Total assets：49.48 亿美元。
- Total liabilities：21.96 亿美元。
- Customer deposits：3.684 亿美元。
- Deferred revenue：2.443 亿美元。
- Loan from customer：9.829 亿美元，其中 current 6.213 亿美元、non-current 3.616 亿美元。

后续 Q2 事项：

- 2026 年 1 月获得 OpenAI 10 亿美元 working capital loan。
- 2026 年 2 月完成 10 亿美元 Series H pre-IPO financing。
- 2026 年 4 月获得最高 8.5 亿美元 revolving credit facility。
- 2026 年 5 月 IPO gross proceeds 64 亿美元。

财务结论：Cerebras 现金资源很强，但业务也明显资本密集。Restricted cash、客户贷款、数据中心扩张和客户权证都让“现金很多”这件事需要打折理解。普通股东最该监控的是：IPO 后净现金到底转化为多少可持续 revenue capacity，以及是否需要继续牺牲 margin 换增长。

### 会计质量与非 GAAP 调整

Cerebras 的 core 指标排除了三类重要项目：

- Stock-based compensation。
- Customer warrants amortization，作为 contra-revenue 抵减收入。
- Data center pass-through revenues and costs。

这些调整有商业逻辑，但不能忽略。客户权证代表公司可能用股权经济利益换取长期客户关系；pass-through 数据中心收入/成本说明部分收入可能不是高毛利核心技术收入；SBC 则是股东稀释成本。研究上应同时看 GAAP 与 core，不应只用 core revenue 放大估值叙事。

## 5. Management and Capital Allocation

Cerebras 由 Andrew Feldman 等创始团队创建。Feldman 曾共同创办 SeaMicro，后出售给 AMD，这给团队带来硬件系统创业与退出经验。当前管理层最大的挑战不是讲清技术，而是把技术优势变成稳定商业模式。

资本配置方向：

- 优先扩张数据中心和推理容量。
- 支持 OpenAI 和 AWS 等大客户部署。
- 持续投入 WSE/CS 系统、软件栈、云推理平台。
- 通过 IPO、客户贷款、pre-IPO financing、credit facility 提前准备资本。

我对管理层执行的初步评价是 **技术和融资能力强，上市公司可验证记录短**。接下来 4-6 个季度比 IPO 故事更重要。

## 6. Valuation Work

### 当前估值快照

基于 StockAnalysis 2026-06-23 数据：

| 指标 | 数值 |
|---|---:|
| 收盘价 | 226.72 美元 |
| 盘后价 | 201.27 美元 |
| 收盘市值 | 497.9 亿美元 |
| 收盘 enterprise value | 489.4 亿美元 |
| Shares out | 2.196 亿股 |
| TTM revenue | 6.039 亿美元 |
| TTM net income | 8,788 万美元 |
| PE ratio | 163.8x |
| IPO price | 185.00 美元 |
| IPO date | 2026-05-14 |

估值观察：

- 收盘 EV / TTM revenue 约 81x。
- 收盘 market cap / FY2026 core revenue midpoint 约 57.9x。
- 盘后 market cap / FY2026 core revenue midpoint 约 51.4x。

这不是“普通半导体公司”估值，而是早期 AI 平台估值。要让这个估值合理，公司需要证明 2026 年 8.6 亿美元收入不是峰值订单，而是通往数十亿美元收入规模的第一步。

### Valuation Method Selection

CBRS 当前不适合用 PE 作为主估值方法，因为 TTM net income 受到 IPO 前后资本结构、非经营项目、优先股/普通股转换和早期规模影响。更合适的方法是：

- EV / forward revenue：因为公司仍处于高增长阶段。
- EV / gross profit：检查毛利率是否足够支撑未来盈利。
- 情景估值：把客户集中、毛利率、capex 和规模经济放入 bear/base/bull。

### Scenario Valuation

以下为研究情景，不是目标价承诺。

| 情景 | 2028 revenue 假设 | 盈利/现金流假设 | 合理估值逻辑 | 隐含股权价值 | 近似每股价值 | 触发条件 |
|---|---:|---|---|---:|---:|---|
| Bear | 15-20 亿美元 | 毛利率 30%-35%，operating margin 仍为负，FCF 持续消耗 | 客户集中和竞争压低倍数，12-18x revenue | 180-360 亿美元 | 约 80-165 美元 | OpenAI/AWS 部署慢、毛利率下行、客户权证/融资成本稀释 |
| Base | 30-40 亿美元 | 毛利率 40%左右，operating margin 逐步接近盈亏平衡，FCF 仍波动 | 高增长 AI 基础设施，18-25x revenue | 540-1,000 亿美元 | 约 245-455 美元 | 收入复合高增长，客户扩大，margin 逐步改善 |
| Bull | 60 亿美元以上 | 毛利率 45%+，operating margin 转正且 FCF 转正 | 成为主流低延迟推理平台之一，25-35x revenue | 1,500-2,100 亿美元以上 | 约 680-955 美元以上 | OpenAI/AWS 大规模放量，客户多元化，云推理利用率高 |

当前盘后约 201 美元仍接近 base case 左侧，但不是低风险。估值主要买的是 2027-2028 的高速放量和平台化，而不是 2026 年利润。

## 7. Catalysts and Monitoring Plan

近中期催化：

- Q2 2026 results：验证 1.94 亿美元 core revenue、36%-38% core gross margin、-30% 至 -32% core operating margin 指引。
- OpenAI 750MW 部署节奏：是否转化为可确认收入和现金流。
- AWS 合作上线范围：是否只是技术合作，还是带来广泛企业客户使用。
- 数据中心采购/租赁进度：capex 和 operating cost 是否超预期。
- 客户多元化：OpenAI、AWS、G42/MBZUAI 之外是否有足够大客户。
- 毛利率：Q1 core gross margin 47% 到 Q2 指引 36%-38% 的下降是否只是阶段性。
- IPO 锁定期和股本流动性：上市早期波动和潜在解禁压力。

重点监控指标：

- GAAP revenue、core revenue、hardware / cloud split。
- Core gross margin、GAAP gross margin。
- Core operating margin 和 GAAP operating loss。
- Capex、operating cash flow、free cash flow。
- Customer deposits、deferred revenue、customer loan balance。
- Customer warrants amortization 与 contra-revenue。
- Backlog / RPO，如果公司未来披露。
- Large customer concentration。
- Data center utilization and capacity。
- 新客户数量、行业分布、AWS marketplace/渠道进展。

## 8. Risk Register

| 风险 | 概率 | 影响 | 为什么重要 |
|---|---|---|---|
| 估值压缩 | 高 | 高 | 50x+ forward revenue 容错率很低，任何增长或 margin 失误都会放大股价波动。 |
| 客户集中 | 高 | 高 | 公司风险披露明确点名 OpenAI、G42、MBZUAI、AWS 等重大客户依赖。 |
| 毛利率下行 | 中高 | 高 | Q2 core gross margin 指引 36%-38%，低于 Q1 47%。 |
| 资本密集 | 高 | 高 | 数据中心扩张、租赁、设备和网络投入会消耗现金流。 |
| 竞争压力 | 高 | 高 | Nvidia 生态、AWS/Google/Meta 自研芯片、AMD/Groq 等都会争夺推理负载。 |
| 客户权证和稀释 | 中高 | 中高 | 大客户激励可能换来订单，但也会抵减收入、稀释股东。 |
| 上市历史短 | 高 | 中高 | IPO 后只有一份财报，公开市场执行可验证记录不足。 |
| 技术替代 | 中 | 高 | 如果模型架构、推理优化或 GPU/ASIC 性价比变化，速度优势可能被压缩。 |
| 供应链和制造 | 中 | 高 | 超大芯片和系统集成对制造良率、供应链和交付能力要求高。 |

最强 disconfirming evidence：如果未来两个季度显示 core revenue 高于指引、gross margin 稳定、客户从 OpenAI/AWS 扩展到更多企业，并且 FCF 消耗没有随规模恶化，那么当前谨慎观点需要上调。

## 9. Final Research Framework

CBRS 是一个值得重点跟踪的 AI 基础设施新股，但当前结论是 **中性 / 等待确认**。它的技术路线和客户背书都强，2026Q1 的增长也确实亮眼；问题在于估值已经非常激进，而公司的商业模式还处于“用资本换增长、用大客户验证平台”的阶段。

我会把 CBRS 上调为 **建设性 / 正面** 的条件：

- 连续 2-3 个季度 core revenue 高于指引，并且不是单一客户拉动。
- Core gross margin 稳定在 40%+，Q2 指引下滑被证明是阶段性。
- OpenAI 和 AWS 合作带来可量化收入、利用率或新客户扩散。
- Customer warrants、pass-through costs、customer loan 等项目透明度提升。
- Operating margin 明确改善，FCF 消耗可控。
- 公司披露 backlog/RPO 或其他能证明未来收入可见性的指标。

我会下调为 **负面 / thesis weakening** 的条件：

- FY2026 revenue 指引被下修，或 Q2/Q3 增长明显低于预期。
- Gross margin 持续低于 35%，说明云/数据中心扩张侵蚀经济模型。
- OpenAI/AWS 部署延迟或合同经济性低于预期。
- 客户集中没有改善，新增客户不足。
- Capex 和租赁负担导致 FCF 明显恶化。
- 大量客户权证、SBC 或解禁压力导致普通股东被稀释。

## Sources

- SEC, [Cerebras Systems Form 8-K, 2026-06-23](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrs-20260623.htm).
- SEC, [Exhibit 99.1 - Cerebras Systems Announces Strong First Quarter 2026 Results](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrsannouncesfinancialresu.htm), 2026-06-23.
- SEC, [Cerebras submissions, CIK 0002021728](https://data.sec.gov/submissions/CIK0002021728.json), checked 2026-06-24.
- GlobeNewswire, [Cerebras Systems Announces Strong First Quarter 2026 Results](https://www.globenewswire.com/news-release/2026/06/23/3316476/0/en/Cerebras-Systems-Announces-Strong-First-Quarter-2026-Results.html), 2026-06-23.
- StockAnalysis, [CBRS stock overview](https://stockanalysis.com/stocks/cbrs/), checked 2026-06-24.
- StockAnalysis, [CBRS market cap](https://stockanalysis.com/stocks/cbrs/market-cap/), checked 2026-06-24.
- StockAnalysis, [CBRS financials](https://stockanalysis.com/stocks/cbrs/financials/), checked 2026-06-24.
- StockAnalysis, [CBRS company profile](https://stockanalysis.com/stocks/cbrs/company/), checked 2026-06-24.
