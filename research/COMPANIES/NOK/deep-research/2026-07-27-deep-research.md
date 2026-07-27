# Nokia（NYSE: NOK）深度研究更新 - 2026-07-27

- **Research view**: Constructive but watchful（建设性但需继续验证）
- **Confidence**: B
- **Time horizon**: 12-36 个月
- **Main thesis**: Nokia 的 AI & Cloud / Optical / IP 网络订单在 Q2 2026 得到更强验证，基本面比 2026-06-04 旧报告更好；但 reported profit 和 FCF 仍弱，NOK 不是“干净的 AI 光互连高利润股”，而是“传统运营商设备商 + AI/cloud 网络基础设施转型 + Infinera 光网络整合 + AI-RAN 期权”的混合体。
- **Key risk**: Q2 AI & Cloud 订单强，但 FCF 为 -7.32 亿欧元、reported operating margin 为 -1.0%，说明重组、整合、营运资本和扩产仍在消耗现金；如果订单不能转成高毛利收入和 reported profit，估值会继续受压。

> 说明：本文是研究支持和决策框架，不构成个性化投资建议。NOK 是 Nokia Oyj 的美股 ADR；公司为芬兰 foreign private issuer，主要通过 Form 20-F 和 6-K 披露。本文主要来源：Nokia 2026-07-23 Form 6-K Q2/H1 2026 report、2026-03-05 FY2025 Form 20-F、SEC submissions JSON、StockAnalysis NOK quote/statistics/financials/forecast、Yahoo Finance chart API。市场数据存在供应商差异：StockAnalysis 显示 2026-07-27 抓取时 previous close $9.73；Yahoo chart API 显示最近 regularMarketPrice $9.10、previousClose $10.12。估值判断采用 $9-$10 区间而非单一价格点。

## 1. Executive View

**观点上调：从旧报告的“中性 / 等待确认”上调到“建设性但需继续验证”。**

上调原因不是估值突然便宜，而是 Q2 2026 的基本面确认明显强于 6 月报告时：

1. **AI & Cloud 订单显著增强。** Q2 AI & Cloud order intake 达 **28 亿欧元**，销售同比翻倍以上；管理层称约一半订单预计未来 12 个月转为收入。
2. **Network Infrastructure 兑现增长。** Q2 Network Infrastructure sales **20.37 亿欧元，同比增长 12%**；其中 Optical Networks **8.68 亿欧元，同比增长 19% / constant currency +20%**，IP Networks **6.79 亿欧元，同比增长 15% / constant currency +16%**。
3. **利润率改善体现在 comparable 层面。** Q2 comparable operating profit **4.34 亿欧元，同比增长 18%**，comparable operating margin **9.0%**，同比 +70 bps。
4. **但 reported 与 FCF 仍是硬伤。** Q2 reported operating loss **-5000 万欧元**，reported operating margin **-1.0%**；主要因 **3.90 亿欧元 restructuring charges**。Q2 FCF **-7.32 亿欧元**，net cash 环比减少 **10.12 亿欧元**至 **27.76 亿欧元**。

因此，NOK 已经不是纯粹“等待确认”的状态，AI/cloud 光网络订单和收入都在确认；但还没有达到“Positive”的程度，因为真正要验证的是：

> AI & Cloud 订单能否转成高毛利 Optical/IP revenue，再转成 reported operating profit 和 free cash flow。

最强反方理由：Nokia 当前价格从 6 月旧报告的 $16.73 大幅回落至约 $9-$10 区间，估值压力已有释放；若 Q2 的 28 亿欧元 AI & Cloud 订单持续，并在未来 12 个月顺利转收入，NOK 可能从传统通信设备估值切换到“AI networking infrastructure”估值框架。

最强谨慎理由：Q2 的 headline 很强，但 FCF 为负、reported margin 为负，说明 Nokia 的转型仍处在“订单强、会计利润/现金流未完全跟上”的阶段。

## 2. Business Model and Industry Structure

### 初学者版：Nokia 现在不是手机公司

