# Cerebras Systems（CBRS）深度研究更新 - 2026-07-07

- **Research view**: 中性偏建设性 / 继续等待确认
- **Confidence**: 中等偏低
- **Time horizon**: 12-24 个月
- **Main thesis**: Cerebras 是 AI 推理基础设施中少数具有真实硬件架构差异化、OpenAI/AWS 顶级客户背书、并已开始商业放量的上市标的；但公司仍处于 IPO 后早期、客户集中、资本密集和亏损扩张阶段。股价从 6 月高位回落后，风险回报比明显改善，但当前仍不适合作为“高确定性核心仓位”，更适合作为小仓位观察型 AI 基础设施期权。
- **Key risk**: OpenAI/AWS/G42/MBZUAI 等少数大客户决定收入节奏；同时，数据中心扩张、客户权证、OpenAI working capital loan、pass-through 数据中心收入/成本，会让收入增长与普通股东自由现金流之间存在很大落差。

> 本文是研究支持与决策框架，不构成个性化投资建议。CBRS 于 2026-05-14 IPO，公开市场交易和财报历史极短，估值置信度低于成熟上市公司。

## 1. Executive View

**结论先讲：CBRS 值得跟踪，但还没到“可以放心重仓”的阶段。**

2026-07-07 Nasdaq 数据显示，CBRS 普通股收盘价为 **176.61 美元**，盘后最新成交约 **175.60 美元**；StockAnalysis 页面显示市值约 **400.1 亿美元**、TTM revenue 约 **6.039 亿美元**、shares outstanding 约 **2.2653 亿股**、PE 约 **124.4x**。以公司 2026 年 core revenue 指引中点 **8.60 亿美元**计算，当前市值 / FY2026 core revenue 约 **46.5x**。这比 2026-06-23 收盘约 57.9x FY2026 core revenue 明显便宜，但仍是非常高的 AI 平台估值。

核心判断：

- **业务故事强**：Cerebras 用 wafer-scale 架构做 AI 计算系统和云推理服务，目标是在低延迟、高吞吐推理中挑战 GPU 集群。公司 2026Q1 GAAP revenue **1.934 亿美元**，同比 **+94%**；core revenue **1.913 亿美元**，同比 **+92%**。
- **客户背书强**：公司 2026-06-23 8-K / Exhibit 99.1 披露，与 OpenAI 达成 **750MW、超过 200 亿美元**的多年合作，并与 AWS 开始多年 fast inference partnership。
- **财务质量仍需验证**：2026Q1 GAAP gross margin 约 **45%**，core gross margin **47%**，但公司全年指引 core operating margin 仍为 **-28% 至 -32%**，说明收入高增长暂时不是高利润增长。
- **估值下修后进入可观察区**：175-180 美元附近已经低于 IPO 价 185 美元，市场开始从“AI 稀缺性溢价”回到“证明商业模式”的阶段。但如果未来 2-3 个季度不能证明 OpenAI/AWS 合同可持续转化为高毛利收入与更好现金流，股价仍可能继续被压缩到 120-150 美元区间。

最强反方理由：如果 Cerebras 的架构真的成为 OpenAI、AWS 和大型企业推理的核心补充，当前 400 亿美元市值可能只是早期平台价值；但这个判断需要用未来财报验证，不能只凭 OpenAI/AWS 的品牌背书下结论。

## 2. Business Model and Industry Structure

### 初学者版：Cerebras 到底是做什么的？

Cerebras 卖的不是普通消费电子芯片，而是 **AI 计算能力**。客户包括大模型公司、云厂商、政府/主权 AI 项目、研究机构和企业客户。客户付钱的原因很简单：AI 模型越大、用户越多，推理请求越多，就需要更快、更便宜、更稳定的计算基础设施。

Cerebras 的商业模式可以拆成三层：

1. **卖硬件系统**：客户购买 Cerebras 的 AI 超算系统，部署在自己的数据中心。
2. **卖云端推理服务**：客户不买机器，而是通过 Cerebras 或 AWS 等渠道使用算力，按合同或使用量付费。
3. **大客户长期容量合作**：例如 OpenAI 承诺购买大量推理容量，Cerebras 先扩建/部署容量，再分期交付服务。

核心经济问题：**Cerebras 能不能把“很快的 AI 推理速度”转化为可持续收入、稳定毛利率和最终自由现金流？**

### 关键术语翻译

