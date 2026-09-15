# Oracle（ORCL）深度研究更新｜2026-09-14

- **Research view**：Constructive but watchful（建设性但需观察）
- **Confidence**：中等；经营数据强，但资本回报和客户集中风险仍需验证
- **Time horizon**：12–24 个月看 OCI/RPO 转化、资本开支、FCF、债务和稀释；3–5 年看 Oracle 能否把软件现金牛成功转成 AI 云平台
- **Main thesis**：Oracle 正从高粘性数据库和企业应用公司转成“软件现金牛 + AI 云基础设施”混合体。Q1 FY2027 证明 AI 云需求和交付速度很强，但尚未证明这些收入对应足够高的税后资本回报。
- **Key risk**：Oracle 可能为大型 AI 客户提前承担过多 GPU、数据中心、电力、租赁和债务责任，最终出现收入高速增长、但自由现金流和每股价值增长不足。

> 本文是研究支持，不构成个性化投资建议。最新已完成的常规交易日价格采用 Oracle IR / Nasdaq 披露的 **2026-09-11 收盘 $150.28**。2026-09-14 的盘中及媒体报道价格不作为已完成收盘使用。

## 1. Executive View

### 结论先行

ORCL 最新一季基本面明显强于 7 月时的旧信息：

- Q1 FY2027 revenue **$19.345B，同比 +30%**；
- Cloud revenue **$11.607B，同比 +62%**；
- Cloud Infrastructure（OCI）收入同比增长 **121%**；
- RPO 从 FY2026 年末 $638B 增至 **$664B**；
- Q1 经营现金流 **$23.103B，同比 +184%**；
- 但 capex **$28.499B**，单季 FCF **-$5.396B**；
- Oracle 在该季度通过 ATM 净融资约 **$19.9B**，发行约 **141M 股**。

**我的判断**：需求证据已经从“强”升级为“非常强”，但股东回报证据只升级了一半。RPO、云收入和经营现金流证明客户愿意签约并预付；capex、债务、租赁和 ATM 则证明 Oracle 仍在用资产负债表和股权为增长提前买单。

按 $150.28 计算，约 3,023.736M 股对应市值 **$454.4B**。以 10-Q 的现金/现金等价物和短期证券约 $37.1B、notes payable and other borrowings 约 $125.3B 的窄口径计算，EV 约 **$542.7B**，约为 FY2027 $90B revenue guidance 的 **6.0x EV/Sales**。按 FY2027 non-GAAP EPS $8.10，forward non-GAAP P/E 约 **18.6x**。

**最强反方理由**：Oracle 已经拥有高毛利数据库护城河，但 AI 云扩张使它承担了大型基础设施公司的资本强度；AI 订单很大，不等于订单利润率、客户信用和终端自由现金流同样优秀。

## 2. Oracle 到底卖什么、怎么赚钱

### 初学者版

Oracle 帮企业保存最关键的数据，并运行财务、人力、供应链、医疗等核心业务。传统客户通常不愿意随意更换数据库，因为迁移会涉及改代码、重新审计、停机风险和员工培训。因此数据库许可、支持和企业应用订阅构成了较稳定的现金流底座。

现在 Oracle 又在出租 GPU、服务器、存储、网络、数据库和数据中心能力，也就是 OCI。客户可以按使用量或长期合同支付云服务费。Oracle 必须先买 GPU/服务器、建设数据中心、支付电力和租赁成本，之后才随着服务交付确认收入。

### 三层利润结构

1. **数据库和 software support**：成熟、高粘性、资本较轻，是传统现金牛。
2. **Cloud Applications**：Fusion、NetSuite、Oracle Health 等企业 SaaS，订阅性强，增速中等。
3. **OCI / AI Cloud Infrastructure**：增长最快，但需要大量服务器、数据中心、电力和融资，资本回报尚未跨越完整周期。

OCI 的简化经济公式是：

`云收入 − GPU/服务器折旧 − 数据中心租赁 − 电力 − 网络 − 运维 − 利息 − 税`

因此，真正重要的问题不是“AI 需求是否真实”，而是：**成熟后的 OCI 资产回报率是否高于债务、租赁和股权资本成本？**

### 关键术语

