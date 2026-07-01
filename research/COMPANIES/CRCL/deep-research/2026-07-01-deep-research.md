# CRCL（Circle Internet Group）中文深度研究报告

- **Research view**: 中性 / 等待确认
- **Confidence**: 中等偏低。公司披露质量较好，但上市时间短，估值、监管、利率、竞争与代币经济模型仍有较大不确定性。
- **Time horizon**: 中期 6–18 个月；长期 3–5 年以上。
- **Main thesis**: Circle 是受监管稳定币基础设施的稀缺上市标的，USDC 规模、链上使用量和机构采用正在扩大；但利润高度依赖利率、USDC 余额、Coinbase/Binance 等分销成本，以及监管框架最终形态。当前更适合作为观察型标的，而不是高确定性复利股。
- **Key risk**: 如果利率下降、USDC 市占率受挤压、分销成本率居高不下，或 Arc / CPN / Agent Stack 不能把“储备利息型业务”转成高质量平台收入，估值可能继续承压。

> 数据日期：行情抓取于 2026-07-01 CST；最新财务资料主要来自 Circle 2026 Q1 Form 10-Q、2026 Q1 earnings release、2025 Form 10-K、SEC 公司 filings。本文为研究支持，不构成个性化投资建议。

## 1. Executive View

### 研究结论

CRCL 是一个值得研究的金融基础设施公司，但目前不适合用传统“确定性复利股”的框架直接买入。它更像是：

1. **稳定币行业的高质量“发行与分销平台”**：USDC 是全球主要美元稳定币之一，Circle 的监管合规形象优于许多 crypto-native 竞争者。
2. **短期利润高度依赖利率和 USDC 余额**：公司大部分收入来自 USDC / EURC 储备资产产生的利息或分红，利率下降会直接压缩收入。
3. **长期故事取决于平台化成功**：Arc、CPN、StableFX、Agent Stack、USYC 等产品如果能把 Circle 从“吃储备利差”变成“支付 / 结算 / 开发者基础设施平台”，估值逻辑才会改善。

### 最强反方理由

市场可能已经把“稳定币长期增长 + 监管利好 + Arc 平台化 + AI agent 支付”提前计入股价，但公司的可验证利润仍主要来自储备收益，且分销伙伴拿走了大量经济利益。若利率下行或分销成本变差，当前盈利质量可能低于表面数字。

## 2. Business Model and Industry Structure

### 小白版解释：Circle 到底怎么赚钱？

Circle 发行 USDC。USDC 是一种“美元稳定币”：用户交给 Circle 1 美元，Circle 发行 1 枚 USDC；用户赎回时，Circle 销毁 USDC 并返还 1 美元。为了保证 USDC 能 1:1 兑回美元，Circle 把收到的钱放在现金、短期国债和货币市场基金等储备资产里。

Circle 赚钱的核心方式很简单：

- 用户持有 USDC 通常拿不到储备利息；
- Circle 用储备资产赚取利息和基金分红；
- Circle 再把其中很大一部分支付给 Coinbase、Binance、交易所、做市商、钱包、区块链生态等分销伙伴，鼓励它们推广和使用 USDC；
- 剩下的部分扣掉员工、合规、技术、营销和运营成本后，才是 Circle 的利润。

因此，今天 Circle 的核心利润引擎不是“每笔支付收很高费用”，而是“USDC 规模 × 储备收益率 × Circle 能留下来的比例”。

### 关键术语翻译

- **USDC in circulation**：外部流通的 USDC 总额，可以理解为 Circle 可投资的稳定币储备池规模。
- **Reserve income**：储备资产产生的利息和分红，是 Circle 当前最主要收入。
- **Distribution costs**：付给 Coinbase、Binance、交易所、做市商、生态伙伴的分销激励成本。
- **RLDC / Revenue Less Distribution Costs**：总收入减分销、交易和其他成本后的收入质量指标，类似“Circle 真正留下来用于覆盖运营费用和利润的毛收入”。
- **Arc**：Circle 推出的 Layer-1 区块链，目标是服务企业级稳定币支付和链上金融。
- **CPN（Circle Payments Network）**：Circle 的支付网络，帮助机构用稳定币做跨境和链上支付。
- **USYC**：Circle 相关的代币化货币市场基金产品，用于把传统短期收益资产上链。

