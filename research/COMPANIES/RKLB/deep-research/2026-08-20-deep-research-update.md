# Rocket Lab（RKLB）深度研究更新 - 2026-08-20

- **Research view**: Constructive but watchful（建设性但需观察）
- **Confidence**: 中等偏高
- **Time horizon**: 12-24 个月验证 Neutron / backlog / Iridium；3-5 年看端到端航天基础设施平台
- **Main thesis**: RKLB 的 Q2 2026 再次证明业务执行力：record revenue、record backlog、Q3 继续指引 record revenue；Electron/HASTE/Space Systems/国防订单均在扩张，Neutron 仍是估值核心期权，Iridium 交易则把公司边界从“发射 + 航天系统”扩到“发射 + 制造 + 在轨通信网络运营”。
- **Key risk**: 当前价格虽从 7 月 $83.41 回落到 $75.84，但 EV/TTM Sales 仍约 56x，仍是高预期资产；Neutron 尚未首飞、Iridium 交易未完成且可能带来债务/稀释/整合风险，公司仍亏损并烧现金。

> 本文是研究支持与决策框架，不构成个性化投资建议。RKLB 属于高 beta、高估值、仍亏损、资本密集的 space / defense / AI infrastructure 交叉资产，必须和组合风险约束一起看。

## 1. Executive View

**结论：维持 Constructive but watchful。**

和 2026-07-08 版本相比，本次更新的核心变化是：

1. **业务确认继续增强。** Q2 2026 revenue 达 **$234.1M**，同比 **+62%**，高于 Q1 的 $200.3M；backlog 达 **$2.356B**，再创新高；Q3 2026 指引 revenue **$250M-$265M**，意味着公司继续刷新季度收入纪录。
2. **订单质量提升。** 公司披露 Q2 及季后 secured more than **$437M** launch contracts，并使 launch backlog 扩至 **90+ launches**；获得 **$397M** U.S. Space Force SB-AMTI Flatellite spacecraft contract，以及 **$160M+** defense space systems contracts。
3. **Iridium 交易仍是最大结构变量。** 交易价格为每股 IRDM **$54**，其中 **$27 cash + RKLB stock**，collar 为 **$67.50-$112.50**；Iridium enterprise value 约 **$8.0B**，RKLB 已取得 **$3.6B** 364-day senior secured bridge term loan commitment。若完成，RKLB 将拥有 recurring satellite communications revenue；若整合不佳，则显著提高资本结构和管理复杂度。
4. **股价回落改善风险回报，但仍不便宜。** 2026-08-19 收盘 **$75.84**，市值 **$45.39B**，EV **$43.13B**，TTM revenue **$769.15M**，EV/TTM Sales 约 **56.1x**；按 Q3 指引中位数年化收入算，EV/Sales 仍约 **41.9x**。

我的判断：**RKLB 比多数 space SPAC 更真实，也比 5 月/7 月报告时更有业务确认；但它仍不是“便宜股”，而是一个要求多个困难 milestones 连续成功兑现的高预期平台股。**

最强正面理由：RKLB 正在成为少数能同时覆盖 launch、spacecraft manufacturing、components、defense missions、on-orbit operations，以及未来 satellite communications applications 的上市平台。

最强反方理由：当前价格仍把 Neutron 成功、国防订单增长、Space Systems 高增长、Iridium 协同和资本市场持续支持都折现进去；任何一个关键环节延迟或失败，都可能导致估值倍数快速压缩。

## 2. Business Model and Industry Structure

### 初学者版：RKLB 到底怎么赚钱？

Rocket Lab 可以理解为一家“太空基础设施公司”。客户想把卫星送上天、制造卫星、买卫星零部件、做国防太空任务或未来使用卫星通信网络时，RKLB 都希望参与。

今天的业务主要是两层：

