# Vistra（VST）深度研究 - 2026-06-10

- **Research view**: 建设性但需观察
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: Vistra 是美国最大的竞争性综合电力公司之一，拥有约 4,400 万千瓦发电能力和约 500 万零售客户。它的核心优势是“发电资产 + 零售售电 + 大规模对冲”一体化，可以用零售负荷和金融合约降低电价波动。Meta、AWS 核电长期购电协议、PJM 容量价格、数据中心负荷增长和 Cogentrix 天然气资产收购正在提高未来现金流，但 199 亿美元债务、并购执行、核电运营和电力价格周期仍是主要风险。以 2026-06-09 的 146.22 美元股价计算，约 9.5 倍 2026 指引中值 EV/调整后 EBITDA，估值不便宜但仍可由现金流和回购解释。
- **Key risk**: 最大风险是市场把当前高电价、容量价格和 AI 用电增长视为永久状态。若数据中心并网延迟、电价回落、核电或燃气机组停运、Cogentrix 整合不及预期，或高债务限制回购，利润和估值可能同时下降。

## 1. Executive View

**研究观点：建设性但需观察。**

Vistra 不是传统受监管公用事业。传统公用事业通常按监管批准的资产回报率赚钱；Vistra 更多依靠竞争性市场中的发电利润、容量收入、零售售电利润和风险管理能力赚钱。因此，它有更高的盈利弹性，也有更大的商品价格、天气和运营风险。

当前 thesis 有四个支柱：

1. **现有资产变得更稀缺。** 数据中心、制造业回流、电气化和油田负荷推高 ERCOT、PJM 等市场的电力需求，而新建可靠电源受到许可、并网、设备交付和资本成本限制。
2. **核电现金流正在合同化。** AWS 与 Comanche Peak 签署最长 20 年、最高约 1,200 MW 的 PPA；Meta 与 PJM 核电站签署 20 年协议，覆盖超过 2,600 MW 的能源、容量和扩容。长期合同降低未来电价波动，并支持核电站延寿和扩容投资。
3. **天然气机组提供可靠性和负荷增长选择权。** 2025 年完成 Lotus 2,600 MW 收购，计划在 2026 年下半年完成 Cogentrix 约 5,500 MW 收购。燃气机组能快速响应电网需求，在可再生能源占比上升的系统中具有调峰价值。
4. **资本回报仍然可观。** 自 2021 年 11 月以来，公司已回购约 63 亿美元股票，将流通股减少约 30%；截至 2026-05-01 尚有约 15 亿美元授权，计划在 2027 年底前完成。

### 为什么不是“Positive”

- 截至 2026-03-31，长期债务含当期到期部分约 191.63 亿美元。
- 2026 年 4 月又发行 40 亿美元高级票据，主要用于再融资和一般公司用途；Cogentrix 仍需现金、股票和承债融资。
- 2026 Q1 GAAP 净利润 10.29 亿美元中包含 7.23 亿美元未来年度对冲的未实现收益，不能直接年化。
- 电力生产是高资本、强运营和强监管业务。核电停机、极端天气、燃料供应或事故都可能造成巨大损失。
- VST 的价值已经包含 AI 和数据中心用电增长预期，若负荷兑现较慢，估值可能回到传统独立发电商区间。

### 最强反方理由

最强反方观点是：Vistra 可能不再适合按传统周期发电商估值。长期核电 PPA、零售业务和高对冲比例正在提高合同化收入占比；若这一转型持续，现金流波动会下降，合理估值倍数可能长期提高。

## 2. Business Model and Industry Structure

### 初学者版：Vistra 如何赚钱

Vistra 同时做两件事：

- **发电**：拥有天然气、核电、煤电、太阳能和电池储能设施，把电卖到 ERCOT、PJM、ISO-NE、MISO、CAISO 等批发市场，或通过长期合同直接卖给客户。
- **零售售电**：通过 TXU Energy 等品牌向家庭、商业和工业客户卖电，收取电费。

把两部分放在一起很重要。单纯发电商害怕电价下跌；单纯零售商害怕采购电力成本上涨。Vistra 既生产电又卖电，可以用自己的发电量、客户负荷和金融对冲相互匹配，减少利润波动。

### 收入如何变成利润

发电端利润大致等于：

`售电收入 + 容量收入 - 燃料成本 - 购电成本 - 电厂运营维护成本`

零售端利润大致等于：

`客户电费 - 电力采购和输配电费用 - 获客、客服和坏账成本`

