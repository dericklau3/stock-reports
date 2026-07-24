# Intel（NASDAQ: INTC）深度研究报告

- **Research view**: Neutral / wait for confirmation（中性 / 等待确认）
- **Confidence**: B。Intel 披露充分、最新 Q2 2026 8-K 与 Q1 10-Q/FY2025 10-K 可核验；但公司正处于产品、制程、晶圆代工、政府股权、资本结构和重组多重转型期，未来回报高度依赖外部客户、Intel 14A、18A/P、AI 需求和资本开支纪律。
- **Time horizon**: 12-36 个月
- **Main thesis**: Intel Q2 2026 证明业务收入和非 GAAP 利润明显恢复，DCAI、CCPG、Foundry 都有增长；但当前股价约 $102.62、市值约 $504B、EV/TTM sales 约 9.6x、P/2026E non-GAAP EPS 约 92x，已经从“困境反转”重估成“AI + 美国本土先进制造 + Foundry 成功”股票。研究上值得跟踪，但不是安全边际充分的低估半导体。
- **Key risk**: Foundry/14A/先进封装和 AI 需求若不能转化为外部客户、高利用率、持续正 FCF 和较低稀释，当前估值可能回落；GAAP 利润、政府股权/escrow shares、partner contributions、债务和 adjusted FCF 都需要持续核验。

> 说明：本文是研究支持与决策框架，不构成个性化投资建议。关键事实来源包括 Intel 2026-07-23 Form 8-K Exhibit 99.1《Intel Reports Second-Quarter 2026 Financial Results》、2026-04-24 Q1 10-Q、2026-01-23 FY2025 10-K、StockAnalysis INTC 页面。市场数据为 2026-07-24 抓取时的点时快照。

## 1. Executive View

**研究观点：中性 / 等待确认。**

Intel 已经不是 2022-2024 年市场眼中的单纯 PC/服务器份额流失老牌芯片公司。2026 Q2 数据显示，公司产品业务和制造业务都有明显改善：收入同比 +25%，DCAI 收入同比 +59%，Intel Foundry 收入同比 +31%，非 GAAP EPS 从去年同期 -$0.10 改善到 $0.42。新的 CEO Lip-Bu Tan 把叙事集中在 AI compute、CPU franchise、ASIC、advanced packaging 和 wafer foundry network。

但投资难点是：**股价已经先涨很多。** StockAnalysis 显示 INTC previous close 为 **$102.62**，52 周区间 **$18.97-$142.35**，market cap **$503.76B**，enterprise value **$515.68B**，TTM revenue **$53.76B**，TTM net income **-$3.17B**，forward PE **94.28x**。这意味着市场已经把 Intel 从“价值/困境反转”重新定价为“AI + foundry + 美国战略资产”。

核心 thesis：

1. **基本面确实在恢复。** Q2 2026 revenue $16.1B，同比增长 25%，是公司披露口径下 15 年以来最强收入增长；non-GAAP operating margin 17.2%，non-GAAP EPS $0.42。
2. **AI 和数据中心给了反转弹性。** DCAI Q2 revenue $6.3B，同比增长 59%；Intel 推进 Xeon 6+、agentic AI infrastructure、SambaNova/Foxconn/VC2 等合作，说明不只是 PC 修复。
3. **Foundry 是最大变量。** Intel Foundry Q2 revenue $5.8B，同比增长 31%，但 segment operating loss 仍为 **-$2.089B**；18A/18A-P 进展是正面，14A 外部客户和资本回报仍未完全证明。

最强反方理由：如果 Intel 14A、18A-P、advanced packaging、ASIC 和外部 foundry 客户兑现，且美国政府/NVIDIA/SoftBank 等战略资本降低融资风险，那么 Intel 可能从低质量周期股重估为美国先进制程和 AI 供应链核心平台。但当前价格已经反映较高概率成功，投资者需要避免把“国家战略重要性”等同于“普通股安全边际”。

## 2. Business Model and Industry Structure

### 初学者版：Intel 到底怎么赚钱

Intel 卖的是芯片和制造能力。