| 层级 | 普通解释 | 谁付钱 | 怎么赚钱 |
|---|---|---|---|
| Launch Services | 用 Electron/HASTE 火箭把客户载荷送入太空，未来用 Neutron 承担更大任务 | 商业卫星公司、政府、国防客户 | 按发射任务收钱；提高发射频率、单发收入和复用能力后毛利率改善 |
| Space Systems | 造卫星、卫星平台、太阳能阵列、反作用轮、星敏感器、无线电、光通信、任务运营等 | 卫星公司、国防/政府、主承包商 | 卖硬件、组件、工程服务和长期项目；订单进入 backlog 后逐步确认收入 |
| Future Applications / Iridium | 如果收购 Iridium 完成，RKLB 会拥有在轨卫星通信网络和客户 | 海事、航空、政府、IoT、偏远通信客户 | 客户按订阅/服务付费，形成 recurring revenue 和现金流 |

关键经济问题：**RKLB 能不能把“会发射、会造卫星、会拿国防订单”转化为可持续自由现金流，而不是一直依赖高估值股票融资？**

### 关键术语翻译

- **Electron**：已商业化的小型运载火箭，适合小卫星专属发射。
- **HASTE**：基于 Electron 的高超音速测试平台，主要服务国防客户。
- **Neutron**：在研中型可复用火箭，是 RKLB 估值上限的核心。
- **Space Systems**：卫星平台、零部件、制造和任务运营业务。
- **Backlog**：已签合同但还没确认收入的未来订单。
- **Book-to-bill**：新增订单 / 当期收入，>1 表示订单池在变大。
- **Flatellite**：Rocket Lab 的平板化卫星平台/架构，面向批量制造和国防星座任务。
- **SB-AMTI**：Space-Based Airborne Moving Target Indicator，天基空中移动目标指示，属于国防/导弹防御/空中目标监测相关任务。
- **Collar**：并购股票对价的价格保护区间；RKLB 股价不同，换股比例会调整。
- **ATM offering**：公司在市场上逐步发行新股融资；企业获得现金，股东被稀释。

## 3. Segment and Product Analysis

### Q2 2026 Headline

| 指标 | Q2 2026 | Q2 2025 | YoY |
|---|---:|---:|---:|
| Product revenue | **$181.3M** | $92.7M | **+95.6%** |
| Service revenue | **$52.7M** | $51.8M | **+1.8%** |
| Total revenue | **$234.1M** | $144.5M | **+62.0%** |
| Gross profit | **$84.6M** | $46.4M | **+82.3%** |
| GAAP gross margin | **36.1%** | 32.1% | +400 bps |
| Operating loss | **-$57.5M** | -$59.6M | improved |
| Net loss | **-$49.3M** | -$66.4M | improved |
| EPS | **-$0.08** | -$0.13 | improved |

Q2 的质量偏强：收入、gross profit、backlog 均创新高，且 operating loss 没有随着收入增长而恶化。但公司仍亏损，adjusted EBITDA 仍为负，FCF 仍为负。

### Launch Services：Electron/HASTE 继续证明执行力，Neutron 尚未证明

Q2 和季后公司披露 secured more than **$437M** launch contracts across Electron, HASTE and Neutron，launch backlog 达 **90+ launches**。这说明客户不只是给 RKLB “看好票”，而是在签真实合同。

正面：

- Electron 是已验证小火箭，不是 PPT。
- HASTE 切入 hypersonic / defense testing，订单质量更偏国防。
- 新 GHOST globally-deployable launch system 计划在 Alaska Kodiak 建 Launch Complex 4，目标是提升 responsive launch 能力，2027 年开始 suborbital operational debut。
- Neutron first-flight hardware assembly/integration/testing 继续推进；Stage 1 tank production 与 Q4 2026 delivery to launch pad 目标一致。

风险：

- Neutron 尚未首飞；这是估值中最贵、但最未证明的一块。
- SpaceX Falcon 9 / rideshare 在价格、cadence 和复用上仍是强压力。
- 国防 responsive launch 机会大，但采购节奏受预算、试验成功率和政治周期影响。

