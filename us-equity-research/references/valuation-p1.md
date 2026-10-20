# P1 多模型估值：FCFF DCF、Forward P/E、SOTP

P1 是 P0 的增量工具，**不替换** `valuation_engine.py` 的 v1 输入契约和已有三种退出倍数法。P1 的计算程序 `us-equity-research/valuation_p1.py` 读取独立 `schema_version: 2` 的 JSON，复用 P0 的 `fact()` 来源/日期验证，不自动联网抓行情。不同方法使用**同一估值基准日和市价快照**，输出独立价格和分歧，不对方法结果取算术平均或以市场价校准假设。

## 命令（仓库根目录）

```bash
python3 us-equity-research/valuation_p1.py research/COMPANIES/TICKER/research-records/YYYY-MM-DD-valuation-p1-input.json --output research/COMPANIES/TICKER/research-records/YYYY-MM-DD-valuation-p1-output.json
python3 -m unittest discover -s us-equity-research/tests -p 'test_valuation_p1.py' -v
```

本目录 `examples/valuation-p1-input.example.json` 是 **DEMO 虚构数字**。所有货币与股份均用**百万美元/百万股**，比率输入为小数，股价及每股估值为美元。输入数值均为 P0 的 `{"value": ..., "basis": "filing|market|guidance|consensus|analyst", "as_of": "YYYY-MM-DD", "source_url": "https://..."}` 格式；研究假设用 `basis=analyst`、`rationale`，市场快照必须包含具有日期的可信来源。程序检查字段/数学/时间，不负责检查来源实际内容。

## 逐年企业现金流折现（fcff_dcf）

- 必须提供 **5–10 个连续年度** `years`；每期结束日 `end_date`，从研究日开始计算每个大约一年（300–430 天）内的**未来期间**。若最新财年还包含研究日前经营活动，先将历史已发生时段剔除，避免整年现金流被重复估入。
- 每年：`revenue_m`、`ebit_margin`、`cash_tax_rate`、`d_and_a_m`、`capex_m`、`delta_nwc_m`。`delta_nwc_m` 为运营营运资本增加（正数消耗现金，负数释放现金）；资本开支包含维护与增长性投资。SBC 已在 GAAP EBIT 计入，但稀释及未来员工奖励须单独核验。
- `FCFF = EBIT - max(EBIT,0)*cash_tax_rate + D&A - capex - ΔNWC`。负 EBIT 默认**不产生税收返还**，不擅自确认亏损结转所得税资产；税率须为适用现金税率，重要抵免/亏损结转应建立税务底稿再建模。
- `PV(enterprise) = Σ FCFF_t/(1+WACC)^t + TV_T/(1+WACC)^T`，其中终值可用 `perpetuity` 终值：`TV = FCFF_T*(1+g)/(WACC-g)`，或 `exit_ev_ebit`：`TV = EBIT_T * multiple`。
- P1 对企业价值**只在估值日**增加现金、扣除有息债务和其他普通股优先索偿，再除以**当日**经济股数；不存在将未来股份和当前资本桥接混算。`capital` 各字段的来源日期若早于研究日，必须记录 `reconciliation_note` 且结果标记 `provisional`。
- 结果包括每年 FCFF、显式期价值、终值及占比、WACC/终值假设 3×3 敏感性、当前价格隐含的终值增长率或退出 EBIT 倍数。终值占企业价值大于 75% 会自动提醒。无有效 Gordon 终值、权益剩余值非正或缺关键输入则计算失败。
- **现金流 DCF 不是自动的融资/稀释预测器**：若扭亏阶段需要增发、收购或发行优先股，必须做独立股数与资金来源桥接；若无法验证，报告不得宣称输出是准确每股公允价值。

## 当前 Forward P/E 及历史样本（forward_pe）