简单讲，一台电脑、服务器或 AI 系统需要“中央处理器 CPU”和各种配套芯片来执行指令。Intel 传统上最强的是 x86 CPU：个人电脑里的 Core、服务器里的 Xeon。客户通常是 PC 厂商、服务器厂商、云厂商、企业和渠道商。

Intel 的特别之处是：它不只是设计芯片，还自己建晶圆厂制造芯片。这和 NVIDIA、AMD、Broadcom 这类大部分依赖 TSMC 制造的 fabless 公司不同。

Intel 现在有两个经济引擎：

1. **产品业务**：设计和销售 CPU、AI PC、server CPU、网络/边缘/ASIC 等产品。赚钱方式类似“卖高性能芯片，毛利扣掉研发和销售费用后形成利润”。
2. **Foundry / 制造业务**：用自己的晶圆厂、封装和制程能力为 Intel 内部产品和外部客户制造芯片。赚钱方式类似“高固定成本工厂出租产能”，只有产能利用率高、良率好、客户量足、价格合理时才会赚钱。

核心经济问题：

> Intel 能否让先进晶圆厂不再只是高 capex 负担，而变成高利用率、高良率、有外部客户的现金流资产？

### 关键术语翻译

| 术语 | 通俗解释 |
|---|---|
| CPU | 中央处理器，是电脑/服务器执行通用计算任务的主芯片。 |
| x86 | Intel 和 AMD 长期主导的 CPU 指令集生态，软件兼容性和企业生态很强。 |
| DCAI | Data Center and AI，数据中心和 AI 芯片/平台业务，包括服务器 CPU、AI/加速和相关平台。 |
| Foundry | 晶圆代工/制造服务，为内部和外部客户制造芯片。TSMC 是最成功的 foundry 代表。 |
| Process node | 制程节点，如 Intel 18A、14A，代表芯片制造工艺代际；越先进通常性能/功耗更好，但研发和建厂成本极高。 |
| EUV / High-NA EUV | 极紫外光刻技术，用于制造先进芯片；High-NA 是更先进、更昂贵的 EUV 设备。 |
| Advanced packaging | 先进封装，把多个芯片/小芯片高速连接在一起，是 AI 芯片性能和良率的重要环节。 |
| ASIC | 为特定客户/用途定制的芯片，例如云厂商自研 AI 或网络芯片。 |
| FCF | 自由现金流，经营现金流减资本开支等；对 Intel 这种重资本公司尤其关键。 |
| Escrowed Shares | Intel 为美国政府相关协议预留/托管的股份，按条件释放；股价变动会带来 mark-to-market 会计损益。 |

### 行业结构

Intel 面对三类竞争：

| 业务 | 主要竞争者 | Intel 优势 | Intel 短板 |
|---|---|---|---|
| PC CPU / AI PC | AMD、Apple、Qualcomm、Arm 生态 | x86 生态、OEM 渠道、企业兼容性、品牌 | 制程领先性曾落后，PC 周期波动，Apple/Arm 压力 |
| Data center CPU / AI | AMD EPYC、NVIDIA Grace/Blackwell、Arm 云芯片、Broadcom/Marvell ASIC | Xeon 生态、企业软件兼容、平台经验、封装/制造协同 | AI 加速器主导权弱于 NVIDIA，云客户自研 ASIC 压力 |
| Foundry | TSMC、Samsung Foundry、GlobalFoundries、先进封装供应链 | 美国本土先进制造、政府支持、18A/14A 路线图、先进封装 | 外部客户信任仍需证明，高固定成本、良率/交付风险 |

公司类型判断：Intel 是 **资本密集型半导体转型公司**，不是纯 fabless AI 芯片公司，也不是稳定成熟现金牛。估值应同时看 revenue growth、segment margin、EV/Sales、non-GAAP EPS、GAAP/非 GAAP差异、现金流、债务、capex、政府/伙伴资本和稀释。

## 3. Segment and Product Analysis

### Segment overview：Q2 2026

