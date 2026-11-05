# Amazon.com, Inc.（NASDAQ：AMZN）深度研究｜2026-11-05

- **投资观点：**中性偏谨慎。AWS增长强劲，但价格高于公司自身历史EV/收入中位数对应的当前参考价，且巨额AI投资持续吞噬现金。
- **核心逻辑：**零售平台、商家服务、广告、会员与AWS的收入来源互补；2026Q3 AWS收入同比增长39.3%、贡献集团约63%营业利润，利润增长已经发生，但投资转化为股东自由现金回报尚未证实。
- **主要风险：**2026现金资本开支预计2200亿美元、TTM自由现金流为负、债务及租赁增加、Anthropic/OpenAI客户和融资关系、广告监管及新业务资本消耗。

## 1. 公司到底是做什么生意的？

Amazon为消费者出售商品、为外部商家提供交易及广告物流服务、为企业出租云计算资源。最新2026Q3的原始[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)披露**三大报告分部**和**七个收入类别**；下面逐一讲解所有可辨认的持续经营收款业务，未单独公开的子业务金额不编造。

<details class="business-detail">
<summary>① 自营线上商店｜Q3 $68,470m</summary>

亚马逊自己购入并销售商品，消费者向Amazon付全额商品款；按交付义务完成确认商品收入。采购、库存、配送、退货、客服是主要成本。

**举例假设（非真实订单）：**消费者在Amazon自营店购买电视，Amazon收货款并负责发货，不能把第三方卖家全额销售额算在这里。

</details>

<details class="business-detail">
<summary>② 实体商店｜Q3 $5,710m</summary>

包括Whole Foods等门店购物：顾客在实体店挑选商品并付款，Amazon确认商品零售收入，负担进货、人工、房租和损耗。线上下单门店自提通常归在线收入。

**举例假设（非真实订单）：**顾客到Whole Foods买蔬菜、刷卡付款，Amazon承担采购和冷链成本。

</details>

<details class="business-detail">
<summary>③ 第三方商家销售佣金｜属$46,492m卖家服务</summary>

外部商家卖自己的货，Amazon向商家收销售佣金及相关平台费；消费者商品付款与Amazon服务费不是同一会计收入。平台、支付风控、客服是成本；佣金收入独立金额未披露。

**举例假设（非真实订单）：**第三方商户自行发货一件衣服，买家付款给交易渠道；商户向Amazon付平台佣金。

</details>

<details class="business-detail">
<summary>④ FBA仓储配送｜属卖家服务，子项未披露</summary>

Amazon替商家提供仓储、分拣、配送、退货等履约服务，向商户收相应仓储和配送费用；仓租、司机、设备、人工、电力为成本。与佣金同属第三方卖家服务披露数，不能独立估算再相加。

**举例假设（非真实订单）：**商家把库存放进FBA仓，买家下单后平台代发货，商家付仓配服务费。

</details>

<details class="business-detail">
<summary>⑤ 广告｜Q3 $19,637m</summary>

卖家、品牌和出版商等广告主购买搜索赞助、展示或视频广告；广告主而非普通购物者承担投放费，按已提供的广告服务确认收入。成本为流量、技术、审核、销售；存在FTC广告收费诉讼。

**举例假设（非真实订单）：**品牌买搜索结果赞助位，用户看见后点击，品牌依广告合同向Amazon付款。

</details>

<details class="business-detail">
<summary>⑥ Prime会员｜订阅总收入$14,006m的一部分</summary>

用户按月或按年支付Prime会员费获得配送/影音等权益，随服务期确认相应订阅收入；Amazon需负担配送福利、内容及技术成本。Prime单独金额未公开。

**举例假设（非真实订单）：**消费者支付一年Prime会员费，Amazon分期履约会员权益并承担配送成本。

</details>

<details class="business-detail">
<summary>⑦ 视频、音乐、有声书、电子书等独立订阅｜金额未拆分</summary>

独立数字订阅用户支付周期费用，按提供服务期间确认收入；Amazon承担内容版权、制作分成、运营等成本。Amazon官方将这些订阅与Prime合并披露。

**举例假设（非真实订单）：**用户订阅Audible服务并按月付款，平台提供有声内容并支付版权成本。

</details>

<details class="business-detail">
<summary>⑧ AWS计算和AI芯片云租用｜AWS总收入$45,984m的一部分</summary>

