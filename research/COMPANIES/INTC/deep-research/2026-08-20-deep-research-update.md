# Intel Corporation（INTC）深度研究更新 - 2026-08-20

- **Research view**: Neutral / wait for confirmation（中性 / 等待确认）
- **Confidence**: 中等
- **Time horizon**: 12-36 个月
- **Main thesis**: Intel 的业务反转是真实的：Q2 2026 revenue $16.1B，同比 +25%；DCAI +59%；CCPG +13%；Foundry +31%；non-GAAP EPS $0.42；Q3 revenue guide $15.8B-$16.8B。但当前 $92.80 仍约对应 EV/Sales 8.91x、Forward PE 55.86x、P/FCF 172x，市场仍按“AI compute + 美国本土先进制造 + Foundry 成功”而不是传统低估半导体来定价。价格从旧报告 $102.62 回落后更值得研究，但还不是强安全边际区。
- **Key risk**: Intel Foundry 仍亏损约 -$2.1B/quarter，14A 仍需显著外部客户/committed demand，Q2 adjusted FCF 为 -$8.4B，政府/DOC escrow shares、warrants、SoftBank/NVIDIA 私募和股数增长让普通股价值复杂化。若 DCAI 增长放缓、Foundry 外部客户兑现不足或 FCF 迟迟不能转正，当前估值可能继续压缩。

> 本文是对 `2026-07-24-deep-research.md` 的深度研究更新。旧报告基于 Q2 8-K/初步材料；本次补充 Q2 2026 10-Q、slides、StockAnalysis 2026-08-19 收盘估值，并重新计算价格区间。本文不是 initial coverage。

---

## 1. Executive View

**研究观点：中性 / 等待确认。**

Intel 已经从 2022-2024 年的“老牌 CPU 份额流失 + 制程落后 + 高 capex”困境股，变成市场重新定价的“AI compute + 美国先进制造 + Foundry optionality”股票。Q2 2026 的收入和 non-GAAP 利润确实比一年前明显改善，但股价和估值也已经提前反映了相当多的成功预期。

### 核心判断

1. **产品业务恢复是真实的。** Q2 2026 consolidated revenue $16.128B，同比增长 25%；Total Intel Products revenue $15.139B，同比增长 28%；non-GAAP operating income $2.8B，non-GAAP EPS $0.42。
2. **DCAI 是最关键利润引擎。** Q2 DCAI revenue $6.262B，同比增长 59%，operating income $2.474B，segment margin 约 40%。如果这一趋势可持续，Intel 会获得 AI infrastructure 相关重估。
3. **Foundry 是最大变量。** Q2 Intel Foundry revenue $5.765B，同比增长 31%，但 operating loss 仍为 -$2.089B；18A 已 ramp、18A-P 进入 risk production、14A 目标 2028 HVM，但外部客户和现金流仍未充分验证。

### 为什么仍不是 Positive

$92.80 已比 7 月旧报告的 $102.62 便宜，但仍不是低估值：

- Market cap **$487.62B**。
- EV **$508.18B**。
- EV/TTM sales **8.91x**。
- Forward PE **55.86x**。
- P/FCF **172x**。
- TTM FCF yield 只有约 **0.6%**。

这意味着 Intel 现在的投资逻辑不是“便宜价值股”，而是“高预期转型股”。只有当 DCAI、Foundry loss narrowing、14A customer commitment 和 FCF 改善同时兑现，当前估值才容易被证明合理。

### 最强反方理由

最强看多理由是：Intel 可能正在从单纯 CPU 公司变成美国先进制程/封装/AI 供应链战略平台。如果 18A/18A-P/14A、先进封装、ASIC、Xeon AI infrastructure 和外部 foundry 客户共同兑现，市场可能长期接受更高 EV/Sales 和更高 earnings multiple。但这个 bull case 需要非常多执行证据。

---

## 2. Business Model and Industry Structure

### 新手解释：Intel 到底怎么赚钱？

Intel 主要卖两类东西：

1. **芯片产品**：包括 PC CPU、服务器 CPU、网络/边缘芯片、AI/数据中心相关产品。客户是 PC 厂商、服务器厂商、云厂商、企业和工业/边缘设备厂商。
2. **制造能力 / Foundry**：Intel 自己建晶圆厂和封装厂，为内部产品和潜在外部客户制造芯片。

