# CRCL（Circle Internet Group）中文深度研究报告 v2

- **Research view**: 中性 / 等待确认，但相较 v1 更明确：当前价格约 $62.63 已从高位大幅回落，进入“可以严肃跟踪、但还不是高安全边际”的区间。
- **Confidence**: 中等偏低。公司披露质量较好，但上市时间短，稳定币监管、利率路径、分销成本、Arc/CPN 经济归属和上市后 SBC/稀释仍有较大不确定性。
- **Time horizon**: 中期 6–18 个月；长期 3–5 年以上。
- **Main thesis**: Circle 是受监管美元稳定币基础设施的稀缺上市标的。USDC 规模、链上交易量和机构采用仍在扩大，但今天利润核心仍是“USDC 储备规模 × 储备收益率 × Circle 留存比例”。要从中性升级为正面，需要看到 USDC 增长、RLDC margin、other revenue 与 Arc/CPN 商业化共同验证。
- **Key risk**: 利率下降、USDC 市占率受压、Coinbase/Binance 等分销伙伴拿走过多经济利益、Arc/CPN 对 CRCL 股东价值归属不清、以及 SBC/稀释侵蚀每股价值。

> 数据日期：行情抓取于 2026-07-01；Yahoo Finance chart 元数据显示 CRCL 2026-06-30 收盘附近价格约 **$62.63**，52 周区间约 **$49.90–$262.97**。公司数据主要来自 Circle 2026 Q1 Form 10-Q、2026 Q1 earnings release、2025 Form 10-K、SEC submissions，以及已有本地研究底稿。本文为研究支持，不构成个性化投资建议。

## 1. Executive View

### 研究结论

CRCL 现在比第一次研究时更值得认真放入观察清单，但我仍不把它定义为“已经有明显安全边际的长期核心仓位”。原因是：

1. **公司业务真实、有稀缺性**：USDC 是全球主要美元稳定币之一，Circle 在合规、机构关系和美国监管叙事上相对领先。
2. **盈利质量仍不够“纯平台化”**：2025 年 reserve income 占总收入约 96%；2026 Q1 reserve income 仍是收入主体。它更像利率敏感的金融基础设施公司，而不是典型软件平台。
3. **当前估值的关键不是收入，而是每股盈利能力**：若用 2026 Q1 年化净利润估算，当前估值仍不便宜；若相信 2028 以后 USDC 规模和平台业务放大，当前价格有中长期选项价值。
4. **新版估值要求下的结论**：基准情景合理价格区间约 **$45–77**；强安全边际更偏向 **$45–55 以下**；当前 $62.63 处于基准区间中部偏上，不是离谱泡沫，但也不是低风险便宜货。

### 最强反方理由

市场可能把“稳定币长期增长 + 美国监管利好 + Circle 合规稀缺性 + Arc/CPN/AI 支付平台化”提前资本化，但可验证利润仍主要来自储备收益。若美国降息、分销成本维持高位、USDC 增长低于预期，当前每股盈利能力很难支撑高倍数。

## 2. Business Model and Industry Structure

### 小白版解释：Circle 怎么赚钱？

Circle 发行 USDC。USDC 是一种“美元稳定币”：用户交给 Circle 1 美元，Circle 发行 1 枚 USDC；用户赎回时，Circle 销毁 USDC 并返还 1 美元。为了保证 USDC 能 1:1 兑回美元，Circle 把收到的钱放在现金、短期国债、货币市场基金等储备资产里。

Circle 今天赚钱的核心机制是：

- 用户持有 USDC 通常拿不到储备利息；
- Circle 用储备资产赚利息和基金分红；
- Circle 把其中很大一部分付给 Coinbase、Binance、交易所、做市商、钱包和生态伙伴，换取流动性和分销；
- 剩下的钱扣掉员工、技术、合规、营销和运营成本后，才成为利润。

一句话：**今天 Circle 的利润主要不是来自支付手续费，而是来自稳定币储备收益；未来估值能否抬升，取决于它能否把稳定币发行商升级为全球数字美元支付和开发者平台。**

### 关键术语翻译

