# Coinbase Global（NASDAQ: COIN）深度研究报告

- **Research view**: Neutral / wait for Q2 confirmation（中性，等待 Q2 交易活跃度、USDC 与衍生品验证）
- **Confidence**: B-。Coinbase 披露充分、资产负债表强、美国合规平台地位清晰；但收入和利润仍高度依赖 crypto 价格、波动率、交易量、监管环境和 stablecoin 利率/分润结构，短期 Q2 财报临近，结论需要等待 2026-07-30 更新。
- **Time horizon**: 中期 3–12 个月；长期 3–5 年。
- **Main thesis**: Coinbase 正在从“高 beta 加密现货交易所”转型为“合规 onchain 金融基础设施 + Everything Exchange”；若 USDC、Base、Deribit/衍生品、机构托管和订阅服务持续放大，它会比纯交易手续费平台更有价值。但当前估值仍要求周期恢复和新产品兑现。
- **Key risk**: Q1 2026 已显示交易量、MTU、AOP 与净利润在弱市场中快速下滑；如果 Q2/Q3 crypto 波动率继续低迷，或监管/安全/竞争事件压缩费率与信任，COIN 可能继续被当作高 beta crypto 代理资产重估。

> 数据截止：2026-07-20。市场价格使用 StockAnalysis 2026-07-17 regular close **$157.12**。最新完整财务季度为 2026 Q1，来源为 Coinbase 2026-05-07 Form 10-Q 与 Q1 2026 earnings presentation；2025 全年业务描述来自 2026-02-12 Form 10-K；近期事件来自 2026-05-05、2026-06-18、2026-07-09 8-K。加密市场背景使用 Coinbase/CoinGecko API：BTC 约 **$63.9K**、ETH 约 **$1.85K**、USDC market cap 约 **$73.2B**。

## 1. Executive View

### 核心判断

COIN 不是简单的“买 BTC 的替代品”，也不是稳定利润的传统交易所。它是一个带有强周期性的 crypto 金融基础设施平台：

1. **周期性交易业务仍是利润弹性核心**：2026 Q1 transaction revenue 为 **$755.8M**，同比 -40%，环比 -23%；Trading Volume 为 **$202B**，同比 -50%。当 crypto 交易量和波动率下降，收入和 GAAP 利润会快速下滑。
2. **订阅服务正在形成缓冲层**：Q1 subscription and services revenue 为 **$583.5M**，占 net revenue **44%**；stablecoin revenue **$305.4M**、blockchain rewards **$100.8M**、interest and finance fee income **$67.8M**。这说明 Coinbase 已不只是收交易手续费。
3. **战略方向更大，但执行复杂度更高**：2025 年 Coinbase 推出/强化 Everything Exchange，覆盖 crypto、股票、商品期货、perpetual futures、prediction markets；2025-08 收购 Deribit 进入全球 crypto options/derivatives 核心市场；Base 和开发者平台给它 onchain 应用入口。但这些扩张都带来监管、技术、M&A 和成本控制挑战。

### 研究观点

当前我给 COIN 的观点是：

> **中性 / 等待 Q2 确认。**

原因不是公司差，而是当前价格仍需要 Q2/Q3 证明：交易收入没有继续恶化、USDC 和 S&S 能稳定、Deribit/derivatives/Prediction Markets 能贡献增量、AI-native 重组能降低费用而不伤害执行。

### 最强反方理由

如果未来 Coinbase 成为美国和全球合规 crypto/onchain 金融入口，USDC、Base、custody、derivatives、institutional prime brokerage 与 retail app 形成网络效应，今天约 $41B 市值可能低估了长期平台价值。

### 最强正方的反驳

这个长期故事目前仍建立在多条不稳定假设上：crypto 资产价格、交易波动率、稳定币利率、监管政策、产品监管分类、费率竞争和安全事件都可能单独改变盈利模型。

## 2. Business Model and Industry Structure

### 小白解释：Coinbase 到底怎么赚钱

你可以把 Coinbase 理解为“加密世界里的证券交易所 + 券商 + 银行托管 + 钱包 + 开发者基础设施”的组合，但它比传统券商更波动。