公司、政府、开发者买EC2、Trainium或相关计算资源，按使用量、预留容量或合同付费；AWS保留服务器产权并负责折旧、芯片、电力、机房和网络。AI算力子项没有独立收入披露。

**举例假设（非真实订单）：**软件公司在AWS租计算实例部署程序，向AWS按用量付费，再向终端客户收软件费。

</details>

<details class="business-detail">
<summary>⑨ AWS存储、数据库和数据服务｜金额未单列</summary>

企业按存储容量、请求量、数据库实例或相关服务用量向AWS付费，Amazon按服务交付确认收入；成本包括硬盘/服务器、备份、带宽、电力和运维。

**举例假设（非真实订单）：**企业把数据放进S3并使用数据库，按容量和实例使用付云费。

</details>

<details class="business-detail">
<summary>⑩ Bedrock及AI模型调用平台｜金额未单列</summary>

企业开发者购买模型推理/AI应用平台服务，付费方式依具体资源、调用量或合同；模型提供商与AWS客户角色不同，AWS需支付算力/模型分成/技术支持等成本。不可把OpenAI/Anthropic投资增值当Bedrock收入。

**举例假设（非真实订单）：**企业让客服软件调用Bedrock模型，并向AWS付接口调用费。

</details>

<details class="business-detail">
<summary>⑪ 对外运输与物流服务｜归入其他$1,645m</summary>

Amazon向外部客户提供配送、运输等服务，客户按合同付运费；公司承担车辆、员工、运力、燃料与系统成本。子项金额不单独披露。

**举例假设（非真实订单）：**非Amazon商户委托Amazon运输包裹，向Amazon物流付服务费。

</details>

<details class="business-detail">
<summary>⑫ 医疗服务（含Amazon Pharmacy/One Medical）｜归入其他</summary>

提供药房及医疗相关服务；付款者按交易可以是患者、保险付款方或企业客户；药品/诊疗服务满足收入确认条件后形成销售，成本包括药品、医疗人员、药师、合规。具体独立收入未披露。

**举例假设（非真实订单）：**患者线上购处方药，个人付自付额、保险承担适用部分，Amazon履约并取得相应收入。

</details>

<details class="business-detail">
<summary>⑬ 视频内容授权与发行｜归入其他</summary>

内容采购或发行方为某影视内容使用权向Amazon支付授权费，按合同授予权利/履约确认收入；成本为制作、版权和分销，不能与消费者视频订阅重复计算。

**举例假设（非真实订单）：**外部平台获准播放某影视内容并支付授权款。

</details>

<details class="business-detail">
<summary>⑭ 联名信用卡合作协议｜归入其他</summary>

发卡金融机构为联名品牌合作与相关服务向Amazon支付合同款项；持卡人贷款和利息通常属于银行业务，不是Amazon自行放贷。成本为营销、会员权益与合作支持。金额和具体费率未披露。

**举例假设（非真实订单）：**银行与Amazon合作发行联名卡，Amazon依合作协议取得对应合同收入。

</details>

**收入结构及两种增长率。** 单位：百万美元，均为**单季度**，数据来源[2026Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)与[季度补充指标](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm)。**同比YoY**＝与去年同季度比较（2026Q3 对2025Q3）；**环比QoQ**＝与紧邻上一季度比较（2026Q3 对2026Q2）；计算都是（本期－对比期）÷对比期×100%。