- **OCI**：Oracle Cloud Infrastructure，提供计算、GPU、存储、网络和数据库云服务。
- **RPO**：已签约但尚未确认的收入义务；类似 backlog，但不是现金或利润。
- **Capex**：购买服务器、GPU、网络设备和建设数据中心的资本支出。
- **Customer prepayment**：客户提前付款，Oracle 后续提供服务并确认收入。
- **Customer-supplied GPU**：客户自己提供 GPU，Oracle 提供机房、电力、网络及运营。
- **ATM**：公司通过公开市场逐步增发普通股融资，会稀释旧股东。

## 3. 产品与竞争结构

### A. OCI：增长引擎与资本风险中心

Q1 FY2027 Cloud revenue $11.607B，同比增长 62%；其中 OCI 同比增长 121%。Oracle 还披露季度内交付 **850MW** 新数据中心容量，并向 AI 云客户交付超过 **300,000 GPUs**。

Oracle 的优势：

- 数据库存量客户提供天然迁云入口；
- 大型 GPU 集群和网络能力适合 AI 训练与推理；
- 可通过多云模式在 Azure、AWS、Google Cloud 环境中继续变现数据库；
- 客户预付和自带 GPU 可减少部分 Oracle 初始资本负担。

Oracle 的弱点：

- AWS、Azure、GCP 拥有更强规模、生态和开发者基础；
- 大型合同可能集中在少数 AI 客户；
- 数据中心建设、电力和 GPU 采购先发生，客户收入可能后发生；
- GPU 供给充分后，算力租赁可能从卖方市场转向价格竞争。

### B. RPO：需求证据，不是股东回报证据

RPO 从 $638B 增至 $664B，Q1 新增 AI 云合同超过 $30B。约 13% 的 RPO 预计未来 12 个月确认，37% 在第 13–36 个月确认，34% 在第 37–60 个月确认，其余更晚。

RPO 的质量要继续核验：

- 客户集中度；
- 合同利润率；
- 预付与自带硬件比例；
- 取消、延期和重议条款；
- 客户信用；
- Oracle 是否必须在服务期前自行承担电力和硬件成本。

RPO 是强需求信号，但不能直接加到市值上，也不能把全部 RPO 乘以软件公司的高毛利率。

### C. Cloud Applications 与传统软件

Cloud Applications 增长不如 OCI 爆发，但 Fusion、NetSuite、Oracle Health 具有企业流程粘性。传统 software revenue 在 Q1 FY2027 同比下降 3%，说明迁云转型会蚕食部分旧软件收入。

这形成关键平衡：

- 数据库和支持业务提供护城河及现金流；
- OCI 负责增长，但资本强度高；
- 如果传统软件下滑过快，Oracle 将失去为 OCI 扩张提供安全垫的现金牛；
- 如果 OCI 增长依靠低价和重资产，规模扩大也可能降低股东回报。

### D. 竞争格局

| 领域 | Oracle 优势 | 主要弱点 |
|---|---|---|
| 企业数据库 | 转换成本、存量客户、Exadata、行业知识 | 开源和云原生数据库抢新工作负载 |
| AI 云 | GPU 集群、低延迟网络、客户预付模式 | AWS/Azure/GCP 规模和生态更强 |
| Multicloud | 可在竞争对手云内继续卖数据库 | 客户关系可能由合作云平台控制 |
| 企业应用 | Fusion、NetSuite、Health | SAP、Workday、Salesforce 竞争强 |

Oracle 最强的护城河依旧是数据库与关键企业工作负载，不是 OCI 的基础设施规模本身。

## 4. Financial Deep Dive

### Q1 FY2027 经营数据

| 指标 | Q1 FY2027 | 同比 / 备注 |
|---|---:|---|
| Total revenue | $19.345B | +30% |
| Cloud revenue | $11.607B | +62% |
| Software revenue | $5.550B | -3% |
| Hardware revenue | $0.774B | +15% |
| Services revenue | $1.414B | +5% |
| GAAP operating income | $6.728B | +57% |
| GAAP operating margin | 35% | 去年 29% |
| GAAP net income | $4.760B | +63% |
| Diluted GAAP EPS | $1.56 | 去年 $1.01 |
| Non-GAAP diluted EPS | $1.92 | +30% |
| RPO | $664B | 去年同期 $455B |

