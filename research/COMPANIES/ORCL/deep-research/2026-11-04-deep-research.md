# Oracle（ORCL）完整深度研究｜2026-11-04

- **投资观点：** Oracle 的企业软件资产、数据库客户黏性和已经兑现的 AI 云增长值得肯定，但其资本密集度、融资成本和普通股稀释已使它不能简单按传统高利润软件公司评价；当前股价是否划算取决于订单转化为扣除全部投资成本后的现金。
- **核心逻辑：** OCI 增长是事实，6,640 亿美元 RPO 是待履行合同义务而非已收到现金；现在最重要的衡量标准是计算容量交付、收入、资本开支、客户付款与普通股每股回报能否匹配。
- **主要风险：** 2026-11-02 已定价的 100 亿美元股票发行和 100 亿美元高息债说明融资需求迫切；大额电力/租赁责任、客户集中及资产更新周期可能令收入高增长却不产生足够可分配现金。

## 1. 公司到底是做什么生意的？

Oracle 是一家同时经营企业数据库、应用软件、云基础设施（OCI）、硬件系统和专业服务的美国公司。它正在利用传统数据库/应用客户基础发展云业务；其中传统软件有较高转换成本，AI 计算基础设施则需要巨额硬件、电力和融资投入。

<details class="business-detail">
<summary>① OCI GPU / AI 算力租赁｜供模型训练与推理使用的计算资源</summary>

**卖什么与解决什么问题：** 把数据中心中的 GPU、计算服务器及其高速网络租给训练、运行 AI 模型的客户，免去客户自己购置和运维大型集群。

**谁购买、谁付款：** 直接采购计算容量的企业/模型公司向 Oracle 支付云服务款；客户的终端用户可能向该模型公司付费，但一般不会直接向 Oracle 购买这批 GPU。

**怎样收费与确认收入：** OCI 云计算以使用量或合约容量/服务期计费，实际提供服务后按会计条款确认收入；合同的剩余履约义务（RPO）不等于已经收到的现金。**成本与利润：** GPU、服务器、网络、机房、电力、折旧、租赁和融资支出可能很高；季度 OCI 收入不等于 GPU 部门已实现净利润。

**举例假设（非真实订单）：** 某 AI 企业向 Oracle 租用一组 GPU 集群训练模型；Oracle 负责交付可用计算服务，AI 企业按合同向 Oracle 付款并向自己的客户销售模型服务。

**披露边界：** OCI 当季收入 73.88 亿美元，但 Oracle 未按“GPU AI 计算”单独披露金额或盈利。

</details>

<details class="business-detail">
<summary>② OCI 常规计算、云存储与网络｜企业 IT 运行所需的基础设施</summary>

**卖什么与解决什么问题：** 向企业出售云虚拟机、块存储/对象存储、网络连接、备份等服务，替代自有机房。**付款人：** 签约的企业 IT 部门或软件公司向 Oracle 支付云费；最终业务用户不一定是直接客户。**收费及会计：** 随资源使用或合约期限确认服务收入。**成本：** 服务器、存储、机房、电力、工程师、折旧和运维。

**举例假设（非真实订单）：** 一家零售企业把自己的订单系统部署在 OCI 服务器，使用 OCI 网络及存储，按实际资源和合同容量向 Oracle 付费。

**披露边界：** 与 GPU 租赁一起计入 OCI，未单独披露本产品线收入。

</details>

<details class="business-detail">
<summary>③ OCI 数据库托管及跨云数据库｜为企业托管 Oracle 数据库</summary>

**卖什么与解决什么问题：** 提供 Oracle Autonomous Database、Exadata Cloud Service，以及部署在客户环境或 AWS/Azure/Google Cloud 合作环境中的 Oracle 数据库能力，让客户维持熟悉的数据库技术而不必整体迁移应用。**付款人：** 购买数据库服务的企业依据具体合同向 Oracle 或相关云平台付款；转售/合作渠道与实际付款人不可混同。**收费及确认：** 托管云服务依使用量或约定期限确认；其中可能与许可/支持相结合，不能把同一笔交易重复计为两个收入。**成本：** 计算/存储、专有数据库开发、合作分发、运营支持。

