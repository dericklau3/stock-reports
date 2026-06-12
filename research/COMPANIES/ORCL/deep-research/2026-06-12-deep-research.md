# Oracle（ORCL）深度研究 - 2026-06-12

- **Research view**: 建设性但需观察
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: Oracle 正从高毛利数据库和企业应用软件公司，转型为“软件现金牛 + AI 云基础设施平台”。FY2026 Q4 OCI 收入同比增长 93%，RPO 达到 6,380 亿美元，FY2027 收入指引为 900 亿美元，证明需求非常强。但 FY2026 资本开支达到 556.63 亿美元、自由现金流为 -236.86 亿美元，总债务口径约 1,562 亿美元；FY2027 还计划融资约 400 亿美元。当前 184.10 美元股价对应约 22.9 倍 forward P/E，风险回报较财报前改善，但价值取决于 RPO 能否以足够高的利润率转化为收入和现金流。
- **Key risk**: 最大风险是 Oracle 为少数大型 AI 客户提前承担巨额数据中心、GPU、电力和租赁义务，但收入确认、客户信用和产能利用率慢于资本投入。若 OCI 成熟利润率不及预期，股权融资和债务增长可能稀释每股价值。

## 1. Executive View

**研究观点：建设性但需观察。**

Oracle 在 FY2026 完成了商业模式的重要转折：

- 全年收入增长 17% 至 673.57 亿美元。
- OCI 全年收入增长 77% 至 181.01 亿美元。
- Q4 OCI 增长进一步加速到 93%。
- RPO 同比增长 363% 至 6,380 亿美元。
- FY2027 收入指引为 900 亿美元，同比增长约 34%。

这是一家大型成熟软件公司少见的增长加速。但增长的代价也非常大：

- FY2026 capex 从 212.15 亿美元升至 556.63 亿美元。
- FY2026 FCF 从 -3.94 亿美元恶化至 -236.86 亿美元。
- Notes payable and other borrowings 从 925.68 亿美元增至 1,295.41 亿美元。
- Operating lease liabilities 约 300 亿美元量级。
- FY2027 预计再通过债务和股权融资约 400 亿美元，其中包括此前宣布的 200 亿美元 ATM 普通股发行。

### 核心判断

1. **需求证据很强。** RPO 6,380 亿美元，Q4 单季增加 850 亿美元。Oracle 表示 Q3/Q4 大部分增长来自大型 AI 合同。
2. **RPO 质量好于表面融资需求。** 大型 AI 合同中，客户预付或自行提供 GPU 的部分累计约 750 亿美元，可降低 Oracle 的资本需求。
3. **但 RPO 不是收入。** 合同可能跨多年，收入确认依赖数据中心按时建设、GPU 到位、电力接入和客户实际使用。
4. **软件护城河仍然重要。** 软件支持全年收入 198.04 亿美元、同比增长 1%，虽然低增长，但具有高续费率、强切换成本和现金流价值。
5. **估值已回到可研究区间。** 2026-06-11 ORCL 收于 184.10 美元，财报后下跌 8.5%；forward P/E 约 22.9x。对于 FY2027 预计 34% 收入增长的公司不算昂贵，但负 FCF 和融资风险要求折价。

### 为什么不是“Positive”

- FY2026 reported capex 相当于收入的约 83%。
- FY2027 净现金资本开支预计约 700 亿美元；考虑客户预付款和客户直接提供设备后的 reported capex 可能更高。
- FY2026 利息费用达到 45.99 亿美元，同比增长 29%。
- Q4 cloud and software delivery cost 同比增长 56%，快于 cloud revenue 增长 47%。
- FY2026 cloud applications 仅增长 11%，传统软件收入下降 1%。
- FY2027 预计股权融资将增加普通股稀释；FY2026 diluted share count 已同比增长约 2%。
- FY2026 non-GAAP EPS 7.63 美元含一次性投资收益；剔除后为 6.83 美元。

### 最强反方理由

最强反方观点是：市场可能低估 Oracle RPO 的长期价值。若客户预付和自带 GPU 显著降低 Oracle 资本负担，OCI 在数据中心满负荷后达到管理层描述的 30%-40%利润率区间，那么当前负 FCF只是建设期现象，Oracle 可能成为增长最快且利润丰厚的 hyperscaler 之一。