- **谁付钱**：散户交易者、机构交易者、资产管理公司、稳定币用户、质押用户、开发者、借贷/融资客户、衍生品交易者。
- **卖什么**：交易入口、托管资产、USDC/稳定币服务、staking、借贷和融资、机构 prime brokerage、开发者工具、Base 链生态、衍生品/预测市场。
- **怎么赚钱**：最传统的是交易费；越来越重要的是 USDC/stablecoin 分成、staking fee、custody fee、interest/finance fee、Coinbase One 订阅、Base/DEX/derivatives/prediction markets 等新产品收入。
- **最大成本**：技术研发、合规/法务、客服/安全、营销、交易处理、USDC rewards、SBC、并购整合和监管成本。
- **利润核心问题**：当 crypto 牛市和波动率高时，交易手续费极高；当熊市或低波动时，交易费会收缩，所以 Coinbase 必须靠 S&S 和费用纪律熬过周期。

### 重要术语

- **MTU（Monthly Transacting Users）**：过去 28 天至少有一次交易或产生收入活动的月活交易用户。Coinbase 警告 MTU 可能高估 unique users，因为用户行为和产品架构不同。
- **AOP（Assets on Platform）**：客户托管在 Coinbase 平台上的 crypto 和 payment stablecoin 美元价值，不包括客户自己持有 key 的资产。
- **USDC / stablecoin revenue**：Coinbase 与 Circle/USDC 生态相关的收入，通常与 USDC 流通量、Coinbase 产品内 USDC 平均余额、利率和分润结构有关。
- **Base**：Coinbase 孵化的 Layer 2 区块链，目标是让交易更便宜、更快，并让开发者在上面构建应用。
- **Derivatives / perpetual futures / options**：crypto 衍生品，如永续合约、期货、期权，通常交易量大、机构参与度高，但监管复杂。
- **Adjusted EBITDA**：非 GAAP 利润指标，剔除税、利息、D&A、SBC、部分 crypto 投资损益和特殊项目；对 Coinbase 有参考价值，但不能替代 GAAP 或 FCF。

### 行业结构

Coinbase 处于多个市场交汇处：

1. **交易所 / 券商**：与 Binance、Kraken、Robinhood、Interactive Brokers、传统券商和去中心化交易所竞争。
2. **托管与机构基础设施**：与银行、托管机构、ETF 服务商、prime brokers 竞争。
3. **稳定币平台**：与 Circle/USDC 生态强绑定，也受 Tether、PayPal PYUSD、银行存款代币、监管稳定币竞争影响。
4. **开发者与链生态**：Base 面临 Ethereum L2、Solana、Arbitrum、Optimism、Polygon 等竞争。
5. **金融超级入口**：Everything Exchange 意味着 Coinbase 想从 crypto app 变成更广义的金融交易 app；这是上限来源，也是使命扩张风险来源。

## 3. Segment and Product Analysis

Coinbase 不按传统分部披露利润，更适合按收入类型和客户群拆解。

### 3.1 Transaction revenue：周期弹性最大

Q1 2026 交易收入：

| 项目 | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| Consumer transaction revenue | **$566.9M** | $1.096B | -48% |
| Institutional transaction revenue | **$135.7M** | $98.9M | +37% |
| Other transaction revenue | **$53.2M** | $67.8M | -22% |
| Total transaction revenue | **$755.8M** | $1.262B | -40% |

专业判断：

- Consumer 仍是交易收入大头，但对 spot trading volume、散户风险偏好和长尾币波动高度敏感。
- Institutional transaction revenue 同比增长，说明机构化趋势在弱市场中仍有支撑。
- Deribit 加入后，COIN 的衍生品收入上限提高，但也带来整合、监管和商誉风险。

### 3.2 Subscription and services：抗周期缓冲层

Q1 2026 S&S：

| 项目 | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| Stablecoin revenue | **$305.4M** | $274.0M | +11% |
| Blockchain rewards | **$100.8M** | $196.6M | -49% |
| Interest and finance fee income | **$67.8M** | $63.1M | +7% |
| Other S&S revenue | **$109.4M** | $140.9M | -22% |
| Total S&S revenue | **$583.5M** | $674.6M | -14% |

这块的好处：比交易收入稳定。坏处：并非完全抗周期。

- Stablecoin revenue 受 USDC 规模、利率和 Coinbase 产品内余额影响。
- Blockchain rewards 受 staked units 和 crypto prices 影响，Q1 已明显下降。
- Interest/finance fee income 受贷款余额、利率和风险控制影响。
- Coinbase One 等订阅可提升 recurring revenue，但规模披露还不够透明。