和 NVIDIA、AMD、Broadcom 这类大多依赖 TSMC 制造的 fabless 公司不同，Intel 是 IDM：既设计芯片，也自己制造。好处是如果制程领先、良率高、产能利用率高，可以把设计、制造、封装和客户需求整合在一起；坏处是建厂和买设备要花巨额资本，且一旦客户不足，固定成本会拖累利润和现金流。

核心经济问题：

> Intel 能否让自己的先进制造资产从“高 capex 负担”变成“高利用率、高良率、有外部客户、能产生正 FCF 的平台”？

### 关键术语

| 术语 | 白话解释 |
|---|---|
| CPU | 中央处理器，负责通用计算任务，是 PC 和服务器的核心芯片。 |
| x86 | Intel/AMD 主导的 CPU 指令集生态，软件兼容性强。 |
| DCAI | Data Center and AI，数据中心和 AI 业务，包括服务器 CPU、AI infrastructure 相关产品。 |
| CCPG | Client Computing and Physical AI Group，PC/客户端/边缘 AI 相关业务。 |
| Foundry | 晶圆代工，为内部和外部客户制造芯片。TSMC 是全球最成功的 foundry。 |
| Process node | 制程节点，如 Intel 18A、18A-P、14A，代表制造工艺代际。 |
| High-NA EUV | 更先进、更昂贵的极紫外光刻技术，用于领先制程。 |
| Advanced packaging | 先进封装，把多个芯片/小芯片高速连接，是 AI 芯片性能和良率的重要环节。 |
| ASIC | 为特定客户/用途定制的芯片，例如云厂商专用 AI 或网络芯片。 |
| Escrowed Shares | 托管股份，按政府协议条件释放给 DOC；股价变化会带来 mark-to-market 损益。 |
| Adjusted FCF | 经营现金流扣除 capex、政府激励、partner contributions、finance lease 等后的调整自由现金流。 |

### 行业结构和竞争

| 业务 | 主要竞争者 | Intel 优势 | Intel 风险 |
|---|---|---|---|
| PC / client CPU | AMD、Apple、Qualcomm、Arm 生态 | x86 生态、OEM 渠道、企业兼容性、Core 品牌 | PC 周期、Arm 化、AI PC 溢价不确定 |
| Data center CPU / AI | AMD EPYC、NVIDIA Grace/Blackwell、Arm 云芯片、云厂商 ASIC | Xeon 生态、企业软件兼容、封装/制造协同 | AI accelerator 主导权弱于 NVIDIA，云客户自研压价 |
| Foundry / advanced manufacturing | TSMC、Samsung、GlobalFoundries | 美国本土制造、政府支持、18A/14A、先进封装 | 外部客户信任、良率、成本、交付和资本回报未证明 |

Intel 是 **资本密集型 IDM / Foundry turnaround**，不应用单一 P/E 分析。必须同时看产品利润、Foundry loss、外部客户、节点进度、capex、现金流、债务和稀释。

---

## 3. Segment and Product Analysis

### Q2 2026 segment snapshot

| Segment | Q2 2026 revenue | YoY | Q2 2026 operating income/loss | Segment margin | 研究解读 |
|---|---:|---:|---:|---:|---|
| CCPG | $8.877B | +13% | $2.343B | 26% | PC/AI PC 是当前利润底座 |
| DCAI | $6.262B | +59% | $2.474B | 40% | 最大亮点，AI compute/CPU density 驱动 |
| Total Intel Products | $15.139B | +28% | $4.817B | 32% | 产品业务利润质量明显改善 |
| Intel Foundry | $5.765B | +31% | -$2.089B | -36% | 收入增长但仍严重亏损 |
| All Other | $701M | -33% | $230M | 33% | Mobileye/IMS/Altera 影响 |
| Intersegment eliminations | -$5.477B | n/a | $254M | n/a | 内部制造交易抵消 |
| Consolidated | $16.128B | +25% | $1.796B GAAP op income | 11.1% | 整体恢复明显 |

### CCPG：Client / AI PC / Physical AI

CCPG 是 Intel 的 PC 和客户端业务。Q2 revenue $8.877B，同比增长 13%，operating income $2.343B，margin 约 26%。这说明 Intel 的 PC 业务仍有利润底座，AI PC、Windows refresh、企业设备更新和边缘 AI/机器人应用提供增长支撑。