## 2. Business Model and Industry Structure

### 初学者版：Oracle 到底卖什么

Oracle 主要卖四类产品和服务：

- **数据库和软件支持**：企业把财务、客户、库存、交易和业务数据存放在 Oracle Database 中，并持续支付软件支持费用。
- **企业云应用**：Fusion ERP、HCM、SCM、EPM、NetSuite 和 Oracle Health 等，用订阅方式帮助企业管理员工、财务、供应链和医疗业务。
- **OCI 云基础设施**：向客户出租服务器、GPU、存储、网络和数据库计算能力，类似 AWS、Azure 和 Google Cloud。
- **硬件与服务**：Exadata、服务器、存储设备、实施、咨询和技术支持。

### 钱是怎么赚到的

软件业务的经济模型：

`订阅或支持收入 - 研发、销售和云交付成本`

客户把关键业务系统建立在 Oracle 数据库和应用上，更换系统需要迁移数据、重写程序、重新培训员工并承担停机风险，因此续约率和切换成本较高。

OCI 的经济模型：

`客户云消费收入 - GPU/服务器折旧 - 数据中心租赁 - 电力 - 网络 - 运维成本`

OCI 前期必须先建设数据中心和购买设备，现金流先流出，客户使用后才逐步确认收入。只有当数据中心利用率上升、合同价格足够高、设备使用寿命和电力成本可控时，巨额 RPO 才能转化为高回报。

### 今天的利润引擎与未来增长引擎

**今天的利润引擎：**

- Oracle Database、软件支持和许可证。
- Fusion、NetSuite 等 SaaS。
- 已投产 OCI 容量。

**未来增长引擎：**

- AI training 和 inference 基础设施。
- Oracle Database@Azure、Database@Google Cloud、Database@AWS 等 multicloud database。
- Autonomous Database 和 AI Database。
- Oracle Health 新一代 AI 医疗应用。
- 大型专用 AI 数据中心合同。

### 关键术语翻译

| 术语 | 白话解释 |
|---|---|
| OCI | Oracle Cloud Infrastructure，Oracle 的云服务器、GPU、网络、存储和数据库平台。 |
| IaaS | 基础设施即服务，客户按使用量租用计算、存储和网络资源。 |
| SaaS | 软件即服务，客户定期付费使用在线应用。 |
| RPO | 已签合同但尚未确认收入的履约义务；它是未来收入线索，不等于现金或保证利润。 |
| Hyperscaler | 拥有超大规模数据中心和全球云平台的公司，如 AWS、Azure、Google Cloud 和 OCI。 |
| Multicloud | 企业可以在其他云平台中直接使用 Oracle Database，而不必把所有工作负载迁回 OCI。 |
| RDMA | 一种低延迟高速网络技术，可让大量 GPU 更高效地互相交换数据。 |
| Capex | 购买服务器、GPU、网络设备和建设数据中心的资本支出。 |
| Customer-supplied GPU | 客户自己购买 GPU 并放入 Oracle 数据中心，Oracle提供网络、电力和运维。 |
| ATM equity issuance | 公司通过公开市场逐步发行新股融资，会增加流通股数并稀释现有股东。 |

### 核心经济问题

Oracle 要产生持久的每股价值增长，必须让 OCI 收入和利润增长速度长期高于债务、租赁义务、折旧、利息和股数增长，同时守住数据库与企业应用的客户基础。

## 3. Product and Segment Analysis

Oracle 按产品类型披露收入，而不是把 OCI 单独作为完整利润分部。

### FY2026 收入结构

| 产品类别 | FY2026 收入 | 同比 | 收入占比 |
|---|---:|---:|---:|
| Cloud | 339.89 亿美元 | +39% | 51% |
| Software | 245.41 亿美元 | -1% | 36% |
| Hardware | 30.84 亿美元 | +5% | 5% |
| Services | 57.43 亿美元 | +10% | 8% |
| Total | 673.57 亿美元 | +17% | 100% |

Cloud 已经超过总收入一半，但 cloud 内部质量差异很大。

### OCI：增长最快，也最需要资本