| Segment | Q2 2026 revenue | YoY | Q2 2026 operating income/loss | 评价 |
|---|---:|---:|---:|---|
| CCPG | **$8.877B** | **+13%** | **$2.343B** | PC/AI PC 恢复，是当前利润底座之一 |
| DCAI | **$6.262B** | **+59%** | **$2.474B** | 最大亮点，AI-driven compute 需求强 |
| Total Intel Products | **$15.139B** | **+28%** | **$4.817B** | 产品业务利润质量明显改善 |
| Intel Foundry | **$5.765B** | **+31%** | **-$2.089B** | 收入增长但仍严重亏损，是最大执行变量 |
| All Other | **$701M** | **-33%** | **$230M** | 包括 Mobileye、IMS、历史 Altera 等影响 |
| Intersegment eliminations | **-$5.477B** | - | **$254M** | 内部制造交易抵消 |
| Total consolidated | **$16.128B** | **+25%** | **$1.796B GAAP op income** | 整体恢复明显 |

### CCPG：Client Computing and Physical AI Group

白话解释：这部分主要卖 PC、AI PC、工作站、边缘设备芯片。客户买 Intel 芯片，是为了生产笔记本、台式机、工业/机器人/边缘 AI 设备。

Q2 数据显示 CCPG revenue **$8.9B**，同比 **+13%**，operating income **$2.343B**，利润率约 **26.4%**。这说明 Intel 的 PC/客户端业务仍有强现金流价值，尤其 Windows 10 结束支持、AI PC 更新周期和企业设备刷新可能提供支撑。

风险是 PC 行业周期性强，AI PC 不等于高毛利软件收入；如果 AI PC 只是硬件升级而没有定价能力，长期估值不应给过高倍数。

### DCAI：Data Center and AI

白话解释：这部分卖服务器 CPU、AI 数据中心相关产品和平台。云厂商、企业数据中心、AI 基础设施公司买这些芯片，用来跑数据库、虚拟化、推理、AI agent 和通用计算。

Q2 DCAI revenue **$6.3B**，同比 **+59%**，operating income **$2.474B**，利润率约 **39.5%**。这是 Q2 最大亮点。

业务亮点包括：

- Intel 推进 agentic AI infrastructure。
- 与 SambaNova、Foxconn 展示 rack-scale inference/agentic workloads infrastructure。
- VC2 展示结合 Intel Xeon、SambaNova RDUs 和 NVIDIA Blackwell GPUs 的 disaggregated agentic cloud。
- Intel launched Xeon 6+，其称为首款使用 Intel 18A 的 server class product。
- Ethernet E835 portfolio 覆盖 10GbE 到 200GbE。

判断：DCAI 是 Intel 反转最重要的利润引擎。如果 DCAI 能维持高增长和高利润率，Intel 可以获得 AI infrastructure 重估；但 Intel 在 AI accelerator/GPU 主导权上仍弱于 NVIDIA，custom silicon 与云客户自研趋势也可能压缩长期议价能力。

### Intel Foundry

白话解释：Intel Foundry 是 Intel 的制造/代工部门，给自己产品和外部客户造芯片。这个业务像重资产工厂：建厂和买设备要先花巨额资金，只有订单足够、良率够高、客户愿意长期使用，才能摊薄固定成本并赚钱。

Q2 Foundry revenue **$5.765B**，同比 **+31%**，但 operating loss **-$2.089B**。这说明收入增长并不等于经济模型已经成立。

正面进展：

- Intel 18A-P entered risk production，按公司说法符合此前给客户/伙伴的时间线。
- Intel Foundry has entered high-volume manufacturing for a subset of Core Ultra Series 3 / Panther Lake using ASML EXE High NA EUV technology。
- 与 Fortinet 合作开发 Fortinet Security Processor 6，使用 Intel design、packaging 和 manufacturing capabilities。
- Intel 宣布 **€5B** 投资扩大 Xeon 6 和下一代 Xeon 产能。
- Bowers campus capacity 扩张，支持 mask operations 和领先制程开发/制造。

核心风险：Intel 在 10-K/Q1 10-Q 中明确提示，如果无法为 Intel 14A 通过外部大客户和内部产品 roadmap 获得足够 committed demand，可能 pause or discontinue Intel 14A 和后续领先节点/制造扩张项目。这是非常重大的反身性风险：如果 14A 没有客户，Intel Foundry 的长期 bull case 会受损；如果 14A 客户成功，则当前估值才可能被证明合理。

