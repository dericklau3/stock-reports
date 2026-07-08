# Rocket Lab（RKLB）深度研究更新 - 2026-07-08

- **Research view**: 建设性但需观察；股价回落后风险回报改善，但 Iridium 交易让故事从“高成长航天制造/发射平台”升级为“端到端航天基础设施 + 在轨网络运营商”，复杂度显著上升
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: RKLB 是少数已经证明 Electron 发射执行、Space Systems 制造能力、国防项目获取和垂直整合能力的上市航天公司。2026Q1 revenue 2.003 亿美元、同比 +63.5%，backlog 22.20 亿美元，流动性强。股价从 2026-05-12 的 117.56 美元回落到 2026-07-07 的 83.41 美元，EV/Sales 从约 98x 降到约 69x，估值压力明显缓解。但 2026-06-28 宣布收购 Iridium Communications 是战略拐点：若成功，RKLB 将把“造火箭/造卫星/发射任务”延伸到“拥有在轨通信网络和现金流客户”；若失败或整合不佳，则可能稀释、分散管理层、增加监管和债务/现金压力。
- **Key risk**: 最大风险从单一的“Neutron 何时成功”扩展为三重风险：Neutron 技术/进度风险、Iridium 并购整合/审批/资本结构风险，以及当前仍高达约 69x TTM EV/Sales 的估值风险。公司仍亏损、TTM FCF 为 -3.163 亿美元，share count 一年增长约 11.16%，容错率仍低。

> 本文是研究支持与决策框架，不构成个性化投资建议。RKLB 是高 beta、高估值、仍亏损的航天成长股，适合与组合风险约束一起评估。

## 1. Executive View

**研究观点：建设性但需观察。**

和 2026-05-13 版报告相比，本次有两个重大变化：

1. **股价和估值明显回落。** 2026-05-12 RKLB 收盘 117.56 美元，市值约 680 亿美元，EV/Sales 约 98x；2026-07-07 收盘 **83.41 美元**，盘后约 **83.75 美元**，市值约 **482.8 亿美元**，enterprise value 约 **469.5 亿美元**，TTM revenue **6.796 亿美元**，EV/Sales 约 **69.1x**。估值压力缓解，但仍极高。
2. **Iridium 交易改变公司边界。** 2026-06-28，Rocket Lab 与 Iridium Communications 签署 merger agreement。每股 Iridium common stock 将获得 **27 美元现金 + RKLB 股票**；股票部分通过 collar 机制给出大约 27 美元价值，交易完成取决于 Iridium 股东批准、HSR、FCC 及其他监管审批、S-4 注册声明生效等。若完成，RKLB 将从 launch + space systems 扩展到拥有大型在轨卫星通信网络的运营公司。

我的结论：**股价回落后，RKLB 已从“几乎只适合观察”变成“可认真研究、但仍不宜重仓追高”的区间。** 当前 83 美元附近相较 5 月 117 美元的风险回报改善，但不是便宜；真正的安全边际仍取决于 Neutron 里程碑、Q2/Q3 收入/毛利、Iridium 交易定价与审批、以及现金流/稀释路径。

最强正面理由：RKLB 可能是除 SpaceX 外，极少数有机会同时覆盖 launch、satellite manufacturing、space components、national security missions、on-orbit services 和 now potentially satellite communications network 的上市平台公司。

最强反方理由：当前估值仍要求公司在未来 3-5 年完成多个困难任务——Neutron 成功、Space Systems 高增长、Iridium 整合成功、亏损收窄、稀释受控——任何一个环节出问题都可能导致估值继续压缩。

## 2. Business Model and Industry Structure

### 初学者版：Rocket Lab 到底怎么赚钱？

Rocket Lab 的业务可以理解为“帮客户把东西送上太空，并且越来越多地帮客户制造和运营太空里的东西”。

它现在主要有两条线：