| 指标 | Q4 FY2026 | FY2026 |
|---|---:|---:|
| OCI revenue | 57.87 亿美元 | 181.01 亿美元 |
| YoY growth | +93% | +77% |
| Constant currency growth | +92% | +75% |

OCI 的优势：

- Oracle Database 与企业数据关系紧密。
- 适合大型、集中式 GPU 集群。
- 可通过 multicloud 把数据库服务部署到 Azure、Google Cloud 和 AWS。
- 客户预付或提供 GPU，可以减少 Oracle 的部分资本投入。
- OCI 规模仍小于三大云平台，低基数提供更高增长空间。

OCI 的限制：

- AWS、Microsoft 和 Google拥有更大的开发者生态和企业关系。
- AI 基础设施客户数量少、合同规模巨大，集中度可能显著提高。
- 新数据中心早期利用率低，会压低 gross margin。
- 数据中心、电力、GPU、网络和租赁交付具有复杂执行风险。

### Cloud Applications：稳定，但没有 OCI 那么快

| 指标 | Q4 FY2026 | FY2026 |
|---|---:|---:|
| Cloud applications revenue | 41.26 亿美元 | 158.88 亿美元 |
| YoY growth | +10% | +11% |

主要产品：

- **Fusion ERP/EPM**：企业财务、预算和经营管理。
- **Fusion HCM**：人力资源、薪酬和人才管理。
- **Fusion SCM**：供应链和制造管理。
- **NetSuite**：面向中小企业的云 ERP。
- **Oracle Health**：医院电子病历和临床管理，核心来自 Cerner。

Cloud applications 是高质量经常性收入，但增长率低于 Salesforce、Workday 等公司部分高增长时期。Oracle Health 仍需要证明新 AI 系统能修复 Cerner 整合和增长问题。

### Software：现金牛正在缓慢迁移

FY2026 software revenue 245.41 亿美元，同比下降 1%：

- Software license：47.37 亿美元，同比下降 9%。
- Software support：198.04 亿美元，同比增长 1%。

许可证下降不一定意味着客户流失，其中一部分是从本地部署迁移到云订阅。但 support 基本不增长，说明传统业务无法独立支撑高估值。

Database 是核心护城河。大型银行、政府、电信商和跨国公司通常运行大量 Oracle 数据库，迁移成本高。风险是 PostgreSQL、AWS、Microsoft、Google、Snowflake、MongoDB 等替代方案持续侵蚀新工作负载。

### Hardware 和 Services

Hardware FY2026 收入 30.84 亿美元、增长 5%；Services 57.43 亿美元、增长 10%。它们可以支持完整解决方案，但通常不是估值核心。

## 4. RPO and Contract Quality

### 6,380 亿美元 RPO 代表什么

RPO 在 Q4 FY2026 达到 6,380 亿美元：

- 同比增长 363%。
- 单季增长 850 亿美元。
- 约为 FY2026 收入的 9.5 倍。

这是极强的需求信号，但不能直接把 RPO 除以年份当作收入预测。

RPO 转收入需要：

- 数据中心完成建设。
- GPU、网络和电力按时到位。
- 客户开始使用合同容量。
- Oracle履行服务水平协议。
- 合同不存在导致延迟、重议或取消的条款。

### 预付款和客户自带 GPU

Oracle 表示，大型 AI 合同中预付或客户自行提供硬件的部分累计约 750 亿美元。这改善了合同质量：

- 降低 Oracle 前期采购 GPU 的现金需求。
- 客户预付代表更强的合同承诺。
- 减少设备价格和供应风险的一部分。

但风险没有消失：

- Oracle 仍需要建设数据中心、电力和网络。
- 客户预付款可能带有长期履约和融资义务。
- 集中于少数客户会增加信用、续约和谈判风险。
- RPO 的利润率没有公开，巨额合同可能用较低价格换取规模。

### 客户集中

Oracle 没有在 Q4 财报中披露各大型 AI 客户的 RPO 占比。媒体报道提到 OpenAI 等大型合同，但由于合同细节未完整公开，本研究不把媒体报道的合同总值直接当成确定收入。