Nokia 今天主要不是卖手机。它卖给电信运营商、云厂商、AI 数据中心、企业、政府和国防客户的是“网络连接基础设施”：

- 手机要连上 5G/未来 6G 基站，需要无线接入网设备；Nokia 卖 RAN、核心网软件和服务。
- AI 数据中心和云网络需要把服务器、GPU、机架、数据中心互相连接，需要光网络和 IP 网络；Nokia 卖 optical transport、coherent optics、routing 和 switching 相关产品。
- 固定宽带需要光纤接入设备；Nokia 卖固定网络产品。
- 通信标准需要专利授权；Nokia 拥有大量 4G/5G/未来 6G 标准必要专利，收取 license fees。

Nokia 的赚钱公式是：

> 网络设备/软件/服务/专利授权收入 − 硬件制造成本 − 研发费用 − 销售和服务交付成本 − 重组/整合成本 = 利润；再扣除营运资本、capex 和税后，才是股东真正拿到的 FCF。

核心经济问题：

> Nokia 能否把传统低增长、强竞争的运营商设备商，转型为 AI/cloud optical + IP networking 的高增长、高毛利、可持续 FCF 平台？

### 关键术语翻译

| 术语 | 通俗解释 |
|---|---|
| ADR | 美国存托凭证，让美国投资者用美元交易外国公司股票。NOK 是 Nokia Oyj 的 NYSE ADR。 |
| Optical Networks | 光网络，用光纤和相干光技术传输大量数据，是 AI 数据中心和骨干网的数据高速公路。 |
| Coherent optics | 相干光传输技术，可在长距离/高容量场景更高效地传输数据。Infinera 收购加强了这一块。 |
| IP Networks | 路由器/交换网络，决定数据包如何在互联网、云和数据中心间移动。 |
| AI & Cloud customers | 云厂商、AI 数据中心和相关客户，不是传统电信运营商。 |
| RAN | 无线接入网，手机连接基站的部分。 |
| AI-RAN | 把 AI 计算与无线基站/网络结合，让网络未来具备 AI 处理和优化能力。现在仍偏早期。 |
| Comparable operating profit | Nokia 非 IFRS 经营利润，剔除重组、收购摊销、交易和整合成本等。必须和 reported profit 对照。 |
| Discontinued operations | 已停止经营/拟出售业务，Nokia Q2 将 Fixed Wireless Access CPE 和 Enterprise Campus Edge 列为 discontinued operations。 |

## 3. Segment and Product Analysis

### Q2 2026 segment snapshot

| Segment | Q2 2026 net sales | YoY | Comparable operating profit | Margin | 判断 |
|---|---:|---:|---:|---:|---|
| Network Infrastructure | **€2.037B** | **+12%** | **€166M** | **8.1%** | AI/cloud 光网络和 IP 网络主线 |
| Mobile Infrastructure | **€2.680B** | **+6%** | **€310M** | **11.6%** | 大盘稳定，但不是高增长核心 |
| Portfolio Businesses | **€94M** | **+6%** | **€0M** | **0.0%** | 逐步清理/缩小拖累 |

### Network Infrastructure：重估核心

Q2 Network Infrastructure sales **€2.037B**，同比 **+12%**。拆分：

| 子业务 | Q2 2026 sales | YoY | Constant currency YoY | 评价 |
|---|---:|---:|---:|---|
| Optical Networks | **€868M** | **+19%** | **+20%** | AI/cloud 与运营商共同推动，最关键 |
| IP Networks | **€679M** | **+15%** | **+16%** | Q1 design wins 开始转化，AI/cloud 强 |
| Fixed Networks | **€490M** | **-3%** | **-2%** | 消费端 CPE/低毛利产品收缩，偏拖累 |

投资判断：Network Infrastructure 正在从传统运营商网络设备，转向 AI data center transport / optical / routing 受益方向。Q2 的订单和收入都支持这一点。

关键新增事项：Nokia 继续扩张美国光组件制造能力：