- **Wafer-Scale Engine（WSE）**：把一整片硅晶圆做成一个超大芯片，而不是把很多小芯片拼起来。好处是减少芯片之间通信瓶颈，理论上适合低延迟推理。
- **Inference（推理）**：AI 模型训练好后真正回答问题、生成代码、生成文字/图片的过程。ChatGPT 每次回答问题，就是推理。
- **Prefill / Decode**：大模型推理的两个阶段。prefill 处理输入上下文，decode 逐字生成答案。Cerebras 与 AWS 的设想是让 AWS Trainium 3 做 prefill，Cerebras CS-3 做高速 decode。
- **Core revenue**：公司非 GAAP 收入口径，排除客户权证摊销、数据中心 pass-through 收入/成本等影响。它有助于看核心业务，但不能替代 GAAP。
- **Customer warrants（客户权证）**：公司给客户未来买股票的权利，商业上可能换来大合同，会计上可能抵减收入并造成稀释。

### 行业位置

CBRS 处于 AI 基础设施链条中游：上游依赖晶圆代工、先进封装、电力/数据中心；下游服务 OpenAI、AWS、企业 AI 和主权 AI 客户。它不是纯芯片公司，也不是纯云公司，而是 **AI 芯片 + 系统 + 云推理平台**的混合体。

主要竞争对手和替代方案：

- **Nvidia GPU 生态**：最大竞争压力。优势是软件生态、开发者基础、供应链规模和客户习惯。
- **AMD / Intel / Groq / TPU / AWS Trainium 等加速器**：都在争夺 AI 推理成本和性能。
- **云厂商自研 ASIC**：OpenAI、AWS、Google、Meta、Microsoft 等大客户可能长期自研或多供应商分散采购。
- **CoreWeave、Oracle Cloud、Azure、Google Cloud 等算力平台**：可能既是分销渠道，也可能是竞争对手。

## 3. Segment and Product Analysis

### Hardware：硬件系统是当前基础收入

2026Q1，Cerebras hardware revenue 为 **1.106 亿美元**，同比 **+59%**；GAAP hardware gross margin 约 **41%**，core hardware gross margin 约 **42%**。

这部分收入更像卖大型计算设备。优点是订单金额大、收入确认相对明确；缺点是项目型波动高，客户集中和供应链风险明显。硬件收入能证明技术被采用，但它本身不一定形成软件公司那种高复购、高毛利、低资本开支模型。

### Cloud and Other Services：未来平台化方向

2026Q1，cloud and other services revenue 为 **8,281 万美元**，同比 **+178%**；GAAP gross margin 约 **49%**，core cloud and other services gross margin 约 **53%**。

这部分更像未来的高质量收入来源：客户持续调用推理服务，Cerebras 收取使用费或合同收入。但代价是公司要提前建设/租用数据中心，购买设备，承担电力、网络、运维和资本成本。公司 10-Q 也提示，云业务投资会在近期间歇性压低 cash flow、gross margin 和 operating margin。

### OpenAI / AWS：最大亮点，也是最大风险

公司披露：

- 2025 年 12 月与 OpenAI 签订 master relationship agreement，OpenAI 承诺购买 **750MW** AI inference compute capacity，预计 2026-2028 分批部署；OpenAI 还有选择权，可在 2030 年前额外购买 **1.25GW** capacity。
- 2026 年 1 月 OpenAI 提供约 **10 亿美元 working capital loan**，Cerebras 表示已开始并预计继续以非现金 service credits 偿还。
- 2026Q1 开始确认 OpenAI arrangement 相关收入。
- 2026 年与 AWS 开启多年 fast inference partnership，计划通过 AWS 分发 Cerebras 推理能力。

这说明 Cerebras 已经从“技术样品”进入“顶级客户商业验证”阶段。但投资者必须问：这些合同到底能产生多少高质量自由现金流？如果大客户要求权证、融资、价格优惠或容量承诺，普通股东实际拿到的经济利润可能低于 headline revenue。

## 4. Financial Deep Dive

### 2026Q1 经营快照

- GAAP revenue：**1.934 亿美元**，同比 **+94%**，环比 **+13%**。
- Hardware revenue：**1.106 亿美元**，同比 **+59%**。
- Cloud and other services revenue：**8,281 万美元**，同比 **+178%**。
- GAAP gross margin：**45%**。
- GAAP operating loss：**-1,504 万美元**。
- GAAP net loss：**-1,401 万美元**。
- Operating cash flow：约 **1,234 万美元**。
- Capex：约 **1.320 亿美元**。
- 粗略 free cash flow：约 **-1.196 亿美元**。
- Cash、restricted cash、short-term investments 合计：约 **33 亿美元**，但这还未反映 IPO 后完整资本结构。

### 2026 年指引