- **Launch Services 发射服务**：客户付钱，让 RKLB 用 Electron 火箭把小卫星送入特定轨道；HASTE 用于高超音速测试；Neutron 是在研中型可复用火箭，目标是承载更大载荷和更多国防/星座任务。
- **Space Systems 空间系统**：客户付钱购买卫星平台、卫星组件、太阳能阵列、星敏感器、反作用轮、无线电、分离系统、光通信终端、任务运营等。简单说，RKLB 不只是“送快递上太空”，还卖“卫星零部件和整机”。

如果 Iridium 交易完成，公司还会增加第三层：

- **在轨通信网络运营**：Iridium 拥有全球卫星通信网络，客户为移动卫星语音/数据、IoT、政府通信、海事/航空等服务付费。这会让 RKLB 不仅是卖设备和发射服务，也拥有一部分 recurring service revenue。

核心经济问题：**Rocket Lab 能否把发射执行、卫星制造、国防订单、并购整合和未来在轨网络运营组合成一个能产生持续自由现金流的平台，而不是一直靠高估值股权融资来追逐更大 TAM？**

### 关键术语翻译

- **Electron**：Rocket Lab 已商业化的小型运载火箭，适合小卫星专属发射。
- **HASTE**：基于 Electron 的高超音速测试发射平台，主要服务国防客户。
- **Neutron**：Rocket Lab 在研的中型可复用火箭，是估值核心期权。
- **Backlog**：已签合同但尚未确认收入的订单金额，代表未来收入可见度。
- **Book-to-bill**：新增订单 / 当期收入，>1 表示订单池在增长。
- **Space Systems**：卫星、组件、子系统、光通信、任务运营等空间基础设施产品。
- **SBI / Golden Dome**：美国导弹防御/天基拦截相关国防项目，潜在规模大但不确定性高。
- **Collar**：并购股票对价中的价格保护机制，股价在不同区间时换股比例调整。
- **ATM offering**：at-the-market 股权发行，公司在市场上逐步卖新股融资，会稀释股东。

## 3. Segment and Product Analysis

### 当前业务：Launch Services + Space Systems

2026Q1：

- Total revenue：**2.003 亿美元**，同比 **+63.5%**。
- Launch Services revenue：**6366 万美元**，同比 **+79%**。
- Space Systems revenue：**1.367 亿美元**，同比 **+57%**。
- Total GAAP gross margin：**38.2%**。
- Launch Services gross margin：**44.3%**。
- Space Systems gross margin：**35.3%**。
- Backlog：**22.20 亿美元**，较 2025 年底 **18.47 亿美元** 增长约 20%。

这说明 RKLB 已经不是纯小火箭公司。Space Systems 是收入主体，Launch Services 是品牌/技术/客户入口，Neutron 是平台跃迁期权。

### Electron / HASTE：当前可信度基础

Electron 已证明 RKLB 能持续执行真实发射任务。2026Q1 公司完成 6 次 Electron launch missions；revenue per launch 从 Q1 2025 的 710 万美元升至 930 万美元，cost per launch 从 570 万美元降至 540 万美元。这是很重要的单位经济改善信号。

HASTE 则把 Electron 能力延伸到高超音速测试和国防任务。公司 2026Q1 签下 31 个新的 Electron and HASTE contracts，并披露 Anduril/MACH-TB 相关 **3000 万美元** HASTE hypersonic launches contract。

### Neutron：估值核心，但还没证明

Neutron 是中型可复用火箭，目标是进入比 Electron 大得多的市场：商业星座、国家安全发射、探索任务、未来可能的自有/合作星座部署。

如果 Neutron 成功，它会让 RKLB 从“小发射 + 空间组件”升级为“商业和国防中型发射替代方案”。如果 Neutron 失败或延迟，当前估值中的很多长期平台溢价会被削弱。

2026Q1 公司披露已签 5 个 dedicated Neutron launches，launch manifest 超过 70 个 contracted missions。这个进展正面，但真正的价值验证仍是首飞、复用、成本、cadence 和客户复购。