| 分部或收入类别 | 2025Q3 | 2026Q2 | 2026Q3 | 同比YoY | 环比QoQ | 收入来源/口径 |
|---|---:|---:|---:|---:|---:|---|
| **A. 法定报告分部（仅本组三项可加总）** | | | | | | |
| 北美报告分部 | 106,267 | 116,177 | **112,852** | 6.2% | -2.9% | 北美电商、广告、订阅和实体 |
| 国际报告分部 | 40,896 | 42,197 | **43,108** | 5.4% | 2.2% | 其他地区电商、广告和订阅 |
| AWS报告分部 | 33,006 | 42,232 | **45,984** | 39.3% | 8.9% | 全球云计算、数据库和AI |
| **A：报告分部合计** | **180,169** | **200,606** | **201,944** | **12.1%** | **0.7%** | 已按外部确认净销售额呈列，无单列抵销 |
| **B. 全球收入类别（与A是不同维度，不可重复相加）** | | | | | | |
| 线上自营商店 | 67,407 | 70,432 | **68,470** | 1.6% | -2.8% | 商品交易按毛额确认 |
| 实体商店 | 5,578 | 5,794 | **5,710** | 2.4% | -1.4% | 线下商品零售 |
| 第三方卖家服务 | 42,486 | 46,780 | **46,492** | 9.4% | -0.6% | 佣金和卖家仓配服务 |
| 广告 | 17,703 | 19,809 | **19,637** | 10.9% | -0.9% | 广告主购买赞助/展示/视频广告 |
| 订阅 | 12,574 | 13,730 | **14,006** | 11.4% | 2.0% | Prime和视频音频等订阅 |
| AWS | 33,006 | 42,232 | **45,984** | 39.3% | 8.9% | 计算/存储/数据库/AI |
| 其他 | 1,415 | 1,829 | **1,645** | 16.3% | -10.1% | 物流、医疗、版权授权、联名卡 |
| **B：类别合计** | **180,169** | **200,606** | **201,944** | **12.1%** | **0.7%** | 与分部合计是同一集团收入 |
| **合并收入对账差额** | **0** | **0** | **0** | — | — | 非额外收入；分部合并未单列内部抵销 |

**对账：** 2026Q3三大报告分部112,852＋43,108＋45,984＝**201,944**；七类收入68,470＋5,710＋46,492＋19,637＋14,006＋45,984＋1,645＝**201,944**。独立FBA、Prime、Bedrock、医疗等子业务没有独立金额，其收入已经包含在母类，不能重复加总；第三方商品GMV不等于Amazon第三方服务收入。

**竞争与利润：** AWS收入同比+39.3%、环比+8.9%，Q3 AWS营业利润17,773m、营业利润率38.7%，集团营业利润28,076m中约**63.3%**来自AWS；北美零售利润8,723m，国际利润1,580m。线上自营同比仅+1.6%，广告+10.9%（恒定汇率+12%）。**2026 Prime Day多数大国提前至Q2，而2025在Q3**，公司称排除时点差异集团Q3同比增速约高4个百分点，所以季度同比不完全是需求变化。Amazon在配送和云产品组合有规模优势，但消费者可转向Walmart等零售商，企业也可改用Microsoft Azure、Google Cloud等云服务；广告商更可能比较投放回报。[公司财报](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/)

## 2. 近期已公布的重大事件

按公告月份呈现经过核实的A级重大事件。重点覆盖2025-11至2026-11，2025-11-03的商业算力投用为稍早仍持续影响当前结论的例外；不同来源/监管档案尚未逐月穷尽核查，限制详见[研究底稿](../research-records/2026-11-05-research.md)。

<div class="event-roadmap" aria-label="重大事件时间轴">
<section class="event-month" data-month="2025-11">
<h3 class="event-month-heading">2025-11</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">Project Rainier上线</span>
<span class="event-entry-preview">大规模Trainium2算力用于Anthropic训练业务</span>
</summary>
<div class="event-detail-content">

**公告日期：**2025-11-03。

**公布了什么：**AWS宣布Rainier使用约50万颗Trainium2承担Anthropic实际AI工作负载。

**对公司的实际意义：**已进入使用阶段，但单项目投入回收和现金盈利未披露。

**原始来源：**[AWS官方文章](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-project-rainier-online-amazon-nova-amazon-bedrock-and-more-november-3-2025/)

</div>
</details>
</section>
<section class="event-month" data-month="2026-02">
<h3 class="event-month-heading">2026-02</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">OpenAI大型AI战略投资与云协议</span>
<span class="event-entry-preview">$500亿美元股权投资安排及追加$1000亿美元AWS长期承诺</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-02-27。

**公布了什么：**Amazon计划投资OpenAI合计$500亿美元，首期$150亿、后续$350亿附条件；OpenAI在既有$380亿AWS多年承诺上增加$1000亿，期限8年，并计划使用约2GW Trainium算力。

**对公司的实际意义：**支撑长期AI需求，但合同收入跨多年交付，Amazon还承担融资和股权风险；不是本季现金收入。

**原始来源：**[Amazon与OpenAI联合公告](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)