公司 2026-06-23 财报指引：

- Q2 2026 core revenue：约 **1.94 亿美元**，同比 **+88%**。
- Q2 core gross margin：**36%-38%**。
- Q2 core operating margin：**-30% 至 -32%**。
- FY2026 core revenue：**8.55-8.65 亿美元**，中点同比约 **+69%**。
- FY2026 core gross margin：**38%-41%**。
- FY2026 core operating margin：**-28% 至 -32%**。

解释：收入增长很强，但 2026 年仍是亏损扩张年。估值不能简单按“收入高增长”处理，必须看毛利率、capex、客户权证、租赁和融资结构。

### 资产负债表与资本结构

截至 2026-03-31 10-Q：

- Total assets：约 **49.48 亿美元**。
- Total liabilities：约 **21.96 亿美元**。
- Deferred revenue：current **1.499 亿美元**，non-current **9,434 万美元**。
- Customer deposits：约 **3.684 亿美元**。
- Working capital loan：current **6.213 亿美元**，non-current **3.616 亿美元**。
- Property and equipment, net：约 **5.724 亿美元**。
- Operating lease right-of-use assets：约 **3.533 亿美元**。

IPO 后：公司披露 2026Q2 通过 IPO raised **64 亿美元 gross proceeds**，2 月还完成 **10 亿美元 Series H pre-IPO financing**，4 月获得最高 **8.5 亿美元 revolving credit facility**。这给了公司很强的扩张资金，但也说明业务路线是重资本的。

### 会计质量提醒

CBRS 的 core 指标排除：

- stock-based compensation；
- customer warrants amortization；
- data center pass-through revenues and costs；
- certain other items。

这些调整不是不能看，但不能只看。尤其是客户权证和 pass-through 收入会让 headline growth 与股东经济回报之间产生差异。

## 5. Management and Capital Allocation

Andrew Feldman 等创始团队具备硬件系统创业背景。管理层目前最强的能力不是传统利润管理，而是：技术路线、顶级客户 BD、融资和快速扩张。

资本配置重点：

- 扩张 AI 推理容量和数据中心能力；
- 支持 OpenAI / AWS 等大客户部署；
- 投入 WSE / CS 系统、软件栈、云平台；
- 用 IPO、客户贷款、pre-IPO financing 和 credit facility 提前准备资本。

管理层目前评价：**技术叙事和融资执行强，上市公司长期治理与资本回报记录太短。** 未来 4-6 个季度需要重点观察管理层是否能把大合同转化为可持续毛利和可控现金消耗，而不是不断以融资和股权激励支持增长。

## 6. Valuation Work

### 当前估值快照

数据口径：Nasdaq 2026-07-07 报价；StockAnalysis 2026-07-07/08 页面；公司 2026Q1 8-K Exhibit 99.1 和 10-Q。

- 收盘价：**176.61 美元**。
- 盘后最新：约 **175.60 美元**。
- 52 周区间：**160.81 - 386.34 美元**。
- 市值：约 **400.1 亿美元**。
- Shares outstanding：约 **2.2653 亿股**。
- TTM revenue：约 **6.039 亿美元**。
- TTM net income：约 **8,788 万美元**。
- 市值 / TTM revenue：约 **66.3x**。
- 市值 / FY2026 core revenue 指引中点 8.60 亿美元：约 **46.5x**。

估值方法选择：CBRS 不适合主要看 PE，因为 IPO 前后资本结构、优先股转换、客户权证、非 GAAP 调整和早期规模让 EPS 解释力很弱。更合适的是 **forward revenue / gross profit / long-term scenario valuation**。

### 情景估值：2028 视角

| 场景 | 核心假设 | 估值方法 | 隐含股价区间 | 相对 176.61 美元 |
|---|---|---|---:|---:|
| Bear | 2028 revenue 1.6-2.0B；OpenAI/AWS 部署慢；gross margin 35%左右；FCF 仍负；市场给 12-16x sales | EV/Sales + 粗略净现金 | **100-160 美元** | -43% 至 -9% |
| Base | 2028 revenue 3.0-3.8B；gross margin 40-43%；operating margin 转正至 5-12%；客户从 OpenAI/AWS 扩散 | 14-20x sales + 净现金 | **180-320 美元** | +2% 至 +81% |
| Bull | 2028 revenue 5-7B；gross margin 45-50%；operating margin 20%左右；成为高端推理重要平台 | 18-25x sales | **350-650 美元** | +98% 至 +268% |