核电和可再生能源没有天然气燃料成本，因此电价上涨时利润弹性通常较大；天然气机组的盈利取决于电价与燃料成本之间的差额；煤电还承担碳排放、环保和退役风险。

### 关键术语翻译

| 术语 | 白话解释 |
|---|---|
| ERCOT | 德州主要电网和电力市场，电价波动大，极端天气时尤其明显。 |
| PJM | 覆盖美国中大西洋和部分中西部地区的大型电力市场。 |
| Capacity payment / 容量收入 | 电厂因承诺在需要时可发电而获得的收入，即使当时没有实际发电。 |
| PPA | 长期购电协议，买方约定在多年内购买一定电量或相关环境属性。 |
| Dispatchable generation | 可按电网需要调度的电源，主要包括天然气、煤电和核电。 |
| Hedge / 对冲 | 提前锁定未来电价或燃料成本，降低利润随市场价格波动的程度。 |
| Mark-to-market | 按当前市场价格重估未来合约，产生未实现会计损益，但不等于当期现金流。 |
| Capacity factor | 实际发电量相对于理论最大发电量的比例，反映机组利用程度。 |
| Nuclear uprate | 通过设备和运营改造提高现有核电站输出功率。 |
| Adjusted FCFbG | 调整后、扣除维护性资本开支但未扣除增长投资前的自由现金流，是管理层资本配置指标。 |

### 产业结构与护城河

Vistra 的护城河来自资产稀缺性，而不是专利或网络效应：

- 新建核电站时间长、成本高，现有核电资产难以复制。
- 新燃气机组面临涡轮设备交付、天然气管道、许可和并网限制。
- 零售客户规模可以降低获客、采购和风险管理成本。
- 跨 ERCOT、PJM、ISO-NE、MISO 和 CAISO 的资产组合减少单一市场依赖。
- 投资级评级和大规模流动性使公司能在商品市场维持对冲头寸。

但客户转换电力供应商的成本并不高，批发电力本身也是商品。公司的竞争优势主要来自资产位置、规模、运营、交易、对冲和资本配置，而不是强定价权。

## 3. Segment and Asset Analysis

### 公司规模

截至 2026-05-01，公司披露：

- 在 18 个州和华盛顿特区经营。
- 服务约 500 万住宅、商业和工业零售客户。
- 发电容量约 44,000 MW。
- 是美国最大的竞争性发电商之一。
- 拥有美国第二大竞争性核电组合。

截至 2026-03-31，详细资产表显示总容量约 43,695 MW，其中 Texas 约 19,858 MW、East 约 22,308 MW、West 约 1,529 MW。

### Retail：稳定器，但受天气影响

Retail 部门把电卖给终端客户。其价值不只是赚零售毛利，还能吸收公司发电量，形成天然对冲。

| 指标 | Q1 2026 | Q1 2025 |
|---|---:|---:|
| Adjusted EBITDA | 0.68 亿美元 | 1.84 亿美元 |
| ERCOT 售电量 | 15,904 GWh | 17,965 GWh |
| 东北/中西部售电量 | 14,205 GWh | 15,358 GWh |
| 总售电量 | 30,109 GWh | 33,323 GWh |

Q1 2026 零售利润下降，主要因为德州天气温和、客户用电减少，以及多余电量以较低批发价格卖出。这说明综合模式能降低波动，但不能消除天气风险。

### Texas：电价弹性和核电资产

Texas 包括 Comanche Peak 核电站、天然气、褐煤/煤电、太阳能和储能。

Q1 2026 Texas Adjusted EBITDA 为 5.86 亿美元，高于去年同期 4.90 亿美元，主要受更高能源利润推动。核电产量约 5,224 GWh，capacity factor 约 100.8%。

AWS 与 Comanche Peak 签署 20 年 PPA，最高约 1,200 MW。长期合同能够提高收入可见度，但合同定价、起始时间和具体利润贡献没有完整公开，估值不应假设全部增量立即兑现。

### East：PJM 容量价格和核电合同核心

East 拥有 Beaver Valley、Perry、Davis-Besse 核电站，以及大量 PJM、ISO-NE 和 NYISO 天然气机组。

| 指标 | Q1 2026 | Q1 2025 |
|---|---:|---:|
| Adjusted EBITDA | 8.01 亿美元 | 5.14 亿美元 |
| 天然气发电量 | 17,450 GWh | 14,642 GWh |
| 核电发电量 | 8,044 GWh | 7,679 GWh |
| 核电 capacity factor | 92.0% | 87.9% |