### Space Systems：收入主体和垂直整合核心

Space Systems Q1 2026 收入 1.367 亿美元，占总收入约 68%。它包括 spacecraft manufacturing、optical systems、solar solutions、star trackers、reaction wheels、radios、separation systems、mission operations 等。

近期并购显示管理层正在强化垂直整合：

- **Mynaric**：laser optical communications terminals，建立 Rocket Lab Europe，增强光通信能力。
- **Motiv Space Systems**：space robotics、motion control、precision mechanisms，尤其补齐 solar array drive assemblies 等紧缺组件。
- **GEOST / defense payload capability**：增强国防载荷和空间感知能力。

这条线的好处：比纯发射更高收入可见度、更接近国防/星座长期预算，也能提高每个任务的内容价值。风险：项目制收入容易受成本估计、交付延期、客户变更和并购整合影响。

### Iridium 交易：从“卖铲子”到“拥有矿山”？

2026-06-28 RKLB 与 Iridium Communications 签署合并协议。对 RKLB 来说，这是非常大的战略变化。

潜在正面：

- Iridium 拥有全球在轨通信网络和既有客户，能带来 recurring service revenue。
- RKLB 可用自身制造/发射能力降低未来星座补网、升级和维护成本。
- 从一次性项目收入，扩展到长期通信服务收入，理论上提高商业模式质量。
- 国防、海事、航空、IoT、偏远地区通信等应用与 RKLB 国防航天方向有协同。

潜在负面：

- 交易需要现金 + 股票，对 RKLB 资本结构和股东稀释有影响。
- Iridium 是成熟运营商，增长曲线和 Rocket Lab 高成长逻辑不同。
- 整合在轨网络运营、通信监管、FCC/国际审批、客户合同、债务和卫星生命周期管理，复杂度显著高于收购组件公司。
- 管理层在 Neutron 首飞关键期同时推动大并购，执行分心风险上升。

简化理解：过去 RKLB 更像“太空基础设施供应商”；收购 Iridium 后，它可能变成“太空基础设施供应商 + 在轨通信网络运营商”。这可能提高长期平台价值，也可能让公司从清晰的高成长制造/发射故事变成复杂的并购整合故事。

## 4. Financial Deep Dive

### Q1 2026 业绩

- Revenue：**2.003 亿美元**，同比 **+63.5%**。
- Gross profit：**7649 万美元**。
- GAAP gross margin：**38.2%**。
- R&D expense：**8051 万美元**。
- SG&A expense：**5195 万美元**。
- Operating loss：**5597 万美元**。
- Net loss：**4502 万美元**。
- Diluted EPS：**-0.07 美元**。
- Stock-based compensation：**2812 万美元**。
- Adjusted EBITDA loss：**1175 万美元**。

Q1 质量总体不错：收入、毛利、backlog 都强；adjusted EBITDA loss 收窄。但公司仍亏损，R&D + SG&A 合计超过收入 66%，说明仍处于高投入阶段。

### TTM 和资产负债表快照

StockAnalysis 2026-07-07/08 数据：

- TTM revenue：**6.7958 亿美元**。
- TTM gross profit：**2.4843 亿美元**。
- TTM net income：**-1.8262 亿美元**。
- TTM operating cash flow：**-1.6163 亿美元**。
- TTM capex：**-1.5467 亿美元**。
- TTM free cash flow：**-3.1630 亿美元**。
- Cash：**13.8 亿美元**。
- Total debt：**1.3867 亿美元**。
- Net cash：约 **13.4 亿美元**。
- Shares outstanding：**5.7887 亿股**。
- Shares change YoY：**+11.16%**。
- Current ratio：**4.47**。

资产负债表强，这是 RKLB 能继续投资 Neutron、并购和产能的核心保障。但资金来自股权融资：公司 2026Q1 ATM equity offerings 带来约 **4.503 亿美元** proceeds；2026-05-20 又提交最高 **30 亿美元** common stock ATM/forward sale prospectus supplement。高股价融资从企业角度合理，但对每股价值是稀释。