### 产业结构

稳定币行业的需求来自四类场景：

1. **交易所和 crypto 交易**：用户用 USDC 作为美元替代品在交易所或 DeFi 中交易。
2. **跨境支付和汇款**：用稳定币降低传统跨境支付速度慢、费用高的问题。
3. **企业资金管理**：企业用 USDC 做 24/7 资金调拨和链上结算。
4. **AI agent / 自动化支付**：未来软件代理可能自动付款、结算和调用服务，Circle 希望 USDC 成为这种机器经济的支付单位。

行业吸引力在于美元稳定币有网络效应：越多交易所、钱包、商户、开发者、金融机构支持 USDC，用户越愿意持有和使用 USDC。但行业也有明显风险：稳定币可替代性较强，监管要求高，发行商必须维持信任和流动性。

## 3. Segment and Product Analysis

Circle 披露不按传统业务分部细分，但可以从三大平台支柱理解。

### 3.1 Circle Digital Assets and Services

包括 USDC、EURC、USYC、Circle Mint、xReserve 等。

- **USDC** 是核心资产，也是大部分收入来源。
- **EURC** 是欧元稳定币，规模相对较小，但可能受益于欧洲合规稳定币需求。
- **USYC** 是代币化货币市场基金，体现 Circle 想把传统收益资产引入链上金融。
- **Circle Mint / xReserve** 是机构铸造、赎回、流动性和储备管理基础设施。

最新可验证数据：

- 2026 Q1 期末 USDC 流通量：**770 亿美元**，同比增长 **28%**。
- 2026 Q1 平均 USDC 流通量：**752 亿美元**，同比增长 **39%**。
- 2026 Q1 USDC 链上交易量：**21.5 万亿美元**，同比增长 **263%**。
- 2026 Q1 meaningful wallets：**720 万**，同比增长 **47%**。

这些数据说明 USDC 的使用范围在扩大，但投资关键不是交易量本身，而是交易量能否转化为稳定、可货币化的收入。

### 3.2 Arc Blockchain and Developer Infrastructure

Arc 是 Circle 自己的 Layer-1 区块链。它的战略含义是：Circle 不想只做稳定币发行商，也想控制一部分企业级稳定币结算基础设施。

2026 Q1 earnings release 披露：

- ARC Token 预售融资 **2.22 亿美元**；
- 预售对应网络完全稀释估值 **30 亿美元**；
- 投资方包括 a16z crypto、Apollo Funds、ARK Invest、BlackRock、Bullish、General Catalyst、Haun Ventures、ICE、Janus Henderson、Standard Chartered Ventures 等。

这提高了 Arc 的外部背书，但也引入新问题：Arc 的代币激励、网络治理、收入确认、对 CRCL 股东的经济归属仍需要进一步观察。

### 3.3 Circle Applications

包括 CPN、StableFX、Managed Payments、Agent Stack 等。

- **CPN**：试图让银行、支付机构和企业用稳定币做全球支付。
- **Managed Payments**：让金融机构可以推出稳定币支付，而不必直接管理数字资产。
- **Agent Stack**：面向 AI agent 时代的支付、钱包、命令行、市场和微支付基础设施。

2026 Q1 earnings release 披露：CPN 以 2026-03-31 前 30 天活动年化计算，交易量约 **83 亿美元**。这仍是早期规模，尚不足以证明其能替代储备利息成为主要收入来源。

## 4. Financial Deep Dive

### 4.1 收入结构

2025 年：

- Total revenue and reserve income：**27.47 亿美元**，同比增长 **64%**。
- Adjusted EBITDA：**5.82 亿美元**，同比增长 **104%**。
- 持续经营净亏损：**6951 万美元**，主要受 IPO 相关股权激励费用影响。
- 2025 年 reserve income 占总收入约 **96%**，说明公司收入仍高度依赖储备利息。

2026 Q1：

