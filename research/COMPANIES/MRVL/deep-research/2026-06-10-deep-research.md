# Marvell Technology（MRVL）深度研究 - 2026-06-10

- **Research view**: 中性 / 等待确认
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: Marvell 已经完成从传统存储、运营商和企业网络芯片公司，向 AI 数据中心“定制计算 + 高速光互连 + 交换芯片 + scale-up 互连”平台的转型。Q1 FY2027 收入创纪录、同比增长 28%，数据中心收入增长 27%，Q2 指引中值对应同比增长 35%，基本面很强。但截至 2026-06-09，MRVL 收于 266.88 美元，市值约 2335 亿美元，EV/Sales 约 26.4x、forward P/E 约 58.9x、P/FCF 约 137x。当前价格不仅要求 AI 收入高速增长，还要求 Marvell 在竞争、客户集中、利润率和稀释方面接近完美执行。
- **Key risk**: 最大风险是估值与可兑现利润不匹配。Q1 GAAP EPS 仅 0.04 美元，远低于 non-GAAP EPS 0.80 美元；SBC、收购无形资产摊销、或有对价重估和收购整合成本都是真实经济负担。若 AI 订单放量不能转化为更高 GAAP 利润和自由现金流，当前高倍数可能快速压缩。

## 1. Executive View

**研究观点：中性 / 等待确认。**

Marvell 的产业位置比一年前更强，但股票的预期也高得多。公司正在同时参与 AI 数据中心最重要的几层连接和计算基础设施：

- 为 hyperscaler 设计定制 XPU/ASIC。
- 提供 800G、1.6T 和未来 3.2T 光互连芯片。
- 提供 51.2T、102.4T Ethernet 数据中心交换芯片。
- 通过 Celestial AI 获取 Photonic Fabric scale-up 光互连技术。
- 通过 XConn 增强 PCIe、CXL 和 UALink scale-up switching。
- 与 NVIDIA 合作，将定制 XPU 和 compatible scale-up networking 接入 NVIDIA AI 基础设施生态。

这些增长点是真实的。Q1 FY2027 收入达到 24.178 亿美元，同比增长 28%；数据中心收入 18.327 亿美元，同比增长 27%；经营现金流达到 6.388 亿美元。公司还把 Q2 收入中值指引提高到 27 亿美元，意味着同比增长约 35%。

但风险/回报已经发生变化：

- 2026-05-22 至 2026-06-09，股价从 196.33 美元上涨到 266.88 美元，约上涨 36%。
- 2026-06-09 市值约 2334.7 亿美元、EV 约 2299.8 亿美元。
- 过去 52 周股价上涨约 290%，股价在几天内曾从 200 美元附近涨到超过 320 美元，再出现双位数回撤。
- MRVL 将在 2026-06-22 开盘前纳入 S&P 500，短期指数资金流可能继续放大波动，但不会改变长期现金流价值。

### 核心判断

1. **业务正在进入 AI 基础设施高增长期。** Q1 data center revenue 占总收入 76%，增长来自 electro-optics、custom silicon、storage 和 switching，而不是单一产品。
2. **未来增长可见度提升。** 管理层表示 AI-related bookings 强劲，并预计 FY2027 每个季度的收入增长继续加速；Q2 收入中值 27 亿美元。
3. **利润质量仍需改善。** Q1 GAAP operating income 3.394 亿美元，但 GAAP net income 仅 3450 万美元；SBC 2.076 亿美元、收购无形资产摊销 2.252 亿美元、或有对价负债及相关远期合约的公允价值净变化 2.507 亿美元。
4. **估值需要多年高速增长。** 当前 EV/Sales 约 26.4x、forward P/E 约 58.9x、FCF yield 约 0.73%，已不允许正常的半导体周期波动。
5. **最强反方理由。** 如果 AI 的瓶颈从 GPU 计算逐渐转向 scale-up、scale-out 和数据中心间互连，Marvell 可能成为少数同时覆盖 custom compute、optics、switching 和 chip-to-chip connectivity 的平台型供应商。若 FY2028/FY2029 收入继续保持高增长，当前高估值可以被时间消化。

