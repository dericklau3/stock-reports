# 美股投研 Skill

## 用途

这个 skill 用于帮助 Codex 对你已经选定的美股上市公司做深度投研和财报后追踪。

默认逻辑是：只要输入股票代码或公司名，就做深度个股研究；如果问题提到财报、季报、指引、10-Q、股东信或业绩电话会，就做财报后追踪。其他形式的问题也应归入这两种模式之一。

## 调用示例

```text
Analyze LMND
Do a deep analysis of NVDA
Analyze TEM's latest earnings
Track PLTR after earnings
分析 LMND
深度分析 NVDA
分析 TEM 最新财报
追踪 PLTR 财报后的变化
```

## 支持模式

- 深度个股研究：所有股票代码或公司名默认使用。
- 财报后追踪：用户提到 earnings、财报、季报、guidance、10-Q、股东信、投资者演示文稿、业绩电话会时使用。

## 输出要求

- 先给研究观点。
- 使用最新且可引用的来源，不编造财务数据或估值假设。
- 区分事实、假设、估算和观点。
- 必须包含风险、反证理由和 thesis 失效条件。
- 估值方法要匹配公司类型。
- 当估值是关键判断依据时，使用 bear / base / bull 三档情景。
- 关键数据不足时，使用 `Insufficient evidence`，不要强行给方向性观点。
- 核心输出开头固定包含五行摘要：Research view、Confidence、Time horizon、Main thesis、Key risk。
- 输出语言匹配用户语言：中文提问用中文，英文提问用英文。

## thesis 是什么意思

`thesis` 在这里可以理解为“投资逻辑”或“研究判断”。

例如：

- 为什么这家公司值得长期跟踪？
- 它未来增长主要靠什么？
- 市场可能低估了什么？
- 什么数据能证明这个判断是对的？
- 什么情况发生时，说明原来的判断错了？

所以 `thesis 失效` 的意思就是：原本支持这家公司投资逻辑的关键假设被证伪了。

## 研究结果怎么保存和查看

建议每家公司单独一个目录，把深度研究、财报追踪和当前状态分开保存：

```text
research/
└── COMPANIES/
    └── LMND/
        ├── deep-research/
        │   ├── 2026-05-12-deep-research.md
        │   └── 2026-11-20-deep-research-v2.md
        ├── earnings-tracking/
        │   ├── 2026-Q2-earnings-tracking.md
        │   └── 2026-Q3-earnings-tracking.md
        └── tracker.md
```

### deep-research/

保存“完整深度研究底稿”，相当于某个时间点的完整投资逻辑快照。

一般不要频繁修改旧文件。公司逻辑发生大变化、需要重做一版完整研究时，再新增一篇，例如 `2026-11-20-deep-research-v2.md`。

### earnings-tracking/

每次财报后新增一篇追踪记录，用来回答：

- 本季度发生了什么？
- 指引有没有变化？
- 财务质量变好还是变差？
- 哪些假设被验证？
- 哪些假设被削弱？

### tracker.md

这是日常最该看的文件，记录这家公司当前最新状态。

建议 `tracker.md` 持续维护：

- 当前 Research view
- 当前 Main thesis
- 关键风险
- 最新财报后的变化
- 下次要重点跟踪的数据
- 什么情况会改变观点

## 更新规则

- 小变化：只更新 `tracker.md`。
- 财报变化：新增 `earnings-tracking/...md`，再更新 `tracker.md`。
- 公司逻辑大变：新增一版 `deep-research/...-v2.md`，再更新 `tracker.md`。

平时主要看 `tracker.md`；需要追溯最初研究逻辑时，再看 `deep-research/`；需要看每次财报如何影响判断时，再看 `earnings-tracking/`。

## 文件说明

`SKILL.md` 是给 Codex / Agent 正式使用的英文 skill。

`SKILL_CN.md` 是中文维护版，用于你自己检查、理解和后续修改这个 skill。
