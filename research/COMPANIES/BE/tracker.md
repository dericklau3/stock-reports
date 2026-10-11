# BE Research Tracker

Last updated: 2026-10-11

## Current Research View

- **投资观点：**中性、等待每股现金回报进一步验证。Q2强化了经营增长证据，但股价仍要求非常乐观的中期盈利路径，关键客户披露存在未调和冲突。

## Current Main Thesis

- **核心逻辑：**现场发电帮助数据中心缩短等待供电的时间，设备销售已放量并形成GAAP经营利润；价值最终取决于维护成本、项目融资和交付回款。

## Key Risks

- **主要风险：**高估值、客户与融资渠道集中、客户股权激励，以及项目许可和燃料基础设施限制可能同时压低每股回报。

## Latest Research

[2026-10-11完整深研](deep-research/2026-10-11-deep-research-update.md)；[可复算记录](research-records/2026-10-11-research.json)。

## 2026-10-11 新完整研究更新块（保留历史）

- 新报告：[2026-10-11](deep-research/2026-10-11-deep-research-update.md)；承接[2026-07-16](deep-research/2026-07-16-deep-research.md)。观点中性等待：增长证据增强，股票仍要求极乐观兑现；最强反方是销售增长未必转成稳态每股现金。
- Q2收入1065.365M、GAAP经营利润182.237M；全年收入3900–4200M、non-GAAP经营利润800–900M、EPS2.55–2.85。旧Q2财报催化已发生，不继续当未来日程。
- H1 OCF300.042M，现金capex77.823M，FCF222.219M；客户预收增加301.232M及SBC100.432M说明现金质量不能仅靠总额。
- 股价239.38→280.50美元（2026-10-09 regular close）；实际股数用7月22日294.527346M，Q2加权稀释323.331M单列。参考总市值82.615B，不声称quote-date精确股数已调和。
- Oracle权证已在5月1日净行权1.905433M股并获.248798M诱导股；不再重复加入3.531073M潜在股。客户对价资产306.5M将随交付减收入，不是可用现金。
- 原件实质冲突：Note1集中度Q2 44%/21%、H1单客户73%，Note11 Q2related仅2.818M；H1单客户在Q2max44%与Q1全部收入下上限67.155%，73%不能成立。251.6+72.3与总324.4M差0.5M；季度与半年权证冲减也未调和。必须保留限制，不输出“所有原始数一致”。
- 新估值为2028-12-31 GAAP EBIT/企业价值情景，14%和2.223年折现，熊27.96–40.11、基准88.99–132.10、牛202.76–288.72美元。基准收入6.5–7.5B、GAAP利润率20–22%仍偏进取；租金在成本，融资义务/少数权益独立处理。牛情景移除2.5B可转债同时加入12.8225M股，未来340M股含额外SBC；熊/基准保留本金不加全转换股。
- 下一验证：Q3正式日期未核实；Jupiter许可与管线、客户注释调和、对价摊销、维护保修、可转债结算。上调需客户披露一致、稳定回款、不依赖预收的FCF和每股改善；下调看指引下调、付款/许可延迟、成本压力、股数超模型。
- 全原件、来源日期、事实与假设、冲突及复算：`research-records/2026-10-11-research.json`、`calculate.py`、`validation.json`；原件同目录q2-release.pdf/.txt、q2-10q.pdf/.txt、fy2025-10k.pdf/.txt、oracle-jupiter.txt、brookfield-framework.txt、quote.txt。


## 历史追踪档案（此前版本原文保留，旧日期与估值不是当前判断）

# BE Research Tracker

- **Ticker**: BE
- **Company**: Bloom Energy Corporation
- **Exchange**: NYSE
- **CIK**: 0001664703
- **Sector / industry**: Industrials / Electrical Equipment & Parts; distributed energy generation; AI data-center power infrastructure
- **Last updated**: 2026-07-16
- **Latest memo**: [2026-07-16 deep research](deep-research/2026-07-16-deep-research.md)