East 是本季度增量利润的主要来源，受益于更高实现容量价格、能源价格和 Lotus 资产贡献。

Meta 与 Vistra 签署 20 年协议，覆盖 PJM 核电站超过 2,600 MW 的能源、容量及扩容，并支持四台核电机组进一步延寿 20 年。部分贡献预计从 2027 年开始。

### West：规模小，Moss Landing 风险突出

West 主要包括加州天然气和电池资产。Moss Landing 300 MW 电池设施在 2025 年 1 月发生火灾，公司已决定不恢复运营，并注销约 4 亿美元账面价值；100 MW 设施也不再恢复，确认约 1.55 亿美元减值。

350 MW 设施原计划评估在 2026 年中恢复，但截至 Q1 10-Q，恢复时间及能否恢复仍有不确定性。其账面价值约 3.16 亿美元。

公司预计现场清理活动总成本约 1.10 亿美元，截至 2026-03-31 已支出约 7,000 万美元，并计提约 4,000 万美元未来成本。保险限额合计 5 亿美元，已于 2026 年 2 月前全部收取，但未来仍可能有诉讼、合同和额外危险废物处置成本。

### Asset Closure：不要从估值中忽略

煤电和受损储能设施退役会产生拆除、环保、复垦和员工相关成本。管理层将这部分排除在 Ongoing Operations 指标之外，但这些现金成本最终由股东承担。

## 4. Growth Drivers

### 数据中心和美国负荷增长

数据中心、制造业、电动车和油田电气化提升电力需求。Vistra 的优势是已有可调度资产，不需要等待多年建设才开始受益。

但数据中心负荷并非无风险：

- 规划项目可能延期或取消。
- 电网互联审批可能成为瓶颈。
- 居民电价压力可能引发监管干预。
- 数据中心客户会比较不同地区、电源和现场发电方案。

### Meta 和 AWS 核电 PPA

长期核电合同可能是公司质量改善的最重要变化：

- 将部分商品电价风险转换为合同现金流。
- 支持核电站延寿和 uprate。
- 大型科技客户信用质量较高。
- 提高核电资产使用寿命和终值。

Meta、AWS PPA 与零售业务将提高合同化现金流占比。需要注意，长期协议的具体定价和利润贡献未完整公开，不能把全部合同容量直接视为增量 EBITDA。

### Cogentrix 收购

Vistra 计划以约 40 亿美元净购买价收购 Cogentrix，包括约 5,500 MW、10 座天然气发电设施。公开报道显示对价包括现金、约 500 万股 Vistra 股票和承接约 15 亿美元债务；交易仍需监管批准，预计 2026 年中后期完成。

战略逻辑：

- 增加高负荷增长地区的可调度天然气容量。
- 收购成本约 730 美元/kW，低于新建同类机组成本。
- 与现有零售、交易和对冲平台结合。

风险：

- 交易融资提高债务和利息负担。
- 需要完成监管审批。
- 老旧机组可能需要更多维护资本开支。
- 若未来电价或容量价格下降，收购回报会低于预期。

### Organic Growth

- Permian Basin 新建两台天然气机组，合计约 860 MW，预计 2028 Q2 前后投运。
- PJM 核电 uprates。
- Oak Hill Solar Phase 2。
- 煤电向天然气转换，包括 Coleto Creek 和 Miami Fort。

管理层对增长项目要求 mid-teens 或更高的 levered return。投资者应关注最终投运成本和真实回报，而不只是项目容量。

## 5. Financial Deep Dive

### 2025 全年

| 指标 | 2025 | 2024 | 变化 |
|---|---:|---:|---:|
| Revenue | 177.38 亿美元 | 172.24 亿美元 | +3% |
| GAAP net income | 9.44 亿美元 | 28.12 亿美元 | -66% |
| Common stock net income | 7.52 亿美元 | 24.67 亿美元 | -70% |
| Operating cash flow | 40.70 亿美元 | 45.63 亿美元 | -11% |
| Ongoing Operations Adjusted EBITDA | 59.12 亿美元 | 56.43 亿美元 | +5% |
| Ongoing Operations Adjusted FCFbG | 35.92 亿美元 | 未列示 | - |

GAAP 净利润大幅下降，主要是未来年度商品对冲的未实现损失。由于电价上涨往往会导致已售出远期电力合约出现账面损失，但同时提高未来未对冲发电价值，因此 GAAP 净利润不能单独代表经营趋势。