## 2. Business Model and Industry Structure

### 初学者版：Marvell 到底卖什么

Marvell 是一家无晶圆厂半导体公司。它负责设计芯片，但把大部分生产交给台积电等晶圆代工厂，以及封装测试供应商。

它主要卖给云计算公司、数据中心设备厂商、网络设备厂商、存储设备厂商和电信运营商。Marvell 的芯片承担四类工作：

- **计算**：替客户设计专用 AI 加速器或其他定制处理器。
- **连接**：让 GPU、XPU、服务器、机架和不同数据中心之间高速交换数据。
- **交换和路由**：决定大量数据如何在网络中传输。
- **存储和安全**：管理硬盘、SSD、数据处理和加密等任务。

客户通常先与 Marvell 共同开发芯片。设计阶段需要数年研发和流片投入；芯片通过验证并进入客户系统后，才开始大规模出货。一个成功的 design win 可能带来数年收入，但如果客户取消项目、换供应商或自研，前期研发投入可能无法获得预期回报。

### 今天的利润引擎与未来选择权

**今天的利润引擎：**

- 800G/1.6T electro-optics。
- Hyperscaler custom silicon。
- 数据中心 storage、switching 和 networking。
- 恢复中的 communications and other。

**未来选择权：**

- Celestial AI 的 Photonic Fabric。
- CPO/NPO 和 scale-up optical connectivity。
- 102.4T Ethernet switching。
- PCIe、CXL、UALink scale-up switching。
- NVIDIA NVLink Fusion-compatible custom XPU 和 networking。

未来选择权的价值很高，但大部分仍需要量产、客户采用和利润率验证，不能直接当作成熟收入计入估值。

### 关键术语翻译

| 术语 | 白话解释 |
|---|---|
| ASIC / Custom silicon | 为某个客户和某种用途量身设计的芯片，不是面向所有客户销售的通用芯片。 |
| XPU | 对各种专用计算处理器的统称，可包括 AI 加速器、CPU、DPU 等。 |
| Design win | 客户选定 Marvell 的设计进入未来产品；不等于立即产生收入，量产可能在数年后。 |
| SerDes | 把芯片内部并行数据转换成高速串行信号，是芯片之间高速通信的关键技术。 |
| Electro-optics | 把电信号和光信号相互转换的芯片和组件，用于高速光模块。 |
| Scale-up | 把同一个 AI 计算系统内的大量 GPU/XPU 紧密连接，追求低延迟和高带宽。 |
| Scale-out | 把更多服务器、机架或集群连接起来，通常使用 Ethernet。 |
| CPO / NPO | 把光学器件放到交换芯片旁边或封装内部，以降低高速传输的功耗。 |
| CXL | 让 CPU、内存和加速器共享数据的一种高速互连标准。 |
| Fabless | 公司设计芯片但不拥有先进晶圆厂，生产依赖外部代工和封装伙伴。 |

### 核心经济问题

Marvell 要产生持久高质量利润，必须做到：定制芯片和光互连收入持续增长、设计胜出扩展到多个客户和多代产品，同时让收入增长快于研发、SBC、摊销和收购成本，并将利润转化为自由现金流。

## 3. Segment and Product Analysis

Marvell 目前按两个终端市场披露收入：Data Center 和 Communications and Other。

| 终端市场 | Q1 FY2027 收入 | 同比 | 收入占比 |
|---|---:|---:|---:|
| Data Center | 18.327 亿美元 | +27% | 76% |
| Communications and Other | 5.851 亿美元 | +29% | 24% |
| Total | 24.178 亿美元 | +28% | 100% |

### Data Center：公司价值主体

数据中心收入覆盖 electro-optics、custom silicon、storage 和 switching。Q1 收入 18.327 亿美元，占总收入 76%，意味着 MRVL 已经不是“传统业务 + AI 选择权”，而是高度依赖 AI/cloud capex 的数据中心公司。

