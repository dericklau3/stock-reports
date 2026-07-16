# Qualcomm（NASDAQ: QCOM）深度研究报告

- **Research view**: Constructive but watchful（建设性，但等待 Q3/Q4 手机周期和多元化验证）
- **Confidence**: B。QCOM 是长上市历史、披露充分、现金流强的成熟半导体公司；但 2026 近端受到手机客户/中国/内存供给影响，多元化增长能否抵消手机周期仍需验证。
- **Time horizon**: 6-18 个月看手机触底、汽车/IoT 持续增长和数据中心初始出货；3-5 年看 Qualcomm 是否能从“手机芯片+专利授权”进化为“边缘 AI / 汽车 / IoT / 数据中心连接与计算平台”。
- **Main thesis**: QCOM 的核心现金牛仍是手机 SoC/基带/RF 与 QTL 专利授权，当前估值约 17x forward-ish EPS、15x P/FCF，并不昂贵；若汽车、IoT、PC/边缘 AI、数据中心 custom silicon 兑现，估值可上修。
- **Key risk**: 手机业务仍占 QCT 大头，Q2 FY2026 handsets -13% YoY，Q3 指引继续反映内存供给与部分 OEM 需求压力；Apple/中国 OEM 自研、华为份额、授权争议和客户集中仍是长期折价来源。

> 数据日期：2026-07-16。市场数据主要使用 StockAnalysis 2026-07-15 regular close；财务和业务披露来自 SEC filings：FY2025 10-K、FY2026 Q1/Q2 10-Q、FY2026 Q1/Q2 earnings 8-K exhibits、2026-06-24 Modular acquisition 8-K。本文是研究框架，不构成个性化投资建议。

---

## 1. Executive View

### 结论先说

Qualcomm（QCOM）是少数同时具备 **高利润率授权业务、全球移动通信专利资产、强现金流、持续回购、以及 AI/汽车/IoT/数据中心期权** 的半导体公司。它不是像 NVIDIA 那样的数据中心训练 GPU 龙头，也不是像 BE 那样的高 beta AI 电力纯概念，而是一个“成熟现金流 + 多元化转型”的科技平台。

截至 2026-07-15：

- 股价 **$177.98**。
- Market cap **$187.59B**。
- Enterprise value **$193.06B**。
- TTM revenue **$44.49B**。
- TTM net income **$9.92B**。
- TTM PE **19.44x**，forward PE **18.05x**。
- P/FCF **15.0x**，EV/FCF **15.44x**。
- Dividend yield **2.07%**。
- 52-week range **$121.99-$259.92**。
- 下一次财报预计 **2026-07-29 after close**。

从估值上看，QCOM 明显比许多 AI 半导体/基础设施股票更克制：约 15x FCF 对应的是一家 ROIC 约 33%、专利授权业务利润率极高、还能回购和分红的公司。但它便宜有原因：手机业务周期、客户自研、华为/中国、Apple 依赖、以及多元化增长能否兑现，是市场给它折价的核心。

### 核心判断

1. **业务质量高**：QTL 授权业务是稀缺资产；QCT 芯片业务在 Android 高端、汽车和 IoT 有明显技术积累。
2. **短期基本面混合**：Q2 FY2026 revenue $10.6B，同比 -3%；non-GAAP EPS $2.65，同比 -7%；Q3 指引 revenue $9.2B-$10.0B，说明手机压力仍未完全过去。
3. **估值有吸引力但不是无脑便宜**：base case 估值区间约 $168-$210，当前 $178 位于 base 区间偏低侧；若 Q3 确认手机触底且数据中心/汽车继续推进，风险收益较好。
4. **最大反方理由**：QCOM 的新增长叙事很多，但手机仍是利润和现金流主引擎；如果手机周期/Apple/中国问题继续压制，同时数据中心/AI 收入兑现慢，估值上修会受限。

---

## 2. Business Model and Industry Structure

### 初学者解释：Qualcomm 到底做什么？

你可以把 Qualcomm 理解成两个生意叠在一起：

1. **卖芯片和系统方案**：给手机、汽车、IoT 设备、PC、工业设备等卖“大脑”和“通信模块”。这些芯片让设备能连接 4G/5G/Wi-Fi/蓝牙，处理 AI、图像、音频、图形、定位、安全等任务。
2. **收专利授权费**：很多手机和无线设备要用 3G/4G/5G 等蜂窝通信标准，Qualcomm 拥有大量基础专利。手机厂商即使不用 Qualcomm 芯片，也可能需要为相关专利付授权费。