风险：PC 是周期行业，AI PC 不一定带来长期高毛利；如果只是一次性更新周期，估值不能给太高倍数。

### DCAI：Data Center and AI

DCAI 是当前最强板块。Q2 revenue $6.262B，同比增长 59%，operating income $2.474B，margin 约 40%。slides 中管理层强调 AI driving CPU density、record YoY growth、purpose-built silicon revenue nearly tripled YoY。

正面：

- Xeon 6+ 是 Intel 首款使用 18A 的 server-class product。
- Intel/SambaNova/Foxconn 展示 rack-scale inference / agentic workloads infrastructure。
- VC2 展示结合 Xeon、SambaNova RDU、NVIDIA Blackwell GPU 的 disaggregated agentic cloud。
- AI infrastructure 不只依赖 GPU，也需要 CPU、networking、memory orchestration、封装和系统级平台。

风险：Intel 在 AI GPU/accelerator 的主导权不如 NVIDIA；AMD EPYC、Arm server CPU、cloud ASIC 和 Broadcom/Marvell custom silicon 都会竞争 DCAI 预算。

### Intel Foundry：最大 upside，也是最大风险

Foundry Q2 revenue $5.765B，同比增长 31%，但 operating loss -$2.089B。这个数字很重要：Foundry revenue 增长不能直接等同于外部客户验证，因为大量可能来自内部产品制造交易。

正面进展：

- 2026 年初 Intel 18A 首批产品进入 high volume production。
- 18A-P 于 2026 年 6 月进入 risk production。
- 10-Q 披露 Intel 已承诺完成 Intel 14A 开发，未来 Intel 产品将使用该节点，相关 manufacturing expansion projects 已在推进。
- 14A 目标 2028 HVM。
- 管理层强调 improving yields & cycle times，Foundry loss margin 从 slides 中历史 -70%+ 改善到约 -36%。

风险：

- Foundry 仍每季度亏损约 $2B。
- 14A 需要 significant external customers / committed demand。
- High-NA EUV、clean room、substrates、equipment capex 会继续消耗现金。
- 若外部客户没有放量，Foundry 可能继续拖累 consolidated FCF。

---

## 4. Financial Deep Dive

### Q2 2026 headline results

| 指标 | Q2 2026 | Q2 2025 | 变化 |
|---|---:|---:|---:|
| Revenue | $16.1B | $12.9B | +25% |
| GAAP gross margin | 40.4% | 27.5% | +12.9 ppts |
| Non-GAAP gross margin | 41.8% | 29.7% | +12.1 ppts |
| GAAP operating margin | 11.1% | -24.7% | +35.8 ppts |
| Non-GAAP operating margin | 17.2% | -3.9% | +21.1 ppts |
| GAAP net income attributable to Intel | -$11.0B | -$2.9B | n/m |
| Non-GAAP net income attributable to Intel | $2.2B | -$0.4B | n/m |
| GAAP diluted EPS | -$2.16 | -$0.67 | n/m |
| Non-GAAP diluted EPS | $0.42 | -$0.10 | n/m |
| Operating cash flow | $7.0B | $2.1B | 改善 |
| Adjusted FCF | -$8.4B | -$1.1B | 恶化 |

### Q3 2026 guidance

| 指标 | GAAP | Non-GAAP |
|---|---:|---:|
| Revenue | $15.8B-$16.8B | same |
| Gross margin | 41.0% | 42.0% |
| EPS attributable to Intel | $0.31 | $0.38 |

Q3 指引说明 Q2 不是单一孤立强季度，但也没有完全解除估值压力。以 $92.80 股价和 forward PE 55.86x 反推，市场隐含 forward EPS 约 $1.66，仍要求利润持续恢复。

### GAAP vs non-GAAP：为什么差这么大？

Q2 GAAP EPS 是 -$2.16，但 non-GAAP EPS 是 $0.42，主要因为：

| 调整项 | Q2 2026 EPS 影响 |
|---|---:|
| Mark-to-market losses on Escrowed Shares | +$2.45 add-back |
| Share-based compensation | +$0.13 |
| Restructuring and other charges | +$0.03 |
| Acquisition-related adjustments | +$0.02 |
| NCI / tax effects | 合计小幅抵消 |