正面因素：

- AI cluster 对带宽的需求增长快于计算芯片数量。
- 800G 向 1.6T 升级，未来还有 3.2T。
- Hyperscaler 希望开发定制 XPU，降低成本、功耗并减少对单一 GPU 平台依赖。
- Ethernet scale-out 和专用 scale-up 互连可能同时增长。

风险因素：

- 数据中心占比 76%，集中度已经很高。
- AI capex 若放缓，多个产品线会同时受影响。
- 客户有能力自研、dual-source 或将项目交给 Broadcom 等竞争对手。

### Custom Silicon：增长快，但客户议价强

Marvell 帮客户完成架构、SerDes、I/O、先进封装、HBM 连接和芯片实现。客户得到更适合自身工作负载的芯片，Marvell获得 NRE、设计服务和量产芯片收入。

优势：

- 高技术门槛和多年代际合作。
- 与光互连、switching 和 chiplet IP 可以交叉销售。
- 成功量产后收入规模大、可持续数年。

限制：

- Hyperscaler 数量少，客户集中天然较高。
- 客户通常具有很强议价能力。
- Custom silicon 毛利率可能低于高价值 merchant optical 产品。
- 每个项目都存在 tape-out、先进封装和量产延期风险。

### Electro-Optics：当前最明确的 AI 受益业务

AI 计算集群需要在芯片、服务器、机架和数据中心之间传输海量数据。Marvell 通过 Inphi 积累了 PAM DSP、coherent DSP、TIA、drivers 和 DCI 模块等能力。

800G 和 1.6T 升级是当前收入驱动。未来 CPO/NPO、scale-up optics 和数据中心间互连提供更大空间。风险是光模块具有速度代际、库存和价格周期，订单增长不一定线性。

### Switching：从 51.2T 向 102.4T

Marvell 于 2026-06-01 宣布 102.4 Tbps Teralynx 10 Ethernet switch 已可供客户使用，面向 AI 和 cloud data center。更高交换容量意味着一颗芯片可以连接更多、更高速的端口。

这是重要产品里程碑，但 merchant Ethernet switching 面临 Broadcom 和 NVIDIA 的强大竞争。判断重点不是“产品发布”，而是客户 design wins、量产时间和毛利率。

### Celestial AI：光学 scale-up 下注

Marvell 于 2026-02-02 完成 Celestial AI 收购，总对价约 35 亿美元。Celestial 的 Photonic Fabric 试图用光互连解决 AI 芯片之间的高带宽、低延迟和低功耗连接问题。

这项收购的战略逻辑清晰，但财务风险也很明确：

- 收购形成大量 goodwill 和 intangible assets。
- 若 Celestial 达到指定收入里程碑，Marvell 可能在 FY2029 前追加现金和普通股对价；最终股数取决于协议和股价等条件。
- 技术采用慢于预期可能导致减值。
- 商业化需要与客户架构、封装和软件生态共同成熟。

### XConn：PCIe/CXL/UALink 补强

Marvell 于 2026-02-10 以约 4.69 亿美元总对价收购 XConn。XConn 提供 PCIe 和 CXL switching silicon，并增强 Marvell 的 UALink scale-up switch 团队。

这让 Marvell 同时拥有 electrical 和 optical scale-up 路线，战略覆盖更完整，但也增加整合和研发支出。

### NVIDIA 战略合作

2026-03-31，NVIDIA 以 20 亿美元购买 Marvell Series A Convertible Preferred Stock，初始可转换为最多约 2178 万股普通股，初始转换价约 91.84 美元。

战略意义：

- NVIDIA 为 Marvell 的 custom XPU、NVLink Fusion-compatible networking 和光互连能力提供生态背书。
- Marvell 有机会进入更广泛的 NVIDIA AI factory 系统。
- NVIDIA 资本投入增强 Marvell 的现金和合作绑定。

风险：

