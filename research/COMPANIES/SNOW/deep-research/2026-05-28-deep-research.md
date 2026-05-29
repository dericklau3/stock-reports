# Snowflake（SNOW）深度研究 - 2026-05-28

- **Research view**: 建设性但需观察
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: SNOW 的 FY2027 Q1 明显超预期，product revenue 13.34 亿美元、同比 +34%，NRR 回升到 126%，RPO 92.1 亿美元、同比 +38%，FY2027 product revenue 指引上调至 58.4 亿美元。AI Data Cloud 叙事从“故事”开始转成消费增长和大客户扩张，但公司仍是 GAAP 亏损、高 SBC、高销售倍数的软件股，盘后大涨后估值容错率下降。
- **Key risk**: 最大风险是估值与盈利质量错配。SNOW 的核心消费增长在恢复，但 FY2027 指引仍只有 13.5% non-GAAP operating margin 和 23% adjusted FCF margin；GAAP operating loss 仍大，SBC/稀释仍高。如果 AI 产品 adoption 不能持续转化为 durable consumption，或客户 consumption optimization 重现，股价会对高 EV/Sales 倍数非常敏感。

## 1. Executive View

**研究观点：建设性但需观察。** Snowflake 刚发布的 FY2027 Q1 是一个明显正面拐点：product revenue 增速从 FY2026 的高 20%/低 30% 区间继续抬升至 34%，NRR 从此前 124%-125% 附近升至 126%，大客户净新增强，AI 使用账户数快速提升，并且公司上调全年 product revenue、operating margin 和 adjusted FCF margin 指引。

但盘后股价大涨约 29%-34% 后，研究结论需要克制。以 2026-05-22 常规收盘价约 172.20 美元计，StockAnalysis 显示市值约 571.6 亿美元、forward PE 93x；按盘后约 29%-34% 涨幅粗略折算，隐含股价约 222-231 美元，市场价值会显著上移。也就是说，财报降低了基本面疑虑，但提高了估值门槛。

核心判断：