- San Jose Fab 预计 2026 Q4 开始 ramp production。
- Pennsylvania advanced test and packaging capacity 从 2026 Q3 开始扩大 **10x**。
- 与 NXP 签署协议，未来收购 Arizona Chandler Semiconductor Fabrication campus，计划从 2027 年初先租用部分产能，并转换为 Indium Phosphide optical components 生产；完整交易预计 2029 Q1 完成。

这意味着 Nokia 正把 Infinera/光网络能力垂直整合为美国本土光组件供应链。利好是供应链安全和 AI optical capacity；风险是 capex、良率、折旧和周期错配。

### Mobile Infrastructure：稳定大盘 + AI-RAN 期权

Q2 Mobile Infrastructure sales **€2.680B**，同比 **+6% / constant currency +7%**；operating profit **€310M**，margin **11.6%**。

这块包括：

- Radio Networks：基站无线设备。
- Core Software：核心网软件。
- Technology Standards：专利和标准相关高利润收入。

Mobile Infrastructure 的重要性在于：它仍是 Nokia 最大收入块，而且 Q2 利润贡献稳定。AI-RAN 是中长期选择权，但不能把它当成已成熟业务。Q2 CEO 提到 Nokia 推出行业首个 commercial AI-RAN platform，目标到 2028 年帮助客户实现 **100%+ spectral efficiency gains**，并提供从 5G 软件升级到 6G 的路径。这是长期技术叙事，不应短期按成熟利润池估值。

### Portfolio Businesses / discontinued operations

Q2 Nokia 将 Fixed Wireless Access CPE 和 Enterprise Campus Edge 从 Portfolio Businesses 转入 discontinued operations：

- Fixed Wireless Access CPE 已达成出售给 Inseego 的协议。
- Enterprise Campus Edge 被认为高度可能出售。
- 若未列为 discontinued operations，Q2 net sales 会高 **€66M**，comparable operating profit 会低 **€13M**。

这对 thesis 是小幅正面：Nokia 正在清理非核心/低利润业务，让报表更聚焦 AI/cloud、Network Infrastructure 和 Mobile Infrastructure。

## 4. Financial Deep Dive

### Q2 2026 headline results

| 指标 | Q2 2026 | Q2 2025 | 变化 |
|---|---:|---:|---:|
| Reported net sales | **€4.815B** | €4.443B | **+8%** |
| Constant currency net sales growth | **+9%** | - | - |
| Reported gross margin | **44.6%** | 44.0% | +60 bps |
| Reported operating profit/loss | **-€50M** | €147M | 转负 |
| Reported operating margin | **-1.0%** | 3.3% | -430 bps |
| Comparable operating profit | **€434M** | €367M | **+18%** |
| Comparable operating margin | **9.0%** | 8.3% | +70 bps |
| Comparable EPS | **€0.07** | €0.04 | +75% |
| Reported diluted EPS | **€0.00** | €0.02 | -100% |

结论：**经营 momentum 好于 6 月报告，但利润质量仍不干净。** Comparable 指标强，reported 指标弱；二者差异主要来自重组和收购相关项目。

Q2 reported vs comparable 差异：

- Restructuring and associated charges：**€390M**。
- Amortization/depreciation of acquired intangibles/PPE：**€46M**。
- Impairment/write-off net：**€30M**。
- Infinera integration related costs：**€14M**。

### H1 2026

| 指标 | H1 2026 | H1 2025 | 变化 |
|---|---:|---:|---:|
| Reported net sales | **€9.248B** | €8.743B | **+6%** |
| Comparable net sales | **€9.251B** | €8.748B | **+6%** |
| Constant currency/portfolio growth | **+7%** | - | - |
| Comparable operating profit | **€735M** | €576M | **+28%** |
| Comparable operating margin | **7.9%** | 6.6% | +130 bps |
| Comparable EPS | **€0.13** | €0.08 | +63% |

H1 支持“业务正在改善”的判断，但 H1 comparable operating profit **€735M** 相对于全年 **€2.1-2.6B** 指引，意味着下半年仍要显著加速。管理层称仍有 momentum，并预计全年达到略高于 guidance midpoint。