这就是 QCOM 独特之处：它不是只卖硬件的普通芯片公司，也不是只收专利费的知识产权公司，而是 **芯片产品 + 标准必要专利授权** 的组合。

### 重要术语翻译

| 术语 | 白话解释 | 为什么重要 |
|---|---|---|
| SoC | System-on-Chip，把 CPU/GPU/NPU/通信/多媒体等功能集成在一颗芯片或平台里 | 手机、汽车座舱、PC、IoT 的核心计算平台 |
| Baseband modem | 负责蜂窝通信的“调制解调器”芯片/模块 | 连接 4G/5G 网络的关键 |
| RF / RFFE | 射频前端，负责把无线信号发出去、收回来、过滤和放大 | 决定手机无线连接质量，也是 QCOM 从 modem 扩展价值量的关键 |
| Snapdragon | Qualcomm 面向手机、PC、汽车等的品牌平台 | 高端 Android 手机最核心的品牌资产 |
| Dragonwing | Qualcomm 面向工业和边缘网络 IoT 的产品品牌 | 多元化业务的重要抓手 |
| QCT | Qualcomm CDMA Technologies，芯片/系统产品业务 | 收入大头，周期性更强 |
| QTL | Qualcomm Technology Licensing，专利授权业务 | 利润率极高，是现金流质量的核心 |
| ADAS/AD | 高级驾驶辅助 / 自动驾驶 | 汽车芯片长期增长方向 |
| On-device AI | AI 在手机、PC、车、IoT 设备本地运行，而不全靠云端 | QCOM 未来叙事核心 |
| Custom silicon | 为大客户定制芯片 | QCOM 进入数据中心的重要路径 |

### Qualcomm 怎么赚钱？

**QCT 芯片业务**：

- Qualcomm 设计芯片和系统软件。
- 台积电/三星等代工厂制造芯片。
- Qualcomm 卖给手机 OEM、汽车厂商/一级供应商、IoT/网络设备厂商。
- 赚取芯片毛利和平台附加价值。

**QTL 授权业务**：

- Qualcomm 授权专利组合给设备制造商。
- 被授权方按照设备销售或协议条款付 royalty。
- 该业务成本低、利润率高，Q2 FY2026 EBT margin **72%**。

**QSI 战略投资**：

- 做战略投资，不是核心利润来源。

### 价值链位置

QCOM 在价值链中不是终端品牌商，而是核心技术平台商：

- 上游：晶圆代工、封测、EDA/IP、存储/RF 元件供应链。
- 中游：Qualcomm 设计 SoC、modem、RF、连接、AI 加速、汽车平台。
- 下游：Samsung、小米、OPPO、vivo、荣耀、汽车厂商、IoT 厂商、PC OEM 等。
- 终端：手机用户、汽车用户、工业设备、网络边缘设备。

核心经济问题是：Qualcomm 能否在手机之外，把过去在移动通信中积累的低功耗计算、无线连接、AI、RF 和软件平台能力，复制到汽车、IoT、PC、XR、机器人和数据中心边缘/推理场景。

---

## 3. Segment and Product Analysis

### 3.1 QCT：芯片和系统产品，收入主引擎

QCT 是 Qualcomm 的半导体业务，FY2026 Q2 revenue **$9.076B**，同比 -4%；EBT **$2.465B**，EBT margin **27%**。

QCT 分为三条主要收入流：

| QCT revenue stream | Q2 FY2026 | YoY | 解释 |
|---|---:|---:|---|
| Handsets | $6.024B | -13% | 手机芯片、modem、RF、Snapdragon 平台 |
| Automotive | $1.326B | +38% | 数字座舱、连接、ADAS/AD、Snapdragon Digital Chassis |
| IoT | $1.726B | +9% | 消费电子、工业、边缘网络、PC/XR/设备连接 |
| Total QCT | $9.076B | -4% | 芯片业务总收入 |

#### Handsets：最大现金牛，也是最大拖累

手机仍是 QCT 最大收入来源。Q2 FY2026 handsets revenue $6.024B，占 QCT 约 66%。但同比 -13%，说明近端压力明显。

公司 Q2 earnings release 指出，Q3 指引包含内存供给约束和相关定价对若干 handset OEM 需求的影响；公司预计来自中国客户的 QCT handset revenues 会在 Q3 触底，并在下一季度恢复环比增长。