### Q1 2026

| 指标 | Q1 2026 | Q1 2025 |
|---|---:|---:|
| Revenue | 56.40 亿美元 | 39.33 亿美元 |
| GAAP net income | 10.29 亿美元 | -2.68 亿美元 |
| Operating income | 14.99 亿美元 | -1.20 亿美元 |
| Ongoing Operations Adjusted EBITDA | 14.94 亿美元 | 12.40 亿美元 |
| Operating cash flow | 11.99 亿美元 | 5.99 亿美元 |
| Capital expenditures | 8.83 亿美元 | 7.68 亿美元 |

Q1 GAAP 净利润包含 7.23 亿美元商品对冲未实现收益；Adjusted EBITDA 同比增长 2.54 亿美元，主要来自更高实现能源与容量价格及 Lotus 资产贡献，部分被温和天气造成的零售利润下降抵消。

### 2026 指引

- Ongoing Operations Adjusted EBITDA：68-76 亿美元，中值 72 亿美元。
- Ongoing Operations Adjusted FCFbG：39.25-47.25 亿美元，中值 43.25 亿美元。
- 2027 Adjusted EBITDA midpoint opportunity：74-78 亿美元。
- 2026/2027/2028 预期发电量对冲比例：约 98%/89%/65%。
- 中期 Adjusted EBITDA 向 Adjusted FCFbG 转化率：60% 以上。

2026 和 2027 数字均不包含 Cogentrix；2027 opportunity 也不包含 Meta PPA。它们提供上行选择权，但“opportunity”不是正式 guidance。

### 资本开支

公司预计 2026 总资本开支约 25.25 亿美元，包括：

- 核电和化石燃料维护：约 10.25 亿美元。
- 核燃料：约 4.75 亿美元。
- 太阳能和储能开发：约 3 亿美元。
- 其他增长项目：约 9 亿美元。

扣除增长项目和非经常项目后的 adjusted capex 约 15 亿美元。FCFbG 的定义在增长投资之前，因此不能把全部 43.25 亿美元中值视为可无条件分给股东的现金。

### 资产负债表

截至 2026-03-31：

- Cash and cash equivalents：6.34 亿美元。
- 总可用流动性：约 41.73 亿美元。
- Long-term debt including current portion：191.63 亿美元。
- Current debt maturities：18.99 亿美元。
- Accounts receivable financing：7.50 亿美元。
- Forward repurchase obligation：6.41 亿美元。

2026 年 4 月，公司发行 40 亿美元高级无担保票据：

- 2028 年到期 5 亿美元，利率 4.55%。
- 2031 年到期 10 亿美元，利率 5.00%。
- 2033 年到期 10 亿美元，利率 5.25%。
- 2036 年到期 15 亿美元，利率 5.55%。

所得资金主要用于偿还或赎回 2027 年票据、Term Loan B-3、一般公司用途及发行费用。再融资延长了期限，但利息负担仍然重要。

### 核退役与环境负债

截至 Q1 2026，资产退休义务约 42.31 亿美元，其中约 40.46 亿美元为长期负债。公司拥有核退役信托资产，但投资者仍应关注核电站寿命、退役成本、监管要求和信托资产表现。

## 6. Management and Capital Allocation

Jim Burke 管理层的资本配置记录总体较强：

- 2024 年整合 Energy Harbor，扩大核电和零售业务。
- 2025 年完成 Lotus 2,600 MW 天然气资产收购。
- 签署 AWS 和 Meta 核电长期协议。
- 自 2021 年以来回购约 63 亿美元股票，股数下降约 30%。
- 获得 S&P 和 Fitch 投资级评级。

未来两年资本配置框架：

- 每年至少约 10 亿美元股票回购。
- 每年约 3 亿美元普通股股息。
- 2026-2027 约 40 亿美元增长用途，包括 Cogentrix、Permian 天然气机组和 PJM 核电扩容。
- 目标 2027 年末 net debt / Adjusted EBITDA 约 2.3x。

风险是公司同时进行并购、扩建、回购和分红。若经营现金流低于预期，管理层必须在降债、增长投资和股东回报之间取舍。

## 7. Valuation Work

### 估值方法选择

Vistra 属于周期性独立发电商，但合同收入和零售业务占比正在提高。适合使用：

- **EV/Adjusted EBITDA**：便于纳入债务，并跨电价周期比较。
- **Adjusted FCFbG yield**：衡量业务在增长投资前的现金生成能力。
- **情景化 equity FCF multiple**：反映电价、PPA、并购和回购的不确定性。

