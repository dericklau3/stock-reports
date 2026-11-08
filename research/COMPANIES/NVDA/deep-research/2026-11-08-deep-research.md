# NVIDIA Corporation（NASDAQ: NVDA）完整深度研究｜2026-11-08

- **投资观点：**中性偏建设性。AI数据中心收入与营业利润增长已被财报验证，股价回撤令同期估值下降；但云客户资本开支、巨额供应承诺和信用担保使当前价格仍需现金质量验证。
- **核心逻辑：**NVIDIA通过GPU、CPU、网络互联、整机系统和CUDA软件生态，让客户为更低的AI计算总成本持续采购；实际经营利润增长是真实的，支付能力最终由客户算力使用和收费决定。
- **主要风险：**数据中心客户融资与循环采购、Rubin供给提前锁定、出口限制及中国H200审批、投资资产收益波动、自由现金流季节性与大型合同担保。

## 1. 公司到底是做什么生意的？

NVIDIA不是只卖一颗“显卡芯片”；它向超大规模云商、AI计算云、企业和个人销售GPU、CPU、交换机、整机机架、软件与相关支持，作为AI训练、推理、网络、PC和物理AI基础设施供应商。**其法律披露按Compute & Networking和Graphics两个报告分部计账，另按客户市场平台披露Data Center（Hyperscale/ACIE）和Edge Computing；两种维度绝不可互相加总。**

<details class="business-detail">
<summary>① 数据中心 Hyperscale｜2026Q2 $48.710B，超大云与大型互联网客户</summary>

**卖什么：**Blackwell/Blackwell Ultra、Rubin相关GPU/CPU、NVLink高速互联、网络交换机及机架级AI服务器集成，支持大规模训练和推理。**客户为什么买：**按实际工作负载缩短训练时间、提升推理token吞吐，降低单位任务电力、机柜、网络管理成本。**谁付款：**可直接向NVDA购买的CSP、OEM、ODM与渠道集成商，最终使用者还包括大型云租户；不能把微软等最终算力使用者自动当每笔订单的直接发票付款人。**如何确认：**一般在合同约定设备控制权交付时确认硬件收入，软件及支持按各自履约义务确认，不因客户租出算力才开始记收入。**成本：**晶圆代工、HBM存储、封装、交换机、整机制造、质保及研发；大客户压价与供需变动影响毛利。

**举例假设（非真实订单）：**云运营商通过OEM购买集成GPU机柜→OEM与NVIDIA按采购合同结算芯片、网络和系统部件→云商将算力租给AI公司；云商收到的云租金不是NVIDIA营业收入。

</details>


<details class="business-detail">
<summary>② 数据中心 ACIE｜2026Q2 $40.313B，AI云、工业、企业及主权算力</summary>

**卖什么：**面向专门AI云商、工业集团、企业、研究机构与政府项目的加速计算服务器、网络硬件及配套软件/支持。**解决问题：**组织不用独立设计训练/推理硬件与互联协议；可选择本地、租赁或专用AI工厂部署。**付款路径：**可能是AI云业主、系统集成商或OEM向NVIDIA付款，最终模型公司、工业企业或公共机构向AI云/集成商付费，不能把合作公告当成NVDA已经赚到最终租金。**确认及成本：**按实际硬件交付和服务履约确认收入；HBM、CoWoS/封装、机架集成、渠道折扣、售后与供应承诺是主要经济成本。

**举例假设（非真实订单）：**一家工业AI云运营商采购整套Rubin机柜→经ODM交付、验收和应收形成NVIDIA收入→运营商另外向制造业客户提供收费推理服务；这项终端收费不直接属于NVIDIA。

</details>


<details class="business-detail">
<summary>③ 数据中心高性能网络与基础软件｜收入包含于数据中心两大子市场，未单列</summary>

**卖什么：**Spectrum-X以太网、InfiniBand、NVLink交换网络、网卡、数据处理器及CUDA、NVIDIA AI Enterprise等软件、支持和许可。网络减少成千上万GPU之间数据通信瓶颈；驱动、工具和优化使客户更容易部署。**直接付款方：**机架/交换机客户、OEM、云商或有独立许可合同的企业；并非每个调用CUDA的开发者都按token付费给NVIDIA。**收费与收入确认：**硬件随交付计价，单独软件许可/支持依合同期间和交付义务确认；报告未单列这块在Hyperscale/ACIE中的金额，不能额外加总。**成本/利润：**网络ASIC制造、PCB/光模块、软件工程与技术支持，网络价值有助于系统成套销售但单项净利润未披露。