## 4. Financial Deep Dive

### Q2 2026 财务结果

| 指标 | Q2 2026 | Q2 2025 | YoY |
|---|---:|---:|---:|
| Revenue | **$16.1B** | $12.9B | **+25%** |
| GAAP gross margin | **40.4%** | 27.5% | +12.9 ppts |
| Non-GAAP gross margin | **41.8%** | 29.7% | +12.1 ppts |
| GAAP R&D + MG&A | **$4.5B** | $4.8B | -6% |
| Non-GAAP R&D + MG&A | **$4.0B** | $4.3B | -8% |
| GAAP operating margin | **11.1%** | -24.7% | +35.8 ppts |
| Non-GAAP operating margin | **17.2%** | -3.9% | +21.1 ppts |
| GAAP net income attributable to Intel | **-$11.0B** | -$2.9B | n/m |
| Non-GAAP net income attributable to Intel | **$2.197B** | -$441M | n/m |
| GAAP diluted EPS | **-$2.16** | -$0.67 | n/m |
| Non-GAAP diluted EPS | **$0.42** | -$0.10 | n/m |
| Operating cash flow | **$7.006B** | $2.050B | 明显改善 |
| Adjusted FCF | **-$8.419B** | -$1.050B | 明显恶化 |

### 为什么 GAAP 和 non-GAAP 差异这么大

Q2 GAAP net loss attributable to Intel 为 **-$11.033B**，但 non-GAAP net income 为 **$2.197B**。最大差异来自：

| 调整项 | Q2 2026 对 net income 的影响 |
|---|---:|
| Gains/losses on mark-to-market of Escrowed Shares | **$12.529B** |
| Share-based compensation | $687M |
| Restructuring and other charges | $170M |
| Acquisition-related adjustments | $117M |
| Income tax effects | -$271M |
| Adjustments attributable to non-controlling interest | -$42M |

重点：Escrowed Shares mark-to-market 是美国政府相关协议下托管股份的公允价值变动，会导致 GAAP 损益剧烈波动。它不是核心产品经营利润，但它是真实资本结构复杂性的体现。投资上不能只看 GAAP，也不能只看 non-GAAP；应把二者分开：

- 产品/经营层面：Q2 明显改善；
- 普通股股东层面：政府股权、托管股份、稀释和公允价值损益使每股价值更复杂。

### 现金流与资本开支

Q2：

- GAAP OCF：**$7.006B**。
- Gross capital expenditures：**-$2.652B**。
- Government incentives proceeds：**$60M**。
- Partner contributions, net：**-$12.216B**。
- Finance lease payments：**-$617M**。
- Adjusted FCF：**-$8.419B**。

上半年：

- OCF：**$8.102B**。
- Additions to PP&E：**-$6.192B**。
- Proceeds from capital-related government incentives：**$167M**。
- Term debt issued：**$13.0B**，term debt repaid **$9.0B**。
- Partner contributions：**$4.082B**，partner distributions **-$14.339B**。

结论：Intel 短期经营现金流改善，但资本结构和 partner/SCIP 现金流复杂，adjusted FCF 仍是弱点。对重资本公司来说，**收入增长必须最终转化为持续正 FCF**，否则高估值难以支撑。

### 资产负债表

截至 2026-06-27：

| 项目 | 数值 |
|---|---:|
| Cash and equivalents | **$12.874B** |
| Short-term investments | **$16.853B** |
| Cash + short-term investments | **$29.727B** |
| Current assets | **$57.213B** |
| PP&E net | **$105.741B** |
| Goodwill | **$20.465B** |
| Total assets | **$202.439B** |
| Short-term debt | **$1.988B** |
| Debt | **$48.549B** |
| Total Intel stockholders' equity | **$87.542B** |
| Common shares issued/outstanding | **5.043B** |

StockAnalysis 口径显示现金 **$32.79B**、total debt **$45.03B**、net cash **-$11.93B**。与公司 6/27 balance sheet 的口径差异可能来自是否合并短期投资、债务分类、更新时间和数据商标准化。投资结论不变：Intel 仍有较大流动性，但已不是净现金轻资产公司，债务/融资/政府权益和 capex 回报必须持续跟踪。