- 转换将带来约 2178 万股潜在稀释。
- NVIDIA 对股东事项具有相应表决和保护权利。
- 战略合作并不保证具体收入规模和利润率。

## 4. Financial Deep Dive

### Q1 FY2027 损益表

| 指标 | Q1 FY2027 | Q1 FY2026 | 变化 |
|---|---:|---:|---:|
| Revenue | 24.178 亿美元 | 18.953 亿美元 | +28% |
| GAAP gross profit | 12.608 亿美元 | 9.524 亿美元 | +32% |
| GAAP gross margin | 52.1% | 50.3% | +180 bps |
| GAAP operating income | 3.394 亿美元 | 2.706 亿美元 | +25% |
| GAAP operating margin | 14.0% | 14.3% | -30 bps |
| GAAP net income | 3450 万美元 | 1.779 亿美元 | -81% |
| GAAP diluted EPS | 0.04 美元 | 0.20 美元 | -80% |
| Non-GAAP net income | 7.180 亿美元 | 5.381 亿美元 | +33% |
| Non-GAAP diluted EPS | 0.80 美元 | 0.61 美元 | +31% |

收入、毛利和 non-GAAP EPS 都很强，但 GAAP net income 同比下降。主要原因不是主业突然恶化，而是收购相关公允价值和会计项目影响。投资者仍需要把这些项目视为经济成本的一部分。

### GAAP 与 Non-GAAP 差距

Q1 FY2027 重要调整项目包括：

- Stock-based compensation：2.076 亿美元。
- Amortization of acquired intangible assets：2.252 亿美元。
- Change in fair value of contingent consideration liability, net of forward stock purchase contract：2.507 亿美元。
- Acquisition-related costs 和 restructuring 等其他调整。

SBC 占季度收入约 8.6%，并不小。收购摊销虽然是非现金项目，但对应过去付出的真实收购价格；如果 Marvell 继续靠收购补技术，摊销和潜在减值会反复出现。

### 现金流质量

Q1 FY2027：

- Operating cash flow：6.388 亿美元。
- Capex：1.557 亿美元。
- 简化 free cash flow：约 4.831 亿美元。
- FCF margin：约 20.0%。

TTM：

- Operating cash flow：约 20.6 亿美元。
- Capex：约 3.91 亿美元。
- Free cash flow：约 16.7 亿美元。

现金流改善明显，但当前市值对应 FCF yield 只有约 0.73%。这意味着市场在给未来现金流很高的增长假设。

### 资产负债表与债务

截至 2026-05-02：

- Cash and cash equivalents：38.436 亿美元。
- Total debt face value：约 50.0 亿美元。
- Net debt：约 11.6 亿美元，若按 StockAnalysis 口径含其他债务则约 14.3 亿美元。
- Revolving credit facility：15 亿美元，季度末未使用。
- 2029 财年到期债务：约 12.499 亿美元。
- 2030 财年：5 亿美元。
- 2031 财年：5 亿美元。
- 其余更长期债务：27.5 亿美元。

债务期限总体可控，短期没有明显再融资墙。但公司在收购、先进产能锁定和研发方面投入很大，资产负债表并非完全无约束。

### 供应承诺与资本强度

截至 2026-05-02：

- 对晶圆代工、封装测试伙伴的无条件采购承诺约 27.568 亿美元。
- Technology services and license fee commitments 约 7.093 亿美元。
- Capex commitments 约 1.855 亿美元。
- 季度结束后新增长期晶圆和基板产能协议，承诺支付 8.70 亿美元押金。

这些承诺说明管理层对需求有信心，也增加了周期下行时的风险。如果订单低于预期，公司仍可能承担容量、押金和采购成本。

### 股份稀释

- 2026-05-21 普通股 outstanding：约 8.748 亿股。
- Q1 diluted weighted-average shares：8.933 亿股。
- Celestial 和 XConn 收购对价中合计发行约 2660 万股普通股，另有被承接的员工股权奖励。
- NVIDIA 优先股初始可转换为最多约 2178 万股。
- Celestial earnout 还可能在 FY2029 前追加现金和普通股对价。
- Q1 employee share tax withholding 支出 2.272 亿美元，反映 SBC 规模。