**投资意义**：如果 Q3 真是底部，QCOM 当前估值较有吸引力；如果不是，市场会继续把 QCOM 当作手机周期股而非 AI/汽车平台股。

#### Automotive：最清晰的多元化亮点

Q2 FY2026 Automotive revenue **$1.326B**，同比 **+38%**，创季度纪录。Q1 FY2026 Automotive revenue $1.101B，同比 +15%，已经连续两个季度超过 $1B。

业务包括：

- 车载连接；
- 数字座舱；
- ADAS/自动驾驶；
- Snapdragon Digital Chassis 平台。

汽车业务的优点是周期更长、设计周期更稳定、平台锁定期较长；缺点是汽车行业价格压力、认证周期、项目延迟和安全责任更复杂。

#### IoT：范围广，质量需要分层

Q2 FY2026 IoT revenue **$1.726B**，同比 **+9%**。Q1 FY2026 IoT revenue $1.688B，同比 +9%。

IoT 覆盖面很广：PC、XR、边缘网络、工业设备、消费电子等。Qualcomm 2025 10-K 把 IoT 分为 consumer、edge networking、industrial 等方向。

IoT 的好处是 TAM 大；问题是内部质量差异很大。PC 和工业可能有长期价值，但消费电子更周期，边缘网络可能有库存周期。因此不能把 IoT 单独当成一个高确定性增长池。

#### Data Center / Custom Silicon：新期权，不应过度提前定价

Q2 FY2026 earnings release 中，CEO 提到：Qualcomm 进入 data center，一项 leading hyperscaler custom silicon engagement 按计划将在 2026 年晚些时候开始初始出货。

此外：

- Q1 FY2026 release 披露公司完成 Alphawave Semi 收购，加速进入数据中心。
- 2026-06-24 8-K 披露，Qualcomm 预计以最多 **19.2M 股** common stock 收购 Modular Inc。

**研究判断**：数据中心是潜在估值上修点，但目前不能按 NVIDIA/AVGO 的数据中心收入规模定价。它更像是“有实质动作的早期期权”：有 hyperscaler engagement、Alphawave、Modular，但还需要订单规模、毛利、客户、量产和收入披露。

### 3.2 QTL：专利授权，高利润现金牛

QTL 是 Qualcomm 最独特的资产。Q2 FY2026 QTL revenue **$1.382B**，同比 +5%；EBT **$994M**，EBT margin **72%**。

2025 10-K 说明，QTL 授权 Qualcomm 的知识产权组合，包括蜂窝标准必要专利和其他有用专利；授权对象覆盖手机、平板、PC、模组、车联网单元、小基站等。

为什么这个业务值钱？

- 手机行业必须使用 3G/4G/5G 等标准。
- Qualcomm 多年参与标准制定并积累了大量基础专利。
- 设备厂商即使用别人的芯片，也可能需要 Qualcomm 授权。
- 成本结构轻，利润率极高。

风险也明显：

- 监管机构和客户长期挑战 Qualcomm 的授权模式。
- 大客户可能重新谈判授权条款。
- 如果终端设备 ASP 或出货结构变差，授权收入承压。

### 3.3 QSI 和投资业务

QSI 是战略投资业务，不是投资 QCOM 的核心理由。它可能产生投资收益或损失，但不应作为估值主锚。

---

## 4. Financial Deep Dive

### 4.1 最近业绩：Q2 FY2026

| Metric | Q2 FY2026 | Q2 FY2025 | YoY |
|---|---:|---:|---:|
| Revenue | $10.599B | $10.979B | -3% |
| GAAP EBT | $2.232B | $3.105B | -28% |
| Non-GAAP EBT | $3.246B | $3.694B | -12% |
| GAAP net income | $7.370B | $2.812B | +162% |
| Non-GAAP net income | $2.840B | $3.172B | -10% |
| GAAP diluted EPS | $6.88 | $2.52 | +173% |
| Non-GAAP diluted EPS | $2.65 | $2.85 | -7% |

Q2 GAAP EPS 很高主要因为 **$5.7B tax benefit / $5.33 per share**，来自 FY2025 Q4 建立的 valuation allowance 释放。这个收益被排除在 non-GAAP 指标外，因此分析经营质量时不能年化 GAAP EPS $6.88。

更真实的经营结论是：

- 收入略降；
- 手机拖累明显；
- 汽车和 IoT 增长抵消一部分压力；
- QTL 稳定增长；
- non-GAAP EPS 下滑但仍保持高盈利。