### 稀释和政府持股

FY2025 10-K 披露：

- 2025-08-27，根据 U.S. Government Agreement，Intel 向 U.S. DOC 发行 **275M shares**，并提供 warrant 可购买最多 **241M shares**，若 Intel 不再直接或间接持有至少 51% Intel Foundry。
- Intel 还向 escrow 发行 **159M shares**，按 Secure Enclave 项目收款和履约释放给美国政府。
- SoftBank 2025 年以 $23.00/股购买 **87M shares**，约 $2B。
- NVIDIA 2025 年以 $23.28/股购买 **215M shares**，约 $5B。

这解释了为什么 StockAnalysis 显示 shares outstanding 一年增加约 **9.52%**。普通股投资者必须把政府/战略投资者股权、warrant、escrow shares 和未来可能融资当作估值折扣项。

## 5. Management and Capital Allocation

新 CEO Lip-Bu Tan 的 Q2 信息集中在：速度、责任、客户聚焦、AI compute、CPU franchise、ASIC、advanced packaging 和 foundry network。CFO Dave Zinsner 强调 Q2 超过指引，原因包括 demand 强、执行改善、higher factory yields 和 improved cycle times；同时公司将 meaningful increase investments in equipment, clean room space, and substrates。

管理层正做两件方向相反的事：

1. **削减低效成本**：2026 full-year GAAP operating expenses 约 $23.0B，剔除 acquisition、SBC、restructuring 后 non-GAAP operating expenses 约 $16.5B；说明 restructuring charges 仍大。
2. **加大关键产能投资**：AI-driven compute 与 foundry 增长需要 equipment、clean room、substrates 和先进封装投入。

资本配置评价：

- 正面：Altera deconsolidation、重组、费用下降、政府/SoftBank/NVIDIA 资金提升战略资本可得性。
- 负面：外部资本和政府持股带来稀释、治理复杂性；Intel Foundry 仍亏损；14A 若没有大客户可能被迫调整。

## 6. Valuation Work

### 当前估值快照

StockAnalysis 2026-07-24 抓取：

| 指标 | 数值 |
|---|---:|
| Previous close | **$102.62** |
| Market cap | **$503.76B** |
| Enterprise value | **$515.68B** |
| Shares out | **5.03B** |
| TTM revenue | **$53.76B** |
| TTM net income | **-$3.17B** |
| TTM operating income | **$2.01B** |
| TTM OCF | **$9.98B** |
| TTM FCF | **-$3.12B** |
| Cash | **$32.79B** vendor口径 |
| Total debt | **$45.03B** vendor口径 |
| Forward PE | **94.28x** |
| PS ratio | **9.37x** |
| Forward PS | **8.32x** |
| EV/Sales | **9.59x** |
| P/OCF | **50.48x** |
| Analyst consensus | Hold |
| Price target | **$108.63** |
| 52-week range | **$18.97-$142.35** |
| Beta | **2.19** |

### 为什么当前不是传统便宜 Intel

以公司 Q2/Q3 非 GAAP EPS 年化：

- Q2 non-GAAP EPS $0.42，年化 P/E 约 **61x**。
- Q3 non-GAAP EPS guide $0.38，年化 P/E 约 **67.5x**。
- StockAnalysis 2026E EPS consensus $1.12，对应 P/E 约 **91.6x**。
- 2027E EPS consensus $1.62，对应 P/E 约 **63.3x**。

以销售额：

- EV/TTM sales 约 **9.6x**。
- EV/2026E revenue $58.99B 约 **8.7x**。
- EV/2027E revenue $66.42B 约 **7.8x**。

这类倍数只有在市场相信 Intel 将转型成 AI/Foundry/先进制造平台时才合理。如果只按传统 PC/服务器 CPU 周期股或低 FCF 重资本制造商看，估值偏高。

### Scenario valuation

以下是研究情景，不是目标价承诺。使用约 5.03B shares、约 $11.9B net debt vendor口径做粗略桥接。