### Space Systems：收入主体、订单主体、平台价值核心

Q2 最重要的新增证据之一是 **$397M U.S. Space Force SB-AMTI Flatellite spacecraft contract**，公司称其为 launch-plus-spacecraft 纵向整合价值的认可。同时 Q2/季后还获得 **$160M+** defense space systems contracts。

Space Systems 的战略意义：

- 比纯发射更高收入天花板；
- 更接近国防预算和大型星座建设；
- 能和 Neutron 形成“自己造卫星 + 自己发射”的平台协同；
- 能通过 Mynaric、Motiv、GEOST 等并购补齐光通信、精密机构、机器人、国防载荷能力。

但它也是项目制业务：合同执行、成本估计、交付延期、供应链和客户变更都可能侵蚀毛利率。

### Iridium：战略上很强，财务和治理上很复杂

Iridium 是全球 L-band 低轨卫星通信网络运营商，服务 aviation、maritime、government、defense、IoT、PNT、safety-of-life 等高可靠通信场景。公司披露 Iridium 支持 **2.55M+ active subscribers**。

交易条款：

| 项目 | 条款 |
|---|---|
| Deal value | 每股 IRDM **$54** |
| Consideration | **$27 cash + RKLB stock** |
| Collar | RKLB stock collar **$67.50-$112.50** |
| Implied Iridium EV | 约 **$8.0B** |
| Financing | **$3.6B** 364-day senior secured bridge term loan commitment |
| Expected close | mid-2027，取决于 Iridium shareholder approval、监管审批、S-4 生效等 |

战略正面：

- RKLB 从“卖铲子”进入“拥有矿山”：拥有在轨网络、频谱和客户。
- Iridium recurring service revenue 可改善商业模式质量。
- RKLB 的 launch/manufacturing 能降低下一代 constellation 部署和 replenishment 成本。
- L-band spectrum 稀缺，政府/国防/海事/航空客户粘性较高。

主要风险：

- 交易未完成前不能把协同当事实。
- 现金 + 股票 + bridge debt 会改变资本结构。
- RKLB 在 Neutron 关键期做大并购，管理层执行负荷显著提高。
- Iridium 是成熟通信运营商，增长曲线与 RKLB 高成长航天制造故事不同，可能带来估值框架混合和 conglomerate discount。

## 4. Financial Deep Dive

### 多期增长趋势

| 指标 | FY2024 | FY2025 | TTM Jun 2026 | Q2 2026 |
|---|---:|---:|---:|---:|
| Revenue | $436.2M | $601.8M | **$769.2M** | **$234.1M** |
| Revenue growth | +78.3% | +38.0% | **+52.5%** | **+62.0% YoY** |
| Gross profit | $116.2M | $207.2M | **$286.6M** | **$84.6M** |
| Operating income | -$189.8M | -$228.8M | **-$212.3M** | **-$57.5M** |
| Net income | -$190.2M | -$198.2M | **-$165.5M** | **-$49.3M** |

业务扩张是真实的：收入和 gross profit 高速增长，gross margin 逐步改善。但 GAAP operating income 和 net income 仍为负，说明 RKLB 还没有从“增长验证”进入“盈利验证”。

### Q2 / H1 现金流

H1 2026：

| 指标 | H1 2026 |
|---|---:|
| Net loss | **-$94.3M** |
| Stock-based compensation | **$47.7M** |
| Operating cash flow | **-$134.4M** |
| Capex / purchases of property, equipment and software | **-$53.1M** |
| Rough FCF | **-$187.5M** |

现金流仍是负数，而且 working capital 占用明显：accounts receivable、contract assets、inventory 均上升。这不一定是坏事，因为高增长项目制业务常见 working-capital drag；但对于估值已很高的股票，市场会要求 burn 逐步收窄。

### 资产负债表和稀释

截至 2026-06-30：