解释：当前价格已经接近 base case 下沿，但并没有给出很厚的安全边际。因为 base/bull 要求非常多事情同时做对：OpenAI 部署兑现、AWS 分销有效、非 OpenAI 客户扩散、毛利率恢复、capex 利用率提升、客户权证/稀释可控。

### 实用价格区间

- **强安全边际区**：120-140 美元以下。此时更接近 bear/base 交界，对长期可选性更有吸引力。
- **观察/小仓位试错区**：140-180 美元。当前 176 美元附近属于这个区间上沿，适合“研究型、小仓位、愿意承受高波动”的配置逻辑。
- **合理但不便宜区**：180-260 美元。需要 Q2/Q3 财报继续确认才能支撑。
- **偏贵/不宜追高区**：260 美元以上。需要非常强的 bull case 证据，否则容易被估值压缩。

结合你的组合规则：如果这是高 beta AI 基础设施股，买入前仍应确保 **现金 + 低 beta / 普通核心股敞口至少 30%**，否则即使价格进入观察区，也不宜用大仓位加风险。

## 7. Catalysts and Monitoring Plan

未来 2-4 个季度最重要的观察点：

1. **Q2 2026 core revenue 是否达到约 1.94 亿美元**。
2. **Core gross margin 是否只是短期降到 36%-38%，还是持续承压**。
3. **FY2026 core operating margin -28% 至 -32% 是否有改善路径**。
4. **OpenAI 750MW 部署节奏**：收入确认、capacity buildout、service credits、working capital loan 余额变化。
5. **AWS partnership 是否带来真实企业客户，而不是单纯公告效应**。
6. **非 OpenAI 客户扩散**：如果收入过度依赖少数客户，估值应打折。
7. **Capex 和 FCF**：收入增长是否持续伴随巨额资本消耗。
8. **客户权证和稀释**：权证摊销、SBC、IPO 后股本变化。
9. **锁定期/内部人交易/二次发行风险**：IPO 后早期股票供给可能增加波动。

## 8. Risk Register

- **估值风险：高概率 / 高严重度**。即使股价回落，46x FY2026 revenue 仍然要求长期高速增长。
- **客户集中风险：高概率 / 高严重度**。OpenAI、AWS、G42/MBZUAI 等少数客户决定商业节奏。
- **资本密集风险：高概率 / 中高严重度**。数据中心、电力、租赁、设备和网络投入可能吞噬现金流。
- **毛利率风险：中高概率 / 高严重度**。Q2 gross margin 指引低于 Q1，说明 mix 和扩张成本会带来波动。
- **竞争风险：高概率 / 高严重度**。Nvidia 生态、云厂商自研 ASIC、AMD/Groq/TPU 都可能压缩 Cerebras 的窗口期。
- **会计与稀释风险：中高概率 / 中高严重度**。customer warrants、SBC、pass-through revenue/costs 会让普通股东回报更复杂。
- **技术路线风险：中概率 / 高严重度**。Wafer-scale 架构若无法在更多模型和客户场景中证明 TCO/性能优势，估值支撑会减弱。

最强反证：如果未来几个季度收入增长主要来自少数合同，gross margin 下行，FCF 持续大幅为负，同时非 OpenAI/AWS 客户没有明显扩散，则“平台化 AI 推理基础设施”的 thesis 会被削弱。

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B-/C+。公司刚 IPO，10-Q 和 8-K 已披露大量信息，但上市公司历史短，公开数据还不足以验证一个完整周期。
- **Main research blind spot**: 公共资料无法证明 OpenAI/AWS 合同最终会以怎样的毛利率、现金回收和客户权证稀释转化为普通股东价值。
- **Strongest reason smart investors may disagree**: 乐观者会认为这是一家稀缺 AI 推理平台，当前下跌后是早期 Nvidia 替代链条的买点；谨慎者会认为这只是高估值、客户集中、重资本 AI 基建股。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这是不是一个 10 年后仍可理解、可预测、高 ROIC 的生意？
- **Evidence supporting**: 产品差异化清楚；OpenAI/AWS 背书强；2026Q1 收入同比 +94%；cloud/services 增速更快。
- **Evidence against**: 业务仍重资本；2026 年 operating margin 指引仍深度为负；客户权证和贷款结构复杂；长期 ROIC 未被证明。
- **Decision implication**: 适合继续研究，不适合用“稳定复利股”框架重仓。
- **Follow-up question**: 如果股市关闭五年，OpenAI/AWS 之外的客户扩散、毛利率和 FCF 能否让人安心持有？

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个故事最可能在哪里骗到投资者？
- **Failure paths**:
  - OpenAI/AWS headline 很大，但实际收入节奏慢、毛利低。
  - 数据中心扩张过快，利用率不足，FCF 长期为负。
  - Nvidia 和云厂商自研 ASIC 继续压制替代方案。
  - 投资者把“技术很快”误当成“股东回报一定好”。