- **USDC in circulation**：外部流通的 USDC 总额，相当于 Circle 能产生储备收益的稳定币规模。
- **Reserve income**：储备资产产生的利息和基金分红，是当前收入核心。
- **Distribution costs**：为了让 USDC 被交易所、钱包、生态伙伴采用而支付的激励和分成。
- **RLDC / Revenue Less Distribution Costs**：总收入扣除分销、交易和其他成本后，Circle 真正留下来的收入质量指标。
- **RLDC margin**：RLDC 占 total revenue and reserve income 的比例，越高说明 Circle 留存经济利益越多。
- **Arc**：Circle 推出的 Layer-1 区块链，面向企业级稳定币支付和链上金融。
- **CPN**：Circle Payments Network，帮助机构和企业用稳定币进行全球支付。
- **Other revenue**：除了储备收益以外的收入，长期最关键，因为它代表平台化收入是否形成。

### 行业结构

稳定币需求来自四类场景：

1. **加密交易和 DeFi**：USDC 作为链上美元和交易媒介。
2. **跨境支付和汇款**：比传统跨境支付更快、更便宜、可 24/7 结算。
3. **企业资金管理**：企业用稳定币做全球资金调拨、供应链结算和链上金融。
4. **AI agent / 自动化微支付**：未来软件代理可能自动付款、调用服务和结算，稳定币可能成为机器支付单位。

行业吸引力在于网络效应和合规门槛；行业风险在于产品可替代、监管不确定、利率周期和分销伙伴议价能力。

## 3. Segment and Product Analysis

Circle 不按传统业务分部披露，但可以拆成三层。

### 3.1 USDC / EURC / Circle Mint：今天的利润引擎

这是当前最重要业务。公司通过发行 USDC/EURC，获取储备收益，再通过 Circle Mint 等工具服务机构铸造、赎回和管理稳定币。

2026 Q1 关键 KPI：

- 期末 USDC 流通量：**770 亿美元**，同比 **+28%**。
- 平均 USDC 流通量：**752 亿美元**，同比 **+39%**。
- USDC 链上交易量：**21.5 万亿美元**，同比 **+263%**。
- meaningful wallets：**720 万**，同比 **+47%**。

这些数据说明使用量增长较快，但投资上要继续问：交易量是否能转化成 Circle 留存收入？如果交易量只是生态热度，而不是付费能力，估值不能过度外推。

### 3.2 Arc：潜在平台化选项，但股东经济归属待验证

Arc 是 Circle 推出的 Layer-1 区块链，战略目标是让企业级稳定币支付、代币化资产和链上金融在 Circle 生态里运行。

2026 Q1 earnings release 披露：

- ARC Token 预售融资 **2.22 亿美元**；
- 对应网络完全稀释估值 **30 亿美元**；
- 参与方包括 a16z crypto、Apollo Funds、ARK Invest、BlackRock、Bullish、General Catalyst、Haun Ventures、ICE、Janus Henderson、Standard Chartered Ventures 等。

这增强了外部背书，但也带来估值难题：Arc 的代币价值、网络费用、治理权和 CRCL 股东之间的经济关系还需要后续文件和经营数据验证。不能直接把 Arc 的网络 FDV 全部算进 CRCL 股东价值。

### 3.3 CPN / StableFX / Managed Payments / Agent Stack：未来收入选项

这部分是 Circle 长期想象空间所在。

- **CPN**：让银行、支付机构和企业用稳定币做跨境和链上支付。
- **StableFX**：帮助稳定币和法币之间兑换、支付和结算。
- **Managed Payments**：让金融机构推出稳定币支付，而不必自己直接管理数字资产。
- **Agent Stack**：面向 AI agent 的钱包、支付、命令行、市场和微支付基础设施。

2026 Q1 披露：CPN 按 2026-03-31 前 30 天活动年化，交易量约 **83 亿美元**。这是好开始，但规模仍早，尚不能证明能替代储备收益成为主要收入。

## 4. Financial Deep Dive

### 4.1 收入结构

2025 年：

- Total revenue and reserve income：**27.47 亿美元**，同比 **+64%**。
- Adjusted EBITDA：**5.82 亿美元**，同比 **+104%**。
- 持续经营净亏损：**6951 万美元**，主要受 IPO 相关股权激励费用影响。
- Reserve income 占总收入约 **96%**。

2026 Q1：

- Total revenue and reserve income：**6.941 亿美元**，同比 **+20%**。
- Reserve income：**6.525 亿美元**，同比 **+17%**。
- Other revenue：**4163 万美元**，同比约翻倍。
- Total distribution, transaction and other costs：**4.068 亿美元**。
- RLDC：约 **2.87 亿美元**。
- RLDC margin：**41%**。
- Net income from continuing operations：**5525 万美元**，同比 **-15%**。
- Adjusted EBITDA：**1.51 亿美元**，同比 **+24%**。