**举例假设（非真实订单）：**云厂商为数千GPU数据中心向NVIDIA购买交换机和网卡、另购买企业软件许可→NVIDIA分别按交付硬件、合同服务期限确认应收或服务收入；不能把网络报价再次叠加到已披露数据中心分类收入。

</details>


<details class="business-detail">
<summary>④ PC与GeForce游戏显卡｜归于Edge Computing及Graphics，未单独给出新口径金额</summary>

**卖什么：**GeForce GPU、RTX图形功能、AI PC推理与游戏/创作图形相关技术。**解决问题：**PC玩家追求帧率与画质，笔记本用户追求本地AI计算；出厂集成商和显卡板卡合作伙伴(AIB)采购芯片，消费者通常向电脑厂商/零售商付费。**收入确认：**NVIDIA向AIB/OEM交货并控制权转移时记录芯片销售，终端零售额不是NVDA确认收入。**成本：**代工晶圆、GDDR、板卡软件、驱动和渠道库存风险。

**举例假设（非真实订单）：**AIB从NVIDIA买GeForce GPU→完成板卡并卖给零售商→玩家最终购买整张显卡；NVIDIA只把向合同客户销售的可确认价格算收入。

</details>


<details class="business-detail">
<summary>⑤ 专业工作站与可视化｜属于Graphics与Edge，未单报本季收入</summary>

**卖什么：**RTX PRO工作站GPU、专业驱动和可视化工具，服务设计、工程仿真、数字内容制作和工业数字孪生。**付款人：**工作站OEM、系统集成商及按合同直接采购的专业用户，最终使用者是工程师、设计师和企业。**收费与确认：**硬件销售及适用软件/维护合同的履约，不能把用户所创造的工业设计价值算作NVIDIA收入。**成本：**GPU制造、驱动认证、行业软件兼容研发、技术支持。

**举例假设（非真实订单）：**汽车设计公司采购带RTX PRO的工作站→OEM向NVIDIA订购GPU→公司按部件交付记收入，设计成果由车企所有，不属于NVIDIA销售。

</details>


<details class="business-detail">
<summary>⑥ 汽车、机器人与工业边缘系统｜收入在Edge Computing，未独立量化</summary>

**卖什么：**DRIVE计算平台、Jetson机器人/嵌入式计算系统及运行时软件，帮助车企、工业设备厂和机器人系统执行本地传感器推理与控制。**付款链：**车企Tier-1供应商、工业OEM、机器人集成商按供货/许可合同向NVIDIA付费，终端车主或工厂最终承担产品价格。**确认与成本：**实际交付硬件及特定软件授权的合同条件决定确认；汽车认证、软硬安全测试、长周期产品支持提高投入。公司本季未在最新市场平台口径给这些子项独立可复算营收，不能将合作设计定点当已收大额销售。

**举例假设（非真实订单）：**机器人OEM采购Jetson模块→整合视觉和动作控制→向仓库售出机器人；NVIDIA收入来自模块/服务合同而不是仓库因效率改善获得的利润。

</details>


<details class="business-detail">
<summary>⑦ 技术云支持、软件和其他交付｜包含在Compute & Networking/Graphics，未独立量化</summary>

**卖什么：**与已售GPU、AI工厂集群有关的系统软件更新、培训、保修、订阅与开发工具；也包含面向客户的部分云开发环境。**谁付款：**采购企业、云商、系统集成商及软件许可订户，具体由合同决定；开源项目与试验产品不能一概认作商业收费。**何时确认：**依据单独履约义务、订阅期间或相关服务实际交付确认；10-Q中的递延收入余额是已收款未完成履约义务，不是可与当期收入相加的新营收。**成本：**数据中心设施、GPU使用、电费、平台研发、运营和支持。

**举例假设（非真实订单）：**企业向NVIDIA购买一批设备附带多年期技术支持→设备交付部分按照合同确认硬件收入→支持服务按合同提供期间逐步确认，不会在首次收款日重复确认两次。

</details>