### 3.3 AOP 与客户资产

2026-03-31 AOP：

| 资产 | 单位 | Value |
|---|---:|---:|
| Bitcoin | 3.0M BTC | **$202.3B** |
| Ethereum | 19.0M ETH | **$40.0B** |
| XRP | 9.175B XRP | **$12.3B** |
| USDC | N/A | **$9.3B** |
| Other | N/A | **$30.5B** |
| Total AOP | — | **$294.4B** |

AOP 同比从 $327.5B 降至 $294.4B，主要受资产价格下跌影响，部分被 BTC units 增长抵消。AOP 是 Coinbase 信任和规模的证据，但不是公司自有资产，不能把客户资产直接作为公司价值。

### 3.4 Everything Exchange 与新产品

2025 10-K 披露 Coinbase 已扩展到：

- stocks；
- commodity futures；
- perpetual futures；
- prediction markets；
- crypto spot；
- derivatives；
- Deribit options/perps/futures/spot。

Q1 presentation 披露：

- Retail derivatives annualized revenue 超过 **$200M**；
- Prediction Markets 以 March revenue annualized 口径超过 **$100M**；
- DEX Trading cumulative volume 到 Q1 已超过 **$450M**；
- 12 个产品达到 $100M+ annualized revenue。

这些是 COIN 的增长期权，但投资者不能把所有 annualized revenue 直接资本化：很多新产品处于早期，且受监管和交易量波动影响。

### 3.5 Deribit 收购

Coinbase 于 2025-08-14 收购 Sentillia B.V.（Deribit），一家 crypto derivatives exchange。

- 总对价：**$4.295B**。
- 现金：**$721.5M**。
- Coinbase Class A stock：**$3.573B**。
- Goodwill：**$2.819B**。
- Intangible assets：**$1.390B**，其中 customer relationships $1.059B、developed technology $288M、trade name $43M。

战略意义：

- 补足 crypto options/derivatives 产品；
- 强化机构与高频交易者生态；
- 让 Coinbase 不只依赖美国 retail spot；
- 提升 Everything Exchange 的可信度。

风险：

- $4.3B 对价不低，且主要用股票支付，稀释显著；
- goodwill 和 intangible assets 较大，若 derivatives volume 或利润率不达预期，存在减值风险；
- 衍生品监管比 spot 更复杂。

## 4. Financial Deep Dive

### 4.1 多年财务趋势

StockAnalysis/Fiscal.ai 年度数据：

| 财年 | Revenue | Operating income | Net income | FCF | Operating margin |
|---|---:|---:|---:|---:|---:|
| 2021 | $7.839B | $3.077B | $3.624B | $4.038B | 39.2% |
| 2022 | $3.194B | -$2.710B | -$2.625B | -$1.585B | -84.9% |
| 2023 | $3.108B | -$161.7M | $94.9M | $673.4M | -5.2% |
| 2024 | $6.564B | $2.307B | $2.579B | $3.104B | 35.2% |
| 2025 | $7.181B | $1.435B | $1.260B | $2.426B | 20.0% |
| TTM / Mar 2026 | $6.560B | $708.2M | $800.6M | $2.792B | 10.8% |

结论：这是极强周期股。2021 和 2024 能产生很高利润；2022 能大亏；2026 TTM 利润率已明显回落。

### 4.2 Q1 2026 经营质量

Q1 2026：

| 指标 | Q1 2026 | Q1 2025 | YoY |
|---|---:|---:|---:|
| Total revenue | **$1.413B** | $2.034B | -31% |
| Net revenue | **$1.339B** | $1.937B | -31% |
| Transaction revenue | **$755.8M** | $1.262B | -40% |
| S&S revenue | **$583.5M** | $674.6M | -14% |
| Net income / loss | **-$394.1M** | $65.6M | nm |
| Adjusted EBITDA | **$303.3M** | $929.9M | -67% |
| MTUs | **8.2M** | 9.7M | -15% |
| AOP | **$294B** | $328B | -10% |
| Trading Volume | **$202B** | $401B | -50% |

Q1 并不漂亮：低波动和风险偏好下降压制交易。好处是 Adjusted EBITDA 仍为正，且公司声称已连续第 13 个季度在各种市场条件下保持正 Adjusted EBITDA。

### 4.3 费用与 SBC