### 现金流：利润强，FCF 仍弱

- Operating cash flow：**$23.103B**；
- Capex：**$28.499B**，去年同期 $8.502B；
- Free cash flow：**-$5.396B**，去年同期 -$0.362B；
- 资本开支约为当季收入的 **147%**；
- Customer prepayments with significant financing component：**$11.363B**。

客户预付款显著改善了当季融资压力，但不等于 Oracle 不承担资本责任：客户预付款最终要通过未来服务交付，且合同包含融资成分；若利用率、客户信用或价格纪律变差，预付并不会自动变成高回报。

### 资产负债表与承诺

截至 2026-08-31：

- Cash and cash equivalents：**$36.369B**；
- Marketable securities：**$0.708B**；
- Notes payable and other borrowings：**$125.337B**；
- Operating lease liabilities：**$30.594B**；
- Property, plant and equipment, net：**$127.845B**；
- Common shares outstanding at 2026-09-07：**3,023.736M**；
- Restricted cash：约 **$2.6B**。

2026 年 FY2026 10-K 还披露了大量长期数据中心租赁、电力与购买承诺。最新 10-Q 显示，Oracle 在 Q1 又新增重大数据中心租赁和合同承诺。它们不是今天全部到期的债务，但会让需求下降时的成本调整更困难。

### ATM 与稀释

Q1 通过 ATM 净融资约 **$19.909B**，发行约 **141M 股**。这相当于从 2026-05-31 的约 2,880M 股增至 2026-08-31 的约 3,024M 股，股数增加约 **5.0%**。

正面：融资降低了完全依赖债务的风险，并为数据中心扩张提供现金。

负面：如果增发发生在资本回报尚未证明时，股东承担的是即时稀释，而 OCI 利润要多年后才能兑现。必须同时追踪：

- 每股 revenue；
- 每股 operating income；
- 每股 FCF；
- ATM 平均发行价；
- mandatory convertible preferred 的转股影响；
- SBC 造成的额外股数。

### 重组成本与管理信号

10-Q 披露 FY2026 Oracle Restructuring Plan 截至 8 月底预计成本最高约 $2.1B；8 月 31 日之后又增加约 **$700M**。这说明 Oracle 在进行成本重构和 AI 自动化，但同时也意味着：

- 传统组织正在为资本密集转型让路；
- 短期存在额外重组现金支出；
- 裁员能降低费用，却不能替代数据中心、GPU、电力和利息成本。

## 5. Management and Capital Allocation

Oracle 管理层拥有长期销售、数据库工程和大型企业合同执行能力。Q1 revenue、cloud growth、RPO 和客户预付说明管理层确实抓住了 AI 云窗口。

但管理层正在执行 Oracle 历史上最激进的资本计划：

- FY2027 revenue guidance 至少 **$90B**；
- FY2027 non-GAAP EPS **$8.10**；
- FY2027 capex 预计约 **$90B–$95B**；
- 同时发行债务和股权；
- 扩建数据中心、电力和 GPU 能力；
- 管理传统软件迁云、重组和新 CFO 过渡。

Ellison 于 2026-09-12 取消了允许出售最多 50M 股的 10b5-1 计划，且公司披露此前没有通过该计划出售股票。这是治理与市场情绪信息，但不是经营现金流改善，也不能抵消 141M 股 ATM 增发。

后续管理层可信度要用以下指标评估，而不是只看 RPO：

1. RPO 转收入速度；
2. 客户预付和自带 GPU 的比例；
3. OCI 毛利率和数据中心利用率；
4. capex 后 FCF；
5. 债务、租赁和电力承诺；
6. 每股指标是否跑赢稀释；
7. 对大型客户集中与信用风险的披露是否更透明。

## 6. Valuation Work

### 估值快照

以 2026-09-11 收盘 $150.28、3,023.736M 普通股计算：

- Market cap：约 **$454.4B**；
- 现金及短期证券：约 **$37.1B**；
- notes payable and other borrowings：约 **$125.3B**；
- 窄口径 EV：约 **$542.7B**；
- EV / FY2027 revenue guidance：约 **6.0x**；
- FY2027 non-GAAP forward P/E：约 **18.6x**；
- FY2026 FCF yield：不适用；当前季度 FCF 为负。