- **Decision implication**: 最大错误不是错过，而是在商业模式验证前把它当成确定性赢家。
- **Follow-up question**: 三年后如果投资失败，今天最明显的红旗是否就是客户集中 + 重资本 + 高估值？

### Duan Yongping-style lens

- **Conclusion**: Needs further observation。
- **Business essence**: Cerebras 帮大模型和企业客户更快、更大规模地运行 AI 推理。
- **User value**: 对需要低延迟和高吞吐的 AI 应用，速度就是产品体验和成本结构的一部分。
- **Evidence for**: OpenAI/AWS 这种客户愿意合作，说明产品至少解决了真实痛点。
- **Evidence against**: 客户选择很多，且大客户议价能力强；产品价值不等于股东价值。
- **Decision implication**: 需要看客户是否持续复购、扩容，并愿意在较好毛利下付费。
- **Follow-up question**: 公司是在创造持久客户价值，还是主要利用当前 AI 算力短缺和资本周期窗口？

### Li Lu-style lens

- **Conclusion**: Needs further observation / watchlist。
- **Circle of competence**: 可以理解 AI 推理需求增长和客户合同，但难以从公开资料完全判断 wafer-scale 相对 GPU/ASIC 的长期 TCO 优势。
- **Industry trend**: 长期 AI 推理需求增长是真实大趋势；Cerebras 位于算力基础设施关键节点。
- **Downside protection**: 现金和融资能力较强，但估值仍高，且 downside 主要由估值压缩决定，不是资产价值保护。
- **Decision implication**: 值得持续研究；高置信度配置需要更多季度数据。
- **Follow-up question**: 10-20 年后，Cerebras 会是 AI 基础设施中的持久节点，还是资本开支周期中的临时赢家？

### Composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 7/10 |
| Financial quality | 4/10 |
| Valuation attractiveness | 5/10 |
| Long-term certainty | 4/10 |
| Downside risk control | 4/10 |

评分解释：业务和管理层有亮点，但财务质量、确定性和下行保护仍不足；估值从极贵降到“可观察”，还没到明显便宜。

## 10. Final Research Framework

### 当前研究观点

CBRS 是值得认真研究的 AI 基础设施标的，但它目前仍是 **高波动、高不确定性、强叙事 + 早期商业验证**的股票。175-180 美元附近比 6 月高位更合理，但依然不是传统意义上的安全边际价格。

### 适合买入吗？

- **无仓位**：可以纳入 watchlist；若要参与，更像小仓位试错，而不是核心仓位。
- **已有仓位**：重点看仓位是否过大、是否破坏组合中“现金 + 低 beta 核心资产至少 30%”的规则。
- **加仓信号**：Q2/Q3 收入超指引，gross margin 回到 40%+，OpenAI/AWS 外客户扩散，FCF 消耗低于预期。
- **减仓/降级信号**：gross margin 持续低于 35%，FY2026 指引下修，OpenAI/AWS 部署延迟，capex/loan/权证压力扩大。

### What would change my view

上调观点需要看到：

1. 连续 2-3 个季度收入高于指引；
2. cloud/services 增长不是靠低毛利 pass-through；
3. core gross margin 稳定 40%+；
4. OpenAI/AWS 之外客户明显增加；
5. capex 与 FCF 消耗可控；
6. 权证/SBC 稀释没有继续放大。

下调观点的条件：

1. FY2026 指引下修；
2. gross margin 长期低于 35%；
3. OpenAI/AWS 部署节奏慢于预期；
4. 数据中心扩张导致现金流恶化；
5. 客户权证、贷款或二次融资显著稀释普通股东；
6. Nvidia/云厂商自研方案明显削弱 Cerebras 的性能或成本优势。

## Sources

- SEC: Cerebras Systems Inc. Form 10-Q for quarter ended 2026-03-31, filed 2026-06-24, CIK 0002021728.
- SEC: Form 8-K filed 2026-06-23, Exhibit 99.1 “Cerebras Systems Announces Strong First Quarter 2026 Results”.
- Nasdaq quote API: CBRS quote as of 2026-07-07 close / after-hours.
- StockAnalysis: CBRS stock overview and key statistics, accessed 2026-07-07 UTC.
- Existing local report: `/home/ubuntu/stock-reports/research/COMPANIES/CBRS/deep-research/2026-06-24-deep-research.md`.
