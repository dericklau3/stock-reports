# Cloudflare, Inc. (NYSE: NET) 深度研究报告

日期：2026-07-08  
公司：Cloudflare, Inc.  
Ticker：NET  
交易所：NYSE  
行业：Software - Infrastructure / Connectivity Cloud / Cybersecurity / Edge Network  
CIK：0001477333

> 本报告是研究支持，不构成个性化投资建议。所有估值均依赖假设，尤其是高成长软件公司的长期增长率、利润率和市场给予的 EV/Sales 倍数。

## 固定摘要

- **Research view**：Constructive but watchful（好公司，但当前价格要求极高）
- **Confidence**：中等偏高（业务质量判断较高，估值安全边际判断较高；AI/agentic 转型长期效果仍需验证）
- **Time horizon**：中长期，1-3 年跟踪；长期可研究，当前不适合按安全边际重仓
- **Main thesis**：Cloudflare 是少数同时覆盖网络、安全、开发者计算、AI 边缘基础设施的全球平台型公司；收入仍保持约 30%+ 增长，DBNRR 回升至 118%，大客户增长强；但当前约 33.6x FY2026 sales / 40.5x TTM sales，已经把非常乐观的长期成长预期提前定价。
- **Key risk**：估值压缩风险最大，其次是 AI-first 重组执行风险、SBC/稀释、毛利率下行、与 hyperscaler / CDN / security vendor 的竞争。

---

## 1. Executive View

### 一句话结论

NET 是“互联网基础设施 + 安全 + 边缘计算 + AI 开发者平台”的高质量平台公司，但当前股价 **268.83 美元** 已经进入高预期区：如果只按 base case，现价没有安全边际；只有在 Cloudflare 未来两年继续维持接近 30%+ 增长、AI/Workers 平台打开新增长曲线、并且市场长期给予 30x 左右远期 EV/Sales 时，现价才比较合理。

### 核心观点

1. **业务质量强**：Cloudflare 不是单一 CDN 公司，而是把全球边缘网络、安全、Zero Trust、应用防护、开发者计算和 AI Gateway / Workers AI 打包成一张统一网络平台。
2. **增长仍强**：2026Q1 revenue 为 **6.3976 亿美元**，同比 **+34%**；>$100k 年化收入客户 **4416** 个，DBNRR **118%**，RPO **25.435 亿美元**。
3. **盈利质量改善但仍不成熟**：Q1 non-GAAP operating margin **11.4%**，FCF margin **13%**；但 GAAP 仍亏损，SBC 高，且 2026 年有约 20% 裁员和 1.40-1.50 亿美元重组费用。
4. **估值很满**：当前 EV 约 **943.8 亿美元**，TTM revenue 约 **23.3 亿美元**，EV/Sales 约 **40.5x**；按公司 2026 revenue guidance 中点 **28.09 亿美元**算，EV/FY2026 sales 约 **33.6x**。

### 最强反对理由

这可能是一家真正稀缺的平台型公司：如果 AI agent、API 安全、边缘推理、Workers、R2、Zero Trust 都在同一张网络上形成复合飞轮，市场可能长期愿意给 NET 极高倍数，传统 EV/Sales 估值会显得过于保守。

---

## 2. Business Model and Industry Structure

### 新手解释：Cloudflare 到底做什么？

你可以把 Cloudflare 理解成“全球互联网入口和防护层”。

普通网站或企业应用如果直接暴露在互联网上，会遇到几个问题：

- 用户离服务器远，访问慢；
- 遭受 DDoS 攻击、恶意爬虫、API 攻击；
- 企业员工访问内部系统时，需要安全身份验证；
- 开发者希望把代码部署到离用户更近的地方；
- AI 应用需要安全、低延迟地调用模型和处理数据。

Cloudflare 的做法是：在全球部署网络节点，把客户的网站、API、企业应用和开发者代码接入 Cloudflare 网络。用户访问这些服务时，流量先经过 Cloudflare，Cloudflare 帮客户做加速、防护、身份验证、路由优化和边缘计算。