最大的未知数不是“有没有订单”，而是这些订单的客户集中度、起始时间、毛利率、资本责任和违约保护。

## 5. Financial Deep Dive

### FY2026 损益表

| 指标 | FY2026 | FY2025 | 变化 |
|---|---:|---:|---:|
| Revenue | 673.57 亿美元 | 573.99 亿美元 | +17% |
| GAAP operating income | 206.06 亿美元 | 176.78 亿美元 | +17% |
| GAAP operating margin | 31% | 31% | 持平 |
| Non-GAAP operating income | 289.26 亿美元 | 250.33 亿美元 | +16% |
| Non-GAAP operating margin | 43% | 44% | -100 bps |
| GAAP net income | 170.87 亿美元 | 124.43 亿美元 | +37% |
| GAAP diluted EPS | 5.83 美元 | 4.34 美元 | +34% |
| Non-GAAP diluted EPS | 7.63 美元 | 6.03 美元 | +27% |

FY2026 GAAP 和 non-GAAP利润包含投资处置收益。Oracle 表示，剔除这些收益后：

- Q4 non-GAAP EPS 为 2.03 美元，同比增长 20%。
- FY2026 non-GAAP EPS 为 6.83 美元，同比增长 13%。

因此评估 FY2027 8.05 美元 non-GAAP EPS 指引时，应使用 6.83 美元作为更合理基数，对应约 18%增长。

### Q4 FY2026

| 指标 | Q4 FY2026 | Q4 FY2025 | 变化 |
|---|---:|---:|---:|
| Revenue | 191.84 亿美元 | 159.03 亿美元 | +21% |
| GAAP operating income | 61.33 亿美元 | 51.09 亿美元 | +20% |
| GAAP operating margin | 32% | 32% | 持平 |
| Non-GAAP operating income | 85.90 亿美元 | 70.35 亿美元 | +22% |
| GAAP diluted EPS | 1.45 美元 | 1.19 美元 | +21% |
| Non-GAAP diluted EPS | 2.11 美元 | 1.70 美元 | +24% |

Q4 stock-based compensation 为 12.03 亿美元，占季度收入约 6.3%。全年 SBC 为 48.11 亿美元，占收入约 7.1%。这是经常性经济成本，不应完全忽略。

### 现金流

| 指标 | FY2026 | FY2025 |
|---|---:|---:|
| Operating cash flow | 319.77 亿美元 | 208.21 亿美元 |
| Capital expenditures | 556.63 亿美元 | 212.15 亿美元 |
| Free cash flow | -236.86 亿美元 | -3.94 亿美元 |
| Net cash outlay for capex | 477.26 亿美元 | 197.93 亿美元 |

FY2026 OCF 增长 54%，表现很强，其中包括：

- 客户带显著融资成分的预付款增加 45.92 亿美元。
- 折旧 76.23 亿美元。
- SBC 48.11 亿美元。

Oracle 定义的 net cash outlay for capex 会扣除短期设备融资和客户预付款，能更好反映当期现金负担，但它仍然高达 477.26 亿美元。

### 资产负债表

截至 2026-05-31：

- Cash and cash equivalents：312.89 亿美元。
- Marketable securities：6.05 亿美元。
- Current borrowings：71.99 亿美元。
- Non-current borrowings：1,223.42 亿美元。
- Notes payable and other borrowings total：1,295.41 亿美元。
- Operating lease liabilities：约 300 亿美元。
- Stockholders' equity：430.56 亿美元。
- Property, plant and equipment, net：999.57 亿美元。

StockAnalysis 将总债务口径列为 1,561.9 亿美元，包含租赁等债务项目；净债务约 1,243 亿美元。Debt/EBITDA 约 4.55x，interest coverage 约 4.88x。

资产负债表变化非常快：

- PP&E 一年增加约 564 亿美元。
- Operating lease right-of-use assets 从 131.45 亿美元升至 296.90 亿美元。
- Non-current borrowings 从 852.97 亿美元升至 1,223.42 亿美元。

这意味着 Oracle 的风险结构正在从轻资产软件公司转向高固定成本云基础设施公司。

### 稀释和股东回报

FY2026：