| 情景 | 2027-2028 假设 | 估值逻辑 | 近似每股价值 |
|---|---|---|---:|
| Bear | 2027-28 revenue 约 $60B；DCAI 增长放缓；Foundry 继续大额亏损；14A 外部客户不足；FCF 低或负 | 约 4x EV/Sales，扣 net debt | **$45** |
| Base low | revenue 约 $68B；DCAI/CCPG 稳定，Foundry亏损收窄但未证明高 ROIC | 约 6x EV/Sales | **$79** |
| Base high | revenue 约 $72B；Foundry亏损明显收窄，18A/P 量产顺利，14A 获部分客户 | 约 7x EV/Sales | **$98** |
| Bull low | revenue 约 $80B；DCAI 高增长，Foundry 外部客户验证，FCF 转正 | 约 8x EV/Sales | **$125** |
| Bull high | revenue 约 $90B；Intel 成为美国先进制程/封装核心平台，14A 与 ASIC 客户兑现 | 约 10x EV/Sales | **$177** |

EPS 交叉验证：

| 情景 | 稳态 EPS | 合理 P/E | 每股价值 |
|---|---:|---:|---:|
| Bear | $1.20 | 35x | **$42** |
| Base | $2.20 | 45x | **$99** |
| Bull | $3.50 | 50x | **$175** |
| Hyper bull | $5.00 | 55x | **$275** |

当前 $102.62 大致在 base high 附近，略低于 bull low。换句话说，当前股价已经要求：

- DCAI 继续强增长；
- Foundry 亏损持续收窄；
- 18A/P 量产无重大事故；
- 14A 至少获得足够客户/内部产品支持；
- adjusted FCF 逐步改善；
- 稀释和政府股权复杂性可控。

### 实用价格区间

| 股价区间 | 研究判断 |
|---|---|
| **<$50** | 困境/资产折价区，若流动性无恶化，开始有明显安全边际。 |
| **$50-$75** | 可积极研究 / 小仓分批区，适合反转假设但仍需跟踪 FCF。 |
| **$75-$100** | 合理观察区，等待 Foundry 亏损收窄和 14A 客户确认。 |
| **$100-$125** | 当前附近；已定价较多 AI/Foundry 成功，不适合追高。 |
| **$125-$175** | bull case 区，需要 DCAI/Foundry/FCF 同时兑现。 |
| **>$175** | 高预期区，基本需要 Intel 成为美国先进制程平台核心赢家。 |

## 7. Catalysts and Monitoring Plan

近期催化：

- Q3 2026 earnings：revenue 是否达到 $15.8-$16.8B，GAAP EPS $0.31 / non-GAAP EPS $0.38 是否兑现。
- 18A-P risk production 是否按节奏进入更高量产。
- Panther Lake / Core Ultra Series 3 on 18A 的真实需求、良率和毛利。
- Xeon 6+、AI infrastructure、SambaNova/Foxconn/VC2/Fortinet 等合作是否转化为订单/收入。
- Intel Foundry external customer revenue 是否从 Q1 的 $174M 和 Q2 尚未完全细分披露的水平显著扩大。
- 14A 是否获得 significant external customer / committed demand。
- Adjusted FCF 是否从 Q2 的 -$8.419B 改善。
- 政府 Escrowed Shares、warrant、DOC 资金、CHIPS/Secure Enclave 项目释放节奏。

## 8. Risk Register

| 风险 | 概率 | 严重度 | 说明 |
|---|---|---|---|
| Foundry 无法获得足够外部客户 | 中高 | 高 | 14A 若没有 committed demand，可能暂停/放弃后续节点。 |
| Capex/FCF 压力 | 高 | 高 | Q2 adjusted FCF -$8.419B，重资本周期仍未结束。 |
| AI 叙事过度定价 | 中 | 高 | 股价已接近/超过 base case，容错率低。 |
| NVIDIA/AMD/TSMC/Samsung 竞争 | 高 | 高 | AI、server、foundry 都是强竞争市场。 |
| 稀释/政府股权复杂性 | 中 | 中高 | DOC shares、escrow shares、warrants、SoftBank/NVIDIA 私募提高股本复杂度。 |
| GAAP vs non-GAAP 质量差 | 中 | 中 | Q2 GAAP loss 和 non-GAAP profit 差异巨大。 |
| 地缘政治和出口管制 | 中 | 高 | 半导体制造和客户分布高度受政策影响。 |
| 执行/良率/节点延期 | 中 | 高 | 18A/14A/High-NA EUV 任一环节失误都会影响估值。 |