结论：

- non-GAAP 更能看核心经营恢复；
- GAAP 反映政府股权/escrow shares 复杂性；
- 普通股投资者不能只看 non-GAAP，也不能被 GAAP mark-to-market 噪音吓到；应该重点跟踪现金流和稀释。

### 现金流和资本结构

Q2 adjusted FCF bridge：

| 项目 | Q2 2026 |
|---|---:|
| GAAP operating cash flow | $7.0B |
| Gross capex | -$2.7B |
| Government incentives proceeds | +$0.1B |
| Partner contributions, net | -$12.2B |
| Finance lease payments | -$0.6B |
| Adjusted FCF | -$8.4B |

H1 2026 现金流：

- Operating cash flow：$8.102B。
- Additions to PP&E：-$6.192B。
- Government incentives：$167M。
- Partner contributions：$4.082B。
- Partner distributions：-$14.339B。
- Term debt issued：$13.0B。
- Term debt repaid：$9.0B。

这说明 Intel 经营层面改善，但股东现金流尚未同步改善。对于这种重资本公司，最终判断不是 revenue growth，而是：Foundry 亏损是否下降、capex 是否产生回报、adjusted FCF 是否转正。

### 最新市场/资产负债数据

StockAnalysis 2026-08-20 访问、2026-08-19 收盘数据：

| 指标 | 数值 |
|---|---:|
| Price | $92.80 |
| Market cap | $487.62B |
| Enterprise value | $508.18B |
| Shares outstanding | 5.25B |
| Shares YoY change | +13.28% |
| TTM revenue | $57.03B |
| TTM net income | -$11.29B |
| TTM EPS | -$2.30 |
| Cash | $29.73B |
| Total debt | $50.54B |
| Net debt | $20.56B |
| Book equity | $103.14B |
| Forward PE | 55.86x |
| EV/Sales | 8.91x |
| EV/EBITDA | 30.18x |
| P/FCF | 172.24x |
| P/OCF | 32.65x |
| Beta | 2.24 |
| Analyst consensus | Hold |
| Analyst target | $114.88 |
| 52-week range | $22.78-$142.35 |

### 稀释和政府/战略投资者资本

需要持续跟踪：

- DOC 普通股和 escrow shares。
- DOC warrants：最多 241M shares，exercise price $20.00，触发条件与 Intel Foundry ownership 相关。
- Escrowed Shares 在 release 前不计入 EPS，但代表潜在普通股经济复杂性。
- SoftBank $2B 私募、NVIDIA $5B 私募已提供战略资本但也增加股数。
- StockAnalysis 显示 shares outstanding YoY +13.28%。

“国家战略重要性”降低融资风险，但不自动等于普通股安全边际，因为普通股可能被稀释、FCF 可能被 capex 吸收。

---

## 5. Management and Capital Allocation

CEO Lip-Bu Tan 的叙事集中在 AI compute、CPU franchise、ASIC、advanced packaging 和 wafer foundry network。Q2 超过原先 outlook，管理层归因于 strong demand、disciplined execution、output beat expectations、improving yields & cycle times。

正面：

- Q2 revenue 比 April outlook midpoint 高约 $1.8B。
- Non-GAAP gross margin 比 April outlook 高约 2.8 ppts。
- DCAI revenue/margin 明显改善。
- 18A/18A-P 节点推进更具体。

需要质疑：

- 增加 equipment、clean room、substrates 投资是否会在合理时间内转成外部 revenue？
- 14A 2028 HVM 是否能拿到足够外部客户？
- Foundry operating loss 何时从 -$2B/quarter 收窄？
- partner contribution/distribution 现金流是否还会制造大额 adjusted FCF 波动？
- 战略投资和政府股权之后是否还需要更多融资？

---

## 6. Valuation Work

### 为什么不用单一 P/E？

Intel 当前 GAAP EPS 为负，non-GAAP EPS 又受到转型期调整影响；Foundry 是重资本亏损业务，产品业务和制造业务经济性差异很大。因此更合理的框架是：

1. EV/Sales：反映市场对 AI + Foundry 平台的收入重估。
2. Forward PE：检查利润恢复预期是否过高。
3. P/OCF / P/FCF：判断重资本模式是否真正创造股东现金流。
4. 情景估值：区分产品恢复、Foundry 亏损收窄、14A 外部客户和 FCF 转正。