### 4.2 盈利质量

Circle 不是重资产公司，资本开支低；但它也不是典型 SaaS。关键指标不是传统 gross margin，而是 RLDC margin。

2026 Q1 分销、交易和其他成本占 total revenue and reserve income 约 59%，意味着 Circle 必须持续和生态伙伴分享大部分经济利益。2025 Form 10-K 披露，与 Coinbase 协议相关分销成本 2025 年约 **14 亿美元**，2024 年约 **9.245 亿美元**。

这同时是护城河和利润天花板：

- 好处：Coinbase 等伙伴帮助 USDC 获取流动性、用户和场景；
- 坏处：Circle 不能独享 USDC 网络收益，长期利润率取决于伙伴议价和生态竞争。

### 4.3 现金流和资本强度

2025 年：

- 经营现金流：**5.421 亿美元**。
- 资本开支：**1243 万美元**。
- 粗略自由现金流：约 **5.30 亿美元**。

2026 Q1：

- 经营现金流：**2108 万美元**。
- 资本开支：**935.6 万美元**。
- 粗略自由现金流：约 **1172 万美元**。

2026 Q1 自由现金流明显弱于 2025 年年化水平，可能与营运资本、分销付款、上市前后结算安排有关；因此不能只看 adjusted EBITDA。

### 4.4 资产负债表

2026-03-31：

- 公司现金及等价物：**15.17 亿美元**。
- 公司投资：约 **1.00 亿美元**。
- 公司数字资产：约 **0.84 亿美元**。
- 为公司持有稳定币隔离的现金及等价物：**7.93 亿美元**。
- 为稳定币持有人隔离的现金及等价物：**768.94 亿美元**。
- 稳定币持有人存款负债：**767.79 亿美元**。
- 股东权益：**34.29 亿美元**。
- 可转换债务净额：**0**，2025-12-31 为 **3682 万美元**。

估值时不能把稳定币储备资产当成公司自由现金。本文估值使用公司层面现金、投资和数字资产约 **17.02 亿美元** 作为净现金近似。

### 4.5 股本、SBC 和每股价值

2026 Q1 摊薄加权股数约 **2.667 亿股**。按 $62.63 估算：

- 市值约 **167 亿美元**；
- 扣除公司层面净现金后企业价值约 **150 亿美元**；
- 2026 Q1 年化净利润约 **2.21 亿美元**，对应年化 P/E 约 **75x**；
- 2026 Q1 年化 adjusted EBITDA 约 **6.04 亿美元**，对应 EV / annualized adjusted EBITDA 约 **25x**；
- 对 2025 粗略自由现金流约 **5.30 亿美元**，市值 / FCF 约 **31x**，但 2026 Q1 FCF 年化显著更低。

这说明：即使股价从高位大幅回落，CRCL 仍需要未来利润增长来证明当前价格，而不是单靠当期盈利就很便宜。

## 5. Management and Capital Allocation

Circle 由 Jeremy Allaire 长期领导，公司在合规路线、机构关系、监管沟通和稳定币基础设施建设上执行力较强。管理层的核心战略是：

1. 坚持受监管美元稳定币定位；
2. 借 Coinbase、Binance、银行、支付公司、区块链生态扩大 USDC 分销；
3. 从稳定币发行商升级为 Arc / CPN / Agent Stack 平台；
4. 通过 other revenue 提高非利率收入占比。

需要跟踪的管理层承诺：

- USDC in circulation 多周期 **40% CAGR**；
- FY2026 other revenue **1.50–1.70 亿美元**；
- FY2026 RLDC margin **38%–40%**；
- FY2026 adjusted operating expenses **5.70–5.85 亿美元**；
- Arc、CPN、Agent Stack 的商业化和 CRCL 股东经济归属。

管理层最大挑战是：把“监管叙事 + 网络故事”转化为可验证的每股自由现金流增长。

## 6. Valuation Work

### 6.1 当前估值输入

- 当前价格：约 **$62.63**。
- Q1 摊薄股数：约 **2.667 亿股**。
- 市值：约 **167 亿美元**。
- 公司层面现金、投资和数字资产：约 **17.02 亿美元**。
- 企业价值：约 **150 亿美元**。
- 2026 Q1 annualized net income：约 **2.21 亿美元**。
- 2026 Q1 annualized adjusted EBITDA：约 **6.04 亿美元**。

