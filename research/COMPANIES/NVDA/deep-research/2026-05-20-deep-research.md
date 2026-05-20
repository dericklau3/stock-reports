# NVIDIA（NVDA）深度研究 - 2026-05-20

- **Research view**: Positive
- **Confidence**: 中等
- **Time horizon**: 12-24 个月
- **Main thesis**: NVDA 已从 GPU 芯片公司升级为 AI data center scale infrastructure 平台，FY2026 revenue 2159 亿美元、net income 1201 亿美元、Data Center revenue 1937 亿美元，且 FY2027 Q1 指引继续到 780 亿美元。当前约 5.34 万亿美元市值看似巨大，但按 FY2027/FY2028 共识 EPS 分别约 26x/19x，如果 AI factory capex 继续扩张、Blackwell/Rubin 迭代维持领先，估值仍可解释。
- **Key risk**: 最大风险是 AI 资本开支周期与监管/竞争同时转向。若 hyperscaler capex 增速放缓、中国出口管制进一步扩大、客户自研 ASIC 抢走高毛利训练/推理需求，或 Blackwell/Rubin 供应链导致毛利率下滑，NVDA 的高质量倍数会被压缩。

## 1. Executive View

**研究观点：Positive。** NVDA 仍是 AI 基础设施产业链中商业模式最强、盈利质量最高、平台控制力最强的公司之一。它的优势已经不只是 GPU，而是 GPU、CPU、networking、NVLink/NVSwitch、InfiniBand/Ethernet、CUDA、systems、AI software、model/tooling、physical AI 和 hyperscaler/sovereign AI/customer ecosystem 共同构成的平台。

但 Positive 不是“无脑追高”。截至 2026-05-20（亚洲时间），NVDA FY2027 Q1 结果尚未发布；公司将在美国时间 2026-05-20 盘后公布 Q1 FY2027 结果。本文使用最新正式财务底稿，即 FY2026 Q4 / FY2026 全年，并把 Q1 FY2027 作为即将到来的关键催化。

核心判断：