- **Q1 FY2027 强劲。** Revenue 13.9095 亿美元，同比增长 33%；product revenue 13.34 亿美元，同比增长 34%；GAAP gross profit 9.2645 亿美元；GAAP operating loss 3.2615 亿美元；net loss 2.9557 亿美元。来源：[Snowflake Q1 FY2027 results](https://www.businesswire.com/news/home/20260527027931/en/Snowflake-Reports-Financial-Results-for-the-First-Quarter-of-Fiscal-2027)。
- **客户和 backlog 质量改善。** Net revenue retention rate 126%；TTM product revenue >100 万美元客户 779 家，同比增长 29%，Q1 净新增 46 家；Forbes Global 2000 customers 813 家；RPO 92.1 亿美元，同比增长 38%。
- **AI adoption 开始可见。** 超过 13,600 个账户使用 Snowflake AI capabilities；Snowflake Intelligence 账户数环比翻倍以上；Cortex Code 已在超过 7,100 个账户使用。
- **FY2027 指引上调。** FY2027 product revenue 指引从 56.6 亿美元上调到 58.4 亿美元，同比增长 31%；non-GAAP product gross margin 75%；non-GAAP operating margin 13.5%；adjusted FCF margin 23%。
- **估值仍是核心争议。** 常规收盘价口径下市值约 571.6 亿美元；若按盘后反应，fully diluted market value 会明显超过 800 亿美元。对一家仍 GAAP 亏损、FY2027 product revenue 指引 58.4 亿美元的公司，估值要求未来多年 25%-30% 增长和 margin expansion 持续兑现。

最强反方理由：Snowflake 的消费模型有天然波动，客户可以优化消费；Databricks、BigQuery、Redshift、Microsoft Fabric、open table formats 和 hyperscaler 原生平台都在竞争。如果 AI 产品只是提高试用和短期消费，而不能形成长期净留存和平台锁定，当前重估会过快。

## 2. Business Model and Industry Structure

Snowflake 是云原生数据平台，核心商业模式是 consumption-based product revenue：客户按计算、存储、数据服务和相关能力使用量付费，而不是纯固定席位订阅。这种模式上行弹性强，但短期可预测性低于传统 SaaS。

主要产品和能力：

- **Data Cloud / Warehouse / Lakehouse**：跨云数据存储、计算、治理、共享。
- **Snowpark / developer platform**：让开发者在 Snowflake 内构建数据应用和 pipelines。
- **Cortex AI / Cortex Code / Snowflake Intelligence**：企业数据上下文上的 AI/agentic workflow。
- **Marketplace and data sharing**：数据/应用生态。
- **Industry data clouds**：金融、医疗、零售、广告、公共部门等。
- **Partnerships**：AWS、OpenAI、SAP、NVIDIA 等。

行业结构：

| 领域 | 主要竞争 | SNOW 优势 | 主要风险 |
|---|---|---|---|
| Cloud data warehouse / lakehouse | Databricks、Google BigQuery、Amazon Redshift、Azure Synapse/Fabric | 多云、中立性、治理、易用、企业客户基础 | Databricks AI/lakehouse momentum，hyperscaler bundling |
| AI data platform | Databricks、Palantir、Microsoft Fabric、Google Cloud、AWS Bedrock ecosystem | 企业数据上下文、Cortex/Snowflake Intelligence、governance | AI 应用层竞争激烈，产品差异需证明 |
| Data apps / marketplace | Databricks Marketplace、cloud marketplaces、vertical apps | Native apps, data sharing network effects | Marketplace monetization still early |
| Open formats | Iceberg ecosystem、Delta Lake、open lakehouse | Polaris/Iceberg support reduces lock-in concerns | Openness may reduce switching cost and pricing power |

SNOW 的护城河不是单一数据库性能，而是企业数据集中、治理、跨云中立性、客户工作流和生态。AI 时代的关键是：AI agents 需要 trusted enterprise data and context，这正是 Snowflake 想占据的位置。

## 3. Segment and Product Analysis

### Key Metrics

| 指标 | Q1 FY2027 | YoY / 说明 |
|---|---:|---:|
| Total revenue | 13.91 亿美元 | +33% |
| Product revenue | 13.34 亿美元 | +34% |
| Net revenue retention | 126% | 消费扩张改善 |
| RPO | 92.1 亿美元 | +38% |
| Customers >$1M TTM product revenue | 779 | +29%，Q1 净新增 46 |
| Forbes Global 2000 customers | 813 | 企业渗透继续提升 |
| AI capability accounts | 13,600+ | AI 使用面扩大 |
| Cortex Code accounts | 7,100+ | 新 AI 产品使用快速扩张 |

这个季度最重要的不是单一 revenue beat，而是几个指标同时改善：product revenue sequential dollar growth 创历史纪录、NRR 回升、大客户净新增强、RPO 仍高增长、FY 指引上调。

### AI Products

Snowflake 把战略重点放在 “AI Data Cloud”：

- **Snowflake Intelligence**：企业数据上下文上的 agentic / natural language interface。
- **Cortex Code**：面向代码和开发者工作流，已在超过 7,100 个账户中使用。
- **Natoma acquisition**：企业 Model Context Protocol platform，目标是让 AI agents 安全连接到企业工具和 workflows。
- **OpenAI partnership**：推进高级 AI 能力、co-innovation 和 go-to-market。
- **AWS $6B agreement**：多年 AWS 合作，支持企业 AI adoption 和 cloud consumption。

这些产品短期贡献收入可能不大，但它们解释了为什么 core product revenue 可能加速：AI workloads 需要数据治理、数据准备、上下文管理、权限和审计。

### Core Data Platform

Snowflake 的核心平台仍是收入主体。AI 产品如果成功，不是替代核心平台，而是增加 usage intensity：

- 更多数据进入 Snowflake。
- 更多 compute 在 Snowflake 内运行。
- 更多应用和 agent 依赖 Snowflake governed data。
- 客户从 data warehouse 扩展到 data engineering、data sharing、apps、ML/AI。

风险是消费模型的反身性：客户预算紧张时会优化查询、压缩 compute、缩短合同期限，导致 revenue growth 和 NRR 快速波动。

## 4. Financial Deep Dive

### Multi-Year and Current Trend

| 指标 | FY2024 | FY2025 | FY2026 | Q1 FY2027 |
|---|---:|---:|---:|---:|
| Revenue | 28.07 亿美元 | 36.26 亿美元 | 46.84 亿美元 | 13.91 亿美元 |
| Revenue growth | +35.9% | +29.2% | +29.2% | +33% YoY |
| Product revenue | N/A | N/A | 约 44.6 亿美元 implied | 13.34 亿美元 |
| GAAP operating income/loss | 亏损 | 亏损 | 亏损 | -3.26 亿美元 |
| RPO | N/A | N/A | 约 97.7 亿美元 Q4 | 92.1 亿美元 |

FY2027 Q1 显示 growth reacceleration，这对 Snowflake 非常重要。市场此前担心公司从 30%+ 高增长永久滑向 20% 区间；本季度把这条担忧线往后推了。

### Q1 FY2027 P&L

Q1 FY2027：

- Revenue：13.9095 亿美元。
- Cost of revenue：4.6450 亿美元。
- Gross profit：9.2645 亿美元。
- GAAP gross margin：66.6%。
- Sales and marketing：5.8895 亿美元。
- R&D：5.3494 亿美元。
- G&A：1.2872 亿美元。
- Operating loss：3.2615 亿美元。
- Net loss：2.9557 亿美元。
- Basic/diluted net loss per share：-0.86 美元。

GAAP gross margin 和 GAAP operating loss 说明 Snowflake 仍然不是成熟盈利软件公司。Non-GAAP 指标改善，但需要持续扣除 SBC 和相关税费影响。

### Free Cash Flow, Balance Sheet, Dilution

公司 FY2027 指引 adjusted FCF margin 为 23%。这是正面，但要注意：

- adjusted FCF 会调整 equity award payroll tax timing。
- GAAP net loss 仍大。
- SBC 和 share count 是长期每股价值稀释因素。
- Non-GAAP diluted share count guidance 为 Q2 3.75 亿股、FY2027 3.76 亿股。

Q1 末 cash and cash equivalents 为 20.85 亿美元，低于 FY2026 年末 28.28 亿美元；公司还有短期和长期投资，资产负债表总体强，不是现金 runway 风险公司。

## 5. Management and Capital Allocation

Sridhar Ramaswamy 上任后，Snowflake 的产品节奏和 AI narrative 明显加强。Q1 的强表现提高了管理层可信度：AI 不再只是 rebrand，而是体现在 product revenue、NRR、大客户和 usage metrics 上。

资本配置重点：

- **AI product velocity**：Cortex Code、Snowflake Intelligence、Natoma、OpenAI/SAP/AWS partnership。
- **Sales capacity**：CRO 更替后大客户扩张和 enterprise go-to-market 是关键。
- **Cloud commitments**：AWS $6B 多年协议既是需求信号，也是未来成本/commitment 管理变量。
- **Buybacks / dilution management**：公司历史上用回购抵消 SBC，但长期稀释仍需监控。

管理层需要证明的是：AI 产品不仅带来使用账户数增长，还能转化为 durable product revenue and net retention。

## 6. Valuation Work

### Valuation Method Selection

SNOW 是高增长、仍 GAAP 亏损、FCF 为正但 SBC 高的软件平台，适合：

- EV/Sales / EV/Product revenue：核心估值方法。
- EV/Gross profit：调整不同 gross margin 的平台比较。
- FCF yield：辅助，但要谨慎看 adjusted FCF。
- Scenario valuation：高增长软件的价值高度依赖 growth duration 和 terminal margin。
- 不适合用 GAAP P/E，因为当前 GAAP 亏损。

当前价格口径有不确定性：

- 最近可验证常规市场价格：2026-05-22 close 约 172.20 美元，StockAnalysis market cap 约 571.6 亿美元。
- FY2027 Q1 发布后，多家媒体报道盘后上涨约 29%-34%，粗略隐含股价约 222-231 美元；这不是正式次日收盘价，估值需在 2026-05-28 美股开盘后重新确认。
- Non-GAAP FY2027 diluted share guidance：约 3.76 亿股；若用盘后约 222-231 美元，fully diluted equity value 粗略约 835-869 亿美元。

基于 Q1 指引：

- FY2027 product revenue guidance：58.4 亿美元。
- Q2 FY2027 product revenue guidance：14.15-14.20 亿美元。
- FY2027 non-GAAP product gross margin：75%。
- FY2027 non-GAAP operating margin：13.5%。
- FY2027 adjusted FCF margin：23%。

按盘后隐含 fully diluted equity value，SNOW 大约在 14x-15x FY2027 product revenue 附近；按常规收盘市值，大约 10x 左右。盘后重估后，股票明显从“便宜的高增长软件恢复”进入“高预期 AI data platform”区间。

### Scenario Valuation

以下是研究情景，不是投资建议或确定性目标价。

| 情景 | FY2028 revenue / margin 假设 | 合理倍数 | 隐含股权价值 | 近似每股价值 | 触发条件 |
|---|---:|---:|---:|---:|---|
| Bear | Product revenue 65-70 亿美元，growth 降至 low-20s，FCF margin 18%-20% | 7-9x sales | 455-630 亿美元 | 约 120-170 美元 | AI 使用不转 revenue，NRR 回落，Databricks/Fabric 压力加大 |
| Base | Product revenue 80-90 亿美元，growth mid/high-20s，FCF margin 23%-26% | 10-13x sales | 800-1170 亿美元 | 约 210-310 美元 | Q1 重新加速持续，AI products 增加 consumption，RPO 高增长 |
| Bull | Product revenue 100-115 亿美元，growth 30%+，FCF margin 28%+ | 14-18x sales | 1400-2070 亿美元 | 约 370-550 美元 | SNOW 成为 Agentic Enterprise data control plane，AI workloads 大规模放量 |

盘后隐含价格约在 base case 下半区。风险回报改善来自 Q1 基本面加速，但被盘后大涨部分抵消。

## 7. Catalysts and Monitoring Plan

近期催化：

- 2026-05-28 正式开盘后的价格确认和成交量。
- Q2 FY2027 product revenue 是否达到 14.15-14.20 亿美元指引。
- Q2/FY2027 是否继续上调 full-year product revenue。
- NRR 是否维持或高于 126%。
- Customers >$1M TTM product revenue 净新增是否持续强。
- AI capability accounts、Snowflake Intelligence、Cortex Code 使用是否转化为 revenue。
- AWS $6B agreement 和 OpenAI/SAP/Natoma 进展。
- SBC、share count、buyback cadence。

重点监控指标：

- Product revenue growth and sequential dollar growth。
- Net revenue retention。
- RPO and current RPO。
- Large customers >$1M TTM product revenue。
- Forbes Global 2000 penetration。
- Non-GAAP product gross margin。
- GAAP operating loss and SBC。
- Adjusted FCF margin and unadjusted FCF。
- Consumption optimization signals。
- Competitive wins/losses against Databricks, BigQuery, Fabric, Redshift。

## 8. Risk Register

| 风险 | 概率 | 影响 | 为什么重要 |
|---|---|---|---|
| 估值压缩 | 中高 | 高 | 盘后大涨后 EV/Sales 重新抬高，容错率下降。 |
| GAAP 亏损和 SBC | 高 | 中高 | Non-GAAP 利润改善，但 GAAP operating loss 仍大。 |
| Consumption volatility | 中 | 高 | 客户可优化消费，增长不如订阅 SaaS 稳定。 |
| 竞争 | 高 | 高 | Databricks、BigQuery、Redshift、Fabric 都在争夺 AI/data workloads。 |
| AI adoption 不能 monetization | 中 | 高 | 使用账户数增长必须转成 durable product revenue。 |
| Cloud cost / AWS commitment | 中 | 中高 | $6B AWS agreement 有利于规模，但也增加 commitment management。 |
| 大客户集中 | 中 | 中 | 大客户贡献增长，也会放大单客户预算波动。 |
| 安全和数据治理事件 | 中 | 高 | 客户数据平台信任一旦受损，影响很大。 |
| 管理层/销售执行 | 中 | 中 | CRO 变动后大客户 sales motion 仍需验证。 |

## 9. Final Research Framework

SNOW 当前是 **建设性但需观察**。Q1 FY2027 让公司重新具备高质量 growth software 的味道：product revenue 加速、NRR 上升、RPO 强、大客户强、AI 使用指标强、全年指引上调。这是很扎实的正面变化。

但盘后股价大涨后，估值已经把很多好消息买进去。现在不再是“财报前被低估的 SNOW”，而是“需要连续兑现的 AI Data Cloud leader”。我会等待正式开盘价格和 Q2 后续验证来决定是否上调至 Positive。

我会把观点上调至 **Positive** 的条件：

- Q2/Q3 product revenue 继续 beat-and-raise。
- NRR 维持 126%+ 或继续改善。
- AI capability accounts 和 Snowflake Intelligence/Cortex Code usage 转成可见 consumption。
- GAAP operating loss 收窄，SBC/稀释下降。
- Adjusted FCF margin 23%+ 兑现，且不是靠一次性 working capital。
- 股价没有明显跑赢 revenue/FCF revisions。

我会下调观点的条件：

- 盘后重估后估值过高，而 Q2 指引没有继续上修。
- NRR 回落或 consumption optimization 重现。
- AI 产品使用增长但不贡献 revenue。
- Databricks/Fabric/BigQuery 竞争导致 pricing 或 gross margin 压力。
- GAAP loss/SBC/稀释继续恶化，抵消 non-GAAP 改善。

## Sources

- Snowflake, [Q1 FY2027 earnings release](https://www.businesswire.com/news/home/20260527027931/en/Snowflake-Reports-Financial-Results-for-the-First-Quarter-of-Fiscal-2027), 2026-05-27.
- Snowflake, [Q1 FY2027 earnings announcement page](https://www.snowflake.com/en/news/press-releases/snowflake-to-announce-q1-fy27-financial-results-may-27-2026/), 2026-05-04.
- Snowflake, [FY2026 Q4 investor presentation](https://s26.q4cdn.com/463892824/files/doc_financials/2026/q4/Q4-FY2026-Investor-Presentation_vF.pdf), 2026.
- Fintel / SEC mirror, [Snowflake FY2026 Form 10-K](https://fintel.io/doc/sec-snowflake-inc-1640147-10k-2026-march-20-20532-5168), filed 2026-03-20.
- StockAnalysis, [SNOW overview and market data](https://stockanalysis.com/stocks/snow/), accessed 2026-05-28.
- StockAnalysis, [SNOW market cap](https://stockanalysis.com/stocks/snow/market-cap/), accessed 2026-05-28.
- ChartMill, [Snowflake surges after Q1 FY2027 results](https://www.chartmill.com/news/SNOW/Chartmill-49118-Snowflake-NYSESNOW-Surges-After-Crushing-Q1-Estimates-and-Raising-Full-Year-Guidance-Amid-AI-Boom), 2026-05-27.
