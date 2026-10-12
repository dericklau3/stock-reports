# Vistra（VST）Tracker

Last updated: 2026-10-11

## Current Research View

**投资观点：**建设性但需观察：现有资产赚钱且长约能见度提高，但现价处于基础情景上半区，安全边际不足以忽视杠杆和新增资本。

## Current Main Thesis

**核心逻辑：**竞争性电厂与零售平台把电价、容量与客户负荷转为收入；Meta/AWS长约及Cogentrix可改善未来现金，但不是AI需求总量直接归普通股。

## Key Risks

**主要风险：**价格曲线转弱、项目延期和增长支出同时发生时，经营收益改善可能抵不过债务、优先股及稀释；资金承诺先于新增现金回报。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)；[真实运行的验收结果](research-records/2026-10-11-validation.json)。

## 2026-10-11 新增深研更新块（保留旧文）

- 旧基线：tracker及2026-10-10完整更新；条件EV76.759B、现价161.48与基础132–172现值。
- 当前观点：建设性但需观察：现有资产赚钱且长约能见度提高，但现价处于基础情景上半区，安全边际不足以忽视杠杆和新增资本。
- 报价桥：{"price": 161.48, "date": "2026-10-09", "session": "regular-close", "currency": "USD", "url": "https://api.nasdaq.com/api/quote/VST/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09", "status": "verified", "timezone": "America/New_York", "time_basis": "交易所常规交易收盘；纽约时区"}

### 旧假设 → 新事实 → 当前判断
- 2026-10-10基线→10/11：报价仍为10/09的161.48，最新IR索引没有新证实经营事件，不制造新进展。
- 最新完整财务仍Q2，Q3已官方安排11/06；历史表从原件重读而非把昨日中文原文当SEC证据。
- 沿用完整债务+优先+NCI条件桥，旧8月遗漏优先索偿的估值继续失效。
- 同一2027末熊/基础/牛成套输入重新按10/11时点折现，只有一天期限差，不能称盈利预测上调。

### 可复算估值与资本结构