### 4.2 H1 FY2026 现金流和回购

截至 2026-03-29 的六个月：

| Metric | H1 FY2026 | H1 FY2025 |
|---|---:|---:|
| Revenue | $22.851B | $22.649B |
| Operating income | $5.676B | $6.675B |
| Net cash from operations | $7.414B | $7.141B |
| Capex | $1.082B | $491M |
| Approx. FCF | $6.332B | $6.650B |
| SBC | $1.749B | $1.461B |
| Share repurchases | $5.442B | $3.498B |
| Dividends paid | $1.895B | $1.880B |

QCOM 的现金流质量总体强：H1 FCF 约 $6.3B，即使 capex 上升，仍能覆盖分红和大额回购的大部分。SBC 较高但被回购明显抵消。

股份数趋势：

- 2025-02-03 shares outstanding 约 1.106B。
- 2026-04-27 shares outstanding 约 1.054B。
- 一年多减少约 4.7%。

这说明回购对每股价值有实际贡献，不只是抵消 SBC。

### 4.3 资产负债表

截至 2026-03-29：

| Item | Value |
|---|---:|
| Cash and cash equivalents | $5.435B |
| Marketable securities current | $4.364B |
| Cash + securities | ~$9.799B |
| Long-term debt | $14.772B |
| Current debt | $498M |
| Total debt used | ~$15.270B |
| Net debt | ~$5.471B |
| Total assets | $57.136B |
| Total liabilities | $29.858B |
| Stockholders' equity | $27.278B |
| Inventory | $7.368B |

净债务不重，利息覆盖充足。StockAnalysis 显示 Debt/EBITDA 约 1.16、Interest Coverage 约 16.82。对 QCOM 这种现金流公司，债务不是核心风险，核心风险是收入结构和估值倍数。

### 4.4 FY2026 Q3 指引

Q2 release 给出的 Q3 FY2026 指引：

| Metric | Q3 FY2026 guidance |
|---|---:|
| Revenue | $9.2B-$10.0B |
| QCT revenue | $7.9B-$8.5B |
| QTL revenue | $1.15B-$1.35B |
| GAAP diluted EPS | $1.26-$1.46 |
| Non-GAAP diluted EPS | $2.10-$2.30 |

这份指引偏保守，说明 Q2 到 Q3 会有环比压力。管理层预计中国 handset revenue 在 Q3 触底，随后季度恢复环比增长。这个判断是未来 1-2 个季度最关键的验证点。

---

## 5. Management and Capital Allocation

### 管理层与战略

CEO Cristiano Amon 的核心战略是把 Qualcomm 从手机通信芯片公司扩展为“intelligent computing everywhere”：

- 手机仍是核心；
- 汽车成为第二增长曲线；
- IoT / edge / industrial / PC / XR 扩展 Snapdragon 和 Dragonwing；
- 数据中心 custom silicon、Alphawave、Modular 是新方向；
- On-device AI 是共同技术主线。

这一路径逻辑清楚：Qualcomm 的低功耗、高性能、连接、AI 加速、modem/RF、软件平台能力，可以横向迁移到更多设备。

### 资本配置

QCOM 的资本配置相对股东友好：

- Q2 FY2026 returned $3.7B to stockholders，包括 $945M dividends 和 $2.8B repurchases。
- H1 FY2026 repurchases $5.442B，dividends $1.895B。
- 公司宣布新的 **$20B share repurchase authorization**。
- 股息率约 2.07%。

这使 QCOM 和许多高估值 AI 股票不同：即便增长没有爆发，股东仍获得分红和回购支撑。

### 收购：Alphawave 和 Modular

- Alphawave：Q1 FY2026 release 称已完成收购，用于加速数据中心扩张。
- Modular：2026-06-24 8-K 披露，Qualcomm 预计最多发行 19.2M 股收购 Modular。

**评价**：这些收购符合“从边缘 AI/移动计算扩展到数据中心和 AI 软件栈”的方向，不算明显偏离使命；但需要跟踪整合、商誉/无形资产、SBC、摊销、以及是否产生实质收入。

---

## 6. Valuation Work

### 6.1 当前估值快照

| Item | Value |
|---|---:|
| Price | $177.98 |
| Market cap | $187.59B |
| Enterprise value | $193.06B |
| Shares outstanding | ~1.05B |
| TTM revenue | $44.49B |
| TTM net income | $9.92B |
| TTM FCF implied by EV/FCF | ~$12.5B |
| PE | 19.44x |
| Forward PE | 18.05x |
| P/FCF | 15.0x |
| EV/FCF | 15.44x |
| EV/Sales | 4.34x |
| EV/EBITDA | 14.85x |
| Dividend yield | 2.07% |