### 它怎么赚钱？

Cloudflare 主要按订阅收费：客户每月或每年付费使用它的网络、安全、Zero Trust、开发者和数据服务。大客户通常签年度或多年合同，小客户可以自助购买。

### 重要术语翻译

- **CDN**：内容分发网络，把图片、网页、文件缓存到离用户更近的服务器，让访问更快。
- **DDoS 防护**：抵御海量恶意流量攻击，防止网站被打挂。
- **WAF**：Web Application Firewall，网站应用防火墙，用来拦截常见攻击。
- **Zero Trust**：零信任安全，不默认相信任何设备或用户，每次访问都要验证身份和权限。
- **SASE**：把企业网络连接和安全功能放到云端统一管理。
- **Workers**：Cloudflare 的边缘 serverless 计算平台，开发者可以把代码部署到 Cloudflare 全球网络上运行。
- **R2**：Cloudflare 的对象存储，类似 AWS S3，但主打低或无出站流量费用。
- **RPO**：Remaining Performance Obligations，剩余履约义务，可粗略理解为已签合同但未来才确认收入的金额。
- **DBNRR**：Dollar-Based Net Retention Rate，老客户留存和扩张率。118% 表示一年前同一批客户现在贡献的年化收入变成 118%，扣除了流失和缩减。

### 行业结构

Cloudflare 处在多个市场交汇处：

- CDN / edge network：Akamai、Fastly、AWS CloudFront；
- 网络安全：Zscaler、Palo Alto、Fortinet、CrowdStrike、Microsoft；
- Zero Trust / SASE：Zscaler、Palo Alto、Cisco、Netskope；
- 开发者平台：AWS Lambda、Vercel、Fly.io、Fastly Compute；
- 对象存储/AI 基础设施：AWS、Google Cloud、Azure、Databricks、Snowflake 生态。

Cloudflare 的独特之处不是每条产品线都最强，而是它试图用同一张全球网络承载所有产品。这个“统一网络平台”是核心护城河。

---

## 3. Segment and Product Analysis

Cloudflare 披露不是传统分部制，但业务可按产品功能拆成几类。

### 3.1 Application Services：应用性能与安全

包括 CDN、DNS、DDoS、防火墙、bot management、API security、SSL/TLS 等。

这部分是 Cloudflare 的起家业务，也是客户接入的入口。优势是部署简单、免费层带来开发者和中小网站入口、品牌强。风险是 CDN 本身容易被视为基础设施商品，长期需要通过安全和高级功能提高 ARPU。

### 3.2 Zero Trust / Cloudflare One：企业安全网络

企业员工、设备和应用越来越分散，传统 VPN 不够安全且体验差。Cloudflare One 让企业用云端策略控制员工访问 SaaS、私有应用、互联网和内部系统。

这部分面对 Zscaler、Palo Alto、Microsoft 等强竞争对手。Cloudflare 的优势是网络覆盖广、集成度高；弱点是大型企业安全采购周期长、销售组织执行要求高。

### 3.3 Network Services：Magic Transit / Magic WAN 等

这些产品服务更大的企业网络需求，如替代传统网络设备、保护整个网络层、优化广域网连接。

战略意义：把 Cloudflare 从网站防护供应商升级为企业网络基础设施供应商。

### 3.4 Developer Platform：Workers、KV、Durable Objects、D1、R2

这是长期可选价值最高的部分。开发者可以在 Cloudflare 边缘网络上运行代码、存数据、构建应用。

如果 Workers 成为 AI agent 和全球低延迟应用的默认平台之一，Cloudflare 的估值逻辑会从“安全/CDN 软件公司”升级为“边缘云平台”。但这条曲线仍处于证明阶段，收入占比、单位经济和长期竞争优势还需要更多披露。