- Total revenue and reserve income：**6.941 亿美元**，同比增长 **20%**。
- Reserve income：**6.525 亿美元**，同比增长 **17%**。
- Other revenue：**4163 万美元**，同比约翻倍。
- Total distribution, transaction and other costs：**4.068 亿美元**。
- RLDC：约 **2.87 亿美元**。
- RLDC margin：**41%**。
- Net income from continuing operations：**5525 万美元**，同比下降 **15%**。
- Adjusted EBITDA：**1.51 亿美元**，同比增长 **24%**。

### 4.2 成本结构和盈利质量

Circle 的关键不是传统 gross margin，而是“储备收入能留下多少”。

2026 Q1：

- 总收入和储备收入 6.94 亿美元；
- 分销、交易和其他成本 4.07 亿美元；
- RLDC margin 41%。

这意味着大约六成收入被分销和交易成本吃掉。Coinbase 是重要伙伴，2025 Form 10-K 披露 2025 年与 Coinbase 协议相关分销成本 **14 亿美元**，2024 年为 **9.245 亿美元**。

这既是护城河的一部分，也是利润限制因素：

- 好处：Coinbase 等伙伴帮助 USDC 获取流动性、用户和交易场景。
- 坏处：Circle 很难独享 USDC 网络的经济利益。

### 4.3 现金流和资本强度

2025 年：

- 经营现金流：**5.421 亿美元**。
- 资本开支：**1243 万美元**。

2026 Q1：

- 经营现金流：**2108 万美元**。
- 资本开支：**935.6 万美元**。

Circle 不是重资产公司，资本开支低。但经营现金流会受到分销付款、应收应付、储备资产和激励安排影响，不能只看净利润。

### 4.4 资产负债表

2026-03-31：

- 公司现金及等价物：**15.17 亿美元**。
- 为公司持有稳定币隔离的现金及等价物：**7.93 亿美元**。
- 为稳定币持有人隔离的现金及等价物：**768.94 亿美元**。
- 稳定币持有人存款负债：**767.79 亿美元**。
- 股东权益：**34.29 亿美元**。
- 可转换债务净额：**0**，2025-12-31 为 **3682 万美元**。

需要注意：稳定币储备资产和对应负债在资产负债表上很大，但这些不是 Circle 可自由支配的企业现金。估值时不能把全部储备资产当作公司净现金。

### 4.5 稀释和 SBC

2026 Q1：

- 摊薄加权股数：**2.667 亿股**。
- 2026-05-06 已发行 Class A：**2.2986 亿股**，Class B：**1872 万股**。
- 2025 年股权激励费用：**5.662 亿美元**，其中 IPO 触发的费用较大。
- 2026 Q1 股权激励费用：**5184 万美元**。

这是一个必须持续跟踪的问题。上市后股权激励可能维持较高水平，真实股东收益要看每股指标，而不只是 EBITDA。

## 5. Management and Capital Allocation

Circle 由 Jeremy Allaire 联合创立并长期领导，公司在稳定币合规、金融机构关系和监管叙事上执行力较强。其管理层最重要的战略选择是：

1. 坚持合规和监管优先；
2. 与 Coinbase、Binance、银行、支付公司、区块链生态建立分销网络；
3. 从 USDC 发行商向 Arc / CPN / Agent Stack 平台演进；
4. 通过代币化基金、企业支付和 AI agent 支付拓展非储备收入。

目前可以肯定的是，公司在产品叙事和生态合作上很强；尚未完全证明的是，这些新业务能否形成高利润、可持续、股东可享有的现金流。

管理层 2026 Q1 指引：

- USDC in circulation：多周期 **40% CAGR**。
- FY2026 other revenue：**1.50–1.70 亿美元**。
- FY2026 RLDC margin：**38%–40%**。
- FY2026 adjusted operating expenses：**5.70–5.85 亿美元**。

这些承诺未来要持续验证，尤其是 USDC 增速是否在利率变化和竞争压力下仍能维持。

## 6. Valuation Work

### 6.1 当前市场状态

行情抓取显示，CRCL 当前价格约 **62.63 美元**。Yahoo chart 数据显示 52 周高点 **262.97 美元**、低点 **49.90 美元**，说明 IPO 后波动极大。