**举例假设（非真实订单）：** 某银行的系统已依赖 Oracle 数据库，希望在 Azure 上运行；它通过适用的 Oracle Database@Azure 安排采购数据库服务，供应方依合同结算，而不是银行必须重新开发整个数据库应用。

**披露边界：** 多云数据库当季增长较快，但绝对收入和独立盈利未披露；不得从增长百分比臆造收入额。

</details>

<details class="business-detail">
<summary>④ Fusion 与 NetSuite 云应用｜财务、人事、供应链等 SaaS</summary>

**卖什么与解决什么问题：** Fusion Cloud ERP/HCM/SCM/CX 与 NetSuite 等业务应用让企业管理财务、人力、采购、库存和客户关系。**直接付款人：** 采用相应 SaaS 的企业客户，通常基于订阅期和用户/模块等商业条款支付费用。**确认收入：** 云服务随订阅履约期确认。**成本：** 软件研发、销售实施、客户服务、托管设施和持续支持；已有规模带来复用优势。

**举例假设（非真实订单）：** 一家跨国制造商购买 Fusion 的财务与人力系统；Oracle 持续提供托管软件和更新，企业按合同支付订阅费用。

**披露边界：** 所有云应用合计当季 42.19 亿美元，Fusion/NetSuite 各自金额未在本研究引用的季度产品表单列。

</details>

<details class="business-detail">
<summary>⑤ Oracle Health 医疗信息系统｜医院电子病历与临床工作流</summary>

**卖什么与解决什么问题：** Oracle Health（含原 Cerner 产品体系）向医院和医疗体系提供电子健康记录、临床和行政管理软件及相关运营支持。**付款人：** 医院、医疗体系或医疗机构依据软件/订阅/支持/服务合同付款，而不是患者使用病历即直接支付 Oracle。**收入与成本：** 依据许可、托管和服务合同分别于交付或履约期间确认；主要成本涉及临床产品研发、部署整合、合规和客户支持。

**举例假设（非真实订单）：** 一家医院采购 Oracle Health 的电子病历与临床流程系统，Oracle 负责上线及维保，医院按照适用合同付费。

**披露边界：** Oracle Health 的收入跨云应用及相关许可/支持/服务分类，季度细分金额未完整公开；不能另造一个“Health 收入”加入合并总额。

</details>

<details class="business-detail">
<summary>⑥ 软件许可｜本地部署数据库、中间件及企业软件</summary>

**卖什么与解决什么问题：** 向需要自主管理系统的企业许可数据库、中间件和部分企业应用。**谁付款：** 直接企业客户或经授权分销渠道，依据合同取得软件使用权。**收费与确认：** 许可费用在满足交付和控制转移条件时通常确认，其节奏不同于逐期订阅。**成本：** 产品研发、渠道销售、知识产权及后续支持；部分后续维护另计入支持收入。

**举例假设（非真实订单）：** 一家企业在自己的服务器上部署 Oracle Database，向授权交易对手支付数据库许可证费用并取得约定版本的使用权。

**披露：** 2026-08-31 季度软件许可收入 6.55 亿美元。

</details>

<details class="business-detail">
<summary>⑦ 软件维护与支持｜老系统升级、修补和技术支持</summary>

**卖什么与解决什么问题：** 对已许可的数据库、中间件与企业软件提供补丁、版本升级及技术支持。**付款人：** 希望关键应用持续可靠运行的企业软件用户。**收费与确认：** 服务/维护合约费用随支持期确认，常有续订性质。**成本：** 工程支持、安全维护、升级研发和服务人员。

**举例假设（非真实订单）：** 某银行已部署 Oracle 本地数据库，每年另付支持合同费用，以获得更新和故障技术服务。

**披露：** 当季支持收入 48.95 亿美元；这是传统业务的核心现金流来源之一，但本报告无法从产品表精确隔离其净利润。

</details>

<details class="business-detail">
<summary>⑧ 硬件与集成系统｜Exadata 设备、服务器及存储硬件</summary>