- 保留 `eps` 与 `basis`（GAAP/adjusted）、`horizon`（NTM/FY1/FY2）、`period_start/period_end`。EPS > 0；研究公司 EPS 预测来源时间不可晚于市价日，须在市价日前 7 日内。
- 同行 `peers` 至少 2 家，分别提供同一 EPS 口径、同一 horizon、近似预测覆盖期、匹配的**当时**股价和 EPS 来源日期、可比理由。拒绝调整后 EPS 与 GAAP EPS 硬比。同行中位数只输出**当前交易倍数参照**及 `peer_implied_price_usd`，**不是独立内在价值**，绝不作为权重平均的价格目标。
- 历史 `history` 可选：每个时点必须保留**彼时可获得**的 EPS 预测和当时股价，不能以今日 EPS 倒推过去 Forward P/E。仅标记 `sample_extrema_not_full_year`，不能伪装为完整一年日频最高/最低。

## 分部估值（sotp）与适用公司

- SOTP 至少拆分两个**不重叠**的独立经营分部，每个分部有边界描述 `boundary_note`、公司经济持有比例 `ownership`；总体必须有 `overlap_reconciliation` 解释内部交易抵销、子公司少数股权、资本开支和融资不会重复计入。
- 每个 segment 的 `kind` 可以是：`current_ev`（当期独立企业价值）、`exit_ebit`（未来 EBIT 和退出倍数按 WACC 折现）、`fcff_dcf`（使用上述逐年企业 FCFF DCF）、`milestone_ev`（成功概率 × 成功企业价值 + 失败概率 × 失败企业价值，并按 WACC 折现；概率明确作为研究假设，不暗示已得到客观统计认证）。
- 统一总桥接：`sum(分部持有比例×分部今日EV) - 未分配总部费用PV + 非经营资产 + 可用现金 - 有息债务 - 其他优先索偿`，最后除以**研究日**经济股数。非经营资产**不得**重复包含在分部 EV 或账面现金内；如果少数股权未通过 ownership 调整，则需在 claims 中处理，不能两次扣减。
- **INTC：**可按 Client、Data Center、Foundry 等经营边界拆分；内部代工收入须抵销，Foundry 不能同时当作独立对外代工全部收入和集团 CPU 利润，巨额未来资本投入不可从 EBIT 终值中消失。**RKLB：**可按 Electron/HASTE、Space Systems、Neutron/其他增量项目拆分；Neutron 成功/失败需考虑融资与技术里程碑，拟收购 Iridium 在未交割前不得默认为全资并表，也不能叠加未扣股权对价的全部 EV。

## 多模型交叉验证、不能机械平均

- 对同一 `scenario`（bear/base/bull）的 DCF 与 SOTP 输出比较，差距超过 30% 标记 `material_disagreement`，不自动纠偏、取中值、赋予主观概率或自动推荐买卖。P/E 仅为可比市场锚点，不能和 DCF 的内在价值混称同一种价格。
- 解释差异：分部边界、需求/利润、CapEx、WACC、终值占比、融资/股本、计算期及 NAV；明显无法调和时仅输出条件情景，降低证据可信度，不给明确安全边际。
- 行业不适用某模型时**说明原因并跳过**，不为形式美观硬塞三组价格。银行保险主要看账面净资产/ROE；尚无可验证现金流的科研项目不能凭精确概率生造 DCF。

## 保存约定

每次研究若使用 P1，额外保存 `YYYY-MM-DD-valuation-p1-input.json` 与 `YYYY-MM-DD-valuation-p1-output.json` 于公司 `research-records/`；底稿说明正式结论采用的主方法、参照方法、不一致原因以及未来未建模资金/稀释条件。历史 P0 研究报告不回填新结果。报告第六节仍遵守 `report-templates.md` 的**一张两列表 + 简要方法说明与总结**，不新增宽表；完整参数留底稿。

## P2 衔接

P1 计算生成的完整 v2 输入可用 [P2 冻结与历史复盘工具](valuation-p2.md)逐项冻结，避免后来重新研究时以新预测覆盖旧假设。仅同一估值模型/情景/目标期才做数值归因；Forward P/E 市场基准不能作为独立内在价格冻结。