由于 CRCL 上市时间短，历史估值区间不稳定，传统 P/E 参考意义有限。更合理的估值框架是：

- EV / RLDC：看 Circle 扣除分销和交易成本后真正留下来的收入；
- EV / Adjusted EBITDA：看平台业务在当前投资强度下的经营利润；
- 情景估值：分别假设利率、USDC 规模、RLDC margin、SBC 和稀释。

### 6.2 为什么不用简单 P/E？

2025 净利润受到 IPO 相关 SBC 冲击，2026 Q1 净利润又受到上市后 SBC、产品投入和利率变化影响。P/E 会显得跳动很大，不足以表达业务本质。

### 6.3 情景估值框架

以下是研究框架，不是精确目标价：

| 情景 | 核心假设 | 估值含义 |
|---|---|---|
| Bear | 利率下降较快，USDC 增长低于管理层 40% CAGR，分销成本率高，Arc/CPN 商业化慢 | 市场会把 CRCL 当作利率敏感金融中介，估值倍数收缩；安全边际需要显著低于当前价格 |
| Base | USDC 继续增长但增速波动，RLDC margin 保持 38%–40%，other revenue 逐步增长，SBC 可控 | 当前价格可能接近合理偏贵区间，是否有吸引力取决于 2026–2027 业绩验证 |
| Bull | USDC 规模持续高增长，CPN / Arc / Agent Stack 带来非利息收入，监管强化合规发行商地位 | 可以支撑较高平台型估值，但需要多个尚未完全验证的假设同时成立 |

我的基准判断：**当前更像“可跟踪但不急于重仓”的价格区间**。若没有持仓，较合理的做法是等待下一到两个季度验证：USDC 平均余额、RLDC margin、other revenue、SBC、Arc 经济归属。

### 6.4 安全边际思考

CRCL 的安全边际不应只看股价是否从高点跌了很多，而要看：

1. 如果利率从 3.5% 降到更低，reserve income 会下降多少？
2. Coinbase / Binance / 其他伙伴拿走的经济利益是否下降，还是随着规模继续上升？
3. Other revenue 是否能从 2026 指引的 1.50–1.70 亿美元继续变成数亿美元级高毛利收入？
4. 每股摊薄是否可控？
5. Arc token 的价值是否能真正归属于 CRCL 股东？

如果这些问题没有答案，估值必须打折。

## 7. Catalysts and Monitoring Plan

### 近期催化剂

- 下一次季度财报：验证 Q2 USDC 平均余额、RLDC margin、other revenue 和 adjusted operating expenses。
- Arc 进展：主网上线、开发者生态、交易量、代币激励规则、收入归属。
- CPN 商业化：年化交易量是否从 83 亿美元继续放大。
- 监管进展：美国稳定币监管框架对 Circle 的牌照、储备、资本、分销、收益分享模式的影响。
- 利率变化：美债收益率下降会压缩储备收益率。

### 必须跟踪的指标

1. USDC in circulation，期末和平均值都要看。
2. Reserve return rate。
3. RLDC margin。
4. Other revenue 增速。
5. Distribution costs，尤其是 Coinbase / Binance 相关成本。
6. Adjusted operating expenses。
7. SBC 和摊薄股数。
8. CPN 交易量。
9. Arc 网络活跃度和 CRCL 股东经济权益。
10. USDC 市占率和 meaningful wallets。

## 8. Risk Register