### 现金流和资产负债表

| 指标 | Q2 2026 |
|---|---:|
| Total cash and interest-bearing financial investments | **€5.176B** |
| Net cash and interest-bearing financial investments | **€2.776B** |
| QoQ net cash change | **-€1.012B** |
| Q2 free cash flow | **-€732M** |
| Q2 capex | 约 **€130M** |
| Q2 working capital cash outflow | 约 **€1.15B** |

Q2 FCF 为负的主要原因：

- receivables 增加约 **€280M**；
- inventories 增加约 **€370M**；
- liabilities 减少约 **€330M**；
- restructuring cash outflow 约 **€170M**；
- cash taxes 约 **€140M**。

判断：这不是破产式现金流恶化，但它提醒我们：AI/cloud 订单增长会带来库存、应收、供应链投入和产能建设。投资人不能只看订单，要看订单是否能转成现金。

### Outlook

Nokia Q2 披露：

- Operationally full-year outlook unchanged。
- 因 discontinued operations presentation，comparable operating profit range 技术性从 **€2.0-2.5B** 调整为 **€2.1-2.6B**。
- Outlook 基于 EUR/USD **1.14**。
- CEO 称仍 on track to deliver somewhat above midpoint of comparable operating profit guidance。

关键：这不是实质上调，而是会计呈现变化导致的技术性调整。基本面语气更强，但正式经营目标未上调。

## 5. Management and Capital Allocation

新 CEO Justin Hotard 的战略方向很清楚：把 Nokia 定位为 **connectivity for the AI era**。

正面：

- Q2 AI & Cloud order intake **€2.8B**，并称约一半未来 12 个月转收入。
- Optical/IP long-term orders broad-based。
- 启动 AI-RAN commercial platform。
- 清理 discontinued businesses，提高战略聚焦。
- 扩大美国 optical component manufacturing capacity，支持 2027-2028 需求。

负面/待验证：

- 加速 restructuring 导致 Q2 reported operating loss。
- Infinera 整合仍带来摊销、整合费用和执行风险。
- Q2 FCF 大幅为负，说明增长不是“轻资产无痛增长”。
- 管理层薪酬使用 comparable operating profit，投资者应防止 management narrative 过度依赖非 IFRS 指标。

## 6. Valuation Work

### 当前估值快照

StockAnalysis 2026-07-27 抓取：

| 指标 | 数值 |
|---|---:|
| Previous close | **$9.73** |
| Market cap | **$52.41B** |
| Enterprise value | **$50.50B** |
| Shares outstanding | **5.60B** |
| TTM revenue | **$23.30B** |
| TTM net income | **$808.87M** |
| TTM EPS | **$0.14** |
| PE | **64.79x** |
| Forward PE | **21.67x** |
| PS | **2.25x** |
| EV/Sales | **2.17x** |
| EV/EBITDA | **24.92x** |
| P/FCF | **86.10x** |
| EV/FCF | **82.97x** |
| Net cash | **$2.02B** |
| Dividend yield | **1.21%** |
| Beta | **0.79** |
| Analyst target | **$15.10** |

Yahoo chart API 同期显示 regularMarketPrice **$9.10**，最近 close 序列包含 $10.08、$10.63、$10.28、$9.73、$9.10。由于不同来源口径不同，本文估值区间采用 $9-$10。

### 与 2026-06-04 旧报告相比

旧报告引用 2026-06-03 StockAnalysis：NOK close **$16.73**、market cap **$96.39B**、EV **$93.59B**。当前 StockAnalysis 显示 market cap **$52.41B**、EV **$50.50B**。这可能反映股价大幅回撤与供应商口径更新/股本口径修正共同影响。无论原因，当前可交易价格约 $9-$10，估值压力明显低于旧报告。

### 为什么仍不能只看 forward P/E

Forward PE **21.67x** 看起来不贵，但 trailing reported EPS 只有 **$0.14**，P/FCF 仍高达 **86x**。这说明市场买的是 2026-2028 年 comparable operating profit / AI orders / margin expansion，而不是现在已经兑现的现金流。