Q1 2026 主要费用：

| 项目 | Q1 2026 |
|---|---:|
| Transaction expense | $195.9M |
| Technology & development | $525.6M |
| Sales & marketing | $266.7M |
| General & administrative | $376.1M |
| Stock-based compensation | $248.1M |

SBC 仍是重要稀释来源。公司通过回购抵消部分稀释：Q1 presentation 称自 Q4 2024 以来回购 9.3M+ Class A shares、返还 $1.9B+ 给股东、剩余授权约 $2.1B。StockAnalysis 显示 shares outstanding 同比仍 +4.15%，说明回购改善但尚未完全消除长期稀释/并购发股影响。

### 4.4 资产负债表

2026-03-31：

| 指标 | 数值 |
|---|---:|
| Cash & equivalents | $10.205B |
| Short-term investments | $233M |
| Cash + ST investments | **$10.438B** |
| Total debt | **$7.776B** |
| Net cash | **$2.662B** |
| Shareholders' equity | $13.481B |
| Tangible book value | $7.907B |
| Current ratio | 2.14 |

Coinbase 的 balance sheet 是核心防线。弱市场中，现金和净现金可以支撑监管成本、并购整合、回购和产品投资。但需要注意：

- 客户资产不是公司资产；
- goodwill/intangibles 因 Deribit 和其他收购上升；
- debt 较 2024/2023 提高；
- high beta 股票在极端市场可能仍受融资/流动性折价影响。

### 4.5 法务、监管和安全

关键风险事件：

- 2025 Data Theft Incident：威胁者不当取得部分客户账户信息和内部文档，用于 social-engineering attempts；公司披露未泄露 passwords/private keys。2025 年公司支付 **$311.2M** 现金，主要包括自愿客户补偿和直接法律成本。
- 10-Q 披露仍存在监管调查/传票/需求函，涉及资产上架、资产分类、staking programs、stablecoin and yield-generating products 等。
- 2026-07-08，Chief Legal Officer Paul Grewal 通知将于 2026-07-31 离任；Molly Abraham 预计接任 General Counsel/Secretary。对 crypto 公司来说，法务负责人变动值得跟踪。

## 5. Management and Capital Allocation

### 管理层战略

Brian Armstrong 管理层长期愿景清晰：把 Coinbase 从 crypto exchange 扩展为 onchain economy 入口和 Everything Exchange。这个愿景与公司“increase economic freedom”的 mission 大体一致，不算明显使命漂移；但 Everything Exchange 进入股票、商品期货、预测市场等更广泛资产类别，已经从纯 crypto 入口扩大为多资产金融平台，需跟踪是否牺牲合规/安全/专注度。

### 资本配置评价

优点：

- 资产负债表强，弱周期仍有现金；
- 通过 Deribit 抢占 derivatives 核心市场；
- 回购用于抵消 SBC 和并购稀释；
- 费用在弱市场中能快速调整，2026-05 宣布裁员 14%。

缺点：

- Deribit $4.3B 对价较大，且股票支付带来稀释；
- SBC 高，长期需要证明每股价值增长而非总规模增长；
- 2026 重组说明此前成本结构仍较重；
- 加密安全和监管事件可能迅速消耗资本和管理层注意力。

### 管理承诺追踪

| 承诺 / 目标 | 当前状态 | 后续验证 |
|---|---|---|
| 在各种市场条件下保持 positive Adjusted EBITDA | Q1 为 $303M，连续第 13 个季度为正 | Q2 低波动环境能否继续 |
| S&S 增加抗周期性 | Q1 占 net revenue 44% | USDC/利率变化后能否稳定 |
| Everything Exchange | 2025 扩展股票、期货、prediction markets；Deribit 已并表 | 收入贡献和监管状态 |
| AI-native 提升效率 | 2026-05 裁员 14%，Q2 restructuring $50-$60M | Q3/Q4 费用率是否下降 |
| 管理稀释 | 已回购 9.3M+ Class A shares，剩余授权 $2.1B | shares outstanding 是否持续下降 |

## 6. Valuation Work

### 6.1 当前市场快照

StockAnalysis 2026-07-17：