因此估值时应优先使用 fully diluted 框架，而不是只看当前基本股数。

## 5. Management and Capital Allocation

CEO Matt Murphy 任内最重要的方向是把 Marvell 从低增长、分散的通信和存储芯片组合，转向数据中心基础设施。

成功之处：

- Inphi 收购让 Marvell 在 optical connectivity 中占据关键位置。
- Custom silicon 进入 hyperscaler AI 项目。
- Teralynx、Celestial、XConn 和 NVIDIA 合作补齐 scale-out 与 scale-up 连接。
- FY2026 收入增长 42%，Q1 FY2027 继续创纪录。

需要警惕：

- 公司依赖大型收购形成平台，goodwill 和 acquired intangibles 较高。
- Q1 结束时 goodwill 达到 138.835 亿美元、acquired intangibles 25.615 亿美元。
- Celestial 总对价 35 亿美元，但商业化仍处早期。
- R&D 同比增长 28% 至 6.523 亿美元，SG&A 同比增长 39% 至 2.584 亿美元。
- 管理层必须证明新增费用和稀释最终能换来每股自由现金流增长。

## 6. Competitive Position

### 主要竞争对手

| 领域 | 主要竞争者 | Marvell 的相对优势 | 主要弱点 |
|---|---|---|---|
| Custom AI ASIC | Broadcom、客户内部团队、MediaTek、Alchip、GUC | SerDes、optics、chiplet、networking IP 组合完整 | Broadcom 规模和客户关系更强 |
| Ethernet switching | Broadcom、NVIDIA、Cisco/Arista 生态 | Teralynx 低延迟和高带宽路线 | 市场份额和生态弱于 Broadcom |
| Optical DSP/interconnect | Broadcom、Credo、MaxLinear、MACOM、Coherent 生态 | Inphi 技术积累和完整光互连组合 | 产品周期和客户集中 |
| Scale-up connectivity | NVIDIA NVLink、Broadcom、UALink 生态 | Celestial 光互连 + XConn PCIe/CXL + NVIDIA 合作 | 标准和生态仍在快速变化 |
| Storage | Broadcom、Microchip、内部方案 | 长期 HDD/SSD controller 和 Fibre Channel 经验 | 增长低于 AI 业务 |

Marvell 的护城河不是某一颗芯片，而是把 custom compute、optics、switching、SerDes、storage 和 advanced packaging 组合起来共同设计。这个护城河有价值，但客户本身技术实力很强，Marvell 的定价权不会像纯软件平台那样高。

## 7. Valuation Work

### 为什么使用多种方法

MRVL 是高增长 AI 半导体公司，但当前 GAAP 与 non-GAAP 差距大、收购较多、客户集中和周期性明显。单看 trailing P/E 会受会计项目影响；只看 non-GAAP P/E 又会忽略 SBC、摊销和稀释。因此使用：

- Forward P/E：观察市场对盈利增长的定价。
- EV/Sales：衡量高增长收入被赋予的价值。
- EV/FCF 和 FCF yield：检验实际现金流支撑。
- FY2028/FY2029 情景 EPS 和 FCF：评估当前价格需要什么结果。

### 当前估值快照

截至 2026-06-09 收盘：

| 指标 | 数值 |
|---|---:|
| 股价 | 266.88 美元 |
| Market cap | 2334.7 亿美元 |
| Enterprise value | 2299.8 亿美元 |
| Current shares outstanding | 8.748 亿股 |
| TTM revenue | 87.2 亿美元 |
| TTM free cash flow | 16.7 亿美元 |
| TTM P/E | 92.2x |
| Forward P/E | 58.9x |
| EV/Sales | 26.4x |
| EV/EBITDA | 84.8x |
| P/FCF | 137.2x |
| FCF yield | 0.73% |
| 52-week price change | +290.5% |