### 3.5 AI 相关产品：AI Gateway、Workers AI、agentic AI 生态

Cloudflare 管理层在 2026Q1 明确强调：AI 正在推动互联网重新平台化，是公司历史上最大顺风之一。AI 产品的逻辑包括：

- 帮企业观察、控制 AI 应用调用；
- 在 Cloudflare 网络上运行或路由 AI 推理；
- 保护 AI 应用和 API；
- 用 Workers / R2 / D1 支持 AI-native 应用部署。

这强化了核心使命“help build a better Internet”，不是明显偏离初心。但如果 AI 叙事强于实际收入贡献，估值会非常脆弱。

---

## 4. Financial Deep Dive

### 4.1 最新季度：2026Q1

来源：Cloudflare 2026-05-07 8-K Exhibit 99.1；2026Q1 10-Q。

- Revenue：**6.3976 亿美元**，同比 **+34%**
- GAAP gross profit：**4.556 亿美元**
- GAAP gross margin：**71.2%**，低于 2025Q1 的 75.9%
- Non-GAAP gross margin：**72.8%**，低于 2025Q1 的 77.1%
- GAAP operating loss：**6199.4 万美元**，约收入 -9.7%
- Non-GAAP operating income：**7309.7 万美元**，non-GAAP operating margin **11.4%**
- GAAP net loss：**2292.7 万美元**
- Non-GAAP net income：**9400 万美元**
- Operating cash flow：**1.5833 亿美元**
- Free cash flow：**8407.4 万美元**，FCF margin **13%**
- Cash, cash equivalents and available-for-sale securities：**41.639 亿美元**

### 4.2 TTM 与估值数据

来源：StockAnalysis / S&P Global Market Intelligence 页面，更新至 2026-07-08。

- 收盘价：**268.83 美元**（2026-07-07）
- Market cap：约 **950.2 亿美元**
- Enterprise value：约 **943.8 亿美元**
- TTM revenue：约 **23.3 亿美元**
- TTM net loss：约 **8674 万美元**
- TTM operating cash flow：约 **6.1566 亿美元**
- TTM FCF：约 **3.0994 亿美元**
- EV/Sales：约 **40.5x**
- Forward PS：约 **31.7x**
- Forward PE：约 **207.7x**
- P/FCF：约 **306.6x**
- Beta：约 **1.67**
- 52 周区间：**158.83 - 276.82 美元**
- RSI：约 **67.6**
- 50 日均线：**227.53 美元**
- 200 日均线：**208.63 美元**

### 4.3 客户和合同质量

来源：2026Q1 10-Q。

- 年化收入 >10 万美元客户：**4416**，上年同期 **3527**
- DBNRR：**118%**，上年同期 **111%**
- RPO：**25.435 亿美元**
- 预计 64% RPO 在未来 12 个月确认为收入

这组数据是本报告最看好的部分：大客户增长和 DBNRR 回升说明 Cloudflare 不只是靠新客户拉动收入，老客户也在扩张使用。

### 4.4 毛利率和资本强度

Cloudflare 的毛利率仍高于大多数基础设施公司，但 2026Q1 毛利率从去年同期下降，说明网络成本、AI/边缘计算、产品组合和基础设施投资可能带来压力。

关键问题：Cloudflare 能否同时维持 30% 左右收入增长、70%+ 毛利率、逐步扩大 FCF margin？如果 AI 工作负载拉低毛利率，市场给的高倍数会受到挑战。

### 4.5 SBC、稀释和债务

2026Q1 SBC and related employer payroll taxes：**1.2746 亿美元**，约为当季收入的 **19.9%**。这对 GAAP 盈利和真实股东回报是明显压力。

资产负债表：

- Cash and equivalents：9.322 亿美元
- Available-for-sale securities：32.3165 亿美元
- Convertible senior notes current：12.9227 亿美元
- Convertible senior notes noncurrent：19.7556 亿美元