### 当前估值锚

| 指标 | 数值 |
|---|---:|
| EV/Sales | 8.91x |
| P/S | 8.55x |
| EV/EBITDA | 30.18x |
| Forward PE | 55.86x |
| P/OCF | 32.65x |
| P/FCF | 172.24x |
| TTM FCF yield | 0.6% |
| P/B | 4.73x |
| Net debt/share | $3.92 |

### Scenario valuation

| Scenario | Revenue | EV/Sales | Net debt | Diluted shares | Implied price | vs $92.80 | Core assumption |
|---|---:|---:|---:|---:|---:|---:|---|
| Bear foundry cash burn | $58B | 4.5x | $25B | 5.4B | $43.7 | -52.9% | Foundry 继续烧钱，DCAI 放缓，市场按普通周期半导体重估 |
| Downside reset | $62B | 6.0x | $23B | 5.35B | $65.2 | -29.7% | 产品恢复但 FCF/14A 证据不足，估值压缩 |
| Base products recover | $68B | 7.0x | $21B | 5.35B | $85.0 | -8.4% | DCAI/CCPG 恢复，Foundry 亏损缓慢收窄 |
| Base plus foundry better | $75B | 8.0x | $18B | 5.4B | $107.8 | +16.1% | Foundry loss 明显收窄，18A/18A-P 客户验证提升 |
| Bull AI foundry | $85B | 9.0x | $15B | 5.5B | $136.4 | +46.9% | DCAI 高增长 + 14A 客户 + FCF 改善 |
| Hyper-bull U.S. foundry | $100B | 10.0x | $10B | 5.7B | $173.7 | +87.2% | Intel 成为美国先进制程/AI manufacturing 平台 |

当前 $92.80 大致位于 base products recover 与 base plus foundry better 之间。也就是说：市场已经不只定价产品业务恢复，还在给 Foundry/AI/国家战略一定成功概率。

### Practical price zones

| Price zone | 研究含义 |
|---|---|
| **<$50** | 强研究区；如果 14A/Foundry/流动性没有恶化，才有显著安全边际。 |
| **$50-$65** | 逆向分批区；对应 EV/Sales 约 5-6x，更能容忍执行波动。 |
| **$65-$80** | 有吸引力但需验证 FCF 区；适合等待 Foundry loss narrowing 证据。 |
| **$80-$95** | 当前区间；较 7 月便宜，但仍非强安全边际。 |
| **$95-$110** | 合理偏贵；需要 Q3/Q4 持续 beat 和 Foundry 改善。 |
| **$110-$135** | Bull-case 预期区；需要 14A/外部客户/FCF 多项证据。 |
| **>$135** | Hyper-bull/重估区；不宜仅凭 AI + 政府支持追高。 |

---

## 7. Catalysts and Monitoring Plan

近期催化：

- Q3 2026 earnings vs revenue guide $15.8B-$16.8B。
- Non-GAAP gross margin 是否维持 42% 附近。
- DCAI revenue growth 和 margin 是否持续。
- CCPG AI PC/PC refresh 是否仍强。
- Foundry operating loss 是否从 -$2B/quarter 收窄。
- 18A/18A-P production yield/cost/cycle time。
- 14A significant external customer / committed demand。
- Adjusted FCF 是否从 -$8.4B 改善。
- DOC escrow shares、warrants、政府股权和战略投资者稀释。

---

## 8. Risk Register

| Risk | Probability | Severity | Mechanism | Monitor |
|---|---|---|---|---|
| Foundry 亏损持续 | 高 | 高 | 高固定成本 + 外部客户不足 | Foundry op loss, utilization |
| 14A 客户不足 | 中高 | 极高 | 14A 无 committed demand，长期 bull case 受损 | 14A design wins, customer commitments |
| DCAI 增长放缓 | 中 | 高 | AMD/NVIDIA/Arm/ASIC 竞争 | DCAI revenue/margin |
| Adjusted FCF 继续为负 | 高 | 高 | capex/partner distributions/lease payments | adjusted FCF bridge |
| 稀释 | 中高 | 中高 | 政府/战略投资者/员工股权/warrants | shares outstanding, escrow release |
| 估值压缩 | 中高 | 高 | EV/Sales 8.9x 需要多项兑现 | multiple vs milestones |
| 地缘政治/出口管制 | 中 | 高 | 中国、台湾、以色列、中东、美国政策 | 10-Q risk updates |
| 执行复杂度 | 中高 | 高 | 多节点、多厂、多客户、多资本伙伴并行 | schedule, yield, capex, customer ramps |