对一个成熟半导体平台，15x FCF、约 18x forward PE 并不激进。关键问题是：未来 EPS/FCF 是停滞、下滑，还是随着汽车/IoT/数据中心多元化重新增长。

### 6.2 为什么用 P/E + FCF + EV/Sales 三种方式？

QCOM 是盈利成熟公司，不适合只用 EV/Sales。更合理的是：

- **P/E**：衡量成熟盈利能力；
- **P/FCF / EV/FCF**：衡量真实现金回报；
- **EV/Sales**：辅助检查半导体周期和多元化收入规模；
- **场景估值**：反映手机周期和新业务兑现的不确定性。

### 6.3 场景估值

以 $177.98 为当前价，使用 EPS multiple 和 FCF multiple 交叉验证。

| Scenario | Core assumptions | Implied price range | Upside/downside vs $177.98 | Trigger |
|---|---|---:|---:|---|
| Bear | 手机继续承压，Apple/中国/华为拖累，汽车/IoT 增速放缓，FY EPS 约 $8.5，市场给 13-15x | **$110-$128** | -38% 至 -28% | Q3 后仍未触底；QTL 或 handset 明显弱于预期 |
| Base | 手机 Q3 触底、Q4 改善，汽车/IoT 保持双位数增长，FY EPS 约 $10.5，市场给 16-20x | **$168-$210** | -6% 至 +18% | Q3 符合指引、Q4 恢复，回购继续降低股本 |
| Bull | 手机稳定，汽车/IoT/PC/数据中心证明新增长曲线，EPS 向 $12.5+，市场给 20-24x | **$250-$300** | +40% 至 +69% | 数据中心初始出货与汽车 pipeline 被证明，市场重新定价 QCOM 为 AI edge/platform company |

FCF 交叉验证：

- Bear：FCF $10B、12-15x，扣净债务后约 **$109-$137/share**。
- Base：FCF $12.5B、14-18x，约 **$161-$208/share**。
- Bull：FCF $15B、18-22x，约 **$251-$308/share**。

两种方法给出的区间一致：当前 $178 靠近 base case 中位偏低，不是深度安全边际，但比多数高预期 AI 股票合理。

### 6.4 实用价格区间

| Zone | Price range | Meaning |
|---|---:|---|
| 强安全边际区 | $120-$145 | 手机周期悲观已充分反映，FCF yield 较高，适合长期研究/分批 |
| 可研究/小仓观察区 | $145-$175 | base case 下有吸引力，但需确认 Q3 手机触底 |
| 合理价值区 | $175-$210 | 当前所在附近；需要 Q3/Q4 验证才有明显上行 |
| 偏贵/需新增长兑现区 | $210-$250 | 需要汽车/IoT/数据中心催化 |
| Bull-case 区 | $250+ | 需要市场确认 QCOM 是 AI edge/data-center platform，而不只是手机芯片股 |

---

## 7. Catalysts and Monitoring Plan

### 近端催化

1. **2026-07-29 Q3 FY2026 earnings**：验证 Q3 revenue $9.2B-$10.0B、non-GAAP EPS $2.10-$2.30。
2. **中国 handset revenue 是否触底**：管理层明确说预计 Q3 触底、下一季度恢复环比增长。
3. **Automotive 是否继续创新高**：Q2 +38%，是最强多元化证据。
4. **IoT 是否保持增长**：Q1/Q2 均 +9%，若加速则估值可上修。
5. **Data center initial shipments**：leading hyperscaler custom silicon engagement 是否按计划在 2026 年晚些时候初始出货。
6. **Modular 收购进展**：最多 19.2M 股发行是否完成，整合计划和收入路线图。

### 需要跟踪的指标

- QCT handset revenue and YoY / QoQ growth。
- QCT automotive revenue and design-win pipeline。
- QCT IoT revenue by end market if disclosed。
- QTL revenue and EBT margin。
- Non-GAAP EPS vs GAAP EPS gap。
- SBC and share count。
- FCF after capex。
- Buyback pace and average repurchase price。
- Inventory trend：2026-03-29 inventory $7.368B，需防止库存压力。
- China revenue and export-control disclosures。
- Apple modem / customer vertical integration updates。