第三方数据口径显示总现金约 **41.6 亿美元**、总债务约 **35.2 亿美元**、净现金约 **6.39 亿美元**。整体流动性不是主要风险，但可转债、稀释和 SBC 需要跟踪。

---

## 5. Management and Capital Allocation

### 管理层与文化

创始人 Matthew Prince 仍是 CEO，Cloudflare 的文化一直偏产品驱动、工程驱动、愿意快速扩展边界。长期看，这是创新能力来源；短期看，也容易导致产品线过多、叙事膨胀和销售执行复杂度提升。

### 2026 年重大管理动作：agentic AI-first operating model

2026-05-07，公司宣布进一步向 “agentic AI-first operating model” 转型，并计划减少当前员工约 **20%**，约 **1100 人**。预计产生 **1.40-1.50 亿美元**重组费用，其中现金支出约 **1.05-1.10 亿美元**，非现金 SBC 相关约 **3500-4000 万美元**。

这件事有两面：

- 正面：如果 AI 工具真正提升研发、销售、支持效率，Cloudflare 的 operating leverage 可能提前释放。
- 负面：一次裁掉 20% 员工不是小动作，说明管理层认为组织结构需要大幅调整；这会带来执行、中层管理、客户服务和文化冲击风险。

### 股本结构与治理

2026 年公司推进 Class C non-voting common stock 相关安排，并修订股权激励计划与 ESPP。这需要持续跟踪对控制权、投票权和股东稀释的影响。创始人控制力和长期主义可能是优势，但也降低外部股东对资本配置的约束。

---

## 6. Valuation Work

### 6.1 为什么主要用 EV/Sales？

NET 当前 GAAP 净利润仍为负，non-GAAP EPS 和 FCF 已转正但利润基数很小，P/E 和 P/FCF 对估值敏感度过高。更合适的方法是：

- 用 EV/Sales 衡量市场对长期增长和未来利润率的定价；
- 用情景估值假设 2028 年收入、退出 EV/Sales 倍数、稀释股数，再折现回今天；
- 同时观察 FCF margin 是否能持续上行。

### 6.2 当前估值

- 当前 EV：**943.8 亿美元**
- FY2026 revenue guidance 中点：**28.09 亿美元**
- 当前 EV / FY2026 sales：**33.6x**
- 当前 EV / TTM sales：**40.5x**

这意味着市场已经用接近“顶级 AI 软件基础设施平台”的标准给 NET 定价。

### 6.3 情景估值

输入假设：

- 当前价：268.83 美元
- FY2026 revenue：28.09 亿美元
- 当前 EV：943.8 亿美元
- 净现金：6.3934 亿美元
- 折现率：12%
- 估值年份：2028 年

| 情景 | FY26-28 收入 CAGR | 2028E 收入 | 退出 EV/Sales | 稀释股数 | 2028 隐含股价 | 折现回今天 | 相对现价 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bear | 20% | 40.4 亿美元 | 15x | 3.90 亿 | 157.2 | 125.3 | -53.4% |
| Base | 28% | 46.0 亿美元 | 22x | 3.85 亿 | 264.6 | 211.0 | -21.5% |
| Bull | 32% | 48.9 亿美元 | 30x | 3.80 亿 | 388.1 | 309.4 | +15.1% |
| Super bull | 34% | 50.4 亿美元 | 35x | 3.80 亿 | 466.2 | 371.7 | +38.3% |

### 6.4 估值解释

当前价 268.83 美元：

- 明显高于 base case 现值约 211 美元；
- 低于 bull case 现值约 309 美元；
- 需要公司持续证明 30%+ 增长、AI 平台化成功、FCF margin 扩张，并维持非常高的估值倍数。

换句话说，当前价格不是“便宜买好公司”，而是“为稀缺高质量成长资产付高价”。

### 6.5 实用价格区间

基于上述模型和当前市场数据：

- **强安全边际区**：约 **125-165 美元**  
  对应 bear/base 下沿和约 15-22x FY2026 sales。除非增长明显恶化，否则这个区间才真正有价值投资式安全边际。