### Q2 2026 指引

公司 Q1 后给出 Q2 2026 指引：

- Revenue：**2.25-2.40 亿美元**。
- GAAP gross margin：**33%-35%**。
- Adjusted EBITDA loss：**-2000 万至 -2600 万美元**。

这意味着 Q2 收入继续创新高，但毛利率预计低于 Q1，adjusted EBITDA loss 扩大。投资者需要判断这是 mix/项目节奏的短期波动，还是毛利和费用压力回归。

## 5. Management and Capital Allocation

Peter Beck 和团队的执行记录仍是 RKLB 的核心资产。Electron 的商业化、HASTE 的国防应用、Space Systems 的规模化、并购补能力，都说明公司不是普通 space SPAC。

资本配置现在进入更激进阶段：

1. **Neutron 高投入**：这是未来估值上限的关键。
2. **Mynaric/Motiv/GEOST 并购**：补齐光通信、机器人、精密机构和国防载荷。
3. **潜在 Iridium 大并购**：把公司扩展到在轨通信运营。
4. **ATM 股权融资**：用高估值股票换现金，支持扩张。

优点：管理层在窗口期融资和并购，战略雄心大；缺点：执行面太多，且每股股东要承受稀释和整合风险。

## 6. Valuation Work

### 当前估值快照

基于 2026-07-07 Nasdaq / StockAnalysis：

- 收盘价：**83.41 美元**。
- 盘后价：约 **83.75 美元**。
- 52 周区间：**35.28-151.00 美元**。
- Market cap：约 **482.8 亿美元**。
- Enterprise value：约 **469.5 亿美元**。
- Shares outstanding：约 **5.7887 亿股**。
- TTM revenue：**6.7958 亿美元**。
- TTM net loss：**-1.8262 亿美元**。
- TTM FCF：**-3.1630 亿美元**。
- PS ratio：**71.05x**。
- EV/Sales：**69.08x**。
- Forward PS：**49.40x**。
- Beta：**2.55**。
- Consensus 2026 revenue：约 **9.145 亿美元**，增长约 **52.0%**。
- Average analyst price target：**112.73 美元**，17 analysts，consensus Buy。

### 估值方法选择

RKLB 仍亏损，P/E、EV/EBITDA、FCF yield 都不能作为主要估值工具。更适合：

- EV/Sales：衡量市场为未来平台增长支付多少倍收入。
- EV/Backlog：衡量订单可见度的定价。
- Scenario valuation：Neutron 和 Iridium 会大幅改变长期收入/利润结构。
- Dilution-adjusted per-share valuation：必须考虑 ATM、SBC、并购股票对价、preferred conversion。

### 情景估值：2028-2030 视角

| 场景 | 核心假设 | 估值逻辑 | 隐含每股价值区间 | 相对 83.41 美元 |
|---|---|---|---:|---:|
| Bear | Neutron 延期/失败；Iridium 交易失败或整合分散管理层；Space Systems 毛利承压；收入增长降至 20%-30%；FCF 继续为负；市场给 10-18x sales | 高成长但执行受挫的航天供应商 | **25-45 美元** | -70% 至 -46% |
| Base | Neutron 2026/2027 首飞并逐步商业化；Space Systems 维持 30%-40% 增长；Iridium 交易获批但协同需时间；2028-2030 revenue 20-35 亿美元，EBITDA 接近转正；市场给 18-28x sales | 稀缺航天平台但仍高风险 | **60-100 美元** | -28% 至 +20% |
| Bull | Neutron 成功 ramp，成为 Falcon 9 外重要中型发射替代；Space Systems 和国防订单继续放大；Iridium 协同显现，形成 recurring network revenue；长期 revenue 40-60 亿美元，FCF 转正；市场给 25-35x sales | 平台型航天基础设施公司 | **120-200 美元** | +44% 至 +140% |