- Diluted weighted-average shares：29.14 亿股，同比增长约 2%。
- Common and preferred stock issuance：约 64 亿美元净现金流入，其中 mandatory convertible preferred stock 约 49.54 亿美元。
- Dividends：57.87 亿美元。
- Common stock buybacks：仅 0.95 亿美元。
- Restricted stock vesting tax withholding：1.11 亿美元。

FY2027 计划的 200 亿美元 ATM 普通股发行可能显著增加股数。股权融资减少债务压力，但会稀释现有股东；评估价值时必须使用未来 fully diluted shares。

## 6. Management and Capital Allocation

### 管理层

Oracle 目前由 Clay Magouyrk 和 Mike Sicilia 担任联席 CEO；Safra Catz 转任 executive vice chair；Larry Ellison 继续担任董事长和 CTO。CFO Hilary Maxson 于 2026 年加入。

优点：

- Clay Magouyrk 长期负责 OCI，对基础设施扩张具有直接经验。
- Mike Sicilia 熟悉行业应用和 Oracle Health。
- Larry Ellison 对数据库、云架构和 AI 战略仍有强影响力。

风险：

- 联席 CEO 模式可能降低决策清晰度。
- CFO 刚上任即面对数百亿美元资本融资计划。
- 管理层激励可能偏向收入和 non-GAAP 指标，而股东更需要关注 FCF、ROIC 和稀释。

### 资本配置

Oracle 已从“回购和分红”转向“数据中心扩张和融资”：

- FY2026 债务融资 430 亿美元。
- FY2026 股权融资约 50 亿美元。
- FY2027 预计再融资约 400 亿美元。
- FY2027 净现金 capex outlay 预计约 700 亿美元。
- Common dividend 维持每季度 0.50 美元。

未来资本配置的考核标准应是：

- OCI data center 投产后的 ROIC。
- 每美元 capex 可产生多少长期收入和 operating profit。
- 客户预付款占新增项目的比例。
- 债务和股权融资是否低于 RPO 转化所创造的企业价值。

## 7. Competitive Position

### OCI 对比三大云平台

| 竞争领域 | Oracle 优势 | Oracle 弱点 |
|---|---|---|
| Enterprise database | Oracle Database installed base、Exadata、Autonomous Database | 开源数据库和 cloud-native database 持续抢占新工作负载 |
| AI infrastructure | 大型 GPU cluster、高速 RDMA、灵活客户硬件模式 | 规模、生态和开发者基础弱于 AWS/Azure/GCP |
| Multicloud | Database 服务可进入 Azure、Google Cloud 和 AWS | 可能让其他云保留客户控制权和更多消费 |
| Enterprise applications | Fusion、NetSuite、行业应用和数据库协同 | 与 SAP、Workday、Salesforce 激烈竞争 |
| Healthcare | Cerner installed base 和临床数据 | Cerner 整合、客户满意度和产品现代化风险 |

### 护城河

Oracle 的最强护城河仍是数据库 installed base 和企业关键工作负载，而不是 OCI 本身。

数据库护城河来自：

- 数据迁移困难。
- 应用和数据库深度绑定。
- 大型企业对稳定性、安全和合规的要求。
- DBA、合作伙伴和行业知识生态。
- 软件支持合同带来的长期关系。

OCI 的护城河正在形成，但需要证明：

- 大型 AI 客户不会只把 Oracle 当作短期 GPU 容量补充。
- 数据中心单位经济性可以接近或超过成熟 hyperscaler。
- Multicloud database 能转化为 Oracle 收入，而不是加速客户留在竞争对手云平台。

## 8. Valuation Work

### 估值方法选择

Oracle 处于异常的过渡阶段：

- 软件和 SaaS 业务适合 P/E、EV/EBIT 和 FCF。
- OCI 高增长业务可参考 EV/Sales 和未来成熟利润率。
- 当前 FCF 为负，不能使用简单 FCF yield。
- 资本结构快速变化，必须考虑 enterprise value、债务和未来股权稀释。

因此使用 forward P/E、EV/Sales、FY2029 EPS/FCF 情景和反向估值。

### 当前估值快照

截至 2026-06-11 收盘：