---

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: A。Intel 披露充分、历史长、市场覆盖广；风险是公开叙事非常强，容易把“美国战略资产”当成普通股安全边际。
- **Main research blind spot**: 外部 foundry 客户、14A committed demand、实际良率/成本和未来 adjusted FCF 转正路径仍不透明。
- **Strongest reason smart investors may disagree**: 看多者会认为 Intel 正在成为美国先进制造平台，当前估值只是长期重估起点；看空者会认为这只是高 capex 反转股在 AI 叙事下被过度定价。

### Buffett-style lens: Needs further observation

- **Key question**: Intel 的利润引擎是否能在 5-10 年内可预测地产生高 ROIC/FCF？
- **Evidence supporting**: x86 生态、DCAI Q2 +59%、CCPG 仍有 26% margin、现金 + 短投 $29.73B、美国政府和战略投资者降低融资风险。
- **Evidence against**: Foundry -$2.089B operating loss、adjusted FCF -$8.4B、股数 YoY +13.28%、EV/Sales 8.91x、Forward PE 55.86x。
- **Decision implication**: 适合继续研究，但不是典型 Buffett-style 明显安全边际；需要 FCF 转正和 Foundry 亏损收窄证明。
- **Follow-up question**: 如果股市关闭五年，最舒服的证据是 DCAI/CCPG 利润稳定、Foundry 外部客户放量、adjusted FCF 转正；最不舒服的是 14A 无客户且继续融资稀释。

### Munger-style lens: Needs further observation

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| AI 叙事过度 | 市场把 CPU/Foundry 全部按 AI 平台估值 | EV/Sales 压缩，股价回 $65-$80 |
| Foundry 收入误读 | 内部收入增长被当成外部客户验证 | 亏损持续，bull case 延后 |
| 14A 执行失败 | 无 significant committed demand | 长期战略价值受损 |
| FCF 被忽略 | non-GAAP EPS 好但 adjusted FCF 负 | 普通股回报迟迟不出现 |
| 稀释低估 | DOC/escrow/warrants/战略投资者/员工股权 | 每股价值被摊薄 |

- **Fragile assumptions**: DCAI +59% 可持续、14A 2028 HVM、外部客户放量、partner contributions 不再造成大额现金流波动。
- **Psychological trap**: “国家战略重要 = 股东一定赚钱”。
- **Decision implication**: 每次想买都要先问：我是买经营证据，还是买叙事？
- **Follow-up question**: 三年后如果错了，今天最明显红旗可能是 adjusted FCF 已经很差，但投资者只看 revenue growth 和 non-GAAP EPS。

### Duan Yongping-style lens: Needs further observation

- **Business essence**: Intel 为全球 PC、服务器和 AI 基础设施提供 CPU/平台芯片，并试图把自有先进制造变成对外 foundry 平台。
- **User value**: 客户买 Intel 是为了 x86 兼容、性能、供应安全、平台稳定和未来美国本土先进制造可选项。
- **Product/brand strength**: Xeon/Core 仍强，但 NVIDIA/AMD/Arm/cloud ASIC 说明客户不会只因品牌买单。
- **People/culture**: Lip-Bu Tan 方向上更强调客户、速度、AI、ASIC 和 foundry network，但转型证据仍早。
- **Right price**: $92.80 比 $102.62 更合理，但 $50-$65 才更符合强安全边际；$80-$95 是观察区。
- **Follow-up question**: Intel 是在创造 durable customer value，还是依靠补贴/政策/AI 情绪支撑估值窗口？

### Li Lu-style lens: Needs further observation