- **合理观察 / 小仓试错区**：约 **165-215 美元**  
  接近 base case 折现价值。适合愿意承担高成长波动、但不想为完美未来付费的投资者研究。

- **成长股可接受但需强信仰区**：约 **215-250 美元**  
  需要相信 NET 维持高增长和高倍数，但仍有一定等待回报空间。

- **高预期区**：约 **250-310 美元**  
  当前 268.83 位于此区间。除非 bull case 概率很高，否则新增仓位风险回报不够舒服。

- **过热区**：**310 美元以上**  
  需要 super bull 假设支撑，任何增长、毛利率或 AI 叙事降温都可能触发大幅估值压缩。

---

## 7. Catalysts and Monitoring Plan

### 近中期催化剂

- 2026-07-30：预计公布下一次财报；
- Q2 是否能达到 revenue **6.64-6.65 亿美元**、non-GAAP operating income **9000-9100 万美元**；
- 裁员后 operating leverage 是否真的改善；
- DBNRR 是否继续高于 115%；
- 大客户数量是否继续快速增长；
- Workers / AI Gateway / R2 是否披露更强商业化数据。

### 必须跟踪的核心指标

1. Revenue growth：是否维持 30% 左右；
2. DBNRR：是否保持或超过 118%；
3. >$100k customers：是否继续高质量增长；
4. Gross margin：是否稳定在 70%+；
5. Non-GAAP operating margin：是否向 15%-20% 走；
6. FCF margin：是否稳定在 13%+ 并逐步提升；
7. SBC / revenue：是否从约 20% 下降；
8. AI / Workers / R2 的真实收入贡献；
9. 股本稀释和 Class C 结构后续影响。

---

## 8. Risk Register

### 主要风险

1. **估值压缩风险：高概率 / 高严重性**  
   当前估值需要非常高成长和高信心支撑。若收入增长从 30%+ 降到 20%-25%，EV/Sales 可能显著压缩。

2. **AI-first 重组执行风险：中概率 / 中高严重性**  
   裁员 20% 可能提升效率，也可能伤害组织执行、客户支持和销售产能。

3. **毛利率下行风险：中概率 / 中高严重性**  
   AI 推理、边缘计算、存储和网络投资可能拉低毛利率。

4. **竞争风险：中高概率 / 中严重性**  
   Microsoft、AWS、Google、Palo Alto、Zscaler、Akamai 等都有强资源。

5. **SBC 和稀释风险：高概率 / 中严重性**  
   Q1 SBC 接近收入 20%，若长期不下降，股东真实回报会被摊薄。

6. **产品线过宽风险：中概率 / 中严重性**  
   Cloudflare 想做网络、安全、开发者平台、AI 平台，范围很大。战略协同若不足，执行复杂度会拖累增长。

### Thesis invalidation signals

- Revenue growth 连续降至 25% 以下；
- DBNRR 低于 110%；
- 大客户增长明显放缓；
- FCF margin 无法提升或因 capex/AI 成本恶化；
- SBC / revenue 长期高于 15%-20%；
- AI/Workers 叙事没有转化为收入数据；
- 管理层继续大规模重组或销售组织执行恶化。

---

## 9. Four Investor-Style Decision Lenses

### Anti-bias note

- **Information richness rating**：A。NET 披露充分、覆盖广，但风险是市场叙事太强，容易把“平台愿景”误认为“已实现利润”。
- **Main research blind spot**：AI / Workers / R2 各产品线的独立收入、毛利率和客户留存披露不足。
- **Strongest reason smart investors may disagree**：Cloudflare 可能是未来 AI-native Internet 的关键基础设施节点，传统估值倍数低估其平台可选价值。

### Buffett-style lens