### 6.2 为什么不用单一 P/S 或单一 P/E？

CRCL 既不是传统银行，也不是纯软件公司。它有金融属性、利率敏感、分销成本和平台化选项。因此估值要结合：

- 当期 earnings power；
- USDC 余额增长；
- 储备收益率下降敏感性；
- RLDC margin；
- other revenue 成长；
- SBC/稀释；
- Arc/CPN 是否形成股东可享有的经济价值。

### 6.3 熊 / 基准 / 牛三情景估值

以下不是预测，而是把可验证假设转化成每股价格区间。价格区间以中期 FY2028 附近的每股盈利能力为核心，辅以平台化业务的倍数差异。当前价按 **$62.63** 计算上行/下行。

| 情景 | 每股盈利能力假设 | 估值倍数 | 隐含合理价格区间 | 相对当前价格 | 核心假设 | 触发条件 |
|---|---:|---:|---:|---:|---|---|
| Bear | EPS $0.80–1.20 | 18–22x | **$14–26** | **-77% 到 -58%** | 利率下降，USDC 增速放缓，RLDC margin 低于指引，平台收入慢 | USDC 平均余额连续走弱、RLDC margin 跌破 38%、other revenue 不达标 |
| Base | EPS $1.80–2.40 | 25–32x | **$45–77** | **-28% 到 +23%** | USDC 增长抵消部分降息压力，RLDC margin 38%–40%，other revenue 稳步增长 | Q2–Q4 验证 USDC 平均余额、RLDC margin、SBC 和平台收入 |
| Bull | EPS $3.20–4.20 | 35–45x | **$112–189** | **+79% 到 +202%** | USDC 持续高增，Arc/CPN 商业化，other revenue 高增长且高质量 | 平台收入超预期、Arc/CPN 费用归属清晰、USDC 市占率提升 |

### 6.4 安全边际价格

基于上述三情景，我的安全边际判断是：

- **强安全边际区间**：约 **$35–45**。这个区间接近或低于基准情景下沿，并对熊市情景有一定缓冲。
- **可分批研究/观察区间**：约 **$45–55**。需要接受公司仍处验证期，适合小仓或观察，不适合把 bull case 当确定性。
- **基准合理但不便宜区间**：约 **$55–75**。当前 $62.63 落在这里；需要未来季度数据继续证明。
- **需要强 bull case 才合理的区间**：高于 **$80–90**。若没有平台收入加速和 RLDC 稳定证据，安全边际不足。

因此，**当前价格不是明显泡沫，但也不是我会称为“安全边际充足”的价格**。更合理的策略是：等待 1–2 个季度看 USDC 平均余额、RLDC margin、other revenue、SBC 和 Arc/CPN 经济归属是否验证。

## 7. Catalysts and Monitoring Plan

### 近中期催化

- 下一次季度财报：验证 Q2 USDC 平均余额、reserve return rate、RLDC margin、other revenue 和 adjusted operating expenses。
- 美国稳定币监管落地细节：可能提高合规发行商门槛，也可能限制收益分享和产品结构。
- Arc / CPN / Agent Stack 商业化数据：交易量、费用、留存收入、机构客户。
- 利率预期变化：直接影响 reserve income。
- 竞争格局：USDT、PYUSD、银行稳定币、DeFi 原生稳定币、交易所自有稳定币。

### 必须跟踪的指标

- USDC 期末和平均流通量；
- USDC 市占率；
- reserve return rate；
- RLDC 和 RLDC margin；
- distribution, transaction and other costs；
- other revenue；
- adjusted operating expenses；
- net income、operating cash flow、free cash flow；
- SBC 和 diluted shares；
- CPN annualized transaction volume；
- Arc network usage 和 CRCL 股东经济链接。

## 8. Risk Register