| 指标 | 数值 |
|---|---:|
| Cash and equivalents | **$2.129B** |
| Current marketable securities | **$172.7M** |
| Non-current marketable securities | **$85.4M** |
| Cash + marketable securities | **约 $2.388B** |
| Total assets | **$4.187B** |
| Convertible senior notes, net | **$13.1M** |
| Total liabilities | **$695.2M** |
| Stockholders' equity | **$3.492B** |
| Common shares outstanding | **598.2M** |
| Q3 guide basic WA shares incl. preferred | **约 641M** |
| Preferred shares outstanding | **40.95M** |

流动性很强，这是 RKLB 能持续推进 Neutron、产能、并购和 Iridium 交易的底气。问题是，这份流动性很大程度来自高估值融资。StockAnalysis 显示 shares outstanding YoY **+15.68%**，QoQ **+4.00%**。这对公司战略有利，但对每股价值是实打实稀释。

## 5. Management and Capital Allocation

Peter Beck 团队的执行记录是 RKLB 的核心资产：Electron 商业化、HASTE 国防化、Space Systems 规模化、Mynaric/Motiv/GEOST 能力并购，以及争取 U.S. Space Force / defense contracts，都显示团队不只是讲故事。

但资本配置已经进入更激进阶段：

1. **Neutron 高投入**：决定 RKLB 是否能从 small launch 进入 medium launch / national security launch。
2. **Space Systems 能力并购**：提高垂直整合和组件自给率。
3. **Iridium 大并购**：从项目制业务进入 recurring communications applications，但也带来债务、稀释、审批和整合风险。
4. **高股价融资**：企业理性，但股东要跟踪每股收入、每股 backlog、每股 FCF，而不是只看总收入增长。

管理层目前值得给执行信用，但必须持续验证：Neutron 是否按时间表推进、Iridium 是否不会拖垮资本结构、订单是否转化为利润和现金流。

## 6. Valuation Work

### 当前估值快照

基于 StockAnalysis 2026-08-19 收盘：

| 指标 | 当前 |
|---|---:|
| Price | **$75.84** |
| Market cap | **$45.39B** |
| Enterprise value | **$43.13B** |
| Shares outstanding | **598.46M** |
| Shares YoY change | **+15.68%** |
| TTM revenue | **$769.15M** |
| TTM net income | **-$165.46M** |
| Cash | **$2.30B** |
| Total debt | **$133.69M** |
| Net cash | **$2.25B** |
| EV/TTM sales | **56.1x** |
| EV/Q2 annualized sales | **46.1x** |
| EV/Q3 guide annualized sales | **41.9x** |
| Forward PS | **39.39x** |
| Beta | **2.63** |

估值解释：

- 不能用 P/E，因为公司仍亏损。
- EV/Sales 是主要锚，但必须配合 backlog、gross margin、FCF burn 和 dilution。
- 对 RKLB，合理方法是 **scenario valuation + milestone-based price zones**，因为 Neutron 和 Iridium 期权价值高度不确定。

### 情景估值

以下为 stand-alone / pre-Iridium close 的粗略情景；用 Q3 指引后更稀释的 **641M** basic weighted average shares 作为保守分母，并加入约 $2.25B net cash。Iridium 若完成，资本结构和股数会重写，需要用 pro forma S-4 再更新。

| Scenario | Revenue assumption | EV/Sales | Implied price | vs $75.84 | 触发条件 |
|---|---:|---:|---:|---:|---|
| Bear reset | $0.95B | 18x | **$30.2** | **-60.2%** | Neutron 延迟/失败、订单转化差、市场压缩 space multiple |
| Downside growth normalizes | $1.05B | 28x | **$49.4** | **-34.9%** | 收入增长仍有但 FCF/Iridium/稀释疑虑压制估值 |
| Base backlog converts | $1.25B | 40x | **$81.5** | **+7.5%** | Q3 run-rate 延续，backlog 转收入，burn 可控 |
| Base plus optionality | $1.55B | 50x | **$124.4** | **+64.0%** | Neutron milestone 顺利、defense orders 继续、Space Systems 毛利稳定 |
| Bull platform | $2.10B | 60x | **$200.1** | **+163.8%** | Neutron + Space Systems + Iridium 协同开始被证实 |
| Hyper-bull scarce space infra | $2.80B | 75x | **$331.1** | **+336.6%** | RKLB 被市场视为稀缺端到端航天基础设施平台 |