**收入结构与合并核验（单位：十亿美元，US GAAP，Q2 FY2027截至2026-07-26）。**同比（YoY）是2026Q2和2025年同季比较，环比（QoQ）是2026Q2和紧邻2026Q1比较，公式均为（本期−比较期）÷比较期×100%。**一张表同时展示两个拆分维度，分类之间不能交叉相加。**

| 分类层级 | 2025Q2 | 2026Q1 | 2026Q2 | 同比 | 环比 | 解释 |
|---|---:|---:|---:|---:|---:|---|
| **报告分部：Compute & Networking** | 41.331 | 74.550 | **88.299** | +113.6% | +18.4% | 芯片、网络、系统与部分软件；报告分部 |
| **报告分部：Graphics** | 5.412 | 7.065 | **7.922** | +46.4% | +12.1% | GeForce/RTX专业显卡与配套；报告分部 |
| **报告分部合计** | **46.743** | **81.615** | **96.221** | **+105.9%** | **+17.9%** | 88.299＋7.922＝96.221 |
| — 市场平台：Data Center（小计） | 41.096 | 75.246 | **89.023** | +116.6% | +18.3% | **以下Hyperscale和ACIE的小计** |
| ↳ Hyperscale | 24.168 | 43.050 | **48.710** | +101.5% | +13.1% | 超大规模云与大型互联网 |
| ↳ ACIE（AI Clouds/Industrial/Enterprise） | 16.928 | 32.196 | **40.313** | +138.1% | +25.2% | 各类AI云、工业、企业 |
| — 市场平台：Edge Computing | 5.647 | 6.369 | **7.198** | +27.5% | +13.0% | PC、游戏、专业图形、汽车/工业等 |
| **市场平台合计（不再加到分部合计）** | **46.743** | **81.615** | **96.221** | **+105.9%** | **+17.9%** | 48.710＋40.313＋7.198＝96.221 |
| 分部间交易/抵销 | 0（不存在） | 0（不存在） | **0（不存在）** | — | — | 10-Q明确无分部间交易 |
| **最终合并营业收入** | **46.743** | **81.615** | **96.221** | **+105.9%** | **+17.9%** | 仅计一次，不混合两个拆分维度 |

**分类变化：**NVIDIA自FY2027 Q1改按“Data Center/Edge Computing”市场平台披露，并于Q2把一名客户从ACIE重分类到Hyperscale，已重述对比期；**不是另一个新财务分部**。2026Q2 Compute & Networking分部经营利润**62.696B**、Graphics **3.899B**，共66.595B，扣未分配SBC、公司费用等2.861B，才与GAAP营业利润**63.734B**相符。客户购买的确是实际GPU/网络，但财报也披露**Q2单一直接客户占合并收入16%**，集中度显著。来源：[Q2 10-Q分部注释与MD&A](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)、[Q2发行人公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/)。

**竞争与议价：**GPU软硬一体、CUDA工具链和互联网络是客户迁移成本；对应证据是Compute & Networking一年营收翻倍、Q2分部经营利润显著为正。可替代选项包括云商TPU/Trainium等自研ASIC、AMD加速器及其ROCm、传统CPU系统。不能把基准测试领先直接外推所有真实负载的总拥有成本；真正危险的是客户以更低价格获得足够好性能、或项目融资不足，令NVIDIA让利/延迟发货。

## 2. 近期已公布的重大事件

按公告月份归档近12个月已确认、足以改变收入/资本结构/经营敞口的重大独立事项；不把新闻式合作、基准测试、技术演示、研究捐赠凑成A级事件。正式来源在每张卡片内。

<div class="event-roadmap" aria-label="重大事件时间轴">
<section class="event-month" data-month="2025-11">
<h3 class="event-month-heading">2025-11</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">FY2026 Q3实际业绩</span>
<span class="event-entry-preview">数据中心需求快速扩张，成为后续同比基线</span>
</summary>
<div class="event-detail-content">

**公告日期：**2025-11-19。

**公布了什么：**报告截至2025-10-26季度收入约$57.0B、数据中心约$51.2B。

**对公司的实际意义：**证明新增AI系统已有实质销售，并非纯市场预期；与2026财报对比要使用同期间口径。

**原始来源：**[原始资料](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026)。

</div>
</details>
</section>
<section class="event-month" data-month="2026-02">
<h3 class="event-month-heading">2026-02</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">FY2026全年业绩</span>
<span class="event-entry-preview">年度营业收入达$215.938B，奠定高现金流基础</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-02-25。