```json
{
  "valuation": {
    "method": "conditional EV/ongoingEBITDA with net-claims and dilution; notDCF",
    "status": "conditional_scenarios_not_realtime_EV",
    "target_year": 2027,
    "target_date": "2027-12-31",
    "discount_years": 1.2210814510609171,
    "discount_rate": 0.12,
    "interim_dividend_assumed": 1.2,
    "current_forward_PE": "未取得可靠当前共识",
    "historical_forward_PE": "未取得当时有效预测完整序列",
    "scenarios": {
      "Bear": [
        {
          "EBITDA_billion": 6.5,
          "EV_multiple": 7,
          "net_claims_billion": 26,
          "shares_million": 350,
          "future_price": 55.714285714285715,
          "present_value": 49.558947574476036
        },
        {
          "EBITDA_billion": 7,
          "EV_multiple": 8,
          "net_claims_billion": 25,
          "shares_million": 345,
          "future_price": 89.85507246376811,
          "present_value": 79.28753749586848
        }
      ],
      "Base": [
        {
          "EBITDA_billion": 8.1,
          "EV_multiple": 9.5,
          "net_claims_billion": 25,
          "shares_million": 345,
          "future_price": 150.57971014492753,
          "present_value": 132.16440483331178
        },
        {
          "EBITDA_billion": 8.5,
          "EV_multiple": 10.5,
          "net_claims_billion": 23,
          "shares_million": 338,
          "future_price": 196.0059171597633,
          "present_value": 171.71993968192822
        }
      ],
      "Bull": [
        {
          "EBITDA_billion": 9,
          "EV_multiple": 11,
          "net_claims_billion": 23,
          "shares_million": 335,
          "future_price": 226.86567164179104,
          "present_value": 198.59152271845457
        },
        {
          "EBITDA_billion": 9.5,
          "EV_multiple": 12,
          "net_claims_billion": 21,
          "shares_million": 330,
          "future_price": 281.8181818181818,
          "present_value": 246.44222552072185
        }
      ]
    },
    "capital_policy": "ordinary claim residual after future total claims; todaybridge excludes restrictedcash and NDT; noaddingDOEloan or equityNCIbuyoutdoublecount; lease splitpending; future netclaims reserves are assumptions notexact reconciliation",
    "claims_components_million": {
      "book_debt": 20508,
      "cash": 435,
      "preferred_liquidation": 2476.066,
      "remaining_NCI_proxy": 12
    },
    "calculations": [
      {
        "name": "Bear0future",
        "expression": "(6.5*7-26)*1000/350",
        "result": 55.714285714285715
      },
      {
        "name": "Bear0PV",
        "expression": "(((6.5*7-26)*1000/350)+1.2)/(1.12**1.2210814510609171)",
        "result": 49.558947574476036
      },
      {
        "name": "Bear1future",
        "expression": "(7*8-25)*1000/345",
        "result": 89.85507246376811
      },
      {
        "name": "Bear1PV",
        "expression": "(((7*8-25)*1000/345)+1.2)/(1.12**1.2210814510609171)",
        "result": 79.28753749586848
      },
      {
        "name": "Base0future",
        "expression": "(8.1*9.5-25)*1000/345",
        "result": 150.57971014492753
      },
      {
        "name": "Base0PV",
        "expression": "(((8.1*9.5-25)*1000/345)+1.2)/(1.12**1.2210814510609171)",
        "result": 132.16440483331178
      },
      {
        "name": "Base1future",
        "expression": "(8.5*10.5-23)*1000/338",
        "result": 196.0059171597633
      },
      {
        "name": "Base1PV",
        "expression": "(((8.5*10.5-23)*1000/338)+1.2)/(1.12**1.2210814510609171)",
        "result": 171.71993968192822
      },
      {
        "name": "Bull0future",
        "expression": "(9*11-23)*1000/335",
        "result": 226.86567164179104
      },
      {
        "name": "Bull0PV",
        "expression": "(((9*11-23)*1000/335)+1.2)/(1.12**1.2210814510609171)",
        "result": 198.59152271845457
      },
      {
        "name": "Bull1future",
        "expression": "(9.5*12-21)*1000/330",
        "result": 281.8181818181818
      },
      {
        "name": "Bull1PV",
        "expression": "(((9.5*12-21)*1000/330)+1.2)/(1.12**1.2210814510609171)",
        "result": 246.44222552072185
      },
      {
        "name": "days",
        "expression": "(446)/365.25",
        "result": 1.2210814510609171
      },
      {
        "name": "marketcapB",
        "expression": "161.48*335.635195/1000",
        "result": 54.1983712886
      },
      {
        "name": "netdebtM",
        "expression": "1876+17719+300+613-435",
        "result": 20073
      },
      {
        "name": "netclaimsM",
        "expression": "20508-435+2476.066+12",
        "result": 22561.066
      },
      {
        "name": "conditionalEVB",
        "expression": "161.48*335.635195/1000+(20508-435+2476.066+12)/1000",
        "result": 76.7594372886
      },
      {
        "name": "EV2026mid",
        "expression": "(161.48*335.635195/1000+22.561066)/7.2",
        "result": 10.661032956749999
      },
      {
        "name": "H1FCF",
        "expression": "2222-1572",
        "result": 650
      },
      {
        "name": "TTMrevenue",
        "expression": "17738+9657-8183",
        "result": 19212
      },
      {
        "name": "TTMop",
        "expression": "1906+2052-395",
        "result": 3563
      },
      {
        "name": "TTMCFO",
        "expression": "4070+2222-1171",
        "result": 5121
      },
      {
        "name": "TTMcapex",
        "expression": "2752+1572-1458",
        "result": 2866
      },
      {
        "name": "TTMNI",
        "expression": "944+1334-59",
        "result": 2219
      },
      {
        "name": "TTMcommonNI",
        "expression": "752+1238-(-37)",
        "result": 2027
      },
      {
        "name": "TTMFCF",
        "expression": "5121-2866",
        "result": 2255
      },
      {
        "name": "FY24FCF",
        "expression": "4563-2078",
        "result": 2485
      },
      {
        "name": "FY25FCF",
        "expression": "4070-2752",
        "result": 1318
      },
      {
        "name": "juniorcouponM",
        "expression": "850*.07+650*.0725",
        "result": 106.625
      },
      {
        "name": "growth-adjusted-midpoint",
        "expression": "(3925+4725)/2-1700",
        "result": 2625.0
      }
    ],
    "sensitivity": "净索偿每增加1B在340M股分母降低未来值约2.94美元；基本情景为研究假设非2027指引。",
    "interpretation": "可复算的研究条件情景，不是已证实预测或精确NAV/DCF；最新股本或其他缺口见gaps。"
  },
  "capital_structure": {
    "cash_M_20260630": 435,
    "restricted_M": 46,
    "book_debt_including_projects_AR_forward_M": 20508,
    "forward_repurchase_M": 613,
    "preferred_M": 2476.066,
    "NCI_book_proxy_M": 12,
    "actual_shares_M_20260803": 335.635195,
    "Q2weighted_diluted_M": 339.230976,
    "postJune_financing_principal_M": 1500,
    "postJune_notes_cash": "净费/使用未全面刷新；不得只加1500债",
    "Sep_notes_coupon_percent": [
      7,
      7.25
    ],
    "preferred_A_reset": "2026-10-15",
    "preferred_B_reset": "2026-12-15",
    "preferred_redemption": "计划而非已确认",
    "SBC_H1_M": 67,
    "SBC_FY25_M": 113,
    "Cogentrix_equity_M": 5,
    "Cogentrix_cash_B": 2.3,
    "Cogentrix_debt_assumed_B": 1.5,
    "finance_lease_ROU_net_M": 152,
    "lease_liability": "Q2完整分拆未独立核实；非零假设，条件EV非完整实时EV",
    "convertible": "无在本次关键原件定位的可转融资，不据此宣称零",
    "Helix_commitment_B": [
      0.5,
      0.5
    ],
    "netclaims_2027_scenarios_B": [
      21,
      26
    ],
    "NDT": "受限用途不减普通EV"
  }
}
```