注意：Bull 和 Hyper-bull 不是当前基本面已经证明的价值，而是多个 milestone 成功后的期权价值。当前 $75.84 大致在 **Downside** 和 **Base** 之间，更接近“业务强但市场仍要求高兑现”的区间。

### 价格纪律

| 价格区间 | 判断 |
|---|---|
| `<$35` | 强安全边际区，前提是 Neutron/现金/订单 thesis 未坏 |
| `$35-$50` | 逆向研究/小仓观察区，downside reset 后风险回报较好 |
| `$50-$70` | 有吸引力但仍需 Neutron 和 FCF 证据 |
| `$70-$90` | 当前区间；业务强，但估值仍高，适合跟踪/已有仓位观察 |
| `$90-$125` | 需要 Neutron Q4 pad delivery、Q3 beat、订单继续扩张支撑 |
| `$125-$200` | Bull-case 区，需要 Neutron + Space Systems + Iridium 同时向好 |
| `>$200` | Hyper-bull 区，不宜只靠“SpaceX 第二”叙事追高 |

## 7. Catalysts and Monitoring Plan

未来 6-12 个月关键催化：

- Q3 2026 revenue 是否达到/超过 **$250M-$265M**；
- Q3 GAAP gross margin 是否守住 **29%-31%**，non-GAAP gross margin 是否守住 **35%-37%**；
- adjusted EBITDA loss 是否控制在 **-$17M 到 -$23M**；
- Neutron Stage 1 tank / pad delivery 是否在 Q4 2026 兑现；
- Neutron first launch 时间、结果、客户 manifest；
- Electron/HASTE launch cadence 和 mission success；
- Launch backlog 是否继续扩大，90+ launches 是否转成可见收入；
- SB-AMTI / defense space systems 合同执行；
- Backlog 中 45% 是否在 12 个月内如期确认；
- Iridium S-4、股东投票、HSR/FCC/监管审批；
- Iridium bridge debt 是否被更长期、更低风险资本结构替代；
- share count、preferred conversion、ATM issuance、SBC；
- operating cash flow 和 FCF burn 是否收窄。

## 8. Risk Register

| 风险 | 概率 | 严重度 | 说明 |
|---|---|---:|---|
| Neutron 延迟/失败 | 中 | 高 | 估值核心期权尚未证明 |
| 估值压缩 | 高 | 高 | 56x TTM EV/Sales 对任何坏消息都敏感 |
| Iridium 审批/融资/整合 | 中 | 高 | 交易大、监管多、资本结构复杂 |
| 稀释 | 高 | 中高 | shares YoY +15.68%，Q3 guide shares 约 641M |
| FCF burn 持续 | 中高 | 中高 | H1 rough FCF 约 -$187.5M |
| 项目成本超支 | 中 | 中 | Space Systems 项目制合同可能侵蚀毛利 |
| 国防预算/政治周期 | 中 | 中 | 大订单受预算和监管影响 |
| SpaceX 竞争 | 中 | 高 | SpaceX 在中大型发射领域优势巨大 |
| 管理层执行负荷 | 中 | 中高 | 同时推进 Neutron、多个并购、Iridium 大交易 |

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**: B。RKLB 披露比多数 space SPAC 好，但 Neutron、Iridium pro forma 和未来 FCF 仍有大量未证明部分。
- **Main research blind spot**: 公共资料无法证明 Neutron 首飞/复用经济性，也无法证明 Iridium 协同的真实净收益。
- **Strongest reason smart investors may disagree**: 多头会认为 RKLB 是唯一稀缺上市 SpaceX-like 平台，短期 EV/Sales 不应约束长期 winner；空头会认为这是高估值、烧现金、稀释和并购复杂度的组合。