</div>
</details>
</section>
<section class="event-month" data-month="2026-04">
<h3 class="event-month-heading">2026-04</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">拟收购Globalstar并与Apple合作</span>
<span class="event-entry-preview">含债务估值约$109亿美元，预计2027年交割</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-04-14；实际签约2026-04-13。

**公布了什么：**拟以股票和现金收购Globalstar，现金比例上限40%；同时与Apple签卫星服务合作；交割需监管批准与卫星里程碑。

**对公司的实际意义：**获取频谱和卫星直连能力但尚未交割，潜在新发股与投资需求不能忽略。

**原始来源：**[Amazon官方公告](https://press.aboutamazon.com/2026/4/amazon-to-acquire-globalstar-and-expand-amazon-leo-satellite-network)

</div>
</details>
<details class="event-entry">
<summary>
<span class="event-entry-title">Anthropic十年算力承诺</span>
<span class="event-entry-preview">逾$1000亿美元AWS使用承诺和最高5GW容量规划</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-04-20。

**公布了什么：**Anthropic宣布未来十年超过$1000亿美元AWS技术采购承诺；Amazon同时新增股权投资与有条件融资安排。

**对公司的实际意义：**需求规模可见但依赖算力交付及客户资金；不能把承诺总额一次确认为收入。

**原始来源：**[Anthropic官方公告](https://www.anthropic.com/news/anthropic-amazon-compute)

</div>
</details>
</section>
<section class="event-month" data-month="2026-08">
<h3 class="event-month-heading">2026-08</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">FTC及22州起诉广告收费机制</span>
<span class="event-entry-preview">指控竞价广告隐蔽加价，案件尚未终结</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-08-31。

**公布了什么：**FTC与22州起诉Amazon，指称部分赞助广告存在不透明竞价附加收费。属于起诉方指控，不等于法院认定事实。

**对公司的实际意义：**潜在影响广告定价权及整改/赔偿费用；无法提前给确定罚金。

**原始来源：**[FTC案件记录](https://www.ftc.gov/legal-library/browse/cases-proceedings/amazon)

</div>
</details>
</section>
<section class="event-month" data-month="2026-10">
<h3 class="event-month-heading">2026-10</h3>
<details class="event-entry">
<summary>
<span class="event-entry-title">第三季度业绩与AI投资拐点</span>
<span class="event-entry-preview">AWS同比增长39.3%，TTM自由现金流为负$423.57亿美元</span>
</summary>
<div class="event-detail-content">

**公告日期：**2026-10-29；10-Q归档2026-10-30。

**公布了什么：**集团Q3营业收入$2019.44亿美元、营业利润$280.76亿美元，AWS收入$459.84亿美元；公司指引Q4营业收入$2400–2470亿美元、营业利润$285–335亿美元，预计2026现金capex约$2200亿美元。

**对公司的实际意义：**AWS增长和利润兑现，但投入资本尚未转为正现金回报。

**原始来源：**[Amazon投资者关系公告](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/)

</div>
</details>
</section>
</div>

重要限制：大额AI多年云承诺不等于当季现金收入；本轮未对2025年底至2026年全部8-K及每位合作方档案进行无遗漏审计。未经核实的普通合作、设备采购权证、供电计划没有因为金额或名气直接提升为重大交易。

## 3. 公司正在做什么、做到哪一步？

| 公司正在推进的重要事情 | 为什么重要、希望实现什么？ | 目前做到哪一步？下一关是什么？ |
|---|---|---|
| **AWS AI计算容量、Trainium和Bedrock** | 抢占企业AI训练/推理预算；关键是扣除服务器折旧及电力后的现金回报。 | Q3 AWS已实现收入45,984m和利润17,773m；管理层预计2026现金capex约220,000m。下一关看已投用算力的收费使用率、AWS利润转化现金及资本开支回落；时间未确定。[IR](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/) |
| **OpenAI和Anthropic长期云算力协议履行** | 超大额承诺可能提升机房利用率，但Amazon也向客户注资/提供条件性融资。 | 2026Q1/2协议及追加投资已披露；OpenAI 2026Q2追加投入13,700m，Anthropic 2026Q2额外投入2×5,000m。下阶段看真实云服务交付、现金付款、模型企业融资及芯片里程碑；合同承诺不能一次计收入。[10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm) |
| **零售快速配送、广告与会员变现** | 低毛利零售借会员和广告改善总利润，监管风险可能改变有效广告价格。 | Q3北美营业利润同比改善82%，广告恒汇率增长12%；公司预计Q4广告增速回到高十几。下一关是Q4真实增长及FTC案件进展（时间未披露）。[财报](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/) |
| **Leo卫星商业化与Globalstar整合** | 取得频谱及移动卫星服务网络以扩展新收入，但投入昂贵、仍需监管许可。 | 2026-04-13签收购协议并宣布Apple卫星服务合作；预计2027交割，尚需审批及卫星交付条件。下一关是完成交割、真实第三方付费规模、亏损与融资安排。[公告](https://press.aboutamazon.com/2026/4/amazon-to-acquire-globalstar-and-expand-amazon-leo-satellite-network) |

## 4. 财务状况：收入、利润和现金

以下为**百万美元、美国GAAP**。TTM＝FY2025＋2026前9个月−2025前9个月；数据来自[2025 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)、[2026Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)和[公司现金流资料](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm)。

| 指标 | FY2024 | FY2025 | 9M2025 | 9M2026 | TTM至2026Q3 |
|---|---:|---:|---:|---:|---:|
| GAAP收入 | 637,959 | 716,924 | 503,538 | 584,069 | **797,455** |
| 毛利（收入－销售成本） | 311,671 | 360,510 | 257,083 | 306,255 | **409,682** |
| GAAP营业利润 | 68,593 | 79,975 | 54,998 | 79,389 | **104,366** |
| GAAP净利润 | 59,248 | 77,670 | 56,478 | 113,587 | **134,779** |
| 经营现金流 | 115,877 | 139,514 | 85,055 | 113,841 | **168,300** |
| 现金购置长期资产（毛额） | 82,999 | 131,819 | 92,297 | 175,670 | **215,192** |
| 简化自由现金流 | 32,878 | 7,695 | −7,242 | −61,829 | **−46,892** |

<small class="financial-glossary">GAAP＝美国会计准则；营业利润扣除日常经营费用；净利润再计入投资收益/损失、利息和税；经营现金流表示实际经营流入，简化FCF＝经营现金流−长期资产现金购置毛额，TTM表示最近12个月，非未来预测。</small>

**资金说明：** 2026-09-30现金及有价证券114,226m，受限现金/证券还有2,931m归入其他资产分类，不可当全部自由现金；长期有息债务面值180,887m（含一年内到期），长期债务账面非流动部分173,125m；租赁负债现值114,783m（含流动及长期）。2026前三季发行长期债融资现金130,027m、SBC股权薪酬15,476m；实际普通股10,811m，2025年底10,731m。2027年长期债本息合同承诺16,566m，另有租赁、采购设备等非同类义务，不应机械加总当已到期债务。[SEC附注](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)

**总结：** Q3营业利润率13.9%为公司公告历史最高，然而**TTM净利润134,779m不能直接视作可持续经营利润**：截至2026Q3前九个月，Anthropic非上市优先股账面价值上调约62,800m计入其他损益；另有可转换票据未实现收益计入其他综合收益。公司官方定义的TTM FCF为**−42,357m**（购建资产扣处置收入与激励），上表毛额简化FCF **−46,892m**，差4,535m源于资本支出计量口径。真实风险是盈利表很好看但新增数据中心资本需求更大。[Q3财报](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/) [Anthropic会计附注](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)

## 5. 管理层与资本分配

CEO **Andy Jassy**押注自研Trainium、AWS和配送效率，已由AWS利润增速及北美零售利润改善形成业绩支持；但最新管理层2026现金capex约**220,000m**的指引高于TTM经营现金168,300m，意味着目前并非可稳定自由分配现金的经营状态。[IR](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/)

**AI股权投资不能算作现金。** 根据Q3 10-Q，截至2026-09-30，Anthropic优先股账面约92,500m，相关可转票据的公允价值约146,200m，后者部分未实现价值变化放在OCI而非净利润。Amazon在OpenAI等模型企业有股权、云合同并可能提供融资，既给AWS带来客户，也带来资产估值波动与交易关联风险。应持续观察每股现金收益、股数稀释、实际模型企业付款以及资本开支回报。[SEC投资附注](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)

## 6. 估值分析：当前股价贵不贵？

**合理价格参考：$220.00/股（基于公司自身历史EV/实际营收倍数中位数）。** 不是保证兑现的目标价，不使用同行估值、2028年利润预测或未来DCF。

采用**2022–2025四个完整财年末**Amazon自身EV/当年已实现收入的四项观察值，计算中位数，再映射最新已实现TTM营收797,455m。全部历史样本保留，包含2022低倍数年份；年末EV/收入存在市场时点与当年财务正式发布日期不同的限制。[历史数据表](https://stockanalysis.com/stocks/amzn/financials/ratios/)

| 可复算输入与结果 | 数值 |
|---|---:|
| 2022年末EV/当年实际营收 | 962,611 / 513,983 = **1.873×** |
| 2023年末EV/当年实际营收 | 1,672,049 / 574,785 = **2.909×** |
| 2024年末EV/当年实际营收 | 2,377,372 / 637,959 = **3.727×** |
| 2025年末EV/当年实际营收 | 2,533,757 / 716,924 = **3.534×** |
| **四期历史EV/营收倍数中位数** | **3.2216×** |
| 实际TTM收入 | **$797,455m** |
| 当前参考价格（2026-11-04美股收盘） | **$266.03** |
| 当前市值 / 当前EV（同源行情数据） | **$2,876,619m / $3,067,234m** |
| 当前EV减市值的综合融资净桥接 | **$190,615m** |
| 当前实际普通股数（2026-09-30） | **10,811m股** |
| **自身历史中位数对应合理价** | **$220.00/股** |
| **模型价与收盘价差额** | **-17.3%** |

公式：**(3.221602 × 797,455 − 190,615) ÷ 10,811 = $220.00/股**。当前数据商EV/实际TTM收入约**3.85×**；市场当前定价高于历史四期中位数。行情与EV来自[价格历史](https://stockanalysis.com/stocks/amzn/history/)、[企业价值统计](https://stockanalysis.com/stocks/amzn/statistics/)，历史EV及公司年营收来自[本公司历史估值表](https://stockanalysis.com/stocks/amzn/financials/ratios/)，历史四期原始收入在[10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)等申报中可核对。9月末实际股数×11月4日股价得到2,876,050m，较数据商市值2,876,619m差约569m，来自时点及股数精度差别，本模型保留这个桥接限制。

**关键限制：** 本次EV口径沿用同一数据提供商的各期历史/现价，包含租赁、现金及融资等估值调整；历史各期EV中租赁和非流动战略投资的详细调整尚未逐项独立审计。2026年Anthropic相关股权/票据账面巨变、债务与租赁大幅增加，历史EV倍数不一定代表当下合理资本结构，**$220.00只能视作明确可复算的历史锚定参考**，不等于对Amazon全部子公司及持有股权做独立SOTP估值。最强反证是AWS近40%收入增速和38.7%的经营利润率可能意味着当前收入质量高于历史，市场会继续给更高倍数；反方是负自由现金流以及AI大客户融资关联意味着历史倍数可能仍过高。按目前已实现业绩，**现价尚不能证明存在安全边际**。

## 7. 主要投资风险

| 主要风险 | 如何损害股东权益 | 值得验证的信号 |
|---|---|---|
| AI数据中心投资现金回收不及预期 | 新设备折旧、升级、电力与融资费用侵蚀真实每股现金收益 | AWS经营利润相对资本开支的回报、TTM自由现金流、客户实际付款 |
| 债务、租赁和未起租承诺继续增加 | 支出刚性增加、现金流承压 | 债务到期明细、租赁和不可撤销采购承诺、利息支出 |
| Anthropic/OpenAI业务融资与云合同互相依赖 | 股权估值波动以及客户支付能力下降，可同时影响AWS与投资回报 | 合同实际履约、资金提款、客户偿付和非上市股权重估 |
| FTC广告诉讼和增长放缓 | 潜在广告费率整改或赔偿，影响重要利润来源 | 案件裁决、广告定价及排除Prime Day时点后的增速 |
| 零售竞争、运输与关税成本 | 低毛利业务对价格、配送和人工成本敏感 | 北美/国际分部利润率、配送成本和客户需求 |
| Globalstar/Leo/Zoox商业化与稀释 | 卫星和自动驾驶持续资本消耗，Globalstar拟以股权支付部分交易对价 | 监管交割、第三方收费规模、长期现金亏损、实际流通股数 |