P/E 只能辅助，因为衍生品未实现损益会造成 GAAP EPS 大幅波动。

### 当前估值快照

截至 2026-06-09 收盘：

| 指标 | 数值 |
|---|---:|
| 股价 | 146.22 美元 |
| Market cap | 493.0 亿美元 |
| Enterprise value | 685.7 亿美元 |
| Shares outstanding | 3.3718 亿股 |
| TTM revenue | 194.5 亿美元 |
| TTM EBITDA | 67.9 亿美元 |
| Forward P/E | 13.9x |
| EV/EBITDA | 10.1x |
| EV/Sales | 3.53x |
| TTM P/FCF | 27.3x |
| Dividend yield | 0.62% |
| 52-week range | 132.66-219.82 美元 |

按公司 2026 Adjusted EBITDA 中值 72 亿美元计算，当前 EV 约为 9.5 倍。按 2026 Adjusted FCFbG 中值 43.25 亿美元计算，市值约为 11.4 倍、对应 8.8% 的理论 FCFbG yield。

但 FCFbG 是增长投资前现金流，且普通股股东之前还有利息、优先股股息、收购和退役相关现金需求，不能直接等同于普通会计 FCF。

### 情景估值

以下为研究框架，不是投资建议。使用 2027 年末约 3.22-3.32 亿股，假设公司继续回购，但 Cogentrix 对价包含约 500 万股发行。

| 情景 | 核心假设 | 估值方法 | 隐含每股价值 |
|---|---|---|---:|
| Bear | 2027 FCFbG 35-40 亿美元；电价和容量价格回落；Cogentrix 整合偏弱；回购放缓 | 9-11x FCFbG | 95-135 美元 |
| Base | 2027 FCFbG 47-53 亿美元；Meta 部分贡献；Cogentrix 正常整合；股数继续下降 | 11-13x FCFbG | 155-210 美元 |
| Bull | 2027-2028 FCFbG 58-65 亿美元；数据中心负荷强；核电合同化成功；扩容按时 | 13-15x FCFbG | 230-300 美元 |

当前 146.22 美元略低于 base case 下沿，但高于 bear case。风险回报有吸引力的前提是：2026 指引兑现、Cogentrix 不明显推高杠杆、Meta/AWS 合同按计划贡献、核电资产保持高可用率。

### 反向估值

当前价格大致要求：

- 2026 Adjusted EBITDA 达到指引中值附近。
- Adjusted FCFbG 转化率维持 60% 以上。
- 长期电价和容量价格不会回到低迷周期。
- Cogentrix 收购不会破坏资产负债表。
- 每年至少 10 亿美元回购能够持续。
- 核电和天然气资产不会发生重大长期停运。

与高估值 AI 股票相比，这些假设不算极端；但它们包含真实的商品、运营和债务风险。

## 8. Catalysts and Monitoring Plan

### 近期催化

- Cogentrix 监管审批及 2026 年下半年交割。
- Meta PPA 的起始时间、定价结构和增量 EBITDA披露。
- AWS Comanche Peak PPA 执行进度。
- 2026 夏季 ERCOT 和 PJM 电价、负荷及机组可用率。
- 下一次财报日期截至 2026-06-10 尚未由公司正式公布。
- Moss Landing 350 MW 是否能够恢复运营。
- 核电 uprate 的资本开支、许可和投运时间。

### 每季监控指标

- Ongoing Operations Adjusted EBITDA 与全年 68-76 亿美元指引。
- Adjusted FCFbG 与 39.25-47.25 亿美元指引。
- Retail、Texas、East 分部 Adjusted EBITDA。
- 2027、2028 hedge percentages。
- ERCOT/PJM 实现电价和容量收入。
- 核电 capacity factor 和计划外停机。
- 天然气 CCGT capacity factor。
- Retail volumes、customer attrition 和天气影响。
- Maintenance capex、growth capex 和核燃料支出。
- Net debt / Adjusted EBITDA。
- 回购价格、回购股数和剩余授权。
- Asset Closure、Moss Landing 和环保现金支出。

## 9. Risk Register