### Scenario valuation

使用 $2.02B net cash、约 5.60B shares，按 normalized EBIT multiple 和 EPS multiple 交叉验证：

| Scenario | Assumptions | Implied value zone |
|---|---|---:|
| Bear | Revenue ~$20B；reported margin 修复慢；AI orders 转化低于预期；15x EBIT 或 EPS $0.30 × 16x | **$4.8-$4.4** |
| Base low | Revenue ~$22.5B；normalized EBIT margin 10%；17x EBIT；EPS $0.42 × 19x | **$7.2-$8.0** |
| Base high | Revenue ~$24B；normalized EBIT margin 11.5%；19x EBIT；EPS $0.50 × 22x | **$9.7-$11.0** |
| Bull low | Revenue ~$26B；AI/cloud 光网络持续强；13% EBIT margin；22x EBIT；EPS $0.62 × 25x | **$13.6-$15.5** |
| Bull high | Revenue ~$28B；Optical/IP 成为 AI 网络核心平台；15% EBIT margin；25x EBIT；EPS $0.75 × 28x | **$19-$21** |

当前 $9-$10 大致位于 **base high 区间**，不再像 6 月 $16.73 那样明显贴近 bull case。也就是说：

- $16-$17：需要 bull case 兑现，不宜追；
- $9-$10：估值回到“基本面改善能解释，但仍需确认 FCF”的区间；
- <$8：如果 Q3 订单和 FCF 未恶化，开始有更明显安全边际；
- <$6：强安全边际候选，但需排除 AI order 反转或 reported profit 无法修复。

### 实用价格区间

| Price zone | 判断 |
|---|---|
| **<$6** | 强安全边际候选区，前提是 AI/cloud order 和 net cash 未恶化。 |
| **$6-$8** | 可积极研究 / 小仓分批区。 |
| **$8-$11** | 当前附近；合理观察区，适合等待 Q3/FCF 确认。 |
| **$11-$15** | 需要 Q3/Q4 order conversion 和 margin/FCF 改善。 |
| **$15-$20** | Bull case 区，必须看到 AI & Cloud 持续订单、reported profit 修复、FCF 转正。 |
| **>$20** | 高预期区，不适合证据不足时追价。 |

## 7. Catalysts and Monitoring Plan

未来 3-6 个月最重要：

1. Q3 2026 AI & Cloud order intake 是否继续强。
2. Q2 €2.8B orders 中约一半未来 12 个月转收入的兑现节奏。
3. Optical Networks 是否继续接近/超过 20% 增长。
4. IP Networks Q1 design wins 是否持续转 revenue。
5. Reported vs comparable operating profit 差距是否收窄。
6. FCF 是否从 Q2 -€732M 修复。
7. Inventory/receivables 是否回落，还是增长继续吞现金。
8. Infinera integration cost、synergy 和 customer wins。
9. San Jose Fab、Pennsylvania 10x packaging/test、Arizona InP fab 计划是否按时。
10. AI-RAN 是否有真实客户 deployment，而非仅 field trial / platform launch。
11. 2026 comparable operating profit guidance 是否实质上调。
12. Mobile Infrastructure 是否维持收入和 margin。
13. Technology Standards license renewal 和专利收入稳定性。

## 8. Risk Register

| 风险 | 概率 | 严重度 | 说明 |
|---|---|---|---|
| FCF 不转正 | 中高 | 高 | Q2 FCF -€732M，增长占用营运资本。 |
| Reported profit 长期弱于 comparable | 高 | 中高 | 重组、摊销、整合成本仍大。 |
| AI & Cloud 订单一次性 | 中 | 高 | Q2 €2.8B 很强，但需连续季度验证。 |
| Optical/IP supply constraint | 中 | 中高 | 供应是行业约束，扩产失败会限制收入兑现。 |
| Infinera 整合风险 | 中 | 中 | 产品、客户、费用、摊销、文化整合。 |
| Mobile/RAN 周期 | 中 | 中 | 运营商 capex 仍周期性，AI-RAN 尚早。 |
| 竞争 | 高 | 中高 | Ciena、Cisco/Acacia、Arista、Huawei、Ericsson、Samsung 等。 |
| 汇率 | 中 | 中 | 欧元报表、美元 ADR、全球收入。 |
| 股本/ADR 数据口径 | 中 | 中 | 供应商市值和价格口径需持续核对。 |