| 风险 | 概率 | 影响 | 机制 | 观察指标 |
|---|---|---|---|---|
| 利率下降 | 高 | 高 | 储备收益率下降，reserve income 下滑 | Fed 利率、reserve return rate、reserve income |
| 分销成本高 | 高 | 高 | Coinbase/Binance/生态伙伴拿走大量经济利益 | RLDC margin、distribution costs |
| USDC 市占率弱化 | 中 | 高 | USDT、银行稳定币、PYUSD 或其他产品挤压 | USDC circulation、市占率、交易所支持 |
| 监管变化 | 中 | 高 | 合规成本上升或收益分享受限 | 美国稳定币法案、SEC/CFTC/银行监管 |
| Arc/CPN 经济归属不清 | 中 | 中高 | 网络价值可能主要归 token 或生态，不归 CRCL 股东 | Arc 收入确认、费用流向、治理披露 |
| SBC/稀释 | 高 | 中高 | 每股价值被稀释，GAAP 盈利受压 | SBC、diluted shares、RSU grants |
| 估值倍数压缩 | 中 | 高 | 平台叙事证伪或利率下行导致 EPS 低于预期 | P/E、EV/EBITDA、增长预期 |

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B。公司已上市并有 SEC/IR 披露，但上市历史短，平台化业务和周期数据不足。
- **Main research blind spot**: Arc、CPN、Agent Stack 最终能给 CRCL 股东带来多少可持续现金流，公开数据尚不能证明。
- **Strongest reason smart investors may disagree**: 有人会认为稳定币监管落地后，Circle 是少数受益者，当前回调已经给了足够长期赔率；也有人会认为这仍是高利率周期下的金融收入套利。

### Buffett-style lens：Needs further observation

- **Key question**: 这是不是一个十年后仍能稳定赚钱、且今天价格有安全边际的生意？
- **Evidence supporting thesis**: USDC 已有规模和网络；Circle 合规品牌强；资本开支低；资产负债表公司层面净现金较好。
- **Evidence against thesis**: 当前利润高度依赖利率；分销伙伴拿走大量经济利益；上市后 SBC/稀释仍需观察；当前价格未给明显保守安全边际。
- **Decision implication**: 适合观察，不适合按“确定性复利股”直接重仓。
- **Follow-up question**: 如果股市关闭五年，USDC 余额、RLDC margin、分销成本和监管地位是否足以让人安心持有？

### Munger-style lens：Needs further observation

- **Key question**: 这个投资最容易在哪些地方被叙事误导？
- **Failure paths**:

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| 稳定币增长但股东不赚钱 | 分销成本和竞争吃掉经济利益 | 收入增长不转化为 EPS/FCF |
| 利率下降 | 储备收益率下行 | reserve income 下滑，倍数压缩 |
| 平台叙事过度 | Arc/CPN 使用量增长但经济归属不清 | bull case 不能兑现 |
| 稀释过高 | SBC 持续大 | 每股价值增长弱于公司增长 |

- **Fragile assumptions**: USDC 能长期高 CAGR；RLDC margin 能稳定 38%–40%；other revenue 能成为第二增长曲线；Arc 能形成股东价值。
- **Psychological traps**: 监管利好叙事、AI 支付叙事、52 周高点锚定、把交易量当收入质量。
- **Decision implication**: 必须用季度数据反复证伪/验证，不应只买故事。
- **Follow-up question**: 如果三年后投资错误，今天最明显的红旗可能是：利润几乎全靠利率，而不是平台收费。

### Duan Yongping-style lens：Needs further observation

- **One-sentence business essence**: Circle 把美元变成链上可编程美元，并希望围绕它建立支付和金融基础设施。
- **User value**: 用户获得 24/7、全球化、链上可组合的美元结算；机构获得合规稳定币入口。
- **Product/brand strength**: USDC 有较强品牌和合规信任，但稳定币本身可替代，分销渠道很重要。
- **People/culture**: 管理层长期坚持合规路线，执行力较强；但资本市场需要看到平台业务和每股价值兑现。
- **Right price**: $35–45 更有明显安全边际；$45–55 可观察；$62.63 需要后续业绩验证。
- **Follow-up question**: 公司是在创造持久客户价值，还是主要货币化高利率、监管窗口和市场热度？

### Li Lu-style lens：Needs further observation

- **Circle of competence**: 稳定币发行、储备收益、分销成本和 SEC 财务可以研究；Arc/CPN 未来经济归属仍需要更多证据。
- **Industry trend**: 数字美元、代币化资产、跨境支付和 AI agent 支付可能是长期趋势。
- **Downside protection**: 公司层面净现金不错，但股价保护主要仍来自未来 earnings power；当前估值对熊市情景保护不足。
- **Margin of safety**: 当前不够明显。安全边际更依赖价格回落或平台收入验证。
- **Research-depth decision**: 值得继续深度跟踪，但暂不升级为高确定性核心仓位。
- **Follow-up question**: 10–20 年后，Circle 会是数字美元金融基础设施的持久节点，还是高利率和加密周期中的阶段性赢家？

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 7/10 |
| Financial quality | 6/10 |
| Valuation attractiveness | 5/10 |
| Long-term certainty | 5/10 |
| Downside risk control | 4/10 |