| 风险 | 概率 | 影响 | 说明 |
|---|---|---|---|
| 电力和容量价格回落 | 中 | 高 | 2028 对冲比例较低，长期利润仍有商品价格暴露。 |
| 高债务 | 中高 | 高 | 债务约 199 亿美元量级，利息和再融资会影响股东现金流。 |
| Cogentrix 整合 | 中 | 高 | 40 亿美元交易规模大，涉及 10 座燃气电厂和承债。 |
| 核电运营事故或长期停机 | 低中 | 极高 | 核电资产价值高，停机、监管或安全事件影响巨大。 |
| 数据中心需求延迟 | 中 | 中高 | AI 用电预期已进入估值，但并网和建设可能延期。 |
| 对冲会计误读 | 高 | 中 | GAAP 净利润会因未实现衍生品损益剧烈波动。 |
| 极端天气 | 高 | 中高 | 冬季风暴、德州高温或温和天气都可能影响负荷和价格。 |
| 燃料与供应链 | 中 | 中高 | 天然气、核燃料、设备和长期维护合同均有成本风险。 |
| 环境与监管 | 中高 | 高 | 煤电、核退役、排放、Moss Landing 和居民电价均可能引发监管成本。 |
| 资本配置过度扩张 | 中 | 高 | 同时并购、扩建、回购和分红可能推高杠杆。 |
| 煤电退役成本 | 高 | 中 | Asset Closure 排除在 ongoing 指标外，但现金成本真实存在。 |

## 10. Final Research Framework

### 当前结论

Vistra 的投资逻辑不是简单的“AI 数据中心缺电”。更完整的逻辑是：

- 美国可靠电源供给增长慢；
- Vistra 已拥有大规模核电和天然气资产；
- 零售业务与对冲降低现金流波动；
- Meta、AWS PPA 将部分高价值核电收入长期合同化；
- 强自由现金流用于回购，使企业价值增长转化为每股价值增长。

以 146.22 美元价格看，VST 的估值明显低于纯 AI 基础设施股票，也低于高质量受监管公用事业的部分高估值案例。与此同时，它承担更高的债务、商品价格、事故和监管风险。因此观点为 **建设性但需观察**，而不是高确定性的 Positive。

### Thesis 取决于什么

- 2026 Adjusted EBITDA 和 FCFbG 指引是否兑现。
- Meta/AWS PPA 是否真正降低长期现金流波动。
- Cogentrix 是否以合理杠杆完成并产生预期回报。
- 核电站保持高 capacity factor。
- 电力负荷增长快于可调度供给增长。
- 回购能否持续降低 fully diluted share count。

### 什么会让我上调观点

- 2026 EBITDA/FCFbG 达到指引上半区。
- Meta 和 AWS 合同贡献、价格和起始时间更清晰。
- Cogentrix 按时交割，净杠杆保持在管理层目标附近。
- 2027 EBITDA 指引高于现有 74-78 亿美元 opportunity。
- 核电和天然气机组可靠性持续改善。
- 股价维持合理估值，同时每股 FCF 持续增长。

### 什么会让我下调观点

- 2026 指引下调或 FCF 转化低于 60%。
- Cogentrix 交易延迟、成本上升或需要更多股权融资。
- 核电长期停机、监管事件或重大安全事故。
- ERCOT/PJM 负荷或电价预期明显下降。
- Asset Closure 和环境成本持续超预算。
- 公司为维持回购而增加杠杆。

## Sources

- Vistra Q1 2026 earnings release, published 2026-05-07: https://investor.vistracorp.com/2026-05-07-Vistra-Reports-First-Quarter-2026-Results
- Vistra Q1 2026 investor presentation: https://investor.vistracorp.com/image/Q1_2026_Results_Presentation_vFINAL.pdf
- Vistra Q1 2026 Form 10-Q, filed 2026-05-08: https://investor.vistracorp.com/image/VST_10-Q_2026-05-08.pdf
- Vistra FY2025 results, published 2026-02-26: https://investor.vistracorp.com/2026-02-26-Vistra-Reports-Fourth-Quarter-and-Full-Year-2025-Results
- Vistra $4.0 billion senior notes offering, published 2026-04-08: https://investor.vistracorp.com/2026-04-08-Vistra-Prices-Private-Offering-of-4-0-Billion-of-Senior-Notes
- Vistra Investor Relations overview: https://investor.vistracorp.com/
- StockAnalysis VST overview, price as of 2026-06-09: https://stockanalysis.com/stocks/vst/
- StockAnalysis VST statistics, updated 2026-06-10: https://stockanalysis.com/stocks/vst/statistics/
- Cogentrix acquisition supporting context: https://www.barrons.com/articles/vistra-stock-ai-power-cogentrix-deal-3000d9df