最强反证：Q2 DCAI、CCPG 和 Foundry 同时增长，gross margin 明显改善，非 GAAP operating margin 17.2%，说明市场重估不是完全没有基本面依据。

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: A。Intel 是长期上市公司，SEC/IR 信息丰富。风险是市场叙事从“Intel 落后”突然切换到“AI/美国制造核心资产”后，容易把新叙事当成事实。
- **Main research blind spot**: 外部 foundry 客户、14A committed demand 和先进封装/ASIC 订单的真实规模与利润率。
- **Strongest reason smart investors may disagree**: 多头可能认为美国本土先进制程战略价值、NVIDIA/SoftBank/政府资金和 AI compute 需求足以支撑更高估值。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: Intel 的现金流是否能在重资本投入后形成可预测、可持续的高 ROIC？
- **Evidence supporting**: CCPG/DCAI 是可理解产品业务，Q2 产品业务 operating income $4.817B；x86 生态、企业兼容性、PC/服务器渠道仍有护城河。
- **Evidence against**: Foundry Q2 operating loss -$2.089B；adjusted FCF -$8.419B；14A 客户不足可能导致节点暂停；政府股权和稀释复杂。
- **Decision implication**: 不符合经典 Buffett-style “高确定性现金牛 + 低资本强度 + 明显安全边际”。适合观察，不适合以当前价格重仓。
- **Follow-up question**: 如果股市关闭五年，Intel 的 Foundry 是否能产生稳定正 FCF，而不是持续融资和政府支持？

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 投资者最可能在哪里被骗？

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| 把战略重要性当成股东回报 | 美国制造重要不等于 ROIC 高 | 多年低 FCF、高稀释 |
| 把 non-GAAP 当真实利润 | 剔除 escrow/SBC/restructuring 后好看 | 忽略资本结构和现金流 |
| 把 Foundry revenue 当外部客户证明 | 大量 intersegment revenue | 外部客户不足导致估值下修 |
| 把 AI 合作当订单 | 合作/演示不等于量产收入 | bull case 落空 |

- **Fragile assumptions**: 14A 有足够外部客户；18A/P 良率和成本符合预期；DCAI 59% 增长可持续；adjusted FCF 快速改善。
- **Major stupidity risk**: 因为股价一年涨很多而追入，忽略当前 EV/Sales 和 P/E 已经很高。
- **Follow-up question**: 三年后如果错了，今天最明显的红旗可能是 Q2 adjusted FCF 仍大幅为负且 Foundry 仍亏损。

### Duan Yongping-style lens

- **Conclusion**: Needs further observation。
- **Business essence**: Intel 为 PC、服务器、AI 和边缘设备提供 x86 芯片，并尝试把自有制造能力变成外部 foundry 平台。
- **User value**: 客户需要性能、供应稳定、软件兼容和成本；Intel 在 x86/企业生态上仍有价值。
- **Product/brand strength**: Intel 品牌强、Xeon/Core 生态深，但 NVIDIA 在 AI 加速、TSMC 在先进代工、AMD 在服务器 CPU 的竞争都很强。
- **People/culture**: 新管理层强调 speed、accountability、customer focus，是正面信号；但执行是否真正改变仍需数季验证。
- **Right price**: $50-$75 更符合反转小仓；$100+ 需要更强证据。
- **Follow-up question**: Intel 是在创造长期客户价值，还是主要受益于 AI/国家战略和资本市场重新定价窗口？

### Li Lu-style lens