- **Conclusion**：Needs further observation
- **Key question**：这个业务 10 年后是否仍能以高回报率赚现金，而不是只保持高收入增长？
- **Evidence supporting thesis**：全球网络、客户粘性、DBNRR 118%、RPO 25.435 亿美元、大客户 4416 个。
- **Evidence against thesis**：GAAP 仍亏损，SBC 高，估值极高，当前 FCF yield 仅约 0.33%。
- **Decision implication**：适合研究和等待，不适合按 Buffett-style 安全边际重仓。
- **Follow-up question**：如果股市关闭五年，能否只靠收入留存、FCF margin 和客户增长证明持有舒服？目前答案是“还需要更多利润证据”。

### Munger-style lens

- **Conclusion**：Needs further observation
- **Key question**：如果三年后这笔投资错了，今天最明显的红旗是什么？

失败路径：

| 路径 | 机制 | 投资后果 |
|---|---|---|
| 增长降速 | 大客户 IT 支出放缓或竞争加强 | EV/Sales 从 30x+ 压到 15-20x |
| AI 叙事落空 | Workers/AI Gateway 收入不够大 | 市场重新按安全/CDN 软件公司估值 |
| 毛利率下降 | AI/edge/storage 成本高 | FCF margin 难扩张 |
| 裁员损伤执行 | 销售、支持、研发效率受影响 | 增长和客户满意度下降 |
| SBC 稀释 | 员工股权成本持续高 | 股东回报低于业务增长 |

- **Fragile assumptions**：AI 会成为最大顺风、平台协同显著、DBNRR 继续上行、市场长期给 30x sales。
- **Psychological trap**：把“伟大产品”和“伟大股票价格”混为一谈。
- **Major stupidity risk**：在 40x TTM sales 附近用传统“好公司长期会涨”逻辑重仓。
- **Follow-up question**：三年后如果错了，今天最明显的红旗可能就是“估值已经提前反映了完美未来”。

### Duan Yongping-style lens

- **Conclusion**：Suitable business, but price needs discipline
- **One-sentence business essence**：Cloudflare 帮企业和开发者把互联网应用变得更快、更安全、更容易部署。
- **User value**：客户付费是因为网络安全、性能、可靠性和开发效率是刚需。
- **Product strength**：免费层和开发者生态带来入口，企业安全和网络产品提升 ARPU。
- **People and culture**：创始人驱动、产品创新强；但 20% 裁员说明组织正在大改，需要观察文化影响。
- **Long-term certainty and right price**：业务方向正确，但当前价格太依赖长期高增长。
- **Follow-up question**：公司是在创造持久客户价值，还是主要享受 AI hype 和资本市场高倍数窗口？目前两者都有。

### Li Lu-style lens

- **Conclusion**：Worth deeper research, but margin of safety insufficient
- **Circle of competence**：公开数据能判断收入、客户、留存、现金流；较难判断各产品线真实单位经济和 AI 平台最终份额。
- **Industry trend**：互联网安全、边缘计算、AI agent、API 保护、全球低延迟计算都是长期趋势。
- **Value-chain position**：位于企业应用、互联网流量和开发者部署的入口层，是重要节点。
- **Downside protection**：现金充足、客户粘性强；但估值太高，价格层面的 downside protection 不足。
- **Margin of safety**：业务有质量，价格没有明显安全边际。
- **Follow-up question**：10-20 年后 Cloudflare 会是 AI-native Internet 的持久节点，还是本轮 AI 基建周期中的高估值受益者？这正是需要持续跟踪的核心问题。

### Four-lens composite score

| Dimension | Score |
|---|---:|
| Business model | 8.5/10 |
| Moat | 8.0/10 |
| Management | 7.5/10 |
| Financial quality | 6.5/10 |
| Valuation attractiveness | 3.0/10 |
| Long-term certainty | 7.0/10 |
| Downside risk control | 4.0/10 |

评分理由：