- **FY2026 规模和盈利仍在高速扩张。** FY2026 revenue 2159.38 亿美元，同比增长 65%；GAAP gross margin 71.1%；operating income 1303.87 亿美元；net income 1200.67 亿美元；diluted EPS 4.90 美元。来源：[NVIDIA FY2026 Q4 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)。
- **Data Center 是绝对核心。** FY2026 Data Center revenue 1937 亿美元，同比增长 68%；Q4 Data Center revenue 623 亿美元，同比增长 75%、环比增长 22%。公司称增长由 accelerated computing、AI、Blackwell platform、NVLink compute fabric、Ethernet/InfiniBand 等驱动。
- **Q1 FY2027 指引仍强。** 公司指引 FY2027 Q1 revenue 780 亿美元 +/- 2%，GAAP/non-GAAP gross margin 约 74.9%/75.0%，并明确没有假设来自中国的 Data Center compute revenue。来源：[NVIDIA FY2026 Q4 outlook](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)。
- **现金流和资本回报极强。** FY2026 operating cash flow 1027 亿美元，capex 约 61 亿美元，粗略 FCF 约 966 亿美元；cash + marketable securities 625.56 亿美元，debt carrying amount 84.68 亿美元。FY2026 repurchase 404 亿美元，另有 585 亿美元 repurchase authorization。
- **估值高但不荒谬。** 2026-05-19 收盘价 220.61 美元，市值 5.34 万亿美元，TTM PE 45.0x，forward PE 26.3x。StockAnalysis/consensus 显示 FY2027 revenue 约 3757 亿美元、EPS 8.47 美元，FY2028 revenue 约 4986 亿美元、EPS 11.57 美元。来源：[StockAnalysis NVDA](https://stockanalysis.com/stocks/nvda/)、[StockAnalysis forecast](https://stockanalysis.com/stocks/nvda/forecast/)。

最强反方理由：NVDA 规模已经非常大，未来每一个增量都越来越依赖 hyperscaler 和 sovereign AI 的资本开支继续加速。AI 投资若从“capacity buildout”进入“ROI scrutiny”，NVDA 的收入增速、毛利率和估值倍数可能同步回落。5 万亿美元以上市值意味着市场对未来几年的执行容忍度不高。

## 2. Business Model and Industry Structure

NVIDIA 业务从传统 GPU 发展为 AI infrastructure full-stack platform：

- **Compute**：Hopper、Blackwell、Blackwell Ultra、Rubin/Vera Rubin roadmap、Grace CPU、AI accelerator systems。
- **Networking**：NVLink、NVSwitch、InfiniBand、Spectrum-X Ethernet、BlueField DPU。
- **Systems**：GB200/GB300 NVL systems、DGX、HGX、rack-scale solutions。
- **Software and ecosystem**：CUDA、libraries、NVIDIA AI Enterprise、NIM、Omniverse、Isaac、Drive、NeMo/Nemotron。
- **End markets**：Data Center、Gaming、Professional Visualization、Automotive、Robotics/physical AI、sovereign AI。

行业结构：

| 领域 | 主要竞争 | NVDA 优势 | 主要风险 |
|---|---|---|---|
| AI accelerators | AMD、Intel、Google TPU、AWS Trainium/Inferentia、custom ASICs | CUDA ecosystem、性能/软件/网络/系统整合、快速 roadmap | 客户自研 ASIC、inference commoditization |
| AI networking | Broadcom、Marvell、Arista、Cisco、custom switches | NVLink/NVSwitch、InfiniBand、Spectrum-X、rack-scale integration | Ethernet ecosystem 竞争、客户去绑定 |
| Data center systems | OEM/ODM、hyperscaler internal design | turnkey AI factories、full-stack optimization | 毛利率受 system mix 和供应链影响 |
| Gaming/RTX | AMD、Intel、console/cloud gaming | GeForce brand、RTX、DLSS、developer ecosystem | 消费周期、渠道库存、供应紧张 |
| Automotive/robotics | Tesla, Mobileye, Qualcomm, in-house chips | Drive platform、Omniverse/Isaac/physical AI stack | 车厂自研、周期长、收入占比小 |

NVDA 的护城河是系统性而不是单点：芯片性能、软件生态、开发者锁定、网络互联、模型优化、供应链获取、客户共同设计和产品节奏都在强化。它的风险也是系统性的：客户太集中、CAPEX 太集中、供应链太复杂、监管太重要。

## 3. Segment and Product Analysis

### FY2026 Segment

| 指标 | Compute & Networking | Graphics | Total |
|---|---:|---:|---:|
| FY2026 revenue | 1935 亿美元左右 | 225 亿美元左右 | 2159 亿美元 |
| Revenue growth | +67% | +57% | +65% |
| Segment operating income | 1301 亿美元 | 92 亿美元 | 1393 亿美元 segment total |

公司同时按 market platform 披露，Data Center 是最大平台。FY2026 Data Center revenue 1937 亿美元，Gaming revenue 约 160 亿美元，Automotive 和 Professional Visualization 的战略价值大于当前收入体量。

### Data Center

Data Center 是 NVDA 的核心。Q4 FY2026 revenue 623 亿美元，全年 1937 亿美元。驱动因素包括：

- Blackwell platform demand。
- NVLink compute fabric for Blackwell systems。
- Ethernet and InfiniBand growth。
- 推理需求上升，agentic AI 和 reasoning workloads 增加 token generation。
- hyperscaler、enterprise AI、sovereign AI、industrial AI 同时投入。

公司 Q1 FY2027 指引明确没有包含中国 Data Center compute revenue，这说明即使在中国受限的情况下，全球其他地区需求仍足以支撑 780 亿美元季度收入指引。这是 thesis 的重要正面信号，也是风险：如果中国缺口更大或其他地区无法长期补上，增长会受压。

### Blackwell, Rubin and Platform Roadmap

Blackwell 是 FY2026 增长核心，Rubin/Vera Rubin 是 FY2027-FY2028 叙事核心。公司在 FY2026 Q4 release 中披露：

- Rubin platform 包括六个新芯片，目标是较 Blackwell 将 inference token cost 降低最多 10x。
- AWS、Google Cloud、Microsoft Azure、Oracle Cloud Infrastructure 将是 Vera Rubin-based instances 的首批部署者之一。
- Blackwell Ultra 在 SemiAnalysis InferenceX benchmark 中相较 Hopper 可实现最多 50x performance 和 35x lower cost for agentic AI。

这些声明的投资意义是：NVDA 不只是卖“更快芯片”，而是在持续降低每 token 成本，从而刺激更多推理需求。若成本下降带来需求弹性，NVDA 的 TAM 会继续扩大；若单位成本下降主要被客户用于压价，毛利率会受影响。

### Gaming, Professional Visualization, Automotive

Gaming 仍是重要现金流和品牌基础，但已不再主导估值。FY2026 Data Center revenue 约 1937 亿美元，而 Graphics segment revenue 约 225 亿美元。Gaming 的作用更多是：

- RTX developer ecosystem。
- AI PC / local inference / creator tools。
- 消费端品牌和渠道。
- 为 developer base 提供入口。

Automotive Q4 FY2026 revenue 为 6.04 亿美元，同比增长 6%。短期不是估值主线，但 Drive、robotics、physical AI、Omniverse/Isaac 可能成为长期选择权。

## 4. Financial Deep Dive

### Multi-Year Trend

| 指标 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Revenue | 609.22 亿美元 | 1304.97 亿美元 | 2159.38 亿美元 |
| Revenue growth | +125.9% | +114.2% | +65.5% |
| GAAP gross margin | 72.7% | 75.0% | 71.1% |
| Operating income | 329.72 亿美元 | 814.53 亿美元 | 1303.87 亿美元 |
| Net income | 297.60 亿美元 | 728.80 亿美元 | 1200.67 亿美元 |
| Diluted EPS | 1.19 美元 | 2.94 美元 | 4.90 美元 |
| Operating cash flow | 280.90 亿美元 | 640.89 亿美元 | 1027.18 亿美元 |
| Capex | 10.69 亿美元 | 33.90 亿美元 | 60.62 亿美元 |

NVDA 的财务模型极其强：高毛利、高 operating leverage、轻资本开支、强现金转换。FY2026 毛利率同比下降，主要因为从 Hopper HGX 过渡到 Blackwell full-scale datacenter solutions，以及 Q1 FY2026 H20 相关 45 亿美元 excess inventory and purchase obligations charge。即便如此，FY2026 GAAP gross margin 仍有 71.1%。

### Q4 FY2026

Q4 FY2026：

- Revenue：681.27 亿美元，同比增长 73%，环比增长 20%。
- GAAP gross margin：75.0%。
- GAAP operating income：442.99 亿美元。
- GAAP net income：429.60 亿美元。
- GAAP diluted EPS：1.76 美元。
- Non-GAAP diluted EPS：1.62 美元。
- Data Center revenue：623 亿美元，同比增长 75%，环比增长 22%。

Q4 质量很高：收入、数据中心、毛利率和 EPS 同时强。需要注意 non-GAAP EPS 低于 GAAP EPS，原因包括 gains/losses on publicly-held equity securities 等项目，因此不能机械地只看 non-GAAP。

### Balance Sheet and Cash Flow

截至 2026-01-25：

- Cash and cash equivalents：106.05 亿美元。
- Marketable securities：519.51 亿美元。
- Cash + marketable securities：625.56 亿美元。
- Debt carrying amount：84.68 亿美元。
- Operating cash flow：1027.18 亿美元。
- Capex：约 60.62 亿美元。
- Rough free cash flow：约 966 亿美元。
- FY2026 buybacks：404 亿美元，repurchased 2.82 亿股。
- FY2026 shareholder returns：411 亿美元，包括 repurchases and dividends。
- Remaining repurchase authorization：585 亿美元。

NVDA 资本效率很强：相比上游 fabs、HBM、advanced packaging、AI data center operators，NVDA 本身 capex 很低。真正的资本密集部分在客户和供应链，NVDA 的风险更多是 purchase obligations、inventory commitments 和供应链协调，而不是自建 fab 资产沉没成本。

### Accounting and Quality Issues

需要重点看三项：

- **SBC**：FY2027 Q1 起，NVDA non-GAAP measures 将不再排除 stock-based compensation。Q1 FY2027 指引 GAAP/non-GAAP opex 均包含约 19 亿美元 SBC。这使 non-GAAP 更干净，但也提醒投资者 SBC 是真实成本。
- **Inventory/purchase obligations**：FY2026 provision for inventory and excess inventory purchase obligations 为 72 亿美元，其中 H20 charge 45 亿美元；截至 FY2026 末，inventory 214 亿美元，outstanding inventory purchase and long-term supply and capacity obligations 952 亿美元。
- **Equity investments**：公司在 AI ecosystem 中有大量投资和合作，可能帮助需求生成，也会带来 valuation volatility 和关联生态风险。

## 5. Management and Capital Allocation

Jensen Huang 和管理团队是 NVDA 溢价的一部分。过去三年公司几乎每一代产品节奏都踩中了 AI 需求爆发：Hopper 到 Blackwell，再到 Blackwell Ultra 和 Rubin。管理层真正的能力不是只做芯片，而是把硬件、网络、软件、开发者、云厂商和供应链一起组织成 AI factory 平台。

资本配置上：

- 大额回购：FY2026 repurchase 404 亿美元。
- 现金储备充足：625.56 亿美元 cash + marketable securities。
- 保持小额股息：季度 0.01 美元/股。
- ecosystem investment：Groq licensing、Anthropic partnership、CoreWeave、Synopsys、OpenAI 潜在投资/合作等。

风险在于生态投资和客户融资边界。若 NVDA 通过投资、融资、合作推动客户采购，市场会开始追问收入质量和循环融资风险。目前没有证据说明这是核心问题，但必须监控。

## 6. Valuation Work

### Valuation Method Selection

NVDA 是高盈利、高增长、高现金转换的 AI 平台公司，适合用：

- Forward P/E：核心方法，反映 FY2027/FY2028 高增长。
- EV/FCF：检查现金流质量。
- EV/Sales：辅助观察 AI 平台溢价是否过热。
- Scenario EPS + multiple：因为最大变量是 AI capex 周期和利润中枢。
- 不适合只用 TTM PE，因为 FY2027 revenue 指引和共识增长远高于 TTM。

当前快照（2026-05-19 收盘）：

- 股价：220.61 美元。
- Market cap：5.34 万亿美元。
- Revenue TTM：2159.4 亿美元。
- Net income TTM：1200.7 亿美元。
- EPS TTM：4.90 美元。
- Shares outstanding：242.2 亿股。
- PE：45.0x。
- Forward PE：26.3x。
- FY2027 consensus revenue：3757 亿美元，EPS 8.47 美元。
- FY2028 consensus revenue：4986 亿美元，EPS 11.57 美元。
- Analyst average target：275.83 美元，61 analysts，Strong Buy consensus。

### Scenario Valuation

以下是研究情景，不是投资建议或确定性目标价。

| 情景 | FY2028 revenue / EPS 假设 | 合理倍数 | 隐含每股价值 | 触发条件 |
|---|---:|---:|---:|---|
| Bear | Revenue 3000-3500 亿美元，EPS 6.50-8.00 美元 | 18-22x EPS | 117-176 美元 | AI capex 放缓，客户自研 ASIC 替代，毛利率回落，中国/监管压力扩大 |
| Base | Revenue 4750-5250 亿美元，EPS 10.50-12.00 美元 | 23-28x EPS | 240-336 美元 | Blackwell/Rubin 持续 ramp，hyperscaler/sovereign AI capex 强，毛利率 70%+ |
| Bull | Revenue 6000-7000 亿美元，EPS 14.00-16.00 美元 | 30-35x EPS | 420-560 美元 | AI factory 建设多年扩张，推理需求爆发，NVDA networking/software attach 提升 |

当前股价约 221 美元，低于 base case 中位区间，但高于 bear case。换句话说，风险回报仍偏正面，但已不适合忽略下行情景。Q1 FY2027 财报和 Q2 指引将决定市场是继续用 base/bull 定价，还是开始担心 AI capex peak。

## 7. Catalysts and Monitoring Plan

近期催化：

- FY2027 Q1 earnings：美国时间 2026-05-20 盘后公布。
- Q1 实际 revenue 是否超过 780 亿美元指引，Q2 revenue guide 是否继续显著上行。
- Gross margin：Blackwell/Rubin systems mix 是否维持 75% 左右。
- 中国：是否继续没有 Data Center compute revenue，是否有替代合规产品。
- Rubin/Vera Rubin roadmap、Blackwell Ultra ramp、GB300 / NVL systems。
- Hyperscaler capex：Microsoft、Meta、Amazon、Google、Oracle、CoreWeave 等。
- Networking growth：NVLink、InfiniBand、Spectrum-X Ethernet。
- Supply chain：HBM、CoWoS/advanced packaging、power/cooling、rack integration。
- Ecosystem investments：OpenAI、Anthropic、CoreWeave、Groq、Synopsys 等。

重点监控指标：

- Data Center revenue growth q/q and y/y。
- Compute vs networking mix。
- Gross margin and inventory/purchase obligation provisions。
- Operating expenses, especially SBC。
- Free cash flow and buyback pace。
- Customer concentration and large cloud provider mix。
- China/export control disclosures。
- Inference revenue mix and token economics。
- Competitor traction from AMD, Broadcom/custom ASICs, TPU, Trainium。
- Hyperscaler AI capex ROI commentary。

## 8. Risk Register

| 风险 | 概率 | 影响 | 为什么重要 |
|---|---|---|---|
| AI capex 放缓 | 中 | 高 | NVDA 增长高度依赖 hyperscaler/sovereign AI 持续建设。 |
| 客户自研 ASIC | 中 | 高 | Google TPU、AWS Trainium、Meta/微软自研、Broadcom/Marvell ASIC 会争夺部分 workload。 |
| 中国出口管制 | 中高 | 高 | Q1 FY2027 指引已不包含中国 Data Center compute revenue，政策变化仍可能冲击。 |
| 毛利率下行 | 中 | 高 | 从芯片到 rack-scale systems mix 可能压低结构性毛利率。 |
| 供应链瓶颈 | 中 | 中高 | HBM、advanced packaging、networking、power/cooling 都可能限制交付。 |
| 客户集中 | 中 | 高 | 大型 cloud providers 对 Data Center revenue 影响巨大。 |
| 收入质量/生态融资质疑 | 低中 | 中高 | 大额生态投资可能引发市场对循环需求的审视。 |
| 估值压缩 | 中 | 高 | 5.34 万亿美元市值要求持续 beat-and-raise。 |
| 监管/反垄断 | 中 | 中高 | 平台控制力越强，监管关注越高。 |

## 9. Final Research Framework

NVDA 当前是 **Positive**，但这是一个需要持续验证的 Positive：公司质量极高、现金流极强、平台地位清晰，forward valuation 在当前增长路径下仍可解释。真正要避免的是把 AI 基础设施扩张当成永远单向上行。

我会维持或增强 Positive 的条件：

- FY2027 Q1/Q2 revenue guide 继续强于 780 亿美元基准。
- Data Center q/q growth 维持强劲，networking attach 提升。
- Gross margin 稳定在 72%-75% 区间。
- China 缺口被全球其他需求吸收，且没有更大监管冲击。
- FY2028 EPS 上修速度快于股价上涨速度。
- 自研 ASIC 没有明显侵蚀 NVDA 的 high-end training/inference platform。

我会下调观点的条件：

- Q1 FY2027 或 Q2 指引显示增长放缓。
- 毛利率因 systems mix、pricing 或供应链成本明显下行。
- Hyperscaler capex commentary 从“继续加速”转向“消化和 ROI 审查”。
- 客户自研 ASIC/AMD 等替代在关键 workloads 上取得明显份额。
- 出口管制范围扩大，或中国以外需求不足以补缺口。
- 估值升至显著高于 base case，而 EPS revisions 跟不上。

## Sources

- NVIDIA, [FY2026 Q4 and fiscal 2026 results press release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/), 2026-02-25.
- SEC, [NVIDIA FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm), filed 2026-02-26.
- SEC, [NVIDIA 2026 Annual Review / Proxy-related filing](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm), filed 2026-05-12.
- NVIDIA, [Q1 FY2027 conference call announcement](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-First-Quarter-Financial-Results/default.aspx), 2026-04-29.
- StockAnalysis, [NVDA overview and market data](https://stockanalysis.com/stocks/nvda/), accessed 2026-05-20.
- StockAnalysis, [NVDA market cap and enterprise value](https://stockanalysis.com/stocks/nvda/market-cap/), accessed 2026-05-20.
- StockAnalysis, [NVDA ratios](https://stockanalysis.com/stocks/nvda/financials/ratios/), accessed 2026-05-20.
- StockAnalysis, [NVDA forecast](https://stockanalysis.com/stocks/nvda/forecast/), accessed 2026-05-20.