**公布了什么：**披露FY2026（截至2026-01-25）GAAP营收$215.938B、营业利润$130.387B。

**对公司的实际意义：**形成当前TTM核算和盈利质量的已实现起点，不代表FY2027指引或2028预测。

**原始来源：**[原始资料](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)。

</div>
</details>
</section>
<section class="event-month" data-month="2026-05">
<h3 class="event-month-heading">2026-05</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">FY2027 Q1业绩与股东回报</span>
<span class="event-entry-preview">当季收入$81.615B，宣布额外$80B回购授权与提高股息</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-05-20。

**实际发生或签约日期：**2026-05-18董事会批准。

**公布了什么：**Q1营收$81.615B、GAAP营业利润$53.536B；董事会于5月18日批准增加$80B回购授权，并将季度每股股息由$0.01提至$0.25。

**对公司的实际意义：**Q1利润和授权有原始依据；回购授权≠已购回股份，不可提前把授权金额减少股数。

**原始来源：**[原始资料](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/)。

</div>
</details>
</section>
<section class="event-month" data-month="2026-08">
<h3 class="event-month-heading">2026-08</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">独立AI基础设施融资MOU</span>
<span class="event-entry-preview">六家资本提供者拟长期动员超$500B第三方资金</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-08-10。

**公布了什么：**与Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs及KKR签署合作备忘录，目标为独立融资平台动员超过$500B第三方资本。

**对公司的实际意义：**这不是NVDA已经取得的收入或由NVDA承担的5000亿美元债务；融资能否落地影响购买芯片的客户资金承受能力。

**原始来源：**[原始资料](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital)。

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">Ohio数据中心担保和股权投资</span>
<span class="event-entry-preview">SB Energy/OpenAI项目形成巨大有条件信用风险</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-08-17。

**公布了什么：**NVIDIA宣布提供Ohio PORTS-Pike项目土地、电力、建筑壳体相关信用支持，并投资SB Energy约$1.5B；后续10-Q披露其合同担保按阶段最高约$105B，合计同类敞口约$108.5B。

**对公司的实际意义：**担保最大额不是当期债务或已发生损失，需等每期租约生效、项目资金和最终租户履约证据；是影响普通股风险的关键事项。