**卖什么与解决什么问题：** 向需要专用性能/可靠性的客户销售集成数据库系统、设备及相关硬件服务。**付款人：** 直接采购设备或维护合约的企业。**收费与确认：** 设备通常在控制权转移时确认销售，硬件支持服务则在服务期确认。**成本：** 零部件采购、组装/物流、保修和现场维护。

**举例假设（非真实订单）：** 某大型企业购买 Exadata 专用数据库硬件并购买后续维保，分别在设备交付和支持期间向 Oracle 支付相关款项。

**披露：** 硬件分部当季总收入 7.74 亿美元；设备与支持未在这里按具体金额拆分。

</details>

<details class="business-detail">
<summary>⑨ 专业实施与咨询服务｜帮助客户迁移、部署和集成系统</summary>

**卖什么与解决什么问题：** Oracle 或服务团队协助企业规划、迁移数据库、配置 ERP、整合遗留 IT 系统。**付款人：** 委托实施工作的企业客户。**收费与确认：** 根据合同按服务时间/工作完成情况和适用履约进度确认收入。**成本：** 顾问工资、交付和项目管理、必要的外包服务。

**举例假设（非真实订单）：** 一家工业企业为上云项目聘请 Oracle 顾问做数据库迁移方案、测试和上线，按合同向 Oracle 支付实施费。

**披露：** 服务分部当季 14.14 亿美元，独立咨询与其他服务的收入并未在本次披露中全部分开。

</details>

**季度收入结构（单位：亿美元；2026 年 6—8 月 FY2027 Q1）。** 同比（YoY）＝最新季度对比去年同季，环比（QoQ）＝最新季度对比紧邻上一季；均为（本期－比较期）÷比较期×100%。上年/上季均为原始单季，不是累计值。

| 报告业务及产品披露层级 | 去年同季 | 上一季 | 最新季 | 同比 | 环比 |
|---|---:|---:|---:|---:|---:|
| **报告分部：云及软件（小计）** | **129.07** | **167.37** | **171.57** | **+32.9%** | **+2.5%** |
| ↳ 云收入（小计） | 71.86 | 99.13 | 116.07 | +61.5% | +17.1% |
| ↳ ↳ OCI 云基础设施 | 33.47 | 57.87 | 73.88 | +120.7% | +27.7% |
| ↳ ↳ 云应用 | 38.39 | 41.26 | 42.19 | +9.9% | +2.3% |
| ↳ 软件收入（小计） | 57.21 | 68.24 | 55.50 | -3.0% | -18.7% |
| ↳ ↳ 软件许可 | 7.66 | 18.81 | 6.55 | -14.5% | -65.2% |
| ↳ ↳ 软件支持 | 49.55 | 49.43 | 48.95 | -1.2% | -1.0% |
| **报告分部：硬件** | **6.70** | **9.24** | **7.74** | **+15.5%** | **-16.2%** |
| **报告分部：服务** | **13.49** | **15.23** | **14.14** | **+4.8%** | **-7.2%** |
| 已披露对外分部收入的其他抵销 | 0.00 | 0.00 | 0.00 | — | — |
| **合并营业收入** | **149.26** | **191.84** | **193.45** | **+29.6%** | **+0.8%** |

**层级与对账：** 171.57（云及软件报告分部）＋7.74（硬件）＋14.14（服务）＝193.45 亿美元；分部内的云/软件及其下级子项目仅用于解释组成，不额外累计。官方产品明细和分部披露在相关财季中不存在需要单列的额外净抵销额；这不表示公司内部完全不存在交易。来源：[FY2027 Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)、[Oracle Q1 财报](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)、[FY2026 Q4 全年公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx)。

**竞争与利润判断：** Oracle 的数据库转换成本、现有企业软件关系和跨云数据库能力有商业优势；客户也可选 AWS、Microsoft Azure、Google Cloud 或自建基础设施。OCI 正贡献最大产品收入和最高增速，但公司未独立披露 GPU 算力的扣除融资与设备更新后的利润；传统软件支持较稳定，也不能直接以某产品收入代替对应净利润。许可收入环比受销售时点/季节性影响，不能简单年化。