第三方供应商可能使用包含租赁或其他准债务的宽口径 EV，因此会得到更高 EV。估值时不能把窄口径市值与宽口径债务混合使用。

### Forward P/E snapshot

| Metric | Value | Date / period | Source | Interpretation |
|---|---:|---|---|---|
| Current forward non-GAAP P/E | 18.6x | $150.28 / FY2027 EPS $8.10 | Oracle Q1 FY27 guidance + calculation | 对 FY2027 高增长并不昂贵，但 EPS 是 non-GAAP 且 FCF 为负 |
| 1-year high forward P/E | 未可靠核验 | 需要连续历史一致预期序列 | 本次不编造 | 无法判断当前处于一年区间高位还是低位 |
| 1-year low forward P/E | 未可靠核验 | 需要连续历史一致预期序列 | 本次不编造 | 不能仅凭当前倍数宣布便宜 |

### 情景估值

P/E 仍有一定解释力，因为 Oracle 有成熟软件利润；但必须把资本强度和 FCF 风险纳入倍数。以 $8.10 FY2027 non-GAAP EPS 为分母：

| 情景 | 倍数 | 隐含价格 | 相对 $150.28 | 核心条件 |
|---|---:|---:|---:|---|
| Bear | 12–14x | $97–$113 | -35% 至 -25% | RPO 延期/重议、OCI margin 弱、FCF 长期负、稀释增加 |
| Downside-normalized | 16x | $130 | -14% | 收入增长仍强，但市场把 ORCL 重新按重资本云估值 |
| Base | 18–22x | $146–$178 | -3% 至 +19% | $90B 指引大体兑现，RPO 转化，融资可控但 FCF 尚未完全证明 |
| Bull | 25–30x | $203–$243 | +35% 至 +62% | OCI 利润率改善、客户预付降低资本负担、FCF 拐点明确 |

**估值结论**：$150.28 已接近 base 区间下沿，而不是明显低于 base。若只看 EPS，ORCL 似乎合理；若把债务、租赁、ATM 和负 FCF 纳入，安全边际明显变薄。

### 实用价格区间

- **≤$110**：强安全边际候选区，前提是指引和客户质量没有断裂；
- **$110–$135**：可接受观察/小仓分批区；
- **$135–$180**：基准价值与合理波动区，需要继续验证 FCF；
- **$180–$200**：偏贵，需要 OCI margin 和资本回报证据；
- **>$200**：明显依赖 bull case，不宜只凭 RPO 追价。

## 7. Catalysts and Monitoring Plan

1. Q2 FY2027 revenue、Cloud 和 OCI 增速；
2. FY2027 $90B revenue / $8.10 EPS guidance 是否维持；
3. RPO 新增量与未来 12/36/60 个月确认速度；
4. 客户预付款、自带 GPU 及客户集中度；
5. 数据中心利用率、OCI 毛利率和每 MW 产出；
6. FY2027 capex 是否维持 $90B–$95B，及客户出资后的 net capex；
7. OCF、FCF 和利息支出；
8. 债务、租赁负债、信用评级和融资成本；
9. ATM 后 fully diluted shares 与每股经营指标；
10. 传统 software support、license revenue、Fusion/NetSuite；
11. Project Jupiter 电力、许可、施工和能源成本；
12. OpenAI 等大型客户的信用、合同延期和法律披露。

## 8. Risk Register

| 风险 | 概率 | 严重度 | 投资含义 |
|---|---|---:|---|
| AI 云资本回报低于预期 | 中高 | 高 | 收入增长不能转化为每股 FCF |
| 大客户集中/信用风险 | 中高 | 高 | 订单延期会同时打击 RPO、利用率和融资能力 |
| 长期租赁与电力固定成本 | 高 | 高 | 需求下滑时成本不能快速削减 |
| 债务和利息上升 | 中高 | 高 | 股东现金回报被利息优先吸收 |
| ATM 与可转优先股稀释 | 高 | 中高 | 总公司变大但每股价值不一定增加 |
| OCI 价格竞争 | 中 | 中高 | GPU 供给增加可能压低租赁价格和 margin |
| 传统软件衰退 | 中 | 中高 | 现金牛减弱，无法充分支撑转型投资 |
| 数据中心/电力建设延期 | 中 | 高 | RPO 无法按期确认，已投入资本闲置 |
| 重组与执行复杂度 | 中 | 中 | 裁员降低成本但可能损害销售、服务和交付 |
| 诉讼/披露风险 | 中 | 中 | 目前应视为未决法律风险，不等于指控已证实 |