**原始来源：**[原始资料](https://nvidianews.nvidia.com/news/nvidia-guarantees-sb-energy-s-ports-pike-technology-campus-in-ohio-to-exclusively-host-nvidia-ai-compute)。

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">FY2027 Q2财报与大额承诺</span>
<span class="event-entry-preview">收入$96.221B，Q3指引$108B但未实现</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-08-26。

**公布了什么：**Q2 GAAP营收$96.221B、营业利润$63.734B、数据中心市场收入$89.023B；发布FY2027 Q3收入指引$108B±2%、毛利约74%±0.5个百分点，指引不含中国数据中心计算收入。

**对公司的实际意义：**确认持续收入增长，同时10-Q报告$279B制造供应承诺及$29B云服务承诺等，预示供应、现金与客户融资风险同时扩大。

**原始来源：**[原始资料](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/)。

</div>
</details>
</section>
<section class="event-month" data-month="2026-09">
<h3 class="event-month-heading">2026-09</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">宣布收购Hugging Face</span>
<span class="event-entry-preview">近$11.9B收购价及最多$1B留任激励，尚待审批</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-09-02。

**公布了什么：**向SEC披露签订收购Hugging Face协议，预计向股东支付约$11.9B，另最多约$1.0B股权留任计划，目标2027上半年完成并受审批条件约束。

**对公司的实际意义：**有望加强模型社区、应用分发和开发软件接触面，但截至本次研究尚未完成交割；不可把Hugging Face收入并入NVDA已实现营业收入。

**原始来源：**[原始资料](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)。

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">追加$150B回购授权</span>
<span class="event-entry-preview">剩余回购总授权增至$235B</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-09-28。

**公布了什么：**董事会授权在原计划上增加$150B，使剩余授权约$235B，并称计划至FY2028执行。

**对公司的实际意义：**资本分配规模重大；授权不是当前现金支出或已经减少的发行股数，仍受现金流和融资条件约束。

**原始来源：**[原始资料](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-a-150-Billion-Share-Repurchase-Authorization-Increase/default.aspx)。

</div>
</details>
</section>
<section class="event-month" data-month="2026-10">
<h3 class="event-month-heading">2026-10</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">供应链扩产与订金</span>
<span class="event-entry-preview">基板产能规划2.5倍，KYEC获$1.1B预订款</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-10-21。

**公布了什么：**与IBIDEN、三星电机和欣兴电子等达成基板扩张安排，目标未来三年总能力2.5倍；Amkor封测拟于2028年底前扩张超300%；NVIDIA向KYEC提供约$1.1B产能预订垫款。

**对公司的实际意义：**可能缓解Blackwell/Rubin系统瓶颈，但产能规划与扩产不是当季交付收入；存在预付现金、提前承诺和最终需求不匹配风险。

**原始来源：**[原始资料](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)。

</div>
</details>
</section>
</div>

**覆盖与限制：**核查NVIDIA 2025年末、FY2026 10-K、FY2027 Q1/Q2 10-Q、2026年5–10月IR重大公告及2026年9月SEC收购文件；未能证明每一份云商保密采购、土地审批、客户融资文件已穷尽。2026年10月的$1B科研支持、与Adobe/Cisco/Modal等合作、英国$250M捐赠属于B/C级经营生态或成本进展，不等于巨额已售合同。11月5日报道中国H200进口审批进展属于风险线索，**尚不能将媒体库存数字当NVDA确认收入**。FY2027 Q3截至2026-10-25，但截至本研究日**尚未发布财报**，不补编Q3实际。

## 3. 公司正在做什么、做到哪一步？

| 公司正在推进的重要事情 | 为什么重要、希望实现什么？ | 目前做到哪一步？下一关是什么？ |
|---|---|---|
| **Blackwell Ultra与Vera Rubin量产交付** | 新架构GPU+CPU+NVLink网络和机架平台决定高价值数据中心销售持续性与毛利 | Q2 10-Q称Blackwell仍占大部分系统出货，Rubin于FY2027 Q3开始生产出货，Q2已在全速扩产阶段；最新Q3 **尚未发布实际财报**。下一关核验11月17日真实Rubin交付/收入、毛利与74%管理层指引兑现情况。[Q2申报](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| **AI工厂客户融资与信用敞口** | 云商/AI模型公司是否能融资并向终端收费，关系到NVIDIA交付、应收收现和下游需求独立性 | 8月签署$500B第三方融资平台MOU和Ohio信用担保，期内$108.5B为有条件分期的担保上限而非已付现金；下一关看贷款签约及生效项目、租户实际付款、担保被要求履行情况。[10-Q承诺与附注](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| **HBM、封装、基板与光互联扩产** | 芯片卖不出去/造不出来都会影响GPU毛利和经营现金，巨额预付和供应承诺也会增加库存风险 | 7月末已披露**$279B**制造供应承诺，10月21日进一步公布基板未来三年2.5倍能力和$1.1B KYEC产能预订款。下一关看实际良率、产能、预付款耗用及库存从7月末$31.575B继续变化。[10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) · [供应扩产公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx) |
| **Hugging Face收购与开发工具平台整合** | 若完成交割可进入模型开发与分发链条，但公司不应因收购新闻直接把未并表业务写入已赚收入 | 9月2日SEC正式披露**约$11.9B对价＋上限$1.0B员工股权激励**；仍待审批、计划2027上半年完成。下一关看监管与交割、商誉、员工奖励、合并收入和利润是否真实体现。[SEC申报](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm) |

## 4. 财务状况：收入、利润和现金

**美国GAAP，统一十亿美元（USD bn）**；FY2025、FY2026为截至2025-01-26/2026-01-25的年度；H1 FY2027截至2026-07-26；TTM按FY2026−H1 FY2026＋H1 FY2027计算。本公司是GPU/系统厂商，不是金融企业；财报没有对两大分部单独披露GAAP毛利，所以列**合并GAAP毛利**而不是从分部自行倒推。

| 指标（十亿美元） | FY2025 | FY2026 | H1 FY2026 | H1 FY2027 | TTM至2026Q2 |
|---|---:|---:|---:|---:|---:|
| **合并收入** | 130.497 | 215.938 | 90.805 | 177.837 | **302.970** |
| GAAP毛利 | 97.858 | 153.463 | 60.521 | 133.299 | **226.241** |
| GAAP营业利润 | 81.453 | 130.387 | 50.078 | 117.270 | **197.579** |
| GAAP净利润 | 72.880 | 120.067 | 45.197 | 118.010 | **192.880** |
| 经营现金流 OCF | 64.089 | 102.718 | 42.779 | 74.421 | **134.360** |
| 购置长期资产和无形资产现金 | 3.236 | 6.042 | 3.122 | 4.434 | **7.354** |
| 简易自由现金流 FCF | 60.853 | 96.676 | 39.657 | 69.987 | **127.006** |

<small class="financial-glossary">GAAP＝美国会计准则；净利润包含证券投资公允价值收益；OCF＝经营现金流；FCF（本表）＝OCF−长期资产及无形资产现金购置，不含另列的设备融资本金，因此与公司定义FCF稍有不同；SBC＝股权激励；H1＝半年；TTM＝最近四个已报告季度。</small>

**财务质量总结：**最近三季**FY2026Q4→FY2027Q1→Q2**收入**68.127→81.615→96.221**，GAAP营业利润**44.299→53.536→63.734**；利润率保持高位，Q1/Q2 GAAP毛利约74.9%/75.0%。对应经营现金流**36.190→50.344→24.077**，简易FCF**34.906→48.587→21.400**。Q2 OCF从H1 74.421减Q1 50.344得到24.077；Q2投入从H1 4.434减Q1 1.757得到2.677。最新季度因收款周期、税收支付和库存投入出现明显现金波动，不能把高营业利润等同立即收到同额现金。过去H1按GAAP确认净利润**118.010**，其中税前股权证券收益**23.707**（Q2单季7.771），非经常浮盈不能外推成未来芯片利润。H1 SBC约**3.954**。另外，Q2末应收账款**63.059**（FY26末38.466）、库存**31.575**（FY26末21.403），两项大幅增长必须在下一季复核收现、拨备和销售质量。[FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) · [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm) · [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

**资产负债与资本压力：**2026-07-26现金22.443、可交易债券34.143，共**56.586**；有息债务33.366，保守可用净现金**23.220**。此外有可交易股票投资42.783及非上市股票投资51.157，股权投资可能随市场波动，**不作为等同无风险现金的EV桥接加项**；Q2末约24.147十亿股在外，回购授权发生在期后并不能前置改变此分母。10-Q还披露约$279B供应及产能承诺、$29B云服务承诺、约$25B待启用数据中心租赁、约$25B权益投资承诺、$8B资本支出类承诺，属于**未来不同性质的履约/现金需求**，不能当已经到期负债直接减两次；额外$36B云容量安排另有条款，须防止和正式表内分类混加。Ohio多期潜在担保最高约$108.5B亦非当前已确认现金损失。[Q2 10-Q附注10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

## 5. 管理层与资本分配

CEO **黄仁勋（Jensen Huang）**通过“Blackwell整机交付→Vera/Rubin下一代平台→GPU网络和开发软件”提高每客户可销售系统范围，Q2数据中心营收$89.023B是已经实现的交付财务证据。Q2公司实现收入**96.221B**，超出先前Q1指引**$91B±2%**的中心值；接下来**$108B±2%**仅是下一季前瞻指引（不假定中国数据中心计算收入）。大额融资合作与保障并非无成本的客户需求扩大，应同时检验最终客户真实运行率和算力租赁现金。

股东分配方面，FY2027上半年现金回购约**$39.044B**，另实际分红现金约**$6.290B**；Q2末真实已发行股数**24.147B**，低于年初24.304B，说明回购已经真实减少股份。2026年5月新增**$80B**、9月28日再新增**$150B**回购授权，公告称剩余总授权**$235B**、预期至FY2028执行；这是批准额度，不是已执行$235B，也不能忽略其未来与产能、融资和Hugging Face拟收购的资金竞争。[Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) · [9月回购公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-a-150-Billion-Share-Repurchase-Authorization-Increase/default.aspx)。

Hugging Face收购尚未交割，约$11.9B支付、最高$1B员工留任股权激励有后续商誉和稀释/费用影响；管理层应交付可辨认的软件/模型分发收入，而非仅增大开发者数量。应把资金承诺与经审计实际现金转化作为业绩考核的另一半。

## 6. 估值分析：当前股价贵不贵？

**三情景每股美元区间（2026-11-08；引用2026-11-06 NVDA美国常规交易收盘 $186.64）：**
- **悲观：$141.31–$188.13**；
- **基础：$227.16–$270.24**；
- **乐观：$270.24–$350.37**。

**本节必须保持估值性质透明：**这三档是**FY2026Q4、FY2027Q1/Q2的实际盈利与现金能力，加上英伟达自身2026-05-20和2026-08-26业绩日可验证市场倍数**的条件性**市场隐含股权估值区间**。两个交易日倍数不能独立证明股票“内在合理价值”；高毛利、真实经营现金和股东回报提供基本支撑，但若市场普遍不愿支付25–33倍营业利润，基础与乐观区间会整体失效。**不使用未来2028财报预测、DCF或同行对比。**

| 情景 | 最近季度实际经营基线及估值锚点 | 美元/股下限–上限 | 相对11/6现价 |
|---|---|---:|---:|
| **悲观** | 下端Q2偏弱单季FCF **$21.400B×4** × Q2财报日自身 P/TTM FCF **39.86x**；上端FY2026Q4较弱单季EBIT **$44.299B×4** × Q2自身EV/TTM EBIT **25.51x**，加净现金 | **$141.31–$188.13** | **-24.3%～+0.8%** |
| **基础** | 下端FY2027Q1已实现EBIT **$53.536B×4**、上端Q2已实现EBIT **$63.734B×4**；两端都采用近期Q2自身EV/TTM EBIT **25.51x**，加当前可用净现金 | **$227.16–$270.24** | **+21.7%～+44.8%** |
| **乐观** | 下端用Q2 EBIT与当时自有25.51x；上端须Q2较强EBIT运行率持续，并重现Q1公布日公司自身EV/TTM EBIT **33.09x** | **$270.24–$350.37** | **+44.8%～+87.7%** |

**2–3季盈利和FCF主锚：**2026年1月的FY2026Q4实际营收68.127、GAAP EBIT44.299、OCF36.190、FCF34.906；2026年4月的FY2027Q1营收81.615、EBIT53.536、OCF50.344、FCF48.587；2026年7月的FY2027Q2营收96.221、EBIT63.734、OCF24.077、FCF21.400（单位十亿美元）。Q1/Q2真实EBIT连续增长，基本上下限分别从两个相邻已实现季度形成，而非多年历史中位数。Q2经营现金显著受营运资金和税款时点影响，**把单季低FCF×4只用于悲观压力测算，绝非未来全年FCF预测**。实际TTM EBIT **197.579B**、FCF**127.006B**；相比Q2 EBIT×4的254.936B和FCF×4的85.6B，说明两项机械年化受近期增长和季节性显著影响。[Q1](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm) · [Q2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

**近期自有市场定价系数的全部输入（上市公司真实已报告口径）：**2026-05-20 Q1财报日收盘**$223.47**、Q1期末**24.221B**股份、普通现金＋可交易债券**$50.335B**、有息债务**$8.470B**，故企业价值EV＝223.47×24.221−(50.335−8.470)＝**$5370.80B**；当时实际TTM EBIT＝FY2026 130.387−FY2026Q1 21.638＋FY2027Q1 53.536＝**162.285B**，自身EV/TTM EBIT＝**33.09x**。2026-08-26 Q2财报日收盘**$209.66**、Q2末**24.147B**股份、普通现金与可交易债券**$56.586B**、有息债务**$33.366B**，EV＝**$5039.44B**；TTM EBIT **197.579B**，自身EV/TTM EBIT＝**25.51x**。当时股权市值209.66×24.147＝**$5062.66B**，P/真实TTM FCF127.006＝**39.86x**。期末资产负债数据与业绩日收盘价之间存在时点差异，属于明确披露的模型近似。[股价日线](https://stockanalysis.com/stocks/nvda/history/) · [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm) · [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)。

**统一价格桥接：**当前用Q2末股份24.147B、可用净现金23.220B，不将股票投资市值当无风险现金。企业价值法公式：**每股价＝（实际季度EBIT×4×已核实自有EV/TTM EBIT倍数＋23.220B）÷24.147B**；股权P/FCF法不再额外加现金/减债。六个端点逐个可复算：

1. 悲观低＝（21.400×4×39.86）÷24.147＝**$141.31**；Q2偏弱现金季度机械年化×自身近期P/FCF。
2. 悲观高＝（44.299×4×25.51＋23.220）÷24.147＝**$188.13**；使用FY2026Q4已实现较弱EBIT。
3. 基础低＝（53.536×4×25.51＋23.220）÷24.147＝**$227.16**；Q1较弱持续EBIT。
4. 基础高＝（63.734×4×25.51＋23.220）÷24.147＝**$270.24**；Q2较强持续EBIT。
5. 乐观低＝同基础高＝**$270.24**，维持Q2同期倍数。
6. 乐观高＝（63.734×4×33.09＋23.220）÷24.147＝**$350.37**；倍数恢复Q1公布日33.09x，须业务增长、资金和毛利同时确认。

**现金流合理性复核：**以11/6收盘$186.64与Q2末股份24.147B计，股权市值**$4506.80B**、EV约**$4483.58B**；当前EV/TTM EBIT约**22.69x**，真实TTM FCF收益率约**2.82%**。基础上端**$270.24**隐含相同TTM FCF收益率会更低；Q2自身市场倍数曾达到高值不构成独立财务合理价证明。Q2经营现金流24.077与净收益59.688显著背离、H1权益证券非经营收益23.707、客户应收63.059和库存31.575共同限制目标价可信度。

**验证与反证：**悲观若11月17日发布FY2027Q3实际营收/毛利明显低于管理层108B±2%及74%±0.5个百分点指引、应收未收回、客户建设延迟，则可能兑现；基础需看营业利润继续强劲、库存及应收转现金、供货保持高质量且不发生实质担保兑付；乐观必须有超强Rubin交付/收款和盈利，同时市场重回更高自身营业利润定价。**最大反证**是NVIDIA可能通过对客户投资、签云购买协议和提供担保促进客户采购芯片，使真实需求与融资链高度相关，且高倍数一旦重估，下跌可远超单季利润变化。

## 7. 主要投资风险

| 风险 | 对股票可能有什么影响 | 可观察的改判信号 |
|---|---|---|
| **融资依赖与循环采购** | GPU最终需求部分由AI云负债、客户预付款、NVIDIA投资及担保共同驱动；下游终端收费不足可能连带压缩设备订单与股权资产价值 | 主要AI云债务利差、租赁现金收款、客户取消或延期机柜项目、担保触发、NVIDIA应收坏账和投资减值 |
| **重大供给承诺及扩产投资** | $279B供应承诺加新增基板/封测/光互联产能，若需求降速，库存跌价、预付款损失或毛利下降 | Q2末库存31.575B和订单/供应承诺继续增长却收入不匹配、减值拨备、超额零件采购 |
| **客户集中、ASIC及价格竞争** | Q2单一直接客户占16%；若大型云商提高自研TPU/Trainium或转AMD方案，NVIDIA议价力和市占可能下降 | 毛利率下降、系统价格压力、客户云租金/利用率下降，独立客户续购 |
| **出口和地缘限制** | H20/H200及更强数据中心计算产品出口许可、中国境内进口审批与本土替代，可限制实际可交货市场 | 监管文件更新、获准出货金额及真实收入；2026-11-05有中国H200入境受阻报道，媒体“香港积压芯片”不得直接认作NVIDIA已确认销售。[Reuters](https://www.reuters.com/world/china/nvidia-chips-pile-up-hong-kong-china-withholds-import-approval-2026-11-05/) |
| **资本配置、收购与股东稀释** | Hugging Face未交割约$11.9B＋最多$1B激励，和$235B回购授权、云容量支持争夺现金；股东不一定全部受益 | 监管交割、费用与商誉、股份回购实际数量、经营现金流减去资本承诺 |
| **股权投资浮盈及估值倍数下降** | H1股票投资收益23.707B税前抬高净利，若回撤且高估值倍数下调，股价会双重承压 | 非经营损益、真实EBIT与FCF、市场EV/EBIT及订单回款低于当前定价所需条件 |

**结论：**NVIDIA的主要财务强项是可核实的高速数据中心销售、75%左右毛利和持续扩张的GAAP营业利润；风险不只是AI GPU竞争，而是**制造/客户融资/算力承租/股权投资/担保**构成彼此相关的资金链。股价从10月高点回撤不自动等于足够安全；在11月17日官方Q3披露前，不应把108B指引、Rubin全部计划交付或任何尚未交割收购当成现有收入。