最强反证：AI & Cloud orders 不只是 headline，管理层明确称 strength broad-based、long-term orders in both Optical Networks and IP Networks，且约一半 12 个月内转收入；如果 Q3/Q4 继续验证，NOK 的估值框架确实应高于传统通信设备商。

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: A。Nokia 披露充分，但 ADR/欧元/美元/IFRS/non-IFRS 口径复杂。
- **Main research blind spot**: AI & Cloud 订单的毛利率、客户集中、取消条款、具体客户和长期 pricing 未完全披露。
- **Strongest reason smart investors may disagree**: 多头会认为 Q2 €2.8B AI & Cloud orders 已经证明 Nokia 从低增长 telco equipment 转为 AI networking infrastructure。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: Nokia 是否已变成可长期预测、现金流稳定的高质量网络基础设施公司？
- **Evidence supporting**: 净现金 €2.776B；Q2 comparable operating profit +18%；Network Infrastructure +12%；AI & Cloud orders €2.8B。
- **Evidence against**: Q2 reported operating loss、FCF -€732M、传统运营商设备竞争激烈、reported/comparable 差距大。
- **Decision implication**: $9-$10 可以研究，但还不是 Buffett-style “高确定性现金牛”。
- **Follow-up question**: 如果股市关闭五年，Nokia 的 AI/cloud order book 是否足够让投资者忽略短期 reported loss 和 FCF 波动？

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个投资最容易哪里看错？

| Failure path | Mechanism | Consequence |
|---|---|---|
| 把 orders 当利润 | 订单转收入、收入转毛利、毛利转现金之间有多道风险 | 股价先涨后跌 |
| 忽略 restructuring | comparable 好看，reported 和 cash 弱 | 盈利质量被高估 |
| 过度外推 AI-RAN | 平台发布不等于大规模商业收入 | TAM 幻觉 |
| 低估竞争 | 光网络/IP/RAN 都有强竞争者 | margin 被压缩 |
| 忽略营运资本 | AI 订单需要库存和应收投入 | FCF 低于预期 |

- **Major stupidity risk**: 看到“AI & Cloud +105% / €2.8B orders”就按 AI 纯成长股估值，而不检查 FCF 和 reported profit。
- **Follow-up question**: 如果三年后错了，今天最明显红旗可能是 Q2 FCF -€732M 和 reported margin -1.0%。

### Duan Yongping-style lens

- **Conclusion**: Needs further observation。
- **Business essence**: Nokia 帮运营商、云厂商和企业构建可靠的移动、固定、光和 IP 网络。
- **User value**: 客户需要高速、低延迟、安全、可扩展网络；AI 数据中心尤其需要光网络和 IP routing。
- **Product/brand strength**: 通信标准、运营商关系和 optical/IP 产品组合强；Infinera 增强相干光能力。
- **People/culture**: 新 CEO 聚焦 AI supercycle，执行初期有效，但仍需证明 reported profit/FCF。
- **Right price**: $6-$8 更舒服；$8-$11 合理观察；$15+ 需要 bull case。
- **Follow-up question**: Nokia 是在创造可持续客户价值，还是主要利用 AI capex 周期窗口重新包装传统设备业务？

### Li Lu-style lens