### Buffett-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 这个业务十年后是否能产生可预测、高回报、低稀释的自由现金流？
- **Evidence supporting thesis**: revenue 高速增长，backlog $2.356B，cash + securities 约 $2.388B，Electron 执行记录真实，Space Systems 已成收入主体。
- **Evidence against thesis**: 公司仍亏损、FCF 为负、Neutron 未证明、Iridium 改变资本结构和业务边界，估值仍极高。
- **Decision implication**: 值得研究，但不是典型 Buffett-style 买点；需要更低价格或更清晰 FCF 证据。
- **Follow-up**: 如果股市关闭五年，哪些业务证据会让持有 RKLB 更舒服？答案是 Neutron 成功、backlog 高质量转收入、Iridium 现金流不拖累、FCF 转正。

### Munger-style lens

- **Conclusion**: Needs further observation。
- **Key question**: 三年后如果错了，今天最明显的红旗是什么？

| Failure path | Mechanism | Investment consequence |
|---|---|---|
| Neutron 延迟 | 技术/测试/复用难度高 | 估值核心坍塌，multiple reset |
| Iridium 交易拖累 | 债务、稀释、整合、监管 | 从高成长平台变复杂并购故事 |
| Backlog 质量不足 | 订单延期/成本超支/毛利低 | 收入有增长但利润不兑现 |
| 高估值融资依赖 | ATM/SBC/preferred/stock deal | 总公司变大，每股价值不增 |
| Narrative intoxication | “第二个 SpaceX”掩盖财务 | 投资者为远期 TAM 付过高价格 |

- **Decision implication**: 最大 stupid risk 是把“伟大行业 + 稀缺公司”自动等同于“任意价格都可买”。
- **Follow-up**: 如果三年后错了，最明显红旗可能是 Neutron 没有商业化 cadence，而公司却继续扩张并购和稀释。

### Duan Yongping-style lens

- **Conclusion**: Needs further observation / small-position research only。
- **Business essence**: RKLB 帮客户更快、更可靠地进入和使用太空，并试图把发射、制造和在轨服务合成一个平台。
- **User value**: 国防和商业客户需要可靠 launch、spacecraft 和 communications；Electron/HASTE/Space Systems 已证明部分用户价值。
- **Product strength**: Electron 的发射记录、Space Systems 的订单和国防合同支持产品强度；Neutron 和 Iridium 协同还未证明。
- **People/culture**: Peter Beck 团队执行力强，但当前战略跨度很大。
- **Right price**: $75.84 不是离谱，但仍要求高兑现；更舒服的研究区在 $50-$70，强安全边际在 $35-$50 或更低。
- **Follow-up**: 公司是在创造持久客户价值，还是在一个资本市场愿意资助的航天 hype window 中扩张？目前答案偏前者，但价格仍按后者高度乐观定价。

### Li Lu-style lens

- **Conclusion**: Suitable for deep watchlist, not yet high-conviction margin-of-safety holding。
- **Circle of competence**: Electron、收入、backlog、现金流可从披露验证；Neutron 复用经济性、Iridium 协同、长期国防预算属于需持续跟踪领域。
- **Industry trend**: 卫星、国防空间、导弹防御、低轨通信、responsive launch 都是长期结构趋势。
- **Downside protection**: 现金充足，但估值没有给传统资产保护；downside protection 主要来自业务进展，而不是价格。
- **Margin of safety**: 当前不足；业务质量在改善，但价格仍高。
- **Follow-up**: 10-20 年后 RKLB 是重要太空基础设施节点，还是资本周期中的阶段性赢家？这取决于 Neutron 和 applications revenue 是否兑现。

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 7.5/10 |
| Moat | 6.5/10 |
| Management | 8.0/10 |
| Financial quality | 5.0/10 |
| Valuation attractiveness | 4.5/10 |
| Long-term certainty | 5.5/10 |
| Downside risk control | 4.5/10 |