### 改判条件与最强反证
加强：2027正式指引达到基础锚且交割/供电与每股现金增厚、去杠杆同时成立；弱化：指引下调，资本/Helix调用增多、重大停机或净索偿增加。最强反证：资产稀缺、Meta客户确认与DOE融资路径可能让长约溢价更持续；但42亿条件贷款不是普通股净资产增加。

### 决定性局限
- 10月实时actual股份、现金使用/债务与优先股赎回未完整闭合；条件EV不是实时EV
- 完整租赁负债分拆及9/14最终424B2未补齐，模型是有边界条件情景而非完整即时索偿
- PPA价格/净利润及2027正式指引未披露，当前/一年历史Forward P/E未取得
- IR新闻索引未出现新实质进展不证明绝对没有其他重大事件；并购交割未核实
- Q2电话会第三方转录并非完整官方音频独立核验；同源公告转载不当独立证据

新报告拟存：`deep-research/2026-10-11-deep-research.md`；原历史文链接保留。研究未发布；父代理负责原件复核、合并和线上验收。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# Vistra（VST）Tracker

- **Ticker / Exchange**：VST / NYSE普通股；美元。
- **Last updated**: 2026-10-10
- **Current research view**：Constructive but watchful（建设性但需观察）；现价没有厚安全边际，不因AI供电题材追高。
- **Confidence**：中等；已披露财务/合同阶段较清楚，2027最终贡献与未来净索取权仍需验证。
- **Time horizon**：12–24个月。
- **Latest memo**：[2026-10-10深度更新](https://github.com/dericklau3/stock-reports/blob/7c05fd1d8c3401e619e0441e49c48edc1fa8bac0/research/COMPANIES/VST/deep-research/2026-10-10-deep-research-update.md)。
- **Prior memo**：[2026-08-19](https://github.com/dericklau3/stock-reports/blob/7c05fd1d8c3401e619e0441e49c48edc1fa8bac0/research/COMPANIES/VST/deep-research/2026-08-19-deep-research-update.md)；[2026-06-10](https://github.com/dericklau3/stock-reports/blob/7c05fd1d8c3401e619e0441e49c48edc1fa8bac0/research/COMPANIES/VST/deep-research/2026-06-10-deep-research.md)。
- **Latest earnings memo**：[2026Q2](https://github.com/dericklau3/stock-reports/blob/7c05fd1d8c3401e619e0441e49c48edc1fa8bac0/research/COMPANIES/VST/earnings-tracking/2026-Q2-earnings-tracking.md)。

## Current Research View

**建设性但需观察；中等置信度。当前价格缺乏厚安全边际，不因AI供电题材追高。**

## Current Main Thesis

现有发电、零售与对冲组合已经盈利；Meta/AWS合同、Cogentrix和核电增容提高潜在收入能见度。但必须扣增长资本、债务/优先股索取权及新股，才能判断普通股回报。Q2 ongoing EBITDA $1.767B、2026指引$6.8–7.6B；FCFbG $3.925–4.725B是增长前调整口径，不能当全部可分配现金。[1][2]

10/9常规交易收盘**$161.48**，较旧8/18 $140.52上涨14.9%。当前位于Base现值上半区；继续观察已有持仓，不因股价上涨自动加仓。[21]

## Latest Update and Financial Basis

- 最新完整财务仍为Q2，截至2026-06-30；release 8/7、10-Q提交8/10。Q3计划2026-11-06上午10点美东公布，尚未发生。[1][3][20]
- 6/30现金$435M、受限现金$46M；账面债务式合计$20.508B，含项目融资、应收融资与$613M递延回购义务；保守净债务$20.073B。优先股约$2.476B、剩余NCI账面代理$12M。[6]
- 8/3actual普通股335.635195M；Q2稀释加权339.230976M，不能当10/10实时股数。[6]
- H1 OCF $2.222B−现金capex含核燃料/LTSA $1.572B=$650M简易FCF；回购+普通/优先股分配$959M。季节性偏H2，勿年化或只看EBITDA。[6]
- 2026增长资本计划$1.7B含Helix初始$500M；FCFbG中值减该增长桶示意$2.625B，仍不是最终普通股可分配现金。[2]
- 9/24已完成$1.5B次级债，7%/7.25%，初始年票息$106.625M；拟用于一般用途和潜在优先股赎回。不能把计划写成赎回完成，或只加债不加融资现金。[7][8]
- 10/5 8-K：9/30商品循环额度延期至2027-09-29，不是新额度现金全额到账，也不是Cogentrix交割。[9]

## Operating Agenda / Execution Progress

| 稳定事项 | 最新已证实阶段 / 证据日期 | 原目标→最新时间表 | 下一关 / 瓶颈 | 自上次变化与股东意义 |
|---|---|---|---|---|
| FLEET：可靠运行/对冲 | Q2盈利，Martin Lake 2月复役；8/3对冲2026/27/28约100%/94%/72%。[1][6] | 持续运营 | 11/6核验夏季现金与指引，停机/负荷风险 | 已兑现利润，不把对冲当万能保险 |
| COGENTRIX：5.5GW收购 | 8月FERC批准、最新公司材料待交割。[6] | 原mid-to-late2026→late2026 | 交割原件、最终现金/承债/新股、整合利润 | 未找到完成公告，不代表停工；5M股与约$3.8B现金+承债须同步建模 |
| META-EXISTING：既有核电合同 | 20年、2,176MW现有容量，客户确认。[6][11][12] | late2026起供→YE2027完整既有部分 | 实际供电、合同溢价净利润 | 合同不是全量新增收入 |
| META-UPRATE：433MW增容 | 10/5 DOE最高$4.2B条件贷款；NRC9/8预计申请表。[10][15] | 2031起增容交付→2034完整；申请2029–2032 | 最终融资、许可、工程和投入 | 新融资路径是进展，非补贴/已到账，不提前塞入2027利润 |
| AWS：Comanche Peak | 20年、1,200MW合同。[6] | Q4 2027起供→2032完整 | 并网分类、实际供电和净贡献 | 无最新完整电网原件，不把旧预计进度升级为当前已获批 |
| HELIX：渠道与基金投资 | 6月平台成立；初始$500M可call、另$500M条件或公司自主选择。[6][14] | 初始贡献假设2026；项目回报时间未披露 | capital call、客户PPA与VST回报份额 | 超过$10B平台资本不是VST收入；防任务漂移 |
| PERMIAN：860MW燃气 | 在建，6月TxEF贷款$583M，6/30已提$172M、3%。[6] | Q2 2028上线目标 | 施工、燃机、调试、可靠投产 | 融资与建设不是利润兑现 |
| OAK-HILL / DISPOSALS：组合调整 | Q2称Oak Hill 2开工；三气厂出售协议/待售。[2][6] | 出售目标H2 2026；当前完成未核验 | 出售回款、项目交付及现金回报 | 无新披露≠无进展，资本释放不当经常收入 |

## Dated Assumption / Valuation Changes

### 2026-10-10：完整资本桥与统一折现

1. **价格**：$140.52（8/18）→$161.48（10/9），+14.9%；公司2026正式指引仍维持。[1][21]
2. **旧EV纠错**：$67.236B旧桥漏优先股与剩余NCI。保持旧时点输入，完整桥约$69.724B；遗漏约$7.41/股。旧未折现情景/价格区不继续当当前买点。
3. **2027经营锚**：原$7.4–7.8B是机会区间，不是正式指引。CFO在Q2 Q&A称趋下沿；Cogentrix+Meta约$700M增量有交割/对冲/曲线条件。Base $8.1–8.5B为研究假设，不机械上沿加增量。[2][18]
4. **新融资**：9/24债与现金同步，10/5循环延期与DOE条件贷款分开，均不虚构实时现金或完成交割。[8][9][10]

### Current Conditional Valuation

市场值使用10/9价格与8/3actual股数，条件市值约$54.198B；6/30净债务+优先股+NCI净索取权约$22.561B，条件EV约$76.759B，对2026 EBITDA中值$7.2B约10.66x。不是实时EV；9月融资和后续经营/赎回尚未完整刷新资本表。[6][21]

统一YE2027：`未来价=(EBITDA×倍数−净索取权)×1000/股数M`；`今日现值=(未来价+假设期间股息1.20)/(1.12^1.223819)`。全部端点为分析师假设。

| 情景 | EBITDA B | EV倍数 | YE2027净索取权B | YE2027股数M | YE2027价格 | 今日现值 | 对161.48现值差 |
|---|---|---|---|---|---|---|---|
| Bear成套端点 | 6.5 / 7.0 | 7 / 8 | 26 / 25 | 350 / 345 | 55.7–89.9 | 49.5–79.3 | −69.3%至−50.9% |
| Base成套端点 | 8.1 / 8.5 | 9.5 / 10.5 | 25 / 23 | 345 / 338 | 150.6–196.0 | 132.1–171.7 | −18.2%至+6.3% |
| Bull成套端点 | 9.0 / 9.5 | 11 / 12 | 23 / 21 | 335 / 330 | 226.9–281.8 | 198.5–246.4 | +22.9%至+52.6% |

Base需Cogentrix交割、Meta既有部分兑现和资本受控；Bull要更好曲线、合同与去杠杆，不靠433MW核电或AWS全量在2027提前兑现。当前Forward P/E和1年历史高低区间未得可靠新数据，旧13.73x不得冒充当前；不用历史价÷今日EPS造历史倍数。

**实用价格区**：$105–110约对应Base低端20%折价；$110–120条件分批研究区；$120–132有限折价；$132–172 Base区；>$172需更强证明，>$199进入Bull定价。严重Bear仍可能大幅下行，低价不自动构成买点。

## Core Assumptions

必须继续成立：2026指引兑现；Cogentrix和Meta提高每股现金而非仅EBITDA；增长资本、净索取权与回购有纪律；机组可靠；长期合同履约与并网可行。[1][6]

## Key Risks

风险包括曲线/容量周期、2028较低对冲覆盖、核电停机、保证金call、优先股reset/赎回、Helix资金call/任务漂移、Moss Landing/环境退役现金负担。ongoing排除项目不等于普通股免付。[2][6][18]

## Red Lines / What Would Change the View

- EBITDA/FCFbG正式指引下调、2027并购/合同新增仅抵消原业务恶化。
- Cogentrix/Meta/AWS明确延迟而资本仍加速投入；贷款/合同发布长期未能转为现金。
- Helix扩大投入或放松回报门槛，无法说明VST利益与额外$500M调用理由。
- 高价回购挤压流动性、合并净索取权长期升高或重大停机/评级/安全事件。
- 上调条件：2027正式指引达到/超越Base经营锚，合同实际供电、Cogentrix每股现金增厚与去杠杆同时有证据；或者基本面不坏但价格提供更厚折价。

## Next Monitoring Gates

1. **2026-11-06 Q3**：夏季结果、2026现金/指引、2027更新与交易纳入方式。[3]
2. **late2026 Cogentrix**：最终交割与资本结构；不要拿FERC批准替代交割。[6]
3. **10/15、12/15 preferred节点**：真实赎回/重置、现金与债务同步。[6][7]
4. **Meta late2026起供**、**AWS Q4 2027**、**Permian Q2 2028**，保留原时钟。[6]
5. DOE最终贷款、NRC申请/批准分别核验；Helix实际客户合同、投入和收益。[6][10][15]

## Verification Limits / Portfolio Discipline

未核验10/10实时现金、actual股数、提款、完整新forward预期、PPA项目利润率及近期完整电网规则/项目分类。最终9/14 424B2全文未取得；最终本金/票息/发行完成由正式定价和8-K核验。已读取可见第三方Q&A，未逐段核验官方音频。[7][8][18]

VST不作为低波动现金替代品。新增配置须维持用户现金+低波动/核心≥30%、同类≤15%，并核验周线条件；未刷新组合，不宣称具体仓位已符合或违反规则。本次无交易执行。

## Sources

[1] https://investor.vistracorp.com/2026-08-07-Vistra-Reports-Second-Quarter-2026-Results — q2-release
[2] https://filecache.investorroom.com/mr5ir_vistracorp_ir/347/Q2_2026_Results_Presentation_vFinal.pdf — q2-slides
[3] https://investor.vistracorp.com/2026-09-29-Vistra-to-Report-Third-Quarter-Results-on-Nov-6,-2026 — q3-date
[6] https://investor.vistracorp.com/image/VST_10-Q_2026-08-10.pdf — Q2 2026 10-Q：公司PDF，期间截至6月30日
[7] https://investor.vistracorp.com/2026-09-10-Vistra-Prices-Registered-Offering-of-1-5-Billion-of-Junior-Subordinated-Notes — 2026-09-10 Junior Notes pricing
[8] https://www.sec.gov/Archives/edgar/data/1692819/000114036126037577/ef20082680_8k.htm — 2026-09-24 8-K：notes完成发行；IR链接QuoteMedia镜像
[9] https://www.sec.gov/Archives/edgar/data/1692819/000114036126038468/ef20083016_8k.htm — 2026-10-05 8-K：commodity-linked revolving facility延期；IR链接QuoteMedia镜像
[10] https://www.energy.gov/articles/energy-department-announces-42-billion-investment-boost-nuclear-power-and-help-lower — DOE 2026-10-05：最高$4.2B有条件贷款承诺
[11] https://investor.vistracorp.com/2026-01-09-Vistra-and-Meta-Announce-Agreements-to-Support-Nuclear-Plants-in-PJM-and-Add-New-Nuclear-Generation-to-the-Grid — Meta PPAs 2026-01-09
[12] https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/amp — Meta客户确认：既有核电与uprate
[14] https://www.helixdi.com/news-insights/kkr-launches-helix-digital-infrastructure-to-finance-and-deliver-the-next-generation-of-ai-infrastructure — Helix平台2026-06-11成立公告
[15] https://www.nrc.gov/facilities-safety/operating-reactors/operating-reactor-licensing/power-uprates/status-of-power-uprate-applications/expected-applications-for-power-uprates — NRC 2026-09-08预计uprate申请时间表
[18] https://www.fool.com/earnings/call-transcripts/2026/08/14/vistra-vst-q2-2026-earnings-call-transcript — 2026-08-07 Q2电话会第三方转录：可见Q&A，非完整音频核验
[20] https://data.sec.gov/submissions/CIK0001692819.json — SEC submissions CIK0001692819
[21] https://api.nasdaq.com/api/quote/VST/historical?assetclass=stocks&limit=5&fromdate=2026-10-08&todate=2026-10-09 — Nasdaq历史行情：10/9已完成常规交易收盘