- Business model：统一全球网络平台很强，但产品线复杂。
- Moat：规模、网络、品牌、开发者入口和切换成本强，但 hyperscaler 竞争不可忽视。
- Management：创始人创新强，但 20% 裁员与 Class C/激励计划需要观察。
- Financial quality：FCF 转正且增长强，但 GAAP 亏损和 SBC 高。
- Valuation attractiveness：当前约 40.5x TTM sales，吸引力低。
- Long-term certainty：趋势强，但 AI/Workers 商业化仍未完全证明。
- Downside risk control：现金不错，价格安全边际不足。

### Integrated decision memo

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | 高质量平台公司 | 高 |
| Moat | 正在扩大的统一网络平台护城河 | 中高 |
| Management and capital allocation | 创新强，重组执行需观察 | 中 |
| Biggest risk | 估值压缩 | 高 |
| Long-term trend | 安全、边缘、AI、开发者平台趋势明确 | 中高 |
| Valuation and margin of safety | 当前无明显安全边际 | 高 |

### Action framing

| Investor state | Research implication |
|---|---|
| No position | 不追高，等待 215 美元以下再认真评估；165-215 美元更适合研究性建仓 |
| Existing position | 可继续持有但不宜让仓位过大；把它视为高 beta 高估值成长股 |
| Add / upgrade signal | 跌至 base case 附近，同时 DBNRR、RPO、大客户和 FCF margin 继续改善 |
| Reduce / downgrade signal | 300 美元以上且基本面未超预期，或增长降至 25% 以下 / DBNRR 低于 110% |

---

## 10. Final Research Framework

### 研究结论

Cloudflare 是值得长期深跟的稀缺平台公司，但当前不属于“安全边际充足”的买点。它的业务质量可以支持高估值，但当前价格已经要求投资者相信：

- 未来两年收入接近或超过 30% CAGR；
- AI/Workers/R2/Zero Trust 继续形成平台协同；
- FCF margin 持续上升；
- SBC 占收入下降；
- 市场长期给予 25-30x 以上远期 EV/Sales。

任何一个条件弱化，股价都可能大幅回撤。

### Practical view

- **当前 268.83 美元**：高预期区，不适合无脑买入。
- **215 美元以下**：开始更有研究价值。
- **165-215 美元**：合理观察 / 小仓试错区。
- **125-165 美元**：更接近强安全边际区。
- **310 美元以上**：需要 super bull 假设，不宜追高。

### What would make the thesis stronger

- Revenue growth 继续 30%+；
- DBNRR 高于 118% 或继续改善；
- 大客户增长继续强劲；
- FCF margin 向 15%-20% 提升；
- SBC / revenue 明显下降；
- AI/Workers/R2 披露更明确收入和客户 traction；
- 重组后销售效率和产品发布速度提升。

### What would change my view

- 升级为 Positive：股价回落至 165-215 美元区间，同时 Q2/Q3 证明 DBNRR、RPO、FCF margin 和 AI/Workers traction 改善。
- 下调为 Neutral：股价继续高于 300 美元但基本面只是符合预期，没有超预期增长和利润率改善。
- 下调为 Negative：收入增长跌破 25%、DBNRR 跌破 110%、毛利率继续下滑、SBC 不降、或 AI-first 重组影响销售/客户执行。

---

## 来源

- Cloudflare 2026Q1 Form 10-Q, filed 2026-05-08, SEC EDGAR, CIK 0001477333。
- Cloudflare 2026-05-07 Form 8-K Exhibit 99.1, “Cloudflare Announces First Quarter 2026 Financial Results”。
- Cloudflare 2026-05-07 Form 8-K, Item 2.05, agentic AI-first operating model and workforce reduction plan。
- Cloudflare 2026-06-30 / 2026-07-01 Form 8-K / 8-K/A, annual meeting, Class C split related proposals and equity plan amendments。
- Nasdaq quote API, NET price as of 2026-07-07 close。
- StockAnalysis / S&P Global Market Intelligence, NET statistics and forecast pages, accessed 2026-07-08。