## 2. 近期已公布的重大事件

本次从 2025-11 至 2026-11 追踪可能改变资本结构、AI 合同经济或公司长期现金流的重大公开事项，兼纳更早的重要背景；以下按**公告月份**分组，属于 A 类的事件进入 Roadmap。已定价不等于交割，规划不等于商用。

<div class="event-roadmap" aria-label="重大事件时间轴">

<section class="event-month" data-month="2025-12">
<h3 class="event-month-heading">2025-12</h3>
<details class="event-entry">
<summary><span class="event-entry-title">FY2026 Q2 订单激增</span><span class="event-entry-preview">RPO 达 5,230 亿美元，OCI 延续高速增长</span></summary>
<div class="event-detail-content">

**公告日期：** 2025-12-10。

**公布了什么：** Oracle FY2026 Q2 业绩显示 RPO 约 5,230 亿美元、OCI 同比增长 68%，期内净利润受到一次性投资收益影响。

**实际意义：** 证明云合同储备增长，但未证明其全部已建成/付款/获利；非经常性收益不能当作未来稳定 EPS。

**原始来源：** [FY2026 Q2 官方业绩](https://www.oracle.com/de/news/announcement/q2fy26-earnings-release-2025-12-10/)。

</div>
</details>
</section>

<section class="event-month" data-month="2026-02">
<h3 class="event-month-heading">2026-02</h3>
<details class="event-entry">
<summary><span class="event-entry-title">450–500 亿美元融资计划</span><span class="event-entry-preview">2026 年提出大规模股票、债券与优先股融资安排</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-02-01；多项具体证券交易于 2026-02-02 至 02-04 继续披露。

**公布了什么：** Oracle 宣布日历年 2026 年 450–500 亿美元筹资方案，后续涉及 ATM 普通股发行、债券及强制可转换优先股；不同交易的最终所得与条款以各自 SEC 文件为准。

**实际意义：** AI 云建设需求已变成明确的债权和股权融资责任；该方案的资金不能与以后公告的资金重复算作“尚可筹集”的额度。

**原始来源：** [Oracle 融资计划](https://investor.oracle.com/investor-news/news-details/2026/Oracle-announces-Equity-and-Debt-Financing-Plan-for-Calendar-Year-2026/default.aspx)。

</div>
</details>
</section>

<section class="event-month" data-month="2026-06">
<h3 class="event-month-heading">2026-06</h3>
<details class="event-entry">
<summary><span class="event-entry-title">FY2026 年报确认资金消耗</span><span class="event-entry-preview">收入 673.57 亿美元，全年自由现金流为负</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-06-10。

**公布了什么：** FY2026 收入约 673.57 亿美元，全年现金资本开支约 556.63 亿美元，经营现金流约 319.77 亿美元，对应标准自由现金流约 -236.86 亿美元。

**实际意义：** 云收入的增长真实存在，但投入强度已经远超当期经营现金创造能力，必须依赖存量资金与新增资本。

**原始来源：** [Oracle FY2026 官方业绩](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx)。

</div>
</details>
</section>

<section class="event-month" data-month="2026-09">
<h3 class="event-month-heading">2026-09</h3>
<details class="event-entry">
<summary><span class="event-entry-title">AI 云交付、订单与增发同步发生</span><span class="event-entry-preview">OCI +121%，RPO 6,640 亿美元，200 亿美元 ATM 完成</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-09-10（Q1 FY2027 财报）；相关 10-Q 于随后申报。

**公布了什么：** 截至 2026-08-31 当季 OCI 73.88 亿美元、同比约 +121%；公司披露新增/交付约 850MW 计算容量和逾 30 万块 GPU，RPO 约 6,640 亿美元。该季度完成此前普通股 ATM 项目毛额 200 亿美元融资。

**实际意义：** 已实现计算服务收入与硬件交付，但以增发和高额资本开支共同支持；不能把 RPO 当作现金，也不能对已经完成的 ATM 再假定第二次稀释。

**原始来源：** [Q1 FY2027 业绩公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)、[季度 10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)。

</div>
</details>
</section>

<section class="event-month" data-month="2026-10">
<h3 class="event-month-heading">2026-10</h3>
<details class="event-entry">
<summary><span class="event-entry-title">Point Beach 电力成本承诺</span><span class="event-entry-preview">提出承担约 3 亿美元相关能源成本，监管条件未获证实落实</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-10-02。

**公布了什么：** Oracle 宣布有条件承担 Wisconsin Point Beach 相关约 3 亿美元能源成本，需依相关州监管审查批准。

**实际意义：** 数据中心配套电力的经济成本可能部分由 Oracle 承担；条件未满足前不是确认的当期现金资本开支。

**原始来源：** [Oracle Point Beach 公告](https://www.oracle.com/news/announcement/oracle-announces-commitment-to-absorb-rising-point-beach-energy-costs-2026-10-02/)。

</div>
</details>

<details class="event-entry">
<summary><span class="event-entry-title">Jupiter 能源供应与许可调整</span><span class="event-entry-preview">电费/居民补贴方案与减排许可修订仍待正式执行</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-10-13（El Paso Electric 提案）；2026-10-15（微电网许可设计修订）。

**公布了什么：** Oracle 公布拟议至少每年 1,000 万美元、10 年能源服务付款，以及最长三年、每年最多 5,500 万美元用户费率补贴提案；随后披露 Jupiter 微电网排放许可修订，计划降低获许可排放约 35%。

**实际意义：** 可能缓和能源与社区许可瓶颈，但成本可能上升。尚未核验最终许可证和确定执行协议，不能提前写成正式获批、实际供电或已支付全部金额。

**原始来源：** [10-13 电力安排](https://www.oracle.com/news/announcement/oracle-proposes-plan-to-offset-customers-utility-costs-2026-10-13/)、[10-15 许可修订](https://www.oracle.com/news/announcement/project-jupiter-microgrid-cuts-permitted-emissions-by-35-percent-2026-10-15/)。

</div>
</details>

<details class="event-entry">
<summary><span class="event-entry-title">投资者日提出现金转正及融资上限</span><span class="event-entry-preview">计划 FY2028 下半年现金转正，新增外部融资上限 200 亿美元</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-10-28。

**公布了什么：** 管理层提出 FY2028 下半年自由现金流转正、FY2029 全年自由现金流不低于 300 亿美元、FY2030 收入至少 2,250 亿美元、调整后经营利润率至少 40%、非 GAAP EPS 至少 21 美元；FY2027—FY2030 投资周期进一步从资本市场筹集不超过 200 亿美元（预计普通股 100 亿、债务 100 亿，另不含存量债务再融资及此前已完成的 200 亿美元 ATM）。

**实际意义：** 提供了清晰的现金与融资承诺，但属于管理层未来目标；投资者必须在后续报表中核查资本投入、GPU 资产更新、融资工具及现金流是否与承诺一致。

**原始来源：** [Oracle Investor Day 2026](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx)。

</div>
</details>
</section>

<section class="event-month" data-month="2026-11">
<h3 class="event-month-heading">2026-11</h3>
<details class="event-entry">
<summary><span class="event-entry-title">200 亿美元发行已定价，尚待交割</span><span class="event-entry-preview">拟发行 8,620.69 万股新股及 100 亿美元 7%–8.65% 债券</span></summary>
<div class="event-detail-content">

**公告日期：** 2026-11-02。

**公布了什么：** Oracle 已完成股票与债券发行定价：普通股 86,206,897 股，每股发行价 116 美元，股票净募集约 99 亿美元；债券总面值 100 亿美元，五档年利率 7.00%、7.45%、7.85%、8.00% 及 8.65%。公司预计于 2026-11-04 交割，须满足通常成交条件；股票和债券两部分并不互为交割先决条件。

**实际意义：** 两类融资并行意味着潜在普通股稀释和新增票息成本：五档债券一年票面利息合计约 7.7675 亿美元。**截至 2026-11-03 纽约常规收盘，不能把预计 11-04 交割写成已经完成**；估值因此将发行条款以“预计交割后备考”呈现。

**原始来源：** [Oracle 2026-11-02 定价公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Pricing-of-20-Billion-of-Common-Stock-and-Senior-Notes/default.aspx)、[SEC 债券最终定价条款](https://www.sec.gov/Archives/edgar/data/1341439/000119312526443918/d87441dfwp.htm)。

</div>
</details>
</section>
</div>

**更早但仍重要的背景：** 2025-07-22 OpenAI 与 Oracle 公布 4.5GW Stargate 额外合作（[OpenAI 原始公告](https://openai.com/index/stargate-advances-with-partnership-with-oracle/)）；2025 年 10 月关于 Michigan / Wisconsin 等园区的公开计划属于后续项目规划，不能把所有园区投资计划金额等同于 Oracle 自身收入。**覆盖限制：** 本轮核验了关键 SEC 文件、公司公告与部分合作/能源公告，但未完成所有地方许可完整卷宗、所有项目最终客户合同或逐月穷尽所有企业公告；重大事件筛选不宣称绝对完备。

## 3. 公司正在做什么、做到哪一步？

| 公司正在推进的重要事情 | 为什么重要、希望实现什么？ | 目前做到哪一步？下一关是什么？ |
|---|---|---|
| AI 计算容量交付与 Stargate 商业履约 | 将已签计算容量订单转成可收费服务，避免“RPO 高、资产闲置”。 | [2026-09-10 财报](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)证明 OCI 实际收费与部分 GPU 交付；下一关是履约转收入速度、客户付款、利用率与项目运营现金流，详细合同保护条款未全部披露。 |
| Jupiter 及其他数据中心供电/许可 | 电力可用性决定服务器能否开始产生收入，也决定项目固定成本。 | [10-15 许可设计修订](https://www.oracle.com/news/announcement/project-jupiter-microgrid-cuts-permitted-emissions-by-35-percent-2026-10-15/)已提交，但截至现有核验未确认最终批准/供电验收；下一关是最终许可证、供电可用与客户实际接受容量，具体日期未核实。 |
| 将资本开支高峰转为持续自由现金流 | 决定这轮扩张是为现有股东创造现金还是不断增发融资。 | [10-28 投资者日](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx)已提出 FY2028 H2 转正与 FY2029 至少 300 亿美元 FCF 目标；[11-02 融资](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Pricing-of-20-Billion-of-Common-Stock-and-Senior-Notes/default.aspx)已定价但未核验交割；下一关是实际交割、后续季度现金流/Capex/融资披露验证管理层承诺。 |
| 跨云数据库、企业/医疗 AI 应用商业化 | 用较轻资本投入的数据库和软件收入改善云增长的盈利质量。 | FY2027 Q1 多云数据库同比增长高，但绝对基数不公开；Fusion 和 Health AI 已发布部分产品但单独新增付费未披露。下一关是实际收费、续约、产品利润与客户验证，不把产品发布当收入。 |

## 4. 财务状况：收入、利润和现金

单位：**十亿美元（USD B）**；按 Oracle 美国 GAAP。FY2025 / FY2026 分别为截至 2025-05-31 / 2026-05-31 的财年，Q1 FY2027 截至 2026-08-31。TTM 使用 FY2026 全年－上一年可比 Q1＋最新 Q1；毛利为按主要直接成本计算的**研究代理**，不是 Oracle 正式单列的统一 GAAP 毛利。

| 指标 | FY2025 | FY2026 | FY2027 Q1 | TTM至2026-08-31 |
|---|---:|---:|---:|---:|
| GAAP 收入 | 57.399 | 67.357 | 19.345 | 71.776 |
| 毛利代理（非官方统一毛利） | 40.472 | 44.336 | 11.612 | 45.906 |
| GAAP 经营利润 | 17.678 | 20.606 | 6.728 | 23.057 |
| 归属普通股 GAAP 净利润 | 12.443 | 16.984 | 4.679 | 18.736 |
| 经营现金流 OCF | 20.821 | 31.977 | 23.103 | 46.940 |
| 现金资本开支 Capex | 21.215 | 55.663 | 28.499 | 75.660 |
| 自由现金流 FCF | **-0.394** | **-23.686** | **-5.396** | **-28.720** |

<small class="financial-glossary">GAAP：美国会计准则；OCF：日常经营流入或使用的现金；Capex：现金购买设备、建设机房等；FCF＝OCF－现金 Capex；TTM：最近 12 个月。</small>

**资金约束：** 截至 2026-08-31，现金与可交易短期证券约 **37.077B**，有息借款 **125.337B**，融资租赁 **9.185B**，经营租赁负债 **34.621B**，优先股约 **5B** 清算额。未起租租赁未来名义付款约 **288B**，为多年未折现承诺，**不是已到期的当期借款**；采购承诺约 34.150B 不应与 Capex/租赁未经核对就简单相加。11 月新债与新股的交割及净所得尚未计入截至 8 月的历史报表。Q1 GAAP OCF 23.103B 包含 **11.363B 具有重大融资成分的客户预付款**；若机械剔除此项，经济敏感性 OCF 11.740B、FCF -16.759B，**不是 GAAP 或公司正式调整 FCF**。[SEC Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)、[FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm)。

**总结：** 收入、经营利润和 OCI 交付明显增长，TTM GAAP 盈利为正；但 TTM 现金资本开支 **75.660B** 超过经营现金流 **46.940B**，FCF **-28.720B**，与传统高现金转化 SaaS 企业的经济质量不同。FY2026 净利润还有 Ampere 投资相关一次性收益，不能把历史净利润无条件当作正常可分配收益。资本投入回报、客户预付款履约成本、GPU 更新及融资现金成本，是未来报表最关键的验证。

## 5. 管理层与资本分配

截至本次核验，Oracle 已由 Clay Magouyrk 和 Mike Sicilia 担任联席 CEO，CFO 为 Hilary Maxson；不以人物履历代替业绩。公司在 2026-10-28 投资者日作出明确的 FCF 路径和额外融资上限承诺，又在 11-02 将 **100 亿美元股权 + 100 亿美元债券**定价，说明已经迅速执行融资，但不是提前证明资金在 AI 资产上产生高回报。

**普通股稀释：** Q1 FY2027 已完成的 200 亿美元 ATM 发行是过去实际稀释，11-02 公布的 **86,206,897 股**是另一笔新发行，预计 11-04 交割。以 2026-09-07 约 3.023736B 股实际普通股为基数，若新发行交割，则增加约 2.85%；新发行价格 116 美元低于 2026-10-30 收盘 130.67 美元。公司此前的强制可转优先股未来可能转换为额外普通股，模型不能把优先股清算额和转换后全部股数重复扣除。股息和回购授权必须放在现金流、融资负担之后审视，不能以回购授权金额误称发行剩余额度。

**新增债券现金成本：** 11-02 定价的五档固定利率债券本金分别为 2.00B（7.000%）、1.75B（7.450%）、2.25B（7.850%）、2.50B（8.000%）、1.50B（8.650%），合计年化票面利息约 **0.77675B 美元**，不包括发行折扣、其它新融资、现有债息；这会压低未来可归属普通股的现金收益。[Oracle 发行公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Pricing-of-20-Billion-of-Common-Stock-and-Senior-Notes/default.aspx)、[SEC 条款](https://www.sec.gov/Archives/edgar/data/1341439/000119312526443918/d87441dfwp.htm)。

## 6. 估值分析：当前股价贵不贵？

**合理价格参考估计：$169.28/股（截至 2026-11-04，使用 Oracle 自身最近四个完整财年 EV/收入倍数中位数，对已定价但尚待交割的融资作条件备考调整）。** 对比 2026-11-03 可核实常规收盘价 **$126.19**，模型参考价与市价差额 **+34.1%**；不是确定的未来涨幅或远期目标价。

| 估值要素 | 数值与来源 |
|---|---|
| **合理价格参考** | **$169.28/股**；Oracle 自身 4 年历史 EV/收入中位数映射到当前已实现 TTM |
| 当前股价、模型价差 | 2026-11-03 收盘 **$126.19**；（169.28÷126.19－1）＝约 **+34.1%**；[Investing 收盘记录](https://jp.investing.com/equities/oracle-corp-historical-data) |
| 自身历史 EV/收入锚点 | FY2023 **7.40×**、FY2024 **7.57×**、FY2025 **9.69×**、FY2026 **11.55×**，中位数 **8.63×**；[StockAnalysis / S&P Global](https://stockanalysis.com/stocks/orcl/financials/ratios/) |
| 当前已经实现的经营 | TTM **收入 71.776B**、经营利润 23.057B、FCF -28.720B；[Oracle 10-Q](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm) |
| 净索偿及经济股数 | 8 月末借款 125.337B、融资租赁 9.185B、优先股 5B、少数股东权益代理 0.424B，现金及短投 37.077B；**条件备考**再计新债 +10B、两类净募资现金 +19.9B；9 月实际普通股 3.023736B＋拟增发 0.086206897B＝**3.109943B 股** |
| 最重要限制 | 11-04 交割尚未确认、募集款可能迅速投入 Capex；历史 EV 指标的负债纳入口径、FY 末价格与当期年报最终披露日存在时点差；极高未来租赁与客户依赖会令历史倍数不一定适用 |

**可复算公式：** （8.63 × 71.776B －〔125.337B＋10B＋9.185B＋5B＋0.424B－(37.077B＋19.9B)〕）÷ (3.023736B＋0.086206897B)＝**$169.28/股**。这里假设发行按已定价条款完成、净融资现金暂未使用；**既有经营租赁 34.621B 与未来尚未起租租赁 288B 未直接当成额外债务扣减**，因为所用历史 EV 口径不能无条件再加完整未折现租约而不相应调整历史样本。

**方法局限：** 历史倍数对应的财年末价格与当年最终业绩发布存在时间差，因此是一组事后可见的财年年度估值样本，**不是严格的当时可交易信息回测**。FY2026 高 AI 估值、如今大幅变化的资金结构及最新新增票息可能使 8.63× 历史中位数偏乐观；此外样本企业价值与本次备考优先索偿/融资租赁桥接存在数据商口径差。模型给出明确可复算的单一价格，不能将其误读为 Oracle 经审核的内在价值或“市场必然回归到 169.28 美元”。

## 7. 主要投资风险

| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |
|---|---|---|
| 数据中心与 GPU 资本开支高于回款 | 收入增长但长期负现金流持续，需要新融资并压低每股价值 | 资本开支继续超过 OCF，FY2028 H2 自由现金流转正目标明显偏离 |
| 新股与高成本债券融资 | 旧股东权益被摊薄，新增约 7.77 亿美元年票面债息压缩未来净现金 | 11-02 融资未能按期交割、后续新增融资超承诺，或利息覆盖能力走弱 |
| RPO 到收入和现金的转化不足 | 订单储备被延迟交付、重议或不能按期待付款 | RPO 增长而客户验收、现金回收与 OCI 可计费收入背离 |
| 能源审批与履约瓶颈 | 设备与固定成本先发生、可收费容量晚到，资本回报下降 | Jupiter 等关键供电/许可迟迟不能最终获批、建成和验收 |
| 客户集中、GPU 技术替代及长期租赁 | 特定 AI 客户需求变化或设备过时，仍须支付融资/租赁费用 | 大客户延期付款、资产更新周期短于会计寿命、未起租租赁承诺增加 |

**总结：** Oracle 最危险的下行并非“完全没有 AI 客户”，而是**订单和收入真实增长，却无法覆盖 GPU 更新、能源、租赁、利息以及每股稀释成本**。10 月投资者日提出的现金转正时间表和 11 月高成本融资应放在一起评价；在合同利润、实际长期支付责任与资本回报尚未充分透明前，历史倍数锚定的 $169.28 只是条件性研究参考。