这是极高估值。即使收入未来两年显著增长，估值仍要求利润率、现金流和长期增长预期同步提高。

### 情景估值

以下是研究假设，不是投资建议或确定性目标价。采用约 9.1-9.4 亿 fully diluted shares，反映 NVIDIA 转换、收购股份和潜在稀释的一部分。

| 情景 | FY2029 假设 | 估值方法 | 隐含价值 | 关键触发条件 |
|---|---|---|---:|---|
| Bear | Revenue 125-140 亿美元；non-GAAP EPS 5.0-6.0；增长降至低双位数 | 25-30x EPS | 125-180 美元 | AI capex 放缓、custom 项目延期、optics 库存调整、倍数回归 |
| Base | Revenue 170-200 亿美元；EPS 7.0-9.0；FCF margin 25%-28% | 30-38x EPS | 210-342 美元 | 数据中心持续增长、多个 custom 项目量产、GM 稳定、稀释受控 |
| Bull | Revenue 230-280 亿美元；EPS 11-14；FCF margin 28%-32% | 38-45x EPS | 418-630 美元 | Marvell 成为多 hyperscaler custom XPU 与光互连核心平台，scale-up 产品成功 |

当前 266.88 美元处于 base case 中部偏上。风险/回报不差的前提是 FY2029 EPS 至少达到约 8 美元，并且市场仍愿意给予 33x 左右倍数。若合理倍数回到 25x，即使 EPS 达到 8 美元，价值也只有约 200 美元。

### 反向估值

当前价格大致隐含：

- 未来三年 non-GAAP EPS 接近翻倍。
- 数据中心业务继续维持高增长。
- Gross margin 不因 custom silicon mix 明显下滑。
- SBC 和收购稀释不抵消每股利润增长。
- AI capex 在 FY2029 前没有明显周期下行。
- 市场长期给予远高于普通半导体公司的估值倍数。

其中任何一项不成立，都可能带来较大回撤。

## 8. Catalysts and Monitoring Plan

### 近期催化

- 2026-06-22：MRVL 纳入 S&P 500，指数基金调仓。
- Q2 FY2027 revenue 是否达到 27 亿美元 +/-5%。
- Q2 GAAP gross margin 是否达到 52.1%-53.1%。
- Q2 non-GAAP gross margin 是否达到 58.25%-59.25%。
- Q2 non-GAAP EPS 是否达到 0.93 美元 +/-0.05。
- 管理层是否给出更具体的 FY2027/FY2028 revenue outlook。
- 102.4T Teralynx 10 客户 design wins。
- Celestial Photonic Fabric 和 XConn/UALink 商业化时间表。

### 每季监控指标

- Data center revenue growth 和收入占比。
- Custom silicon revenue、客户数量和项目代际。
- 800G/1.6T optics 增长及 3.2T 进展。
- Switching design wins 和量产收入。
- GAAP gross margin 与 non-GAAP gross margin。
- GAAP operating margin 与 non-GAAP operating margin。
- SBC 占收入比例。
- Acquired intangible amortization 和 contingent consideration。
- OCF、capex、FCF 和 FCF per diluted share。
- Fully diluted share count。
- Inventory、purchase commitments 和 capacity deposits。
- 客户集中、订单取消或项目延期信号。

## 9. Risk Register