| 风险 | 概率 | 严重性 | 机制 | 监控信号 |
|---|---:|---:|---|---|
| 利率下降 | 高 | 高 | 储备收益率下降，收入和 EBITDA 受压 | Reserve return rate、Fed path、T-bill yield |
| 分销成本过高 | 高 | 高 | Coinbase/Binance/生态伙伴拿走大量经济利益 | RLDC margin 是否低于 38% |
| 市占率下降 | 中 | 高 | USDT、银行稳定币、支付公司、链上原生资产竞争 | USDC 市占率、交易所支持度 |
| 监管变化 | 中 | 高 | 储备、牌照、收益分享、跨境使用受限 | SEC/银行监管/稳定币法案细则 |
| Arc 失败或经济归属不清 | 中 | 中高 | 新平台不能转化为股东现金流 | Arc TVL、交易量、收入确认、token 分配 |
| 股权激励稀释 | 高 | 中 | 每股价值被稀释 | SBC、diluted shares、RSU grants |
| 声誉 / 挤兑风险 | 低中 | 极高 | 稳定币信任一旦受损，赎回压力剧烈 | USDC depeg、赎回量、储备证明 |

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B。公司披露较完整，但上市时间很短，缺少多年公开市场检验。
- **Main research blind spot**: Arc、CPN、Agent Stack 的长期经济归属和可货币化能力尚未被财报充分验证。
- **Strongest reason smart investors may disagree**: 有人会认为监管稳定币是未来金融基础设施，Circle 是最稀缺的合规入口，应该给平台型高估值。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个生意的现金流能否在未来 10 年稳定、可预测、可防守？
- **Evidence supporting the thesis**: USDC 规模大，流通量增长，Circle 合规形象强，资产负债表中企业现金充足，资本开支低。
- **Evidence against the thesis**: 收入依赖利率，分销伙伴拿走大量经济利益，长期利润率和监管框架仍不稳定。
- **Decision implication**: Buffett-style 投资者可能会继续观察，而非在商业模式仍快速变化时重仓。
- **Follow-up question**: 如果股市关闭五年，USDC 余额、RLDC margin、分销成本和监管地位是否足以让人安心持有？

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这笔投资最容易在哪些地方被叙事骗到？

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| 把交易量当利润 | 链上交易量巨大但费用率低 | 收入转化低于预期 |
| 把监管当护城河 | 监管也可能带来成本和限制 | 合规优势变成成本负担 |
| 忽视利率周期 | 储备收益率下降 | EBITDA 下滑 |
| 忽视伙伴议价权 | Coinbase 等渠道重要 | Circle 留存经济利益受限 |
| 过度相信 Arc | token 和网络价值不一定归属于股东 | 平台估值落空 |

- **Fragile assumptions**: USDC 能长期 40% CAGR、RLDC margin 能稳定在 38%–40%、Arc 能形成新收入层。
- **Incentive structure**: 管理层和生态伙伴都被激励扩大 USDC 使用，但生态伙伴可能更关心自身收益而非 CRCL 股东利润。
- **Psychological traps**: “稳定币未来很大”不等于“CRCL 当前估值便宜”。
- **Major stupidity risk**: 只因为股价从高点大跌就认为有安全边际。
- **Follow-up question**: 三年后如果投资错误，今天最明显的红旗可能是利率敏感和分销成本率。

### Duan Yongping-style lens

- **Conclusion**: Needs further observation。
- **One-sentence business essence**: Circle 把美元变成可在互联网上 24/7 流动的数字美元，并通过储备收益和支付基础设施赚钱。
- **User value**: 用户得到快速、全球、链上可编程的美元结算能力；企业和开发者得到支付和流动性基础设施。
- **Product or brand strength**: USDC 的合规品牌和生态支持较强，但稳定币本身有一定同质化，用户切换成本取决于交易所、钱包和应用集成。
- **People and culture**: 管理层长期坚持监管优先和机构化路线，这是优势。
- **Long-term certainty and right price**: 生意方向有吸引力，但好价格必须补偿利率、监管、分销和稀释风险。
- **Decision implication**: 可以深入研究，但当前应避免把“好方向”直接等同于“好股票”。
- **Follow-up question**: Circle 是在创造长期客户价值，还是主要在货币利率周期中赚储备收益？

### Li Lu-style lens