- **Conclusion**: Needs further observation。
- **Circle of competence**: PC/CPU/DCAI 财务可研究；18A/14A 良率、外部客户 pipeline、先进封装真实成本需要更深行业验证。
- **Industry trend**: AI compute、先进封装、美国本土制造、供应链安全是长期结构趋势。
- **Downside protection**: Intel 有 $29.7B cash+ST investments、$105.7B PP&E 和政府/战略资本支持，但普通股 downside 不由资产价值自动保护，因为高 capex、负 FCF 和稀释会侵蚀价值。
- **Margin of safety**: 当前价格缺少明显 margin of safety。
- **Research depth decision**: 值得继续研究，但需要季度化跟踪，不适合一次性高信心判断。
- **Follow-up question**: 10-20 年后，Intel 会是美国先进制造和 AI 供应链的 durable node，还是一轮政策/资本周期中的高成本参与者？

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 7/10 |
| Management | 6/10 |
| Financial quality | 4/10 |
| Valuation attractiveness | 3/10 |
| Long-term certainty | 5/10 |
| Downside risk control | 4/10 |

- Business model 7：产品业务强，但 foundry 模型未证明。
- Moat 7：x86/enterprise/manufacturing moat 仍在，但被 NVIDIA/AMD/TSMC 挑战。
- Management 6：新团队方向正确，但执行历史和转型结果仍需验证。
- Financial quality 4：non-GAAP 改善，但 GAAP/FCF/稀释复杂。
- Valuation 3：当前 $100+ 已接近 base high，不便宜。
- Long-term certainty 5：结构趋势强，但具体赢家不确定。
- Downside control 4：流动性强，但估值和资本开支带来下行。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 产品业务改善，Foundry 未证明 | 中 |
| Moat | x86/制造/美国战略资产有价值 | 中 |
| Management | 新 CEO 方向更清晰 | 中低 |
| Biggest risk | Foundry/14A/FCF 无法兑现 | 高 |
| Long-term trend | AI compute 与本土先进制造有利 | 中高 |
| Valuation | 当前不便宜，缺少安全边际 | 高 |

| Investor state | Research implication |
|---|---|
| No position | 不急于追，等待 $75 以下或 Foundry/FCF 明确改善。 |
| Existing position | 可继续持有观察，但不宜因 Q2 headline 盲目加仓。 |
| Add / upgrade signal | 14A 外部客户、Foundry亏损大幅收窄、FCF转正、DCAI连续高增。 |
| Reduce / downgrade signal | Foundry亏损扩大、14A暂停、FCF持续负、稀释继续扩大。 |

## 10. Final Research Framework

### Thesis depends on

- DCAI 增长是否从 Q2 的 +59% 延续到未来数季。
- CCPG 是否能借 AI PC 和 PC refresh 维持收入/利润。
- Foundry 是否从高 intersegment revenue 转向真实外部客户收入。
- 18A/P 是否量产顺利，14A 是否获得 significant external customer。
- Adjusted FCF 是否转正。
- 政府股权、escrow shares、warrants 和战略投资者稀释是否可控。

### What would make thesis stronger

- Q3/Q4 revenue 持续高于指引中点。
- Non-GAAP EPS 改善同时 GAAP/FCF 也改善，而非仅靠调整项。
- Foundry operating loss 从 -$2B/quarter 快速收窄。
- 外部 foundry customer revenue 明确披露并放大。
- 14A 获得客户设计定点或长期产能承诺。
- Gross capex 和 adjusted FCF 进入可持续区间。

### What would change my view

- 上调：DCAI 连续高增、Foundry外部客户兑现、FCF转正、14A客户确认、稀释停止扩大。
- 维持中性：收入继续恢复但 FCF/Foundry 仍弱，估值继续高。
- 下调：14A 暂停或客户不足、Foundry亏损扩大、DCAI增长放缓、adjusted FCF持续大幅为负、政府/战略资本进一步稀释普通股。

## Sources

- Intel Form 8-K filed 2026-07-23, Exhibit 99.1: `q226earningsrelease.htm`, Intel Reports Second-Quarter 2026 Financial Results.
- Intel Form 10-Q filed 2026-04-24 for quarter ended 2026-03-28.
- Intel Form 10-K filed 2026-01-23 for fiscal year ended 2025-12-27.
- SEC submissions JSON, CIK `0000050863`.
- StockAnalysis INTC quote/statistics/financials/forecast pages, accessed 2026-07-24.