解释：当前 83 美元在 base case 中部，不再像 117 美元那样明显偏向 bull case，但仍不是强安全边际。它要求 Neutron 和 Space Systems 继续兑现，并且 Iridium 交易不能破坏资本结构和管理专注度。

### 实用价格区间

- **强安全边际区**：35-45 美元。接近 bear/base 交界，更适合长期高风险仓位。
- **可观察 / 小仓试错区**：45-70 美元。对看好 Neutron 和航天平台化的人更合理。
- **合理但仍贵区**：70-95 美元。当前 83.41 美元在此区间，需要 Q2/Q3 和 Neutron/Iridium 进展支撑。
- **偏贵区**：95-120 美元。需要持续好消息和 Q2 后上修。
- **过热区**：120 美元以上。除非 Neutron 首飞和 Iridium 协同显著超预期，否则风险主导。

结合你的组合规则：RKLB beta 约 **2.55**，且仍亏损、估值高、稀释风险大，属于高 beta 高波动成长股。即使看好，也应确保 **现金 + 低 beta / 普通核心股票敞口至少 30%**，并避免把 RKLB 与 AI/半导体/加密等高 beta 仓位叠加过重。

## 7. Catalysts and Monitoring Plan

未来重点跟踪：

1. **Q2 2026 earnings**：预计 2026-08-06 after market close，验证 revenue 2.25-2.40 亿美元和 gross margin 33%-35%。
2. **Neutron first flight timing**：是否仍能在 2026 年 debut。
3. **Archimedes engine qualification**：发动机是 Neutron 成败核心。
4. **Neutron contracted launches**：5 个 dedicated launches 后是否继续增加商业/国防客户。
5. **Electron/HASTE cadence**：任务成功率、revenue per launch、cost per launch。
6. **Space Systems margin**：是否稳定在 35%+，是否有项目成本超支。
7. **Backlog and book-to-bill**：22.20 亿美元 backlog 后是否继续增长。
8. **Iridium transaction progress**：Iridium 股东投票、HSR、FCC、外国投资/卫星通信审批、S-4 注册。
9. **Iridium deal financing and dilution**：现金对价来源、股票对价稀释、交易后债务和现金。
10. **Mynaric/Motiv integration**：光通信和机器人组件是否转化为收入/毛利协同。
11. **ATM issuance and share count**：股数增长是否继续超过业务价值增长。
12. **FCF burn**：TTM FCF -3.163 亿美元，需要逐步收窄。

## 8. Risk Register

- **估值风险：高概率 / 高严重度**。即使从高位回落，EV/Sales 仍约 69x，forward PS 约 49x。
- **Neutron 风险：中高概率 / 高严重度**。首飞、复用、成本和 cadence 都尚未证明。
- **Iridium 并购风险：中高概率 / 高严重度**。审批、整合、资本结构、战略分心和文化差异都重要。
- **稀释风险：高概率 / 中高严重度**。Shares outstanding YoY +11.16%，且有 30 亿美元 ATM/forward sale shelf。
- **现金流风险：中概率 / 高严重度**。TTM FCF -3.163 亿美元，仍需投入。
- **毛利率风险：中概率 / 中高严重度**。Q2 gross margin 指引 33%-35%，低于 Q1 38.2%。
- **项目成本风险：中概率 / 高严重度**。Space Systems 项目制收入可能受成本估计变化影响。
- **SpaceX 竞争：高概率 / 高严重度**。SpaceX 在价格、复用和 cadence 上仍是行业引力中心。
- **国防预算/政治周期风险：中概率 / 中高严重度**。SBI/Golden Dome/MACH-TB 等项目大但政策和预算不确定。
- **发射事故风险：低中概率 / 高严重度**。单次失败可能影响客户信任和 backlog。

