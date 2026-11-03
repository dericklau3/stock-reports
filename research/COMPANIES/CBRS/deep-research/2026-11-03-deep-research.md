# Cerebras Systems（CBRS）完整深度研究 — 2026-11-03

- **投资观点：**谨慎观察。真正的云推理收入、OpenAI合同及AWS/Oracle分销合作证明商业需求存在，但高资本开支、客户股权对价与硬件可靠性争议尚未转化成可验证的每股现金回报。股价下跌不自动意味着有安全边际。
- **核心逻辑：**公司通过晶圆级计算系统出售硬件与高速推理算力；核心看点不是基准测试速度，而是客户持续付费、芯片寿命、机器使用率与扣除客户让利后的全成本现金利润。
- **主要风险：**客户高度集中、数据中心扩张先消耗现金、设备寿命/折旧估计争议、股份和客户权证稀释，以及上市短而造成的高估值不确定性。

## 1. 公司到底是做什么生意的？

Cerebras 是一家美国AI计算基础设施公司，以晶圆级处理器（Wafer-Scale Engine，WSE）、整机系统及相应软件向客户提供现场计算设备或通过云端销售大模型训练和高速推理服务。**财报只有一个报告分部**，按收入性质披露两大类：硬件、云及其他服务。后一类实际上含多种不同收费方式，下文逐一说明；公司没有为这些子业务分别公布收入，不能分摊臆造金额。[2026Q2 10-Q：收入与MD&A](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

<details class="business-detail">
<summary>① 现场 AI 硬件：卖晶圆级计算服务器｜2026Q2 GAAP 收入 5,411.9 万美元</summary>

**实际卖什么及需求：**向希望在自己机房掌控训练、推理、数据和部署节奏的客户销售搭载WSE的完整计算系统、设备与配套软件；并非把裸晶圆直接卖给终端个人。直接采购方为企业、研究机构或算力运营商；合作渠道不能自动视为付款人。

**付款和确认：**买方依硬件合同向Cerebras支付采购款；控制权在按合同发货、交付或达到客户验收条件时转移，才形成硬件收入。预订不等于交付，客户融资也不等于Cerebras收现。

**成本和利润：**第三方晶圆制造、封装、组装、检测、运输、质保、存货跌价、人员和设施费用。2026Q2硬件收入54.119百万美元、直接成本53.141百万，GAAP毛利仅0.978百万美元，约1.8%；其中客户权证摊销使净收入下降，不能据此直接计算未经让利的产品售价利润率。

**举例假设（非真实订单）：**某研究机构为本地训练模型采购一套WSE机柜，向Cerebras或其合同销售方付款，设备交付且满足合同验收后Cerebras确认相应系统销售收入；机构自己的研究人员是使用者，晶圆厂是上游供应商，不是最终付款客户。

[10-Q收入确认与成本](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
</details>

<details class="business-detail">
<summary>② 专属云算力 Dedicated Capacity：客户预订固定算力容量｜子项收入未单独披露</summary>

**实际卖什么及需求：**客户为确定的模型推理负载预留专用计算容量，以获得可计划的吞吐与响应速度，无须自行投资所有服务器及机房。

**付款和确认：**直接购买长期算力的模型公司或平台依据承诺容量合同向Cerebras付款；公司披露通常为take-or-pay，即使实际用量偏低也有合同付款义务。服务提供期间逐步确认收入，不能在签下多年合同的当季一次性确认。OpenAI是有原始合同、服务和Q2收入证据的真实客户，但其750MW承诺的剩余未交付容量不等于已经确认收入。

**成本和利润：**系统折旧、机房租金、电力网络、维护人员、供应成本与空闲容量。长约降低部分需求不确定性，却未消除交付、资金和合同履约风险。

**举例假设（非真实订单）：**某大模型公司按月购买一段预留推理容量，让其应用按合同使用；应用终端用户向模型公司订阅付费，模型公司再履行向Cerebras购买容量的义务；Cerebras按服务期间形成收入。

[10-Q Dedicated Capacity、OpenAI合同](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
</details>

<details class="business-detail">
<summary>③ 按量云算力 On-Demand：卖推理 token 或约定时长的训练资源｜子项收入未单独披露</summary>

**实际卖什么及需求：**小型开发者、AI应用公司及平台可先以按量计费方式调用推理API或在约定时间运行训练任务，不必先承诺大型长期部署。

**付款和确认：**直接付费方是使用Cerebras云的开发者或与Cerebras签约的平台，取决于实际合同；最终在第三方应用里提问的人不一定是Cerebras客户。按已消耗token收取费用，或预付token包、随用量消耗结转收入；训练负载按合同期间确认。预收款不等于所有收入已实现。

**成本和利润：**推理计算资源占用、服务器折旧与运维、电力、网络以及促销或渠道分成；高吞吐不必然等于高毛利。

**举例假设（非真实订单）：**某创业团队在Cerebras云预购token包用于AI客服，用户询问触发推理，Cerebras按实际消耗确认收入，团队为直接付款者；客户服务的最终使用者并不直接购买WSE硬件。

[10-Q On-Demand业务及收费](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
</details>

<details class="business-detail">
<summary>④ 软件支持与代管：为已安装的超级计算系统持续运维｜子项收入未单独披露</summary>

**实际卖什么及需求：**对已经购买设备的机构提供软件维护、技术支持及客户机房内超级计算集群的运营管理，解决长期运行、故障处理和升级维护问题。

**付款和确认：**拥有相关系统并与Cerebras签订支持或管理合同的客户支付服务费；官方披露软件支持合同一般为1–5年，按实际提供服务期间逐步确认。不同于购买时一次确认的硬件收入。

**成本和利润：**工程师、技术支持、软件维护和驻场/远程运营；毛利取决于服务工作量、合同价格和支持成本，未见该子项独立利润。

**举例假设（非真实订单）：**一家科研中心买下机柜后再与Cerebras签三年软件支持合同，研究人员使用集群，科研中心按合同支付维护费用，Cerebras在提供支持的期间确认服务收入。

[10-Q服务收入政策](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
</details>

<details class="business-detail">
<summary>⑤ 定制 AI 模型服务：协助客户训练、开发或优化模型｜子项收入未单独披露</summary>

**实际卖什么及需求：**为特定企业/机构提供模型开发、训练、性能调优与专用解决方案服务。客户购买的是完成的模型服务或成果交付，并非必然自购全部设备。

**付款和确认：**委托方依服务及验收合同付款；按照合同条款，在持续履约期间确认，或在客户验收约定成果时一次确认。合作名称不代表该类业务已贡献可单独识别的金额。

**成本和利润：**模型工程师、研究资源、开发工具和计算成本；要通过合同定价、交付效率覆盖研发人工。

**举例假设（非真实订单）：**某机构委托Cerebras对行业模型优化推理效率，双方约定验收成果，机构支付项目费用，Cerebras按实际合同的服务期间或成果验收时确认收入。

[10-Q custom AI modeling](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
</details>

<details class="business-detail">
<summary>⑥ 机房建设/运营成本转付：向特定客户转收数据中心费用｜2026Q2约1,450.3万美元，含在云及其他服务中</summary>

**实际卖什么及需求：**在定制客户协议下，Cerebras为机房部署和运营先发生部分支出，再将合同约定费用转付给该客户。它不是一项与高毛利AI推理相同的独立产品，不能把转付规模当技术竞争力。

**付款和确认：**直接合同客户补偿相关支出，公司依据适用会计规定将相应金额同时体现在营业收入及成本。2026Q2转付收入14.503百万美元已包含在云及其他服务125.991百万中，不可另加。财报披露该项2026Q1起出现，具体单独合同成本与利润未充分细拆。

**成本和利润：**机房建设、运营等转付对应成本；即使总收入上升也不代表核心业务毛利同步增加。

**举例假设（非真实订单）：**为某大客户开通专属机房算力时，Cerebras根据合同先支付一定配置运营费用，再向该客户转收，客户负担成本；这与客户另外购买长期算力属于可以共同存在的不同收费组成。

[2026Q2 GAAP/core对账及10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm)
</details>

**最新收入结构对账。** 以下单位均为**百万美元、美国GAAP**；最新季为2026年4–6月。**同比（YoY）**＝2026Q2相对2025Q2；**环比（QoQ）**＝2026Q2相对紧邻的2026Q1。公式均为（本期－比较期）÷比较期×100%。2026Q1由两期上半年实际披露的累计数减去Q2单季数复算，非业绩指引。

| 财报收入类别/组成 | 2025Q2 | 2026Q1 | 2026Q2 | 同比 | 环比 | 业务及合并说明 |
|---|---:|---:|---:|---:|---:|---|
| 硬件 Hardware | 70.295 | 110.593 | 54.119 | −23.0% | −51.1% | 现场系统销售；已含权证收入抵减 |
| 云及其他服务 Cloud and other | 33.027 | 82.813 | 125.991 | +281.5% | +52.1% | 专属云、按量云、支持、模型服务、转付收入 |
| ↳ 其中：机房成本转付（子项，不重复相加） | 0 | 4.111 | 14.503 | 新增业务，不适用 | +252.8% | 包含在上行云及其他服务中，2026Q1开始 |
| 跨分部内部收入抵销/合并调节 | — | — | — | — | — | 只有一个报告分部；两行收入直接相加即合并额 |
| **合并 GAAP 营业收入** | **103.322** | **193.406** | **180.110** | **+74.3%** | **−6.9%** | **54.119 + 125.991 = 180.110** |

公司披露云及其他服务的Dedicated/On-Demand/支持/定制模型细分收入金额**未单独提供**，故不假装这些项目是可加总的正式分部。2026Q2公司自定义core收入209.869百万美元，等于GAAP的180.110－转付14.503＋客户权证摊销44.262；core并非GAAP，也不是实际收现，不能与GAAP收入相加或将未来合同都当core收入。[Q2 10-Q收入分解](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[GAAP/core官方桥接](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm)。

**竞争和利润判断：** 相对客户使用GPU、AMD加速器或云巨头自建方案，Cerebras的差异化在低延迟生成，但优势是否扩展到系统总拥有成本、跨模型兼容性及长期可靠性仍缺可比客户级审计数据。云收入迅速扩张，但第二季度GAAP硬件毛利仅0.978百万、云毛利24.581百万，两类业务都被客户股权让利及高投入影响；公司披露调整后core毛利率40.6%，不能据此替代真实GAAP毛利率14.2%或自由现金流。[官方成本和毛利率披露](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

## 2. 近期已公布的重大事件

以下按**首次确认公告月份升序**显示主要A级事件；公司/合作伙伴的普通集成、营销演示与无重大约束的合作不因新闻数量进入本时间轴。近12个月检索仍存在源覆盖缺口，尤其不能宣称所有SEC附件与所有相关方社交披露已逐条核实。

<div class="event-roadmap" aria-label="重大事件时间轴">
<section class="event-month" data-month="2026-01">
<h3 class="event-month-heading">2026-01</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">OpenAI 750MW长期容量合同</span>
<span class="event-entry-preview">OpenAI确认分批采购推理容量；额外1.25GW仅是选择权。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-01-14（OpenAI原始公开公告）；**签约时间：** 2025-12，具体签约日未在本次资料中核实。

**公布了什么：** OpenAI确认与Cerebras合作部署750MW推理能力，预计2026–2028年逐批提供；另有1.25GW的潜在选择权，不等于已购买。

**对公司的实际意义：** 从技术故事变成有约束力的容量合同。2026Q2公司已确认OpenAI相关收入56.8百万美元，但合同总名义容量不等于全额已付现或利润；客户贷款与分批交付使现金质量复杂。

**原始来源：** [OpenAI原公告](https://openai.com/index/cerebras-partnership/)｜[SEC 10-Q合同条款](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)

</div>
</details>
</section>

<section class="event-month" data-month="2026-03">
<h3 class="event-month-heading">2026-03</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">AWS Bedrock推理合作</span>
<span class="event-entry-preview">AWS公开确认异构推理合作，但正式商用及相关收入待验证。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-03-13。

**公布了什么：** AWS公布拟把Trainium与Cerebras系统组合用于Bedrock AI推理；2026年6月双方另订立全球硬件租赁及支持协议。按Cerebras 6/30 10-Q，合同租赁尚未开始，相关收入尚未确认。

**对公司的实际意义：** 有可能借助大云平台扩大客户触达，但不能在2026Q2财务里提前算入AWS商用收入；AWS客户权证亦要计入股东经济成本。

**原始来源：** [AWS独立公告](https://press.aboutamazon.com/aws/2026/3/aws-and-cerebras-collaboration-aims-to-set-a-new-standard-for-ai-inference-speed-and-performance-in-the-cloud)｜[10-Q AWS租赁说明](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)

</div>
</details>
</section>

<section class="event-month" data-month="2026-05">
<h3 class="event-month-heading">2026-05</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">IPO募资并上市</span>
<span class="event-entry-preview">以185美元发行3,450万股，为扩产筹集约62亿美元净额。</span>
</summary>
<div class="event-detail-content">

**公告/事件日期：** 2026-05-13定价；2026-05-14纳斯达克开始交易；2026-05-15 IPO完成。

**公布了什么：** 按每股185美元发行34.5百万股A类普通股；公司披露净募资约62亿美元（以招股费用计量，最终现金流入科目另有差异）。

**对公司的实际意义：** 大幅增强当期现金缓冲，也意味着新股、历史优先股转换、A/B/N多类别经济权益与IPO后锁定期成为每股估值的核心输入，不能只用A类流通股算总市值。

**原始来源：** [IPO最终招股书](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)｜[10-Q IPO事项](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)

</div>
</details>
</section>

<section class="event-month" data-month="2026-07">
<h3 class="event-month-heading">2026-07</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">AMD异构推理架构</span>
<span class="event-entry-preview">两种处理器分工完成模型推理，需验证实际生产成本和利用率。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-07-23。

**公布了什么：** AMD宣布与Cerebras将高吞吐预填充计算与低延迟生成计算组合，计划在2026年下半年推进生产部署，后续Cerebras业绩材料指向2026Q4。

**对公司的实际意义：** 如果全系统效率得到真实客户确认，可能拓宽可服务模型，但增加的GPU/网络硬件不能在比较成本时隐去；公告和早期基准测试并非已兑现收入或稳定整机毛利。

**原始来源：** [AMD投资者关系共同公告](https://ir.amd.com/news-events/press-releases/detail/1293/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference-solution)

</div>
</details>
</section>

<section class="event-month" data-month="2026-08">
<h3 class="event-month-heading">2026-08</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">第二季度财报与经营指引</span>
<span class="event-entry-preview">云业务同比高增长，GAAP与core差异、资本开支同样突出。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-08-12；报告截止2026-06-30。

**公布了什么：** Q2 GAAP收入180.110百万美元、core收入209.869百万；Q2 GAAP毛利率14.2%和core毛利率40.6%；2026Q3 core收入指引214–216百万，FY2026 core指引880–890百万。

**对公司的实际意义：** 云服务真实采用上升，但硬件GAAP收入下降、激励摊薄、机房支出及会计调整均会影响股东价值。11/12财报才可检验Q3，不能提前写实际值。

**原始来源：** [SEC财报及MD&A](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[公司业绩公告及core桥接](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm)

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">CS-4新一代系统发布</span>
<span class="event-entry-preview">公司公布新硬件性能并承诺Q3首批发货，交付验收尚未核实。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-08-18。

**公布了什么：** Cerebras发布CS-4及其针对特定模型/基准的相对性能宣称，最初计划2026年第三季度开始交付。

**对公司的实际意义：** 晶圆级芯片的竞争力与折旧回本都取决于实际交付和稳定使用寿命。本轮未取得足以证明Q3按时发货和客户验收的原始证据，状态应写“未核实”，不能偷改原时间表。

**原始来源：** [Cerebras CS-4发布公告](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)

</div>
</details>
</section>

<section class="event-month" data-month="2026-09">
<h3 class="event-month-heading">2026-09</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">芬兰机房长期产能项目</span>
<span class="event-entry-preview">规划50→80→165MW分期部署，增加长期容量与租约约束。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-09-01。

**公布了什么：** 与Compute Nordic Finland披露芬兰Mikkeli项目，首期50MW建设启动、分阶段计划总计165MW，涉及长期服务安排。

**对公司的实际意义：** 有助于履约的物理资源储备，也放大固定费用；建设开工不等于正式带电或高利用率。地方投资总额不能记为Cerebras自身收入或由其独自承担的资本开支。该项目与欧洲旧有200MW整体规划有重叠风险，不直接叠加。

**原始来源：** [Cerebras/Compute Nordic公告](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-and-compute-nordic-finland-announce-new-165-mw-ai-data)

</div>
</details>
</section>

<section class="event-month" data-month="2026-10">
<h3 class="event-month-heading">2026-10</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">Oracle OCI云推理合作</span>
<span class="event-entry-preview">Oracle独立确认2027年计划上线，尚非已确认订单及2026收入。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-10-27。

**公布了什么：** Oracle宣布计划在其OCI云基础设施提供Cerebras高速推理，目标为2027日历年。公告未提供约束性最低采购金额、合同分成或具体上市日期，并且包含未来产品交付免责条款。

**对公司的实际意义：** 与AWS类似，提高潜在分销覆盖，但“云平台公开支持”与“已经部署、客户付费、Cerebras确认毛利”是不同阶段；不能因Oracle品牌就直接上修财务。

**原始来源：** [Oracle公司原始公告](https://www.oracle.com/asean/news/announcement/ai-world-cerebras-and-oracle-team-up-to-bring-cerebras-ai-inference-to-oracle-cloud-infrastructure-2026-10-27/)

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">Culper发布做空及设备寿命指控</span>
<span class="event-entry-preview">针对WSE可靠性、折旧寿命和数据中心成本提出争议；尚非核实结论。</span>
</summary>
<div class="event-detail-content">

**公告日期：** 2026-10-28（空头机构自行公开，不是发行人证实的事项）。

**公布了什么：** Culper Research声明持有CBRS空头，并称芯片实际寿命短于市场预期、质疑硬件连接件与有关寿命及成本表述。证实的是**存在这份带利益冲突的指控**，不是证实“WSE两年必坏”。本轮未获得独立、可复现且覆盖在役样本的设备失效率或寿命审计。

**对公司的实际意义：** 若未来确认实际使用寿命显著低于预期，维护更换成本、折旧、客户可靠性和全系统投资回报均需下修；若客户连续运行、保修数据和经审计资产寿命支持公司口径，则指控的关键部分可被证伪。旧版报告未覆盖此项，属于必须跟进的新重大反证。

**原始来源：** [Culper发布的自述与系列说明（第三方保留的原帖文本）](https://teapawt.net/CulperResearch/status/2115473790033363377)｜[IPO招股书设备折旧政策](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)。不能把做空方报告当独立事实审计。

</div>
</details>
</section>
</div>

**核验边界：** 因官方财报尚未更新到Q3、未完成近12个月所有监管文件及合作方社交资料逐条覆盖，以上为已取得直接原件的重大事项清单，并非无遗漏保证。重要事件还包括2026-10-14及10-28分批解禁资格：这属于可售限制变化，**不等于卖出，也不等于新增股数**；相关供应压力在第5/7节分析。[424B4限制说明](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)。

## 3. 公司正在做什么、做到哪一步？

| 公司正在推进的重要事情 | 为什么重要、希望实现什么？ | 目前做到哪一步？下一关是什么？ |
|---|---|---|
| **OpenAI已承诺容量分期部署** | 这是大规模收入、算力使用率与长期客户现金回收的支柱；客户过度集中也会让一次大规模路线变更冲击营业收入。 | 2026Q2已确认相关GAAP收入56.8百万，H1 74.4百万，证明不是纯意向；750MW按计划分期至2028，1.25GW只是选择权。下一步核验实际部署容量、持续使用、非现金贷款抵偿与新模型仍采用比例；具体后续交付批次日期未完整披露。[10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) |
| **CS-4商业交付与AMD整机架构** | 决定公司能否将性能优势扩展到经济可行的规模化生产，并降低每单位有效token的总设备成本。 | 2026-08发布CS-4、2026-07 AMD确认方案；CS-4原Q3首批发货目标已过，但本次没有确认验收的原始数据。下一关是出货/验收、可持续运行时间、整机加上GPU和网络之后的成本、实际故障及保修水平；AMD目标Q4生产仍属计划。[CS-4](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-unveils-cs-4-30-times-faster-gpu-based-solutions)｜[AMD](https://ir.amd.com/news-events/press-releases/detail/1293/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference-solution) |
| **AWS和Oracle转化为真实付费云分销** | 让公司不只依赖少数直接采购方，还可以由大型云平台带来第三方客户。 | AWS已签硬件租赁/集成，但截至6/30未启动相应租赁、未确认收入；Oracle 10/27宣布2027拟上线。下一关是AWS Bedrock实际商用、OCI上线、实质算力使用与Cerebras可确认收入，相关合同金额和利润分成尚未披露。[AWS及10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[Oracle](https://www.oracle.com/asean/news/announcement/ai-world-cerebras-and-oracle-team-up-to-bring-cerebras-ai-inference-to-oracle-cloud-infrastructure-2026-10-27/) |
| **数据中心交付、现金效率和设备寿命证明** | 已投入现金能否产出可持续收益，取决于机房实际带电、硬件寿命与使用率；空头报告让设备可靠性变成更需要客观验证的核心问题。 | 2026H1现金资本开支548.873百万，芬兰9/1首期建设启动，2026Q2末还有约23亿美元的未开始/期后相关最低未来租约款。下一关是新增机房可用容量、客户利用率、保修/更换频率、实际使用寿命和GAAP与core成本桥接；不能以短期演示代替长时间生产数据。[10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[项目公告](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-and-compute-nordic-finland-announce-new-165-mw-ai-data) |

## 4. 财务状况：收入、利润和现金

金额单位：**百万美元**。采用美国GAAP；完整财年截止12月31日，H1是六个月，TTM至2026-06-30按FY2025＋2026H1−2025H1逐项重算。年度数据取[上市最终招股书中的审计报表](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)，半年数据取[2026Q2 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

| 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2 |
|---|---:|---:|---:|---:|
| GAAP 营业收入 | 290.252 | 509.991 | 373.516 | 680.673 |
| GAAP 毛利 | 122.738 | 199.071 | 111.735 | 237.103 |
| GAAP 经营损益 | −101.438 | −145.862 | −492.270 | −552.480 |
| GAAP 合并净损益 | −481.602 | +237.827 | −464.534 | −512.352 |
| 经营活动现金流 OCF | +451.978 | −10.050 | −47.488 | +66.305 |
| 现金资本开支 Capex | 23.435 | 382.739 | 548.873 | 746.518 |
| 简化自由现金流 FCF | +428.543 | −392.789 | −596.361 | −680.213 |

<small class="financial-glossary">GAAP＝美国会计准则；毛利＝收入减直接成本；经营损益＝再扣研发、销售等费用后的盈亏；OCF＝经营现金流；Capex＝购建设备/基础设施的现金支出；简化FCF＝OCF－Capex；TTM＝最近12个月。</small>

**资金说明：** 2026-06-30现金及等价物6,742.157百万美元＋短期投资1,179.390百万＝7,921.547百万；**受限现金684.680百万另列、不算可自由用现金**。若扣除OpenAI工作资本贷款918.244百万及已入表经营租赁负债568.827百万，得到研究定义的租赁调整后净现金代理6,434.476百万。尚未开始及期后新租赁未来最低付款约23亿美元，属于未来约束，不可与已入表租赁机械双扣。[10-Q资产负债和租赁附注](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

**总结：** 收入在同比增长（2026H1较2025H1约+84%），但最新Q2 GAAP合并收入环比−6.9%，GAAP毛利率仅14.2%；Q2 core 40.6%毛利率剔除了公司定义的客户权证及其他调整，两者不应混用。2025年正净利包含约363.336百万美元一次性远期合同负债终止收益，并非稳定盈利；2024年经营现金流明显受到大额客户预收款支撑。2026H1的FCF为−596.361百万，显示真实扩张耗现，IPO募资储备虽大，仍须证明将来可转成设备全生命周期利润和每股现金。[10-Q利润及现金流](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

## 5. 管理层与资本分配

公司由联合创始人兼CEO **Andrew Feldman**领导。2026-05成功完成IPO，对扩张融资是重大兑现，但这笔现金来自向股东发行股份而非主营自由现金；IPO后保留A/B/N多类别经济权益，B类附高投票权、N类无投票权，对公众股东治理权构成限制。[10-Q股本与IPO](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

2026-08-05实际发行三类经济权益合计**237,564,041股**（A 112,247,109、B 111,601,424、N 13,715,508）；这是可核实的已发行股数，**不是**2026-11-03最新完全稀释权益股数。OpenAI/AWS客户权证与员工股权激励有可能影响实际稀释，已行使计入8/5股数的权证不得再双算。Q2确认股权激励377.008百万美元，含IPO时点一次性触发约273.6百万，不能把全部金额直接年化，也不能因为非现金而忽视稀释；公司新增客户权证被按会计政策摊销抵减收入。[10-Q股票、激励及客户权证](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)。

管理层2026Q2时对下一季提出**core收入214–216百万**、全年**core收入880–890百万**、全年core毛利率41%–43%、core经营利润率−19%至−17%等指引。Q3已于9/30结束，正式业绩预计**2026-11-12美股收盘后**公布；截至研究日没有公开的新Q3实绩可用于验证这项承诺。按H1 core 401.217百万、Q3指引中点215百万倒算，全年指引中点885百万要求Q4 core约268.783百万，属于研究者门槛，不是官方Q4指引。[业绩披露](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm)｜[Q3官方公布日期](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-date-third-quarter-2026-financial)。

2026-10-14与10-28分批股份解禁资格可能扩大可售股票供给；Form 144仅是拟售申报、Form 4各交易代码意义不同，不能把“解禁”“计划出售”或账户间转移混同已经执行的二级市场卖出。新一批稀释、权证履约和所有11月实际已发行股数未完全重建，故估值保留时点缺口。[IPO锁定条款](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)。

## 6. 估值分析：当前股价贵不贵？

**合理价格参考：目前不能可靠给出持续经营意义上的单一公允价格。可复算的当期资产负债表参考为 $33.79/股（剔除客户权证资产的账面权益敏感性），但它**不是**已独立评估可变现净资产、目标价或下跌保护。** 核心障碍是：公司直到**2026-05**才上市，缺乏Skill要求的至少三个完整财年、同口径、真实交易所得的自身历史EV/收入倍数；公司TTM经营亏损、持续投入、没有稳定可资本化的自身盈利；未经核验的WSE资产回收价值与客户权证不应强行包装成可靠净资产估值。**不使用同行倍数、凭空倍数或未来DCF代替缺口**。

| 估值要素 | 截止本次研究可核实的数字与解释 |
|---|---|
| **单一资产价格参考** | **$33.79/股**＝(2026-06-30 GAAP账面股东权益9,154.642百万美元－客户权证相关资产1,128.397百万)÷2026-08-05全部三类经济股237.564041百万。纯账面压力参考，**非经核实的真实可清算NAV**。未经调整的GAAP每股账面权益为$38.54。 |
| **股价与参考差额** | **$96.36**（2026-11-02美东收盘）；$33.79比市价低约**64.9%**，表示市场愿为未来持续经营及无形能力支付溢价，**不是说价格必然跌到$33.79**。相较2026-10-19旧报告$120.66下跌约20.1%。 |
| **自身历史估值锚点** | 2026-05才IPO，不存在2023–2025年市场真实EV/收入可比观察值，更没有三个有效完整年度本公司交易中位数；故不编造所谓自身合理EV/收入倍数。 |
| **当前已实现经营与市场倍数** | TTM GAAP收入**680.673百万**、毛利237.103百万、营业亏损552.480百万、简化FCF−680.213百万；$96.36×237.564041百万股＝**$22.892bn经济市值代理**，减调整净现金$6.434bn＝**$16.457bn企业价值代理**，即**24.18× EV/TTM GAAP收入**。亏损状态下不机械算P/E。 |
| **现金与股数桥接** | 2026-06-30租赁调整后净现金**$6.434bn**（约$27.09/已发行经济股）；2026-08-05三类已发行合计237.564百万，未覆盖11月所有行权/授予/解禁变化和非同步资产时点。 |
| **最主要估值缺口** | 硬件寿命/使用率、客户股权经济让利、未来资本支出和已发行＋潜在稀释更新；资产账面值、可变现价值与持续经营价值不可混同。 |

**算术桥接：** $96.36 ×237.564041百万股－(6,742.157＋1,179.390－918.244－568.827)百万＝$16,457.2百万调整EV；再除以实际TTM GAAP收入680.673百万＝24.18倍。公司给出的2026全年**core收入指引中值885百万**对应18.60倍EV/指引收入，仅是未来指引对照，**不是**已实现TTM倍数，亦不拿它生成目标价。[10-Q财务与股本](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)｜[11月2日收盘历史报价](https://stockanalysis.com/stocks/cbrs/history/)。

**总结：** 市价仍隐含对多年成长与可持续高盈利能力的期待；股价下跌20%并没有改变“目前TTM GAAP亏损、资本密集、公司本身缺乏历史估值锚”的客观限制。想把$33.79资产账面代理升级为可信**合理股价**，还需能独立证明WSE寿命和可变现资产、完整实股及潜在股数、真实重复付费与现金利润，或在上市后累积足够本公司历史实际交易倍数；缺这些输入就不应凭个人偏好的倍数捏造$100或$150的公允目标。

## 7. 主要投资风险

| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |
|---|---|---|
| **OpenAI/G42等客户集中** | 少数客户的容量利用率或模型架构改变，就可能造成收入与现金回收波动；Q2前三大客户约占**76%**。 | 主要客户实际部署延误、收入占比恶化、OpenAI的贷款服务抵偿或合同条款发生实质不利变化。[10-Q客户分布](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) |
| **设备寿命和折旧估计争议** | 若WSE比财报折旧政策暗示的实际可用时间更短，设备更换、折旧、维护与现金投资回报会恶化；空头指控未独立证实。 | 长期生产环境可靠性/故障率披露恶化、维修质保准备增加、资产减值、会计折旧年限与实测寿命不相称。[IPO资产年限政策](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm) |
| **机房与硬件支出先于收入** | 长期租约和系统采购在客户大规模使用前先耗现，可能让高收入增长无法创造每股FCF。 | 2026H1 FCF−596百万后继续走弱、规划MW未能带电、资产使用率长期偏低。[10-Q现金/租赁](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) |
| **core调整与真实股东让利** | 客户权证抵减收入、IPO激励、未来授予与多类别股权导致GAAP和core差距扩大，损害每股收益。 | 真实GAAP毛利与FCF未跟上core增长、经济总股数或权证摊销超出可解释水平。[业绩桥接](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm) |
| **云渠道未转为真实付费且估值仍高** | AWS与Oracle的产品计划迟延或低使用，股价可能因高达24倍的EV/TTM GAAP收入而继续重估，即使合作未取消。 | AWS/Oracle未按计划GA、没有可观察租赁收入与使用量、Q3偏离指引、销量增长但营业利润持续恶化。[Oracle公告](https://www.oracle.com/asean/news/announcement/ai-world-cerebras-and-oracle-team-up-to-bring-cerebras-ai-inference-to-oracle-cloud-infrastructure-2026-10-27/) |

**总结：** 最危险的失败路径是“长期订单与云合作不断增加，但晶圆级设备折旧与更新频率、客户权益让利、机房固定成本和额外稀释使新增收入无法变成普通股股东的现金”。反过来，最强的反证将是Q3及后续季度对真实交付、长期WSE可靠性、GAAP利润改善、现金资本效率和持续多客户付费的独立、可复核披露。