| 指标 | 数值 |
|---|---:|
| Share price | **$157.12** |
| Market cap | **$41.39B** |
| Enterprise value | **$38.92B** |
| Shares outstanding | **263.46M** |
| TTM revenue | **$6.56B**（financials page；statistics page 显示 $6.29B，存在 vendor 口径差异） |
| TTM net income | **$800.6M** |
| TTM FCF | **$2.792B** |
| TTM P/E | **约 52x** |
| EV/TTM revenue | **约 5.9x** |
| P/FCF | **约 14.8x** |
| EV/FCF | **约 13.9x** |
| EV/LTM Adjusted EBITDA | **约 17.8x** |
| Beta | **3.35** |
| 52-week price change | **-60.5%** |
| Next earnings | **2026-07-30 after close** |

估值难点：

- 用 TTM FCF 看不贵；
- 用 GAAP earnings 看贵；
- 用 Q1 低谷年化 Adjusted EBITDA 看也不便宜；
- 真正决定估值的是未来 crypto 交易量、波动率、USDC 余额/利率、Deribit 贡献和费用纪律。

### 6.2 情景估值

方法：用 2027 年 revenue × EBITDA margin × EV/EBITDA multiple，再加 net cash，除以 276M diluted shares。由于 COIN 周期性强，这只是研究框架，不是目标价。

| 情景 | 2027 revenue | EBITDA margin | EV/EBITDA | Equity value | Implied price | vs. $157.12 |
|---|---:|---:|---:|---:|---:|---:|
| Bear | $5.2B | 10% | 14x | ~$9.9B | **~$36** | -77% |
| Base | $6.8B | 23% | 18x | ~$30.8B | **~$112** | -29% |
| Bull | $9.0B | 35% | 20x | ~$65.7B | **~$238** | +51% |

这张表的含义很重要：

- 如果 Q1 这种弱交易环境延续，当前 $157 并不便宜。
- 如果 crypto 市场回暖、Deribit 和 S&S 放量，$157 可以有显著 upside。
- COIN 的风险/收益不是线性的，它更像一个带平台期权的 crypto 周期资产。

### 6.3 实用价格分区

| 区间 | 含义 |
|---|---|
| **<$80** | 强安全边际 / crisis entry zone；市场按弱周期/监管折价定价 |
| **$80-$120** | 可研究 / 小仓观察区；base case 附近或以下 |
| **$120-$170** | 当前附近；需要 Q2/Q3 证明收入和费用没有继续恶化 |
| **$170-$240** | 高预期区；需要交易量恢复、S&S 稳定、Deribit 放量 |
| **>$240** | Bull case / 不宜追高；需要 crypto 牛市和平台重估共同兑现 |

## 7. Catalysts and Monitoring Plan

### 近期催化剂

1. **2026-07-30 Q2 2026 earnings after close**。
2. Q2 transaction revenue 是否明显高于 QTD $215M extrapolation。
3. Q2 S&S revenue 是否落在 **$565M-$645M** 指引。
4. Q2 T&D + G&A 是否下降至 **$820M-$870M**。
5. Restructuring expense 是否在 $50M-$60M，且 Q3 开始费用率改善。
6. Deribit 交易量、收入、客户关系和整合进展。
7. USDC market cap 与 Coinbase 产品内 USDC average balance。
8. BTC/ETH/长尾资产波动率是否恢复。
9. CLO 离任后的监管/诉讼沟通质量。

### 中期 thesis 里程碑

- S&S revenue 能在低交易量环境中稳定增长。
- derivatives/prediction markets/DEX/Base 从 annualized revenue 叙事转为可持续季度收入。
- AI-native 重组能降低费用而不降低安全/合规能力。
- 回购能真正降低 diluted shares。
- 监管环境改善，资产上架、staking、stablecoin、derivatives 规则更清晰。

## 8. Risk Register

| 风险 | 概率 | 影响 | 解释 |
|---|---|---|---|
| Crypto 交易量/波动率持续低迷 | 高 | 高 | Q1 Trading Volume 已同比 -50% |
| Stablecoin 利率/分润压缩 | 中 | 高 | Stablecoin revenue 是 S&S 核心 |
| 监管/诉讼/传票升级 | 中 | 高 | 涉及资产分类、staking、stablecoin、yield products |
| 安全事件/客户信任受损 | 中 | 高 | 2025 data theft 已产生 $311M cash cost |
| Deribit 整合或减值 | 中 | 中高 | $4.3B acquisition，goodwill $2.8B |
| 费用结构过重 | 中 | 中高 | Q1 GAAP operating loss，Q2 重组 |
| SBC/并购稀释 | 高 | 中 | shares outstanding 同比仍增长 |
| 竞争压费率 | 高 | 中高 | CEX、DEX、Robinhood、传统券商和全球交易所竞争 |
| Mission drift | 中 | 中 | Everything Exchange 可能强化 mission，也可能扩张过度 |