最强反证：如果 Q2/Q3 收入增长但毛利率下滑、cash burn 扩大、Neutron 延期，同时 Iridium 交易带来明显稀释或审批不确定，RKLB 的“端到端航天平台”叙事会被市场重新定价。

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B。RKLB 披露较完整，但 Neutron 成功概率、Iridium 协同、国防订单长期规模仍有大量不可验证假设。
- **Main research blind spot**: 公开资料无法证明 Neutron 的真实单位经济、复用成本、发射 cadence，以及 Iridium 并购后的整合回报。
- **Strongest reason smart investors may disagree**: 乐观者认为 RKLB 是上市市场里最接近 SpaceX 的稀缺平台，谨慎者认为它是高估值、未盈利、重稀释、技术风险高的航天概念股。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个业务十年后能否产生可预测、高 ROIC 的自由现金流？
- **Evidence supporting**: Electron 执行记录真实；Q1 revenue +63.5%；backlog 22.20 亿美元；cash/net cash 强；Space Systems 收入主体化。
- **Evidence against**: 公司仍亏损；TTM FCF -3.163 亿美元；Neutron 未证明；Iridium 并购增加复杂度；当前估值仍很高。
- **Decision implication**: 不适合按稳定复利股重仓，更适合高风险创新资产的小仓位跟踪。
- **Follow-up question**: 如果股市关闭五年，Neutron、Space Systems backlog、Iridium recurring revenue 和 FCF 路径是否足以让人安心？

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 投资者最容易在哪里被骗？
- **Failure paths**:
  - 把 SpaceX 稀缺性投射到 RKLB，忽略两者规模和技术差距；
  - 把 backlog 当成高利润收入，忽略成本超支和交付风险；
  - 把 Iridium 交易当成无缝协同，忽略成熟通信运营商整合难度；
  - 忽略 ATM/SBC/股票对价稀释；
  - 在 Neutron 尚未首飞前用成熟平台倍数估值。
- **Decision implication**: 最大错误不是错过 RKLB，而是在多个未验证假设同时成立前给太大仓位。
- **Follow-up question**: 三年后如果错了，今天最明显的红旗是不是“高估值 + 未盈利 + 大并购 + Neutron 未验证”？

### Duan Yongping-style lens

- **Conclusion**: Needs further observation / partly suitable for small exploratory position。
- **Business essence**: RKLB 帮客户制造、发射并运营太空基础设施。
- **User value**: 小卫星专属发射、国防快速响应、空间组件和在轨通信都是真实需求。
- **Product strength**: Electron 证明执行；Space Systems 产品组合扩大；若 Iridium 交易完成，在轨网络提高客户粘性。
- **Evidence against**: 客户价值不等于股东价值；发射和航天制造资本密集、技术风险高、竞争强。
- **Decision implication**: 好公司但价格和执行验证更重要，当前适合观察/小仓而非重仓。
- **Follow-up question**: RKLB 是在创造持久客户价值，还是主要受益于政府航天预算和市场对 SpaceX 稀缺替代品的想象？

### Li Lu-style lens

- **Conclusion**: Suitable for deeper research, not yet high-conviction allocation。
- **Circle of competence**: Electron 发射记录、财报、backlog 可验证；Neutron 单位经济、Iridium 协同、国防预算规模不完全可知。
- **Industry trend**: 卫星、国防空间、通信、地球观测和高超音速测试都是长期结构性趋势。
- **Downside protection**: 现金和 backlog 提供一定保护，但估值太高，downside 更多由倍数压缩决定。
- **Decision implication**: 值得长期深跟；高置信度配置需要更低价格或 Neutron/Iridium 明确兑现。
- **Follow-up question**: 10-20 年后，RKLB 会是太空基础设施里的持久节点，还是本轮航天资本热潮中的高估值赢家？

### Composite score

| Dimension | Score |
|---|---:|
| Business model | 7/10 |
| Moat | 6/10 |
| Management | 8/10 |
| Financial quality | 4/10 |
| Valuation attractiveness | 4/10 |
| Long-term certainty | 5/10 |
| Downside risk control | 4/10 |