## Current research stance

- **View**: Neutral / wait for confirmation（中性，等待验证）
- **Confidence**: B-
- **Core conclusion**: Business momentum is real, but current valuation prices in a bull-case path. At ~$239.38, BE trades around 18.9x EV / 2026 revenue guidance midpoint and ~117x 2026 non-GAAP EPS midpoint.
- **Best use of this memo**: Track Q2/Q3 2026 execution before deciding whether current valuation is justified.

## Key thesis

Bloom Energy is a highly leveraged beneficiary of AI data-center power scarcity. Its modular solid oxide fuel cell Energy Server can provide on-site power faster than many grid-upgrade paths, and Q1 2026 showed a clear revenue/profit inflection. However, the stock already reflects very high expectations, and public investors must underwrite execution, customer concentration, warrant/dilution, and supply-chain risks.

## Key numbers to monitor

| Metric | Latest disclosed |
|---|---:|
| Q1 2026 revenue | $751.1M |
| Q1 2026 product revenue | $653.3M |
| Q1 2026 GAAP gross margin | 30.0% |
| Q1 2026 non-GAAP gross margin | 31.5% |
| Q1 2026 GAAP operating income | $72.2M |
| Q1 2026 non-GAAP operating income | $129.7M |
| Q1 2026 adjusted EBITDA | $143.0M |
| Q1 2026 operating cash flow | $73.6M |
| 2026 revenue guidance | $3.4B-$3.8B |
| 2026 non-GAAP gross margin guidance | ~34% |
| 2026 non-GAAP operating income guidance | $600M-$750M |
| 2026 non-GAAP EPS guidance | $1.85-$2.25 |
| Cash + restricted cash at 2026-03-31 | ~$2.52B |
| Debt used in valuation at 2026-03-31 | ~$2.60B |
| Shares out / diluted avg shares | 284.44M / 319.71M |

## Price framework

| Zone | Price range | Meaning |
|---|---:|---|
| Strong margin of safety | $70-$100 | Bullish business can be bought without paying full AI multiple |
| Base-case research zone | $100-$160 | Reasonable if 2026 guidance remains intact |
| High-expectation zone | $160-$225 | Requires continuing execution and margin expansion |
| Expensive / no-chase zone | $225+ | Current area; requires bull-case continuation |

## Upcoming catalysts

- 2026-07-28 expected earnings date.
- Q2 2026 revenue and margin trajectory versus $3.4B-$3.8B FY guidance.
- Oracle/data-center deployment details and warrant accounting impact.
- Customer concentration and related-party revenue trend.
- Scandium oxide / critical materials supply-chain validation.
- Operating cash flow and capex conversion.

## Risks to track

1. Valuation compression from very high EV/Sales and P/E.
2. Customer concentration: Q1 2026 top two customers represented ~50% and ~12% of revenue; first is related party.
3. Oracle warrant / customer incentive economics and dilution.
4. Project timing delays from permitting, construction, interconnection and customer financing.
5. Scandium oxide / critical materials supply-chain controversy.
6. Competition from gas turbines, grid upgrades, batteries, nuclear/SMR and other distributed generation.
7. Policy, tax-credit and emissions/regulatory changes.

## Source checklist

- [x] SEC submissions and companyfacts for CIK 0001664703.
- [x] 2026 Q1 earnings release and investor presentation.
- [x] 2026 Q1 10-Q.
- [x] 2025 10-K.
- [x] 2026-07-09 8-K response to short-seller/scandium claims.
- [x] 2026 CEO performance award 8-K/8-KA.
- [x] StockAnalysis market data snapshot.

## Next update triggers

- Q2 2026 10-Q and earnings release filed.
- Any new Oracle or AI data-center contract disclosure.
- Any SEC or auditor/accounting issue related to revenue recognition.
- New short-seller report or company rebuttal on supply chain.
- Major change in share count, convertibles, warrants or capital raise.