| 风险 | 概率 | 影响 | 说明 |
|---|---|---|---|
| 估值压缩 | 高 | 高 | 约 59x forward P/E、26x EV/Sales 和不足 1% FCF yield 不容许普通失误。 |
| 客户集中 | 高 | 高 | Hyperscaler 数量有限，单个项目可能显著影响收入。 |
| Custom silicon 竞争 | 中高 | 高 | Broadcom、内部团队及其他 ASIC 供应商会争夺项目。 |
| AI capex 周期 | 中 | 高 | 数据中心已占收入 76%，AI 支出放缓会同时影响多个产品线。 |
| 毛利率压力 | 中高 | 高 | Custom silicon 占比提高可能压低产品组合毛利率。 |
| SBC 与稀释 | 高 | 中高 | NVIDIA 转换、收购股份、Celestial earnout 和员工股权影响每股价值。 |
| 收购整合与减值 | 中 | 高 | Celestial 和 XConn 商业化不及预期可能导致费用和减值。 |
| 供应链承诺 | 中 | 中高 | 大额 wafer、substrate 和 capacity commitments 在下行期形成负担。 |
| 技术路线变化 | 中 | 高 | NVLink、UALink、Ethernet、CPO/NPO 竞争格局仍未稳定。 |
| 出口管制和地缘风险 | 中 | 中高 | 生产、封装和客户供应链高度全球化。 |
| 股价波动 | 高 | 中高 | Beta 约 2.28，近期单日涨跌可达双位数。 |

## 10. Final Research Framework

### 当前结论

Marvell 是高质量的 AI 数据基础设施受益者，基本面明显强于传统半导体周期公司。但当前股票已经把“从优秀供应商变成 AI 平台型赢家”的大量预期计入价格。

因此研究观点从 2026-05-26 的 **建设性但需观察** 下调为 **中性 / 等待确认**。这不是看空业务，而是认为 266.88 美元的价格需要过多正确假设同时成立。

### Thesis 取决于什么

- FY2027 每季度收入增长是否继续加速。
- Data center revenue 是否保持 25%-35% 以上增长。
- Custom silicon 能否从少数项目扩展到多客户、多代产品。
- Optical 和 switching 是否共同增长，而非单一产品周期。
- GAAP 利润和 FCF 是否追上 non-GAAP 增长。
- Fully diluted share count 增长是否低于每股利润增长。

### 什么会让我上调观点

- Q2/Q3 收入和指引持续高于当前预期。
- FY2028/FY2029 revenue visibility 明显提高。
- GAAP operating margin 和 FCF margin持续改善。
- SBC 占收入下降，摊销和收购调整项占比收敛。
- Celestial、XConn 和 102.4T switching 获得明确量产客户。
- 股价回调，但长期基本面没有削弱。

### 什么会让我下调观点

- Data center 或 optics 增长明显放缓。
- Custom silicon 项目延期、丢单或客户 dual-source。
- Non-GAAP gross margin跌破管理层长期框架。
- GAAP 与 non-GAAP 利润差距继续扩大。
- 收购导致更多稀释、或有对价和减值。
- AI capex 下调但产能采购承诺仍高。
- 股价继续上涨，而 FY2028/FY2029 每股盈利预期没有同步上修。

## Sources

- Marvell Investor Relations, Q1 FY2027 results, published 2026-05-27: https://investor.marvell.com/news-events/press-releases/detail/1023/marvell-technology-inc-reports-first-quarter-of-fiscal-year-2027-financial-results
- Marvell Q1 FY2027 Form 10-Q, filed 2026-05-28: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000019/mrvl-20260502.htm
- Marvell FY2026 Form 10-K, filed 2026-03-11: https://investor.marvell.com/sec-filings/all-sec-filings/content/0001835632-26-000011/mrvl-20260131.htm
- Marvell Investor Relations overview and financial results: https://investor.marvell.com/
- Marvell Teralynx 10 102.4 Tbps switch announcement, published 2026-06-01: https://investor.marvell.com/news-events/press-releases/detail/1024/marvell-announces-availability-of-industrys-first-102-4-tbps-switch-purpose-built-for-ai-and-cloud-data-center-infrastructure
- StockAnalysis MRVL overview, price as of 2026-06-09: https://stockanalysis.com/stocks/mrvl/
- StockAnalysis MRVL statistics, updated 2026-06-09: https://stockanalysis.com/stocks/mrvl/statistics/
- S&P 500 inclusion context and effective date: https://www.investors.com/news/sp-500-marvell-technology-flex-to-join-index-roku-quarterly-rebalance/