评分解释：管理层执行强、业务稀缺，但公司仍亏损、现金流为负、估值高、Neutron 和 Iridium 都未完成验证，因此财务质量和 downside control 分数较低。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 稀缺航天平台，执行力好 | 中高 |
| Moat | Electron 记录、垂直整合、国防关系有壁垒，但 SpaceX 压力大 | 中 |
| Management and capital allocation | 执行强但扩张激进，Iridium 交易提高复杂度 | 中 |
| Biggest risk | 高估值叠加 Neutron/Iridium/稀释三重风险 | 高 |
| Long-term trend | 航天基础设施和国防空间长期顺风 | 中高 |
| Valuation and margin of safety | 83 美元比 117 美元合理，但强安全边际仍在 35-45 美元 | 中 |

### Action framing

| Investor state | Research implication |
|---|---|
| No position | 当前 80 美元附近可观察或小仓试错，但不属于强安全边际。 |
| Existing position | 可继续持有核心观察仓，但应控制高 beta 仓位和稀释风险。 |
| Add / upgrade signal | Neutron 首飞成功、Q2/Q3 超指引、gross margin 稳定、Iridium 审批顺利且融资结构清晰、FCF burn 收窄。 |
| Reduce / downgrade signal | Neutron 延期/失败、Iridium 审批或融资恶化、Space Systems 毛利下滑、share count 快速膨胀、Q2/Q3 指引下修。 |

## 10. Final Research Framework

### 当前是否值得买？

RKLB 当前更适合定义为 **“高质量高风险航天平台，股价回落后可观察/小仓试错，但仍不具备强安全边际”**。

- 若无仓位：83 美元附近可开始认真跟踪，若参与应小仓、分批，等待 Q2 和 Neutron/Iridium 进展。
- 若已有仓位：可以持有观察，但不应忽略估值和稀释；若仓位因上涨过大，应考虑组合风险。
- 若等安全边际：45-70 美元更合理，35-45 美元更接近真正强安全边际。

### What would make the thesis stronger

1. Q2 revenue 达到或超过 2.25-2.40 亿美元指引；
2. Gross margin 没有明显低于 33%-35% 指引；
3. Neutron 2026 首飞成功；
4. Archimedes engine 和复用系统里程碑明确；
5. Backlog 继续增长，book-to-bill >1；
6. Iridium 交易审批顺利，融资/稀释可控；
7. TTM FCF burn 开始收窄；
8. Share count 增速下降。

### What would change my view

上调至 **Positive**：Neutron 首飞成功并披露后续 manifest，Q2/Q3 继续超指引，Space Systems 毛利稳定，Iridium 交易结构清晰且协同可信，FCF burn 收窄。

下调至 **Neutral / Negative**：Neutron 延期或失败，Iridium 交易造成显著稀释/债务/审批拖延，Q2/Q3 revenue 或 margin 低于指引，backlog 增长放缓，share count 继续快速扩张。

## Sources

- SEC: Rocket Lab Form 10-Q for quarter ended March 31, 2026, filed 2026-05-07.
- SEC: Rocket Lab Form 8-K / Exhibit 99.1 Q1 2026 financial results, filed 2026-05-07.
- SEC: Rocket Lab Form 424B5 ATM prospectus supplement, filed 2026-05-20.
- SEC: Rocket Lab Form 8-K, Agreement and Plan of Merger with Iridium Communications Inc., filed 2026-06-29.
- Nasdaq quote API: RKLB quote as of 2026-07-07 close.
- StockAnalysis: RKLB overview, statistics, financials, forecast, accessed 2026-07-08 UTC.
- Rocket Lab News page: May-June 2026 launch, contract, Motiv and Space Force updates, accessed 2026-07-08 UTC.
- Existing local report: `2026-05-13-deep-research.md`.