| 指标 | 数值 |
|---|---:|
| 股价 | 184.10 美元 |
| Market cap | 5,294.8 亿美元 |
| Enterprise value | 6,537.8 亿美元 |
| Shares outstanding | 28.8 亿股 |
| Trailing P/E | 31.6x |
| Forward P/E | 22.9x |
| P/S | 7.86x |
| Forward P/S | 5.94x |
| EV/Sales | 9.71x |
| EV/EBITDA | 20.6x |
| Debt/EBITDA | 4.55x |
| FCF | -236.9 亿美元 |

按 FY2027 900 亿美元收入指引计算：

- 当前 EV/FY2027 revenue 约 7.3x。
- 按 8.05 美元 non-GAAP EPS 指引，forward P/E 约 22.9x。

单看 P/E 并不昂贵，但 EPS 没有扣除 capex。市场真正担心的是达到 8.05 美元 EPS 仍可能伴随巨额负 FCF。

### 情景估值

以下是研究框架，不是投资建议。使用 FY2029 fully diluted shares 约 31-33 亿股，反映 ATM、mandatory convertible preferred stock 和员工股权的潜在稀释。

| 情景 | FY2029 假设 | 估值方法 | 隐含每股价值 |
|---|---|---|---:|
| Bear | Revenue 1,100-1,200 亿美元；non-GAAP EPS 9-10.5；FCF 仍弱；OCI margin 不及预期 | 16-19x EPS | 145-200 美元 |
| Base | Revenue 1,400-1,600 亿美元；EPS 12-15；FCF 转正并快速改善 | 20-24x EPS | 240-360 美元 |
| Bull | Revenue 1,750-2,100 亿美元；EPS 17-22；OCI 达到高利用率和 30%-40%成熟利润率 | 24-28x EPS | 410-615 美元 |

当前 184.10 美元接近 bear case 上半区、低于 base case。表面风险回报不错，但 base case 要求：

- FY2027 900 亿美元收入兑现。
- FY2028/FY2029 OCI 继续高速增长。
- Gross margin 在产能爬坡后恢复。
- FCF 在重资本建设期后显著转正。
- 稀释控制在情景假设内。

### 反向估值

当前股价大致要求：

- FY2027 non-GAAP EPS 达到约 8.05 美元。
- 中期 EPS 达到 10-12 美元。
- 市场仍给予约 18-20x 成熟期倍数。
- RPO 不发生重大延期或信用损失。
- 债务不会导致评级、融资或资本配置危机。

相比财报前价格，184 美元已经反映部分融资风险；但如果 OCI 合同回报率低，当前股价仍不便宜。

## 9. Catalysts and Monitoring Plan

### 近期催化

- Q1 FY2027 revenue 是否达到 27%-29%增长指引。
- Q1 FY2027 cloud revenue 是否达到 58%-64%美元增长。
- Q1 non-GAAP EPS 是否达到 1.72-1.76 美元。
- FY2027 900 亿美元收入和 8.05 美元 non-GAAP EPS 指引是否维持。
- 200 亿美元 ATM 股权发行的价格、节奏和实际稀释。
- FY2027 债务与股权融资构成。
- 客户预付和 customer-supplied GPU 的进一步增长。
- 下一次正式财报日期截至 2026-06-12 尚未公布。

### 每季监控指标

- OCI revenue growth 和绝对收入。
- Cloud applications growth。
- Software support revenue 和续约趋势。
- RPO 总额、季度新增量和转收入速度。
- RPO 中客户预付款和自带 GPU 比例。
- Cloud and software gross margin。
- Capex、net cash outlay for capex 和 data center commitments。
- OCF、FCF 和 customer prepayment contribution。
- Total debt、interest expense 和 credit ratings。
- Common shares、preferred conversion 和 SBC。
- Oracle Health 增长与产品交付。
- Multicloud Database revenue 和使用量。

## 10. Risk Register