---

## 8. Risk Register

| Risk | Probability | Severity | Mechanism | Monitoring signal |
|---|---|---:|---|---|
| 手机周期继续下行 | Medium-high | High | Handsets 仍是 QCT 大头，Q2 -13% | Q3/Q4 handset 未恢复环比增长 |
| Apple / 大客户自研 | High | High | 客户自研 modem/SoC 减少 QCOM 内容价值 | Apple modem rollout、premium Android share loss |
| 中国/华为/地缘政治 | High | High | 华为份额、出口限制、客户转向本土芯片 | China OEM revenue、license payments、出口规则 |
| QTL 授权模式受挑战 | Medium | High | 客户/监管挑战 royalty 模式 | 诉讼、监管、授权续约条款变化 |
| 新业务低于预期 | Medium | Medium-high | 汽车/IoT/数据中心无法抵消手机成熟 | Automotive/IoT 增速放缓，data center 无收入披露 |
| 收购整合/稀释 | Medium | Medium | Alphawave/Modular 需要整合，Modular 最多发行 19.2M 股 | SBC、摊销、商誉减值、收入贡献不足 |
| 库存/毛利压力 | Medium | Medium | 内存供给约束、库存上升、价格压力 | Inventory rising, QCT EBT margin falling |

### 最强反证

如果 Q3 之后 handset 没有触底、QTL 开始下滑、汽车/IoT 增长放缓、而数据中心仍停留在“engagement/roadmap”没有收入规模，QCOM 就会继续被市场当作低增长手机周期股，合理估值应靠近 bear/base 下沿。

---

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: A。QCOM 披露充分、历史长、业务被市场充分研究；风险是把公司新 AI/汽车叙事过度包装，忽略手机仍是现金流主引擎。
- **Main research blind spot**: 公开数据不能完全证明 data center custom silicon、Modular/Alphawave 的单位经济性和客户粘性。
- **Strongest reason smart investors may disagree**: 多头会说 QCOM 被低估为手机股，空头会说所谓多元化不足以抵消 Apple/中国/手机成熟压力。

### 9.1 Buffett-style lens

- **Conclusion**: Suitable for further research / potentially suitable at the right price（适合进一步研究，价格合适可纳入长期候选）
- **Key question**: 这是不是一个可理解、能长期产生高现金流、并以合理价格买到的业务？

**Evidence supporting the thesis**:

- QTL 是高利润授权业务，Q2 FY2026 EBT margin 72%。
- TTM FCF 约 $12.5B，P/FCF 约 15x。
- H1 FY2026 operating cash flow $7.414B，FCF 约 $6.332B。
- 公司持续分红和回购，H1 repurchases $5.442B，dividends $1.895B。
- Shares outstanding 从 2025-02 的 1.106B 降至 2026-04 的 1.054B。

**Evidence against the thesis**:

- 手机业务仍主导利润，Q2 handsets -13%。
- 大客户自研和 Apple/中国问题长期存在。
- GAAP EPS 有大额 tax benefit 扭曲，必须看 non-GAAP 和 FCF。
- 新业务还不足以完全改变市场对 QCOM 的手机周期股定位。

**Decision implication**: 当前 $178 不是深度安全边际，但对长期投资者而言已进入可研究/可小仓观察区；更理想买点在 $145-$175，强安全边际在 $120-$145。

**Follow-up question**: 如果股市关闭五年，令人舒服的证据是 QTL 稳定、手机不崩、汽车/IoT 继续扩张、FCF 和股本回购持续；令人不舒服的是 Apple/中国/自研持续侵蚀，同时新业务没有规模。

### 9.2 Munger-style lens

- **Conclusion**: Needs further observation（需要继续观察）
- **Key question**: 这笔投资最容易在哪些地方被“好公司叙事”骗到？

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| 把 QCOM 错看成纯 AI 股 | Data center 还早，收入规模未披露 | 给太高倍数，回报不达预期 |
| 手机周期低估 | Handsets 仍是最大收入池 | EPS 下修，估值靠近 bear case |
| 客户自研 | Apple/大型 OEM 减少外购内容 | 长期增长率下移 |
| 授权模式争议 | QTL royalty 被挑战或重谈 | 高利润现金牛受损 |
| 收购整合失败 | Alphawave/Modular 不产生预期协同 | 稀释、摊销、减值 |

**Fragile assumptions**:

- Q3 是 handset 底部。
- Automotive + IoT 可以持续双位数增长。
- Data center custom silicon 能从 engagement 变成大规模收入。
- 回购价格足够理性，不会在高位消耗过多现金。

**Incentive structure**: 管理层有动力讲“AI everywhere”和多元化故事，但投资者必须要求收入、毛利、FCF 和每股价值证据。

**Psychological traps**:

- “便宜的 AI 半导体”叙事；
- 用 Q2 GAAP EPS $6.88 年化；
- 忽略 QTL 法律/监管折价；
- 只看回购金额，不看回购价格和新收购稀释。

**Major stupidity risk**: 在 data center 收入尚未规模化前，按高增长 AI 倍数买入；或在手机低谷时完全忽略 QTL/FCF 价值。

**Follow-up question**: 如果三年后投资错误，今天最明显的红旗可能是：投资者低估了 Apple/中国/手机业务对总利润的牵引力。

### 9.3 Duan Yongping-style lens

- **Conclusion**: Suitable if price and patience are right（价格合适且有耐心时适合）
- **Business essence**: Qualcomm 把无线连接、低功耗计算和 AI 能力做成芯片平台，并把基础通信专利授权给整个无线设备行业。

**User value**:

- 手机厂商需要 Snapdragon、modem、RF、AI/NPU 等能力做高端产品。
- 汽车厂商需要数字座舱、连接、ADAS/AD 平台。
- IoT 和工业客户需要可靠低功耗连接和边缘计算。
- 授权客户需要合法使用 3G/4G/5G 等专利。

**Product / brand strength**:

- Snapdragon 在 Android 高端市场有强品牌。
- QTL 专利组合是行业级资产。
- 低功耗计算和连接能力可以迁移到 PC、汽车、XR、IoT。

**People and culture**:

管理层方向清楚：从手机到 intelligent computing everywhere。但收购和新业务必须证明不是为了追 AI 热点，而是强化核心能力。

**Right price**:

- $120-$145：明显更舒服。
- $145-$175：值得认真研究/小仓观察。
- $175-$210：合理但需要验证。
- $210+：需要新增长曲线证据。

**Follow-up question**: QCOM 是在创造长期客户价值，还是主要受益于手机换机周期和 AI 叙事窗口？当前证据显示长期价值存在，但转型兑现仍需观察。

### 9.4 Li Lu-style lens

- **Conclusion**: Suitable for watchlist / potentially long-term node（适合重点跟踪，可能是长期产业节点）
- **Key question**: 站在 10-20 年视角，QCOM 是否仍是无线连接和边缘智能的重要节点？

**Circle of competence**:

可通过公开数据理解：收入、分部利润、QTL 授权、现金流、回购、手机周期。较难通过公开数据完全理解：data center custom silicon 客户、未来 Apple 自研影响、汽车 pipeline 真实利润率。

**Industry trend**:

- 5G/6G、Wi-Fi、边缘 AI、汽车智能化、工业 IoT、机器人、XR/可穿戴、低功耗 AI 设备，是长期趋势。
- QCOM 在“云端 AI 训练”不是最核心，但在“边缘设备 AI 推理 + 连接”处于较重要位置。

**Downside protection**:

- FCF 强、QTL 高利润、回购和分红提供保护。
- 但如果手机利润池下移，保护会减弱。

**Margin of safety**:

当前价格有一定合理性，但安全边际不算厚。若跌到 $145 以下而基本面未恶化，吸引力显著提升。

**Research-depth decision**:

值得继续跟踪，尤其是 Q3/Q4 FY2026。若手机触底确认，QCOM 可能成为“合理估值 AI edge/汽车半导体”候选。

**Follow-up question**: 10-20 年后，QCOM 是智能设备与无线连接的持久节点，还是手机黄金时代后的成熟现金牛？答案取决于汽车/IoT/数据中心能否真正成为第二曲线。

### 9.5 Composite score

| Dimension | Score |
|---|---:|
| Business model | 8/10 |
| Moat | 8/10 |
| Management | 7/10 |
| Financial quality | 8/10 |
| Valuation attractiveness | 7/10 |
| Long-term certainty | 6/10 |
| Downside risk control | 7/10 |

