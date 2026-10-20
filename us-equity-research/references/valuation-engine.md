# P0 估值计算引擎：数值与口径契约

P1 增量模型使用独立 `valuation_p1.py` 和 `schema_version=2`，详见 [P1 多模型估值契约](valuation-p1.md)；P0 的 v1 格式和老报告不变。

本文件是 valuation.md 的执行细则。仅对新产出的、给出具体每股估值端点的研究报告生效；历史报告不自动改写。AI/研究者负责财务核验和构建有依据的经营假设，Python 引擎负责统一计算与拦截不一致的输入。**本工具不会联网验证来源、预测业务或证明倍数的合理性。**

## 使用

从仓库根目录：

~~~bash
python3 us-equity-research/valuation_engine.py research/COMPANIES/TICKER/research-records/YYYY-MM-DD-valuation-input.json --output research/COMPANIES/TICKER/research-records/YYYY-MM-DD-valuation-output.json
python3 -m unittest discover -s us-equity-research/tests -p 'test_valuation_engine.py' -v
~~~

完整结构参考 ../examples/valuation-input.example.json。示例中的 DEMO 证券和 example.com 是虚构的，**绝不是证券研究的数据来源**。运行只依赖 Python 标准库；校验失败打印 VALUATION BLOCKED 并以退出码 2 终止。失败时不得手算补上数字或悄悄放宽验证。

## 输入 JSON schema_version=1

- 根字段：schema_version=1, ticker, valuation_date(YYYY-MM-DD), currency=USD, price, cases，以及可选的 capital。
- 统一单位：收入、利润、现金、债务、其他索偿均为 **百万美元**；股数为 **百万股**；利润率/折现率用小数（20%=0.20）；倍数用 20 表示 20 倍。跨币种、ADR/ADS 换算、GAAP 与 Non-GAAP 差异必须在底稿中先处理。P0 当前拒绝 USD 以外币种。
- price 为当期有效市场报价，来源 basis 必须是 market，as_of 不晚于估值日，也不能早于估值日超过 7 个日历日。
- 每一个输入数值都是附有来源或明确假设的对象。例如：
~~~json
{
  "value": 22,
  "basis": "analyst",
  "as_of": "2026-10-20",
  "rationale": "基于可比企业历史前瞻倍数以及增长趋缓假设；该值是研究判断而非事实"
}
~~~
- basis 允许 filing / market / guidance / consensus / analyst。前四类必须附 source_url（https 原始申报、IR 或带时点的提供商页面）；analyst 必须附能解释为何选择该数值的具体 rationale，不能只写“合理”。所有 as_of 是**信息可获得日期**，不得晚于 valuation_date；目标年份单独填写 target_date。模型推导值也使用 analyst 并在理由里写明公式、锚定数据。
- cases 是非空数组，name 唯一，method 属于下列三种之一，target_date 晚于 valuation_date，interim_distributions 固定为 excluded。区间上下沿作为独立案例，例如 bear_low/bear_high；不能把不匹配的乐观利润率、股本、倍数拼成端点。
- 如果需要 enterprise_ebit，必须提供 capital：bridge_as_of 等于 valuation_date，shares_m、cash_m、debt_m、other_claims_m 全部附来源；股数必须为正，其余三项非负。cash_m 仅包括可归普通股的可用现金，不能含受限或客户现金；debt_m/other_claims_m 需互斥，少数权益和优先索偿不得重复扣减。
- capital 底层源日期早于估值日时，必须附 reconciliation_note，说明期后发行、融资、回购、现金消耗及哪些尚未核实。输出标记 capital_status=provisional；该结果只能称为**条件压力测试**，不能称经过完整调和的精确公允价值。

## 三种估值路径及公式

### equity_pe：盈利股权法

需要 revenue_m, net_margin, forecast_shares_m, exit_pe, cost_of_equity。

未来股权价值/股 = (目标年收入 × 归属普通股净利率 × 目标 P/E) / 目标年预测经济稀释股数；
今日每股条件现值 = 未来股权价值/股 ÷ (1 + cost_of_equity)^T。

**不能再机械加现金或扣债。**归属普通股净利润必须考虑持续 SBC、利息、税和少数股权等，避免把非经常性利润当持续收益。

### enterprise_ebit：今日企业价值桥接

需要 revenue_m, ebit_margin, exit_ev_ebit, wacc，以及 capital。

今日每股条件现值 = [(目标年收入 × 经营利润率 × EV/EBIT) ÷ (1+WACC)^T + 今日可用现金 − 今日有息债务 − 今日其他索偿] ÷ 今日经济股数。

**WACC 折现企业价值；不得用股权折现率；不得把未来股数配上今日索偿。** capital.bridge_as_of 必须等于估值日。此方法只折现未来 EV 代理，并不包含逐年中间现金流。

### equity_exit_ebit：未来股权桥接

需要 revenue_m, ebit_margin, exit_ev_ebit, terminal_net_cash_m, forecast_shares_m, cost_of_equity。

今日每股条件现值 = [(目标年 EBIT × EV/EBIT + 目标日净现金) ÷ 目标日预测经济稀释股数] ÷ (1+cost_of_equity)^T。

目标日净现金可为负数，必须是**同一目标日**的可信情景、已经考虑未来融资/现金使用；不能把今日募集款当作未来多余现金并加两次。目标日净现金、股数与收购/融资路径应一致。

对所有方法，T = (target_date - valuation_date).days / 365.25；报告要说明折现到今日而非未来未折现价格。盈亏为负不能套用正 EBIT 倍数或正 P/E，缺条件时明确写“无法可靠估值”。

## 强制限制和产物

**P0 不是逐年 FCFF/FCFE DCF。**它仍然基于未来退出倍数，没有逐年模拟资本开支、营运资金、资本融资与经营现金流，interim_distributions=excluded 表示期间分红等股东现金分配不纳入模型。企业价值法只是终值近似，未来股权法也只是条件性未来价折现。多模型交叉验证、逐年 DCF 属于下一步 P1。

每次深度研究的研究底稿须新增：
- YYYY-MM-DD-valuation-input.json：各案例每个数值/口径/来源/假设理由；
- YYYY-MM-DD-valuation-output.json：自动生成的价格、折现年限、价差、警告和完整输入快照。

报告只能引用输出文件中的 present_value_per_share_usd 与 upside_vs_reference；不得手改计算结果。研究者仍须**实际打开 source_url 检查内容**、核对估值倍数出处、现金债务合规性及稀释假设，做反向估值和敏感性分析。程序只验证格式和算式，**不能替代金融事实核验或经济合理性判断**。重要数据不可得时停止给出精确价，不以漂亮区间填空。