| 风险 | 概率 | 影响 | 说明 |
|---|---|---|---|
| 资本开支回报不足 | 中 | 极高 | 巨额数据中心投入若无法产生高利用率和利润率，将破坏每股价值。 |
| 债务和融资 | 高 | 高 | 总债务约 1,562 亿美元，FY2027 仍需约 400 亿美元融资。 |
| 股权稀释 | 高 | 中高 | 200 亿美元 ATM、mandatory convertible preferred 和 SBC 增加股数。 |
| AI 客户集中 | 中高 | 高 | 大型 AI 合同可能集中在少数客户，具体占比未披露。 |
| RPO 转化延迟 | 中 | 高 | 数据中心、电力、GPU 或客户部署延迟会推迟收入。 |
| OCI 毛利率 | 中高 | 高 | 新产能早期折旧和运营成本压低利润率。 |
| 传统软件衰退 | 中 | 中高 | 软件许可证下降 9%，support 仅增长 1%。 |
| 云竞争 | 高 | 高 | AWS、Azure、GCP 规模和生态显著领先。 |
| 数据库替代 | 中 | 高 | 开源、cloud-native 和专用数据库持续抢占新工作负载。 |
| Oracle Health 执行 | 中 | 中 | Cerner 整合和新 AI 医疗系统仍需验证。 |
| 数据中心电力与监管 | 中高 | 高 | 电网、能源价格、许可和居民电费政治压力可能限制建设。 |
| 网络安全 | 中 | 高 | 数据库和关键企业系统发生漏洞会损害客户信任。 |
| 管理层转换 | 中 | 中 | 联席 CEO 和新 CFO 正在执行公司历史上最大的资本计划。 |

## 11. Final Research Framework

### 当前结论

Oracle 已经不再只是成熟数据库公司，也还不是已经证明自由现金流模型的 AI hyperscaler。它正处于两种商业模式之间：

- 高毛利、低资本、低增长的软件现金牛；
- 高增长、重资本、需要债务与股权融资的 AI 云基础设施。

FY2026 结果证明需求和收入增长，但尚未证明资本回报。184.10 美元的股价较财报前明显回调，forward P/E 约 23x，使风险回报进入可研究区间。因此观点为 **建设性但需观察**。

### Thesis 取决于什么

- RPO 转收入的速度和利润率。
- 客户预付/自带 GPU 是否持续降低资本需求。
- OCI 成熟 gross margin 和 operating margin。
- FY2027 900 亿美元收入是否兑现。
- FCF 何时转正以及转正后的规模。
- 债务和 fully diluted shares 是否低于企业价值增长。
- Database 和 SaaS 业务是否保持稳定。

### 什么会让我上调观点

- FY2027 Q1/Q2 收入、OCI 和 EPS 连续达到指引上半区。
- 新增 RPO 保持强劲且客户预付款比例提高。
- 数据中心利用率上升，cloud margin 开始改善。
- FY2027 capex/融资低于当前预期。
- 管理层给出可信的 FCF 转正时间表。
- 软件支持和 cloud applications 增长稳定。

### 什么会让我下调观点

- FY2027 900 亿美元收入指引下调。
- RPO 增长停滞或出现重大延期、重议或信用问题。
- OCI 收入增长但 gross margin 持续恶化。
- capex、债务和租赁义务继续超预期。
- ATM 和其他股权融资造成大于预期的每股稀释。
- 利息费用增长快于 operating income。
- 传统数据库和 SaaS 客户流失加速。

## Sources

- Oracle Q4 and FY2026 results, SEC Exhibit 99.1, filed 2026-06-10: https://www.sec.gov/Archives/edgar/data/1341439/000119312526265848/orcl-ex99_1.htm
- Oracle Form 8-K, filed 2026-06-10: https://www.sec.gov/Archives/edgar/data/1341439/000119312526265848/orcl-20260610.htm
- Oracle Q3 FY2026 Form 10-Q, filed 2026-03-11: https://www.sec.gov/Archives/edgar/data/1341439/000119312526101045/orcl-20260228.htm
- Oracle FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm
- Oracle Investor Relations: https://investor.oracle.com/
- StockAnalysis ORCL overview, price as of 2026-06-11: https://stockanalysis.com/stocks/orcl/
- StockAnalysis ORCL statistics, updated 2026-06-11: https://stockanalysis.com/stocks/orcl/statistics/
- FY2027 capex context from the earnings call, reported by The Wall Street Journal: https://www.wsj.com/business/earnings/oracle-reports-higher-profit-on-surging-cloud-revenue-5f7d25eb