评分理由：

- **Business model 7**：稳定币发行和数字美元基础设施有真实需求，但收入过度依赖储备收益。
- **Moat 6**：合规品牌和网络有价值，但稳定币可替代，分销伙伴议价强。
- **Management 7**：管理层合规路线清晰、生态执行力强，但股东价值兑现仍待证明。
- **Financial quality 6**：adjusted EBITDA 和低资本开支有吸引力，但 SBC、利率敏感和分销成本降低质量。
- **Valuation attractiveness 5**：当前价格落入基准区间，但不是强安全边际。
- **Long-term certainty 5**：行业趋势好，但商业模式最终形态仍未完全确定。
- **Downside risk control 4**：熊市情景下行仍大，价格保护不足。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 有潜力，但当前利润引擎偏利率敏感 | 中 |
| Moat | 合规和网络有价值，但不等于强定价权 | 中 |
| Management/capital allocation | 执行力较强，需验证平台收入和每股价值 | 中 |
| Biggest risk | 利率下降 + 分销成本高 + 平台化不兑现 | 高 |
| Long-term trend | 数字美元和稳定币支付趋势值得跟踪 | 中高 |
| Valuation/margin of safety | 当前基准合理偏中性，强安全边际不足 | 中 |

### Action-framing

| Investor state | Research implication |
|---|---|
| No position | 不急于重仓；可等待 $45–55 或下一季数据验证；强安全边际偏 $35–45。 |
| Existing position | 继续跟踪 USDC 平均余额、RLDC margin、other revenue、SBC 和 Arc/CPN 经济归属。 |
| Add / upgrade signal | USDC 高增长、RLDC margin 稳定、other revenue 超指引、SBC 可控、Arc/CPN 收入归属清晰。 |
| Reduce / downgrade signal | RLDC margin 跌破指引、USDC 市占率弱化、利率下降导致 EPS 明显不达预期、分销成本恶化。 |

## 10. Final Research Framework

### 当前是否值得继续研究？

值得。CRCL 是少数能直接表达“受监管美元稳定币基础设施”主题的上市公司，行业位置稀缺，长期选项价值真实。

### 当前是否适合买？

以研究框架看，**当前 $62.63 不是明显高估泡沫，但也不是高安全边际买点**。我会把它归为：

- 可跟踪；
- 可小仓研究；
- 不适合把 bull case 当确定性重仓；
- 更理想的安全边际区间是 **$35–45**；
- **$45–55** 可开始更认真分批观察；
- 高于 **$80–90** 则需要非常强的 Arc/CPN/other revenue 证据支撑。

### Thesis depends on

1. USDC 继续增长且市占率稳定或提升；
2. RLDC margin 维持 38%–40% 或更高；
3. other revenue 超过 FY2026 $150–170M 指引并持续增长；
4. Arc/CPN/Agent Stack 形成 CRCL 股东可享有的收入或现金流；
5. SBC 和 diluted shares 不持续侵蚀每股价值；
6. 监管既提高门槛，又不显著破坏盈利模式。

### What would make the thesis stronger

- 连续两个季度 USDC 平均流通量高增；
- RLDC margin 稳定在 40% 附近；
- other revenue 增速明显高于 reserve income；
- CPN 交易量从 83 亿美元年化显著提升，且开始贡献收入；
- Arc 费用、代币和治理结构明确体现 CRCL 股东价值；
- SBC 占收入比例下降，摊薄股数可控。

### What would change my view

- **上调**：如果 USDC 增长、RLDC margin、other revenue 和平台化收入同时验证，且股价仍在基准区间或低于基准区间。
- **下调**：如果利率下降导致 reserve income 下滑，RLDC margin 跌破 38%，USDC 市占率下行，或 Arc/CPN 进展主要停留在叙事层面。
- **买入吸引力增强**：价格接近 **$45–55** 且基本面没有恶化；若跌到 **$35–45** 且 USDC/RLDC 仍健康，安全边际明显改善。