### Thesis invalidation signals

- 连续两个季度 Adjusted EBITDA 接近 break-even 或转负。
- S&S revenue 明显低于指引，且不是短期价格影响。
- Deribit 未能贡献收入或出现重大监管问题。
- 净现金快速下降且不是高回报投资/回购。
- 新增重大安全/客户资产/私钥事件。
- 监管导致 staking、USDC、derivatives 或主要资产交易显著受限。

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B。COIN 披露丰富，但 crypto 行业周期、监管和链上数据复杂，公开财务很难完全证明长期 moat。
- **Main research blind spot**: S&S 与 Everything Exchange 的长期正常化利润率，尤其在低利率/低波动环境下是否足以支撑平台估值。
- **Strongest reason smart investors may disagree**: 有人会把 COIN 视为下一代合规金融基础设施核心入口，因此愿意为长期期权支付更高价格；另一些人会认为它只是高 beta crypto broker，难以形成稳定护城河。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个生意 10 年后是否仍能产生可预测现金流，还是主要靠 crypto 周期？
- **Evidence supporting**: $294B AOP、强品牌/合规、净现金、S&S 44% net revenue、连续 13 季度 positive Adjusted EBITDA。
- **Evidence against**: Q1 net loss、Trading Volume -50%、交易收入 -40%、监管不确定、SBC 高、Deribit 大额 goodwill。
- **Decision implication**: 适合 watchlist，不适合按稳定 compounder 给高仓位。
- **Follow-up question**: 如果股市关闭五年，是否能放心只看 Coinbase 的用户资产、S&S、监管牌照和 FCF？目前答案是“还不能”。

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 哪些假设最可能让投资者被 crypto 叙事骗到？

| Failure path | Mechanism | Consequence |
|---|---|---|
| 把周期收入当 recurring | 牛市交易费不可持续 | 高位买入后利润塌陷 |
| 把 AOP 当公司资产 | 客户资产不是股东资产 | 估值错误 |
| 忽略监管 | staking/stablecoin/derivatives 分类变化 | 收入线受限 |
| 忽略稀释 | SBC + stock M&A | 每股价值增长弱 |
| 忽略安全风险 | 社工/数据泄露/第三方风险 | 信任和成本冲击 |

- **Fragile assumptions**: USDC revenue 维持、derivatives 放量、AI 重组不伤安全合规、retail spreads 不被压缩。
- **Psychological trap**: 用 BTC 价格上涨直接推导 COIN 盈利上涨，忽略波动率/交易量/费率/成本。
- **Major stupidity risk**: 在 crypto 情绪最热、COIN 高估值时把它当“必然长期复利股”。
- **Follow-up question**: 三年后如果错了，最明显的红旗可能是：S&S 并不抗周期，且新产品收入无法抵消交易费下滑。

### Duan Yongping-style lens

- **Conclusion**: Needs further observation。
- **Business essence**: Coinbase 为用户提供一个相对合规、简单、安全的 crypto/onchain 金融入口。
- **User value**: 对新用户是“放心买/卖/存 crypto”；对机构是合规托管、交易和 prime brokerage；对开发者是 Base 和开发者工具。
- **Evidence supporting**: 强品牌、合规、AOP、Base、USDC、Deribit、机构客户和多产品生态。
- **Evidence against**: 用户切换成本不高，高手可以去 DEX/低费率交易所；监管和安全事故会快速削弱信任。
- **Right price**: 更接近 $80-$120 才更符合“好公司也要好价格”；$157 需要 Q2/Q3 给确认。
- **Follow-up question**: Coinbase 是在创造持久客户价值，还是主要变现 crypto 周期和监管窗口？目前两者都有。

### Li Lu-style lens