Rationale：业务模型稀缺但仍未完全盈利；护城河来自执行和垂直整合但 Neutron 未证明；管理层执行强但战略跨度大；财务质量受亏损、FCF burn、稀释影响；估值虽回落但仍高；长期方向强但具体赢家路径不确定；下行保护更多来自 cash 和业务 momentum，而不是价格安全边际。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 明显高于多数 space SPAC，是真实平台候选 | 中高 |
| Moat | Electron + Space Systems +国防订单形成初步 moat；Neutron/Iridium 决定上限 | 中 |
| Management | 执行强，但当前资本配置激进 | 中高 |
| Biggest risk | Neutron 未证明 + Iridium 复杂化 + 高估值 | 高 |
| Long-term trend | 太空基础设施、国防空间、卫星通信长期趋势强 | 中高 |
| Valuation and margin of safety | 当前可研究但安全边际不足 | 中 |

| Investor state | Research implication |
|---|---|
| No position | 不建议因股价从高点回落就追；可在 $50-$70 更认真，小仓也需接受高波动 |
| Existing position | 可继续跟踪持有，但应按高 beta space / defense / infrastructure 分类控制仓位 |
| Add / upgrade signal | Q3 beat、Neutron Q4 pad delivery/首飞进展、FCF burn 收窄、Iridium 资本结构清晰 |
| Reduce / downgrade signal | Neutron 延迟、Iridium 审批/融资恶化、gross margin 低于指引、稀释加速、backlog 转化差 |

## 10. Final Research Framework

### 当前结论

RKLB 的业务比 7 月更强，Q2 和 Q3 指引都确认了收入、订单、国防项目和 backlog momentum。股价从 $83.41 回落到 $75.84 后，风险回报改善。

但这仍不是“便宜的航天股”。当前估值仍高，且 thesis 依赖多个未完全证明的变量：Neutron、Space Systems margin、Iridium、FCF、稀释控制。

### 我会如何跟踪

- **维持 Constructive but watchful**。
- **不因股价回落就升级 Positive**，因为估值仍高且 Neutron/Iridium 未确认。
- **若 $50-$70 区间且业务未坏**，研究吸引力明显提高。
- **若 $35-$50 区间且 Neutron/现金/订单 thesis 未坏**，才接近强安全边际。
- **若 >$125**，需要非常强的 Neutron、国防订单、Iridium 和 FCF 证据支撑。

### What would change my view

上调条件：

- Neutron 在 Q4 2026 pad delivery / 首飞路径明确，后续 commercial/government manifest 增强；
- Q3/Q4 revenue 持续 beat，gross margin 稳定，adjusted EBITDA loss 收窄；
- Backlog 继续增长且 45% within 12 months 转化顺利；
- Iridium 交易审批顺利，融资结构不显著伤害普通股；
- FCF burn 明显收窄，share count 增长放缓。

下调条件：

- Neutron 延迟、失败或成本/复用指标不达预期；
- Iridium 交易导致债务、稀释、审批或整合风险显著恶化；
- Space Systems 项目成本超支导致 gross margin 低于指引；
- Backlog 增长停滞或合同取消；
- 继续大量发行股票而每股收入/每股 FCF 没有改善。

## Sources

- Rocket Lab Q2 2026 earnings release, Exhibit 99.1, 2026-08-10（StockAnalysis/Quartr mirror）
- Rocket Lab Q2 2026 Form 10-Q, 2026-08-10（StockAnalysis/Quartr mirror）
- Rocket Lab / Iridium merger press release and investor presentation, 2026-06-29（StockAnalysis/Quartr mirror）
- StockAnalysis RKLB quote/statistics/financials, accessed 2026-08-20; close price as of 2026-08-19
- Prior internal memos: `2026-05-13-deep-research.md`, `2026-07-08-deep-research-v2.md`