- **Circle of competence**: 财报、估值、现金流、分部利润可研究；良率、节点竞争力、客户设计导入需要更深产业验证。
- **Industry trend**: AI compute、先进封装、本土半导体制造是长期重要趋势，Intel 处于战略价值链关键节点。
- **Downside protection**: 现金、政府支持、产品业务利润提供保护；但高估值、Foundry亏损、FCF负值和稀释削弱 margin of safety。
- **Margin of safety**: 当前中等偏弱；更强安全边际在 $50-$65。
- **Research-depth decision**: 值得持续跟踪，但高置信配置必须等待 14A/Foundry/FCF 三个证据同时改善。
- **Follow-up question**: 10-20 年后 Intel 会是美国先进制造核心节点，还是这一轮政策/资本周期中被高 capex 稀释的过渡赢家？

### Composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 6/10 |
| Financial quality | 5/10 |
| Valuation attractiveness | 4/10 |
| Long-term certainty | 5/10 |
| Downside risk control | 4/10 |

Rationale：产品业务和 x86 生态仍强，但 Foundry 经济性未证明；管理层转型方向合理但仍早；财务质量被 adjusted FCF、债务和稀释拖累；估值相对基本面恢复并不便宜；长期确定性取决于 14A/18A-P/外部客户和 FCF。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 产品业务恢复明显，Foundry 仍待证明 | 中高 |
| Moat | x86/制造/封装/政府支持组合，但并非无敌 | 中 |
| Management and capital allocation | 新 CEO 方向合理，capex/FCF 纪律待检验 | 中 |
| Biggest risk | Foundry/14A/FCF 不兑现而估值已先行 | 高 |
| Long-term trend | AI compute + 本土先进制造长期重要 | 高 |
| Valuation and margin of safety | $92.80 不贵于 7 月，但仍非强安全边际 | 中 |

| Investor state | Research implication |
|---|---|
| No position | 可放入重点观察池；若要买，优先等 $65-$80 或 Q3/Q4 证明 Foundry/FCF 改善。 |
| Existing position | 可持有跟踪；不建议因股价从 $102 跌到 $92 就重仓摊平。 |
| Add / upgrade signal | DCAI 持续强、Foundry loss 明显缩窄、14A 客户确认、adjusted FCF 改善。 |
| Reduce / downgrade signal | 14A 客户不足、Foundry loss 不降、FCF 持续深负、股数继续大幅增加。 |

---

## 10. Final Research Framework

### Thesis depends on

1. DCAI revenue/margin 持续强劲。
2. CCPG 保持 PC/AI PC 利润底座。
3. Foundry loss 从 -$2B/quarter 明显缩窄。
4. 18A/18A-P 良率、成本和量产顺利。
5. 14A 获得 significant external customers / committed demand。
6. Adjusted FCF 从 -$8.4B 朝 breakeven/positive 改善。
7. 政府/战略投资者/escrow/warrants 不继续显著恶化稀释。

### What would make thesis stronger

- Q3 revenue 高于 $16.3B midpoint，gross margin 接近或高于 42%。
- DCAI 连续几个季度保持高增长且 margin 不大幅回落。
- Foundry quarterly operating loss 明显低于 -$2B。
- 14A 外部客户/设计导入明确。
- Adjusted FCF 明显改善，partner distributions 不再造成巨大负数。
- Share count 增速放缓。

### What would change my view

- **Upgrade to Constructive**: 股价 $80-$95 区间内，Q3/Q4 继续 beat、Foundry loss 缩窄、adjusted FCF 改善。
- **Upgrade to Positive**: 14A 重要外部客户确认、Foundry 亏损快速下降、FCF 转正，同时估值未重新大幅上行。
- **Downgrade to Negative**: DCAI 增长失速、14A 缺 committed demand、Foundry loss 维持 -$2B/quarter、adjusted FCF 持续深负或新增大额稀释。

## Sources

- Intel Q2 2026 earnings release / Exhibit 99.1, published 2026-07-23, via StockAnalysis/Quartr filing mirror.
- Intel Q2 2026 Form 10-Q, published 2026-07-24, via StockAnalysis/Quartr filing mirror.
- Intel Q2 2026 earnings slides, published 2026-07-23, via StockAnalysis/Quartr filing mirror.
- StockAnalysis INTC overview/statistics/financials/filings pages, accessed 2026-08-20; market data as of 2026-08-19 close.
- Prior repository memo: `research/COMPANIES/INTC/deep-research/2026-07-24-deep-research.md` and `research/COMPANIES/INTC/tracker.md`.