- **Conclusion**: Needs further observation。
- **Circle of competence**: 财务、交易量、AOP、S&S 可跟踪；长期监管、Base 生态价值、onchain adoption 和衍生品份额需要持续研究。
- **Industry trend**: Crypto/onchain economy、stablecoin、tokenization 和 global settlement 是长期趋势；Coinbase 位于合规入口和基础设施节点。
- **Downside protection**: 净现金 $2.7B 和强 liquidity 是保护，但估值仍远高于 tangible book，不能只靠资产负债表保护下行。
- **Margin of safety**: 当前 $157 不够强；需要更低价格或更强 Q2/Q3 证据。
- **Research-depth decision**: 值得长期跟踪，但高确信配置需要更好价格或更稳定收入结构。
- **Follow-up question**: 10-20 年后，Coinbase 是重要金融基础设施节点，还是 crypto 资本周期里的阶段性赢家？这是核心长期问题。

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 7/10 |
| Financial quality | 6/10 |
| Valuation attractiveness | 5/10 |
| Long-term certainty | 5/10 |
| Downside risk control | 5/10 |

简要理由：

- Business model: 平台价值高，但周期性强。
- Moat: 合规和信任强，用户切换成本和费率压力限制 moat。
- Management: 战略清晰、动作快，但 M&A 和重组需要验证。
- Financial quality: 现金强、FCF 可观，但 GAAP 利润波动大、SBC 高。
- Valuation: 相对高点便宜很多，但 base case 下仍不便宜。
- Certainty: 监管和 crypto 周期降低长期可预测性。
- Downside control: 净现金保护有限，股价 beta 很高。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 有平台价值，但仍周期性强 | B |
| Moat | 合规/托管/品牌强，交易费 moat 一般 | B- |
| Management and capital allocation | 战略主动，Deribit 和重组需验证 | B- |
| Biggest risk | 交易量低迷 + 监管/安全事件 | B |
| Long-term trend | onchain/stablecoin/tokenization 有长期趋势 | B |
| Valuation and margin of safety | 当前不够便宜，需 Q2 确认 | B- |

### Action-framing table

| Investor state | Research implication |
|---|---|
| No position | 等 Q2；若跌入 $80-$120，研究价值更高 |
| Existing position | 重点看 Q2 revenue mix、Adjusted EBITDA、S&S、USDC、Deribit |
| Add / upgrade signal | Q2/Q3 证明弱市 positive EBITDA + S&S 稳定 + 稀释下降 |
| Reduce / downgrade signal | Adjusted EBITDA 走弱、S&S 低于指引、监管/安全事件升级 |

## 10. Final Research Framework

### 当前结论

COIN 值得跟踪，但当前更像：

> **带平台期权的高 beta crypto 基础设施股，而不是稳定复利股。**

我不会在 $157 附近给出高确信买入结论。更合理的框架是：等待 2026-07-30 Q2 财报确认弱市场下的真实盈利能力；如果价格回到 $80-$120，或 Q2/Q3 证明收入结构和费用杠杆明显改善，再上调观点。

### What would make thesis stronger

- Q2 transaction revenue 明显高于低波动 extrapolation。
- S&S revenue 高于 $605M midpoint，stablecoin revenue 稳定。
- Adjusted EBITDA 在弱市场仍保持高于 $250M-$300M。
- Q3 费用率显著改善，AI-native restructuring 兑现。
- Deribit 有清晰收入/volume/EBITDA 贡献。
- Diluted shares 稳定下降。
- 监管风险下降，尤其 staking、stablecoin、derivatives 规则更清楚。

### What would change my view lower

- Q2/Q3 Adjusted EBITDA 接近 breakeven 或转负。
- S&S revenue 下滑说明抗周期叙事失效。
- USDC 市值或 Coinbase product balances 明显下降。
- Deribit 整合不顺或 goodwill/intangibles 风险上升。
- 新数据泄露/安全事件或客户资产事件。
- CLO 离任后监管/诉讼沟通恶化。
- 管理层继续用股票做大额并购、share count 上升，削弱每股价值。

## Sources

- Coinbase 2026 Q1 Form 10-Q filed 2026-05-07, CIK 0001679788.
- Coinbase Q1 2026 earnings presentation filed as Form 8-K Exhibit 99.1 on 2026-05-07.
- Coinbase 2025 Form 10-K filed 2026-02-12.
- Coinbase 8-K filed 2026-05-05, restructuring plan.
- Coinbase 8-K filed 2026-07-09, Chief Legal Officer transition.
- StockAnalysis COIN quote/statistics/financials accessed 2026-07-20.
- Coinbase/CoinGecko public crypto price APIs accessed 2026-07-20.