- **Conclusion**: Needs further observation。
- **Circle of competence**: 可以从公开数据理解 USDC 规模、储备收益、分销成本和财务趋势；但 Arc 生态、代币经济、稳定币监管最终形态需要更多实地和专家验证。
- **Industry trend**: 稳定币和代币化现金资产可能是长期金融基础设施趋势，Circle 处在价值链核心位置之一。
- **Downside protection**: 公司企业现金较强、无明显传统债务压力，但股价估值保护取决于盈利质量而非储备资产规模。
- **Margin of safety**: 目前安全边际不厚，因为多个关键变量尚未证明。
- **Research-depth decision**: 值得继续跟踪，但暂不应视为高确定性长期核心仓位。
- **Follow-up question**: 10–20 年后，Circle 会成为全球数字美元基础设施的长期节点，还是稳定币资本周期中的阶段性赢家？

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

评分理由：

- Business model 7：稳定币基础设施有真实需求，但收入过度依赖储备收益。
- Moat 6：合规品牌、生态和流动性有价值，但稳定币竞争和伙伴议价权限制护城河。
- Management 7：战略和合规执行不错，但平台化仍需结果验证。
- Financial quality 6：Adjusted EBITDA 和现金流不错，但 SBC、利率敏感和分销成本影响质量。
- Valuation attractiveness 5：股价回落后比高点理性，但仍不算明显便宜。
- Long-term certainty 5：行业方向强，商业模式最终利润结构不确定。
- Downside risk control 5：企业现金充足，但股价对预期和监管敏感。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 稳定币基础设施优质，但利率敏感 | 中 |
| Moat | 合规 + 网络 + 分销，但非绝对护城河 | 中 |
| Management and capital allocation | 长期战略清晰，需验证新业务回报 | 中 |
| Biggest risk | 利率下行 + 分销成本 + 估值压缩 | 中高 |
| Long-term trend | 稳定币和链上支付趋势正面 | 中高 |
| Valuation and margin of safety | 当前不算厚安全边际 | 中 |

### Action-framing

| Investor state | Research implication |
|---|---|
| No position | 更适合观察和等待财报验证，不急于重仓 |
| Existing position | 关注 RLDC margin、USDC 增长和 SBC；若指标恶化应降级 |
| Add / upgrade signal | USDC 高增长 + RLDC margin 稳定 + other revenue 超预期 + SBC 可控 |
| Reduce / downgrade signal | USDC 市占率下降、reserve return rate 下降但成本不降、Arc 经济归属不清、稀释扩大 |

## 10. Final Research Framework

### 投资 thesis 依赖什么？

1. USDC 继续扩大流通规模和机构采用。
2. Circle 能保持或改善 38%–40% 左右的 RLDC margin。
3. Other revenue 从小基数成长为可观平台收入。
4. Arc、CPN、Agent Stack 不是只有叙事，而能产生股东可享有现金流。
5. 监管框架提高合规发行商门槛，而不是压缩 Circle 的经济利益。
6. SBC 和稀释逐步正常化。

### 什么会让我更看多？

- 连续几个季度 USDC 平均余额高速增长，且不是靠不可持续补贴。
- RLDC margin 稳定或提升。
- Other revenue 超过管理层 2026 指引并继续加速。
- CPN 交易量从几十亿美元年化走向数百亿美元以上。
- Arc 经济模型清晰，且 CRCL 股东能明确受益。
- SBC / revenue 比例下降，摊薄股数可控。

### 什么会改变我的观点？

- **上调**：如果 Circle 证明自己不是利率敏感发行商，而是稳定币支付和链上金融平台，且非利息收入快速增长。
- **下调**：如果利率下降导致 reserve income 下滑，RLDC margin 跌破指引，USDC 市占率下降，或 Arc / CPN 进展主要停留在叙事层面。

## Sources

- Circle Internet Group, Inc. Form 10-Q for quarter ended March 31, 2026, filed 2026-05-11: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm
- Circle Q1 2026 earnings release, filed as Exhibit 99.1 to Form 8-K on 2026-05-11: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000148/final_05x11q1epr30.htm
- Circle Internet Group, Inc. Form 10-K for fiscal year ended December 31, 2025, filed 2026-03-09: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000062/crcl-20251231.htm
- Circle 2026-06-12 Form 8-K, Board update: https://www.sec.gov/Archives/edgar/data/1876042/000187604226000192/crcl-20260612.htm
- Yahoo Finance chart endpoint for CRCL price snapshot, fetched 2026-07-01 CST.