## 9. 四种投资视角

### 反偏差检查

- **Information richness：A**。Oracle 长期上市、披露丰富，但大型 AI 合同的利润率、客户集中和资本责任仍不透明。
- **Main blind spot**：公开数据无法证明 $664B RPO 最终对应多少利润和自由现金流。
- **聪明投资者分歧**：多头认为负 FCF 是高回报建设期，空头认为 Oracle 正从高回报软件公司变成重资产、负现金流的基础设施融资平台。

### Buffett-style：Needs further observation

- **关键问题**：Oracle 仍否是能长期产生高回报现金流的软件公司？
- **支持证据**：数据库转换成本、Q1 35% GAAP operating margin、$23.1B OCF、企业应用粘性。
- **反对证据**：Q1 FCF -$5.4B、$28.5B capex、$125.3B borrowings、长期租赁与持续融资。
- **决策含义**：传统 Oracle 可长期研究，转型后的整体公司尚未达到高确定性；等待 FCF 和资本回报证据。
- **五年停市问题**：软件现金牛能否覆盖 AI 云的完整债务、租赁、电力和更新换代周期？

### Munger-style：Needs further observation

| 失败路径 | 机制 | 后果 |
|---|---|---|
| RPO 质量被高估 | 客户集中、合同利润率低或延期 | 订单大但股东回报差 |
| 资本责任失控 | GPU、数据中心、电力和租赁先于收入发生 | 需求下降时固定成本放大亏损 |
| 客户信用恶化 | 关键客户不能按长期合同付款 | RPO、应收账款和资产利用率同时受损 |
| 稀释掩盖增长 | ATM 和优先股增加股数 | EPS/FCF per share 落后于总收入 |
| 软件护城河变弱 | 开源、云原生和竞争云平台侵蚀支持收入 | 转型失去现金流底座 |

- **最大心理陷阱**：把 AI 需求真实等同于 Oracle 的 capex 一定有高回报。
- **三年后复盘问题**：最明显的红旗是否是 RPO 继续增加，但 FCF、每股收入和客户信用没有同步改善？

### Duan Yongping-style：Needs further observation

- **业务本质**：Oracle 为企业保存关键数据并运行核心流程，再把数据库能力延伸到云和 AI 算力。
- **用户价值**：数据库与企业软件价值长期已验证，OCI 的 AI 需求已验证，但 OCI 资本经济性尚未验证。
- **产品强度**：数据库护城河强；OCI 有技术和客户入口，但生态和规模弱于三大云。
- **人和文化**：执行力和销售能力强，正在接受资本纪律和信息透明度的压力测试。
- **合适价格**：$110–$135 更具安全边际；$135–$180 可研究；$200 以上需 bull-case 证据。
- **追问**：OCI 是在持续创造企业客户价值，还是在用 Oracle 资产负债表追逐短期算力短缺？

### Li Lu-style：Needs further observation

- **能力圈**：数据库、支持和企业应用可理解；AI 云大型合同的资本回报和信用风险暂时超出高置信能力圈。
- **长期趋势**：企业 AI、数据基础设施和多云是长期趋势，Oracle 位于企业数据与算力交叉点。
- **下行保护**：传统软件、现金和经营现金流提供保护，但债务、租赁、负 FCF 和稀释削弱保护。
- **研究结论**：值得继续深挖，可在组合纪律内小仓验证；不应只因 forward P/E 不高就高置信重仓。
- **追问**：20 年后 Oracle 是企业 AI 的关键基础设施节点，还是 AI capex 高峰期的过度扩张者？

### Composite score

| 维度 | 分数 |
|---|---:|
| Business model | 8.0/10 |
| Moat | 8.0/10 |
| Management | 7.0/10 |
| Financial quality | 5.0/10 |
| Valuation attractiveness | 6.5/10 |
| Long-term certainty | 6.5/10 |
| Downside risk control | 4.5/10 |