- **Business model 8**：芯片+授权组合稀缺，现金流强。
- **Moat 8**：专利组合、标准参与、Snapdragon 平台、RF/modem 集成形成壁垒，但客户自研削弱护城河。
- **Management 7**：战略清晰，资本回报积极；收购整合和数据中心路线仍需验证。
- **Financial quality 8**：FCF 强、ROIC 高、资产负债表可控；SBC 和一次性 tax benefit 需调整。
- **Valuation 7**：15x FCF 不贵，但不是深度折价。
- **Long-term certainty 6**：手机确定性下降，新曲线确定性尚未完全建立。
- **Downside risk 7**：现金流、分红、回购支撑较好，但周期和客户风险仍会带来 25%-40% 下行。

### 9.6 Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 高质量成熟半导体+授权平台 | High |
| Moat | QTL 和连接平台强，但客户自研是长期侵蚀 | Medium-high |
| Management and capital allocation | 分红回购积极，AI/汽车/数据中心方向合理 | Medium |
| Biggest risk | 手机业务和关键客户拖累超过多元化贡献 | High |
| Long-term trend | 边缘 AI、汽车智能化、IoT 连接长期趋势真实 | Medium-high |
| Valuation and margin of safety | 当前合理偏有吸引力，但安全边际一般 | Medium |

| Investor state | Research implication |
|---|---|
| No position | 可放入重点观察；$145-$175 更适合分批研究，$120-$145 更有安全边际 |
| Existing position | 若仓位不大，可继续持有跟踪 Q3/Q4；不宜把它当作高 beta AI 纯弹性 |
| Add / upgrade signal | Q3 handset 触底确认、Q4 恢复、Automotive/IoT 持续双位数、data center 初始出货披露 |
| Reduce / downgrade signal | Q3/Q4 继续下修、QTL 走弱、Apple/中国冲击扩大、收购稀释但无收入证据 |

---

## 10. Final Research Framework

### 这个投资逻辑依赖什么？

1. 手机业务在 Q3/Q4 FY2026 附近触底，而不是持续恶化。
2. QTL 授权业务维持高利润率和稳定收入。
3. Automotive 继续高速增长，并证明数字座舱/ADAS 平台价值。
4. IoT 不只是周期性消费电子，而能在工业/边缘网络/PC/XR 中形成稳定增长。
5. Data center custom silicon、Alphawave、Modular 能产生实质客户收入，而不是只停留在战略叙事。
6. 回购继续降低股本，且不被收购发行和 SBC 完全抵消。
7. 中国/Apple/监管风险不出现超预期恶化。

### 什么会让观点更积极？

- Q3 FY2026 符合或超过 revenue $9.2B-$10.0B、non-GAAP EPS $2.10-$2.30。
- 管理层确认 Chinese handset revenue 已触底并 Q4 环比增长。
- Automotive revenue 继续创新高，QCT EBT margin 稳住或改善。
- Data center initial shipments 如期发生，并披露可量化 revenue/pipeline。
- 回购持续降低股本，FCF 保持 $12B+ run-rate。

### 什么会改变观点？

**上调至 Positive**：股价仍在 $145-$180 区间，同时 Q3/Q4 证明 handset 触底、Automotive/IoT 保持强增长、data center 不是空叙事。

**下调至 Neutral/Negative**：Q3 后 handset 没有触底、QTL revenue/EBT margin 开始下滑、库存继续上升、数据中心没有可量化进展、或 Modular/Alphawave 造成明显稀释/摊销/整合压力。

### Final answer

QCOM 是比多数 AI 热门股更“现金流友好”的半导体标的：估值不离谱、FCF 强、QTL 护城河深、回购和分红扎实。但它不是无风险便宜货，手机周期、Apple/中国和客户自研是长期折价来源。当前 $178 附近属于 **合理偏有吸引力但需要 Q3/Q4 验证** 的区域；若跌到 $145-$175 且基本面未恶化，风险收益更好；若跌到 $120-$145，则更接近强安全边际区。

---

## Sources

- SEC, Qualcomm FY2025 Form 10-K filed 2025-11-05.
- SEC, Qualcomm FY2026 Q2 Form 10-Q filed 2026-04-29.
- SEC, Qualcomm FY2026 Q2 earnings 8-K Exhibit 99.1 filed 2026-04-29.
- SEC, Qualcomm FY2026 Q1 Form 10-Q and earnings 8-K Exhibit 99.1 filed 2026-02-04.
- SEC, Qualcomm 8-K filed 2026-06-24 regarding Modular acquisition share issuance.
- SEC companyfacts API for financial statement and share-count data.
- StockAnalysis QCOM quote/statistics pages for 2026-07-15 close, market cap, EV, multiples, dividend yield, shares outstanding and next earnings date.