- **Conclusion**: Needs further observation / selective watchlist。
- **Circle of competence**: 网络设备和财务数据可研究；AI-RAN 商业化、客户真实订单条款和未来光组件供应链需要更深行业调研。
- **Industry trend**: AI 数据中心、光网络、6G、企业/国防安全网络都是长期趋势。
- **Value-chain position**: Nokia 处在 connectivity layer，不是 GPU/模型层，但 AI infrastructure 缺不了高速网络。
- **Downside protection**: 净现金提供一定防守；但 FCF 和 reported earnings 仍弱。
- **Margin of safety**: $9-$10 比旧报告 $16.73 明显改善，但强安全边际仍要等 <$8 或 FCF 修复。
- **Follow-up question**: 10-20 年后 Nokia 会是 AI 时代连接层的持久节点，还是传统通信设备周期里暂时受益者？

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 7/10 |
| Financial quality | 5/10 |
| Valuation attractiveness | 6/10 |
| Long-term certainty | 6/10 |
| Downside risk control | 6/10 |

评分解释：业务方向改善明显，但仍是竞争激烈、资本/研发密集的设备商；净现金有防守，估值从 6 月高位改善，但 FCF/reporting quality 仍是扣分项。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | AI/cloud 光网络改善真实，但传统设备属性仍在 | B |
| Moat | 专利、运营商关系、光网络/IP 组合有壁垒，但竞争强 | B- |
| Management | 新 CEO 执行和战略聚焦初步有效 | B |
| Biggest risk | Orders 不转 FCF / reported profit | A- |
| Long-term trend | AI networking、optical transport、AI-RAN 长期趋势正面 | B |
| Valuation | $9-$10 合理但不极便宜；<$8 更有安全边际 | B |

| Investor state | Research implication |
|---|---|
| No position | 可以进入 watchlist；不急于重仓，等 Q3 或 <$8 更好。 |
| Existing position | 可继续持有观察；重点看 Q3 order conversion 和 FCF 修复。 |
| Add / upgrade signal | AI & Cloud orders 连续强、reported/comparable gap 收窄、FCF 转正、guidance 实质上调。 |
| Reduce / downgrade signal | Q3 orders 回落、库存/应收继续吞现金、reported loss 延续、Optical margin 不升反降。 |

## 10. Final Research Framework

### What the thesis depends on

- Q2 €2.8B AI & Cloud orders 是否在未来 12 个月如管理层预期约一半转收入。
- Optical Networks 是否持续 20% 左右增长。
- IP Networks 是否持续将 design wins 转化为收入。
- Comparable operating margin 是否继续扩张。
- Reported operating profit 是否从 Q2 loss 修复。
- FCF 是否从 Q2 -€732M 修复。
- Infinera 整合是否带来协同而非持续费用。
- 美国 optical manufacturing 扩产是否按时、低风险、能支撑 2027-2028 需求。

### What would make the thesis stronger

- Q3 AI & Cloud orders 继续强，且 backlog/order conversion 明确。
- Reported operating margin 转正并向 comparable 收敛。
- FCF 转正，库存和应收压力下降。
- 管理层实质上调 2026 comparable operating profit，而不仅是会计呈现调整。
- Optical/IP margins 扩张且竞争未恶化。
- 股价回到 $8 以下但基本面未破坏。

### What would change my view

- **上调至 Positive**：Q3/Q4 AI & Cloud orders 和 revenue 继续强，reported profit 修复，FCF 明显转正，2026/2027 指引上调，且股价仍处 $8-$11 或更低。
- **维持 Constructive but watchful**：订单强、comparable 好，但 FCF/reporting quality 仍未完全验证。
- **下调至 Neutral/Negative**：Q3 订单显著回落，Q2 订单转收入慢于预期，reported loss 延续，FCF 继续大幅为负，或扩产/整合成本超预期。

## Sources

- Nokia Form 6-K filed 2026-07-23: Nokia Corporation Report for Q2 and Half Year 2026.
- Nokia FY2025 Form 20-F filed 2026-03-05.
- SEC submissions JSON, CIK `0000924613`.
- StockAnalysis NOK quote/statistics/financials/forecast pages, accessed 2026-07-27.
- Yahoo Finance chart API for NOK, accessed 2026-07-27.
- Prior repository memos: `deep-research/2026-05-28-deep-research.md`, `deep-research/2026-06-04-deep-research.md`.