业务模型和数据库护城河得分高；管理层抓住 OCI 需求，但资本计划规模过大使管理层得分受限；财务质量和下行控制被负 FCF、债务、租赁和稀释压制；估值较高点改善，但仍不足以覆盖全部资本回报不确定性。

### Integrated decision memo

| 维度 | 结论 | 置信度 |
|---|---|---|
| 生意质量 | 数据库/应用高质量，OCI 高增长但重资本 | 中高 |
| 护城河 | 数据库强，OCI 需要继续证明 | 中高 |
| 管理层 | 执行强，资本配置压力极大 | 中 |
| 最大风险 | RPO 转化质量与 AI 云资本回报 | 高 |
| 长期趋势 | 企业 AI、数据和云基础设施方向强 | 中高 |
| 估值与安全边际 | $150 附近接近 base 下沿，尚非强安全边际 | 中 |

| 投资状态 | 研究含义 |
|---|---|
| 无持仓 | 可纳入重点观察；更适合分批而非一次性重仓 |
| 已持仓 | 重点看每股 FCF、债务、ATM 和 RPO 质量，不能机械按跌幅补仓 |
| 加仓信号 | OCI margin 改善、capex/net capex 可控、FCF 收窄、RPO 转化透明 |
| 减仓/回避信号 | 指引下调、客户延期/信用风险、租赁和债务继续超预期、每股指标恶化 |

## 10. 与用户交易纪律的匹配

Oracle 从数据库、企业软件扩张至云基础设施和 AI，仍围绕企业数据与计算核心使命，目前不构成明确使命漂移。

但若资本越来越主要用于为少数模型公司提供通用 GPU，而数据库、应用和多云协同无法证明，公司可能从“企业数据平台”变为“高杠杆算力出租商”。这会构成使命稀释风险。

ORCL 应归入：**企业软件 / 云基础设施 / AI 基础设施混合类别**。与 MSFT、AMZN、GOOGL、NVDA、VRT、GEV 等可能存在类别重叠。没有最新完整组合数据，因此不能确认同类资产是否低于 15%，也不能确认买入后现金加低 beta/核心资产是否仍高于 30%。

## 11. Final Research Framework

**ORCL 现在不是一个简单的“便宜 AI 股”，而是高质量数据库现金牛与高资本强度 AI 云平台的合并体。**

- 传统业务：质量高、粘性强、长期可持有；
- OCI：需求强、增长快，但需等待资本回报验证；
- RPO：非常强的需求指标，但不是利润；
- 资产负债表：有现金和经营现金流，但债务、租赁和 capex 已成为核心变量；
- 估值：$150.28 下约 18.6x FY2027 non-GAAP EPS，表面合理，考虑负 FCF 后安全边际一般。

### What would change my view

**上调至 Positive**：

- Q2/Q3 FY2027 revenue 和 OCI 增速仍在指引上半区；
- RPO 按 13%/37%/34% 节奏转为收入；
- 客户预付和自带 GPU 降低 net capex；
- OCI margin、利用率和每 MW 收入改善；
- FCF 从负数持续收窄并形成转正时间表；
- 债务、租赁和稀释低于市场担忧。

**下调至 Neutral/Negative**：

- FY2027 revenue 或 EPS guidance 下调；
- RPO 延期、重议或关键客户信用风险显性化；
- capex 持续大幅超出收入增长和客户出资能力；
- OCI 规模增长但毛利率/利用率恶化；
- ATM、优先股和 SBC 使每股指标落后；
- software support 开始持续负增长。

## Sources

- [Oracle Q1 FY2027 results, 2026-09-10](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)
- [Oracle Form 10-Q for quarter ended 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)
- [Oracle Form 8-K for Q1 FY2027 results, 2026-09-10](https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-20260910.htm)
- [Oracle Form 8-K on Larry Ellison 10b5-1 plan cancellation, filed 2026-09-14](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389753/d20034d8k.htm)
- [Oracle stock information](https://investor.oracle.com/stock-information/default.aspx)
- [Oracle SEC submissions](https://data.sec.gov/submissions/CIK0001341439.json)
- Saved prior research: `deep-research/2026-07-14-deep-research.md`
