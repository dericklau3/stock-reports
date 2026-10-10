# Research Output Templates

## Deep Company Research Template

Read this section for a full deep-research memo. For a narrow question, use only relevant sections. Before writing, load [data rules](data-verification.md), [valuation rules](valuation.md), [execution progress](operating-agenda-execution-progress.md), [company types](company-types.md) and [investor lenses](investor-lenses.md).

Open with **exactly three brief, reader-facing items** in the user's language. For Chinese reports use **投资观点**, **核心逻辑**, **主要风险**; for English reports use **Investment view**, **Core thesis**, **Key risks**. Do not print both languages together.

- **Investment view / 投资观点:** In 1–2 plain-language sentences, say how the company looks as an investment at the current valuation; reflect the supported research-view category without using unexplained labels.
- **Core thesis / 核心逻辑:** In 1–2 sentences, explain the main business and cash-generation drivers behind the investment view.
- **Key risks / 主要风险:** In 1–2 sentences, identify the most important realistic ways the thesis could fail, translating jargon into everyday language.

The bilingual labels above specify meaning only: render each heading in the user's language. **Do not add standalone Confidence or Time horizon fields.** Evaluate evidence strength internally and discuss decision-critical uncertainty where it matters. State the research cutoff, quote timestamp/session, latest fiscal period/end date and valuation target year(s) once in a compact metadata line or relevant valuation section.

Do **not** create a separate or numbered executive overview under any name (including **Executive View**, **Executive Summary**, **执行摘要**, or **先给结论**). The three short items above are the only opening verdict; do not append a second recap, "three most important judgments", lengthy quote/price discussion, or "changes since last report" digest. Relocate unique details to the relevant sections: prices and share-count assumptions → **Valuation Work** (or relevant valuation analysis); product and customer progress → **Segment, Product and Execution Progress** (or the relevant progress section); changes versus previous reports → **Updated Thesis and Tracking Plan** or the pertinent update section. Later sections should add original evidence, numbers, and conditions, not rewrite the initial summary.

1. **Business Model and Industry Structure / 公司到底是做什么生意的？**
   - **First: the beginner explanation**, before any industry jargon, acronyms, accounting detail, valuation ratios or competitive claims. In natural, straightforward language answer these questions in order:
     1. **What does this company actually do?** Say what product/service it provides and what a customer can accomplish with it, in a concrete sentence.
     2. **What customer problem does it solve?** Describe the before-versus-after situation and the business benefit. Avoid unsupported claims of lower cost/faster speed.
     3. **Who buys it and why?** Identify direct buyer types and, if independently verifiable, actual customer examples. Say who ultimately pays; do not mistake partnerships, announced integrations or end users for proven paying customers.
     4. **What is sold and how is the company paid?** Describe each major product/service and the charging mechanism in simple terms, distinguishing equipment sales from rented/usage-based service, subscriptions, transaction fees, etc. only as applicable.
     5. **Where does the money go?** Describe the main costs and why revenue does or does not turn into profit/cash; distinguish today's proven revenue from future plans.
   - **Then a relatable example:** narrate a short real, sourced case if available; otherwise label it a *hypothetical illustration* that shows customer need → product delivery → benefit → payment path. Do not fabricate customer names, contract prices, measured outcomes or adoption.
   - **Only afterward:** explain at most the necessary technical/business terms at their first appearance (usually two to four), with a practical explanation in everyday language. Never make a jargon glossary, acronym list, architectural comparison, market sizing or financial multiples the main beginner explanation.
   - After the reader understands the buying/payment path, cover unit economics when available, industry size and growth, competitive advantage, customer concentration, pricing power and switching costs. Avoid duplicating the later product-progress or valuation sections.

2. **Business Progress / 公司正在做什么、做到哪一步**
   - Reader-facing output: **one compact three-column table of normally 3–5 high-priority items** (fewer if less evidence), optionally preceded by one plain-language context sentence. Crucially, **every initiative must explain its purpose**, not just name a partnership or product:
     | 重点项目 | 为什么做？希望达到什么结果？ | 当前进展与下一步 |
     |---|---|---|
     | Simple project name | State the real problem this work solves, who benefits and the practical intended outcome for customers/company (1 concise sentence; don't repeat generic "growth") | One verified development with date/source and one concrete next check, brief enough for one cell |
   - The **second column is mandatory and substantive**: e.g., a chip upgrade may aim to serve more customer requests per unit of power, a cloud distribution partnership may make it easier for customers to access the service, and a capacity buildout may enable delivery of already contracted services. These are explanatory examples, not asserted facts about a particular issuer; verify actual objectives and mark analyst inference clearly. Distinguish **the result being sought** from **the result already achieved**.
   - The third column combines progress and next proof to keep the table at three columns. Do not sacrifice the purpose column merely to present more milestones, dates or financial metrics.
   - **Never generate the former five-column initiative inventory or 3.1, 3.2, 3.3... essays for each row by default.** Do not copy table entries into follow-up paragraphs, another list or a concluding recap.
   - Select projects by potential effect on future sales, cash or downside risk; group related work if useful. Do not hide consequential delays or cancellations. Describe announcements, tests, deliveries and actual paid usage separately, in beginner-friendly language.
   - Preserve the complete dated initiative inventory, original versus updated deadlines, stage/finance evidence and bottlenecks in `tracker.md`; move material revenue/cost detail to the financial chapter, valuation/dilution calculations to the tracker or linked valuation file, and risk consequences to the brief Key Investment Risks table. Cite key facts in the table.
   - Expand one project only when the user explicitly requests a project deep dive. A short update on a thesis-changing fact belongs in its analytical section instead of recreating the whole project list.

3. **Financial Position / 财务状况：收入、利润和现金**
   - **Mandatory presentation order:** ONE historical financial comparison table with years/periods in columns, THEN 1–3 small-font definition lines immediately below, THEN a single short **总结：** paragraph. Keep this classic multi-year grid, **not the former two-column "指标 | 数据" table**.
   - Use a verified table of normally 5–8 financial rows and 2 historical fiscal years + the latest interim + latest trailing-twelve-month period when available. Adapt periods and metrics to the issuer. The following is a structure-only example (years are placeholders; never output the literal cell placeholder as data):
     | 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2 |
     |---|---:|---:|---:|---:|
     | GAAP收入 | 数据 | 数据 | 数据 | 数据 |
     | GAAP毛利 | 数据 | 数据 | 数据 | 数据 |
     | GAAP经营损益 | 数据 | 数据 | 数据 | 数据 |
     | GAAP总净损益 | 数据 | 数据 | 数据 | 数据 |
     | 经营现金流 | 数据 | 数据 | 数据 | 数据 |
     | 现金资本开支 | 数据 | 数据 | 数据 | 数据 |
     | 自由现金流 | 数据 | 数据 | 数据 | 数据 |
   - State currency and unit above the table, attach reliable source citations and period definitions. Replace example years and "数据" placeholders with dated, issuer-supported figures or mark cells unavailable. Avoid false comparisons between full fiscal years and H1; compute any growth only on comparable time windows. Don't conflate reported/adjusted figures, net income and common-attributable profit, or operating cash and remaining cash on hand.
   - **Directly after the table**, write brief small-font explanations for the used labels, using the website-compatible HTML element in Markdown. For example:
     <small class="financial-glossary">GAAP收入：按会计准则确认的销售及服务收入；GAAP毛利：收入扣除产品或服务的直接成本后剩余的钱；GAAP经营损益：扣除日常经营费用后的利润或亏损；GAAP净损益：算上利息、税费等后的总利润或亏损。</small>
     <small class="financial-glossary">经营现金流：实际经营产生或使用的现金；现金资本开支：购买设备、建设基础设施等投入；自由现金流：经营现金流减资本开支。FY：财年；H1：上半年；TTM：截至该时点的最近12个月。</small>
     Only explain terms actually included, with industry-appropriate definitions. Keep the glossary to 1–3 short lines, using small font; do not put material investment conclusions in small print. The small element should remain understandable even if a renderer drops styling.
   - **After the definitions, include one paragraph starting 总结：** of 2–4 clear sentences describing revenue trend, profitability, operating cash and capital spending, and the largest financing/quality concern. Address material one-off or non-operating gains and missing cash/debt data here, not via lengthy accounting reconciliation. This is the only interpretive paragraph.
   - No 4.1/4.2... finance mini-essays, a second data table, individual row commentary paragraphs or exhaustive source disputes. The underlying source verification, accounting bridges and scenario calculations still take place in the research/tracker or valuation/risk work.

4. **Management and Capital Allocation**
   - Management credibility and execution history.
   - Management promise tracking: prior targets, guidance, strategic claims, product milestones, margin goals, capital allocation promises, and whether they were met, delayed, reframed, or abandoned.
   - Earnings-call answer quality when transcripts are available: whether management answers hard questions directly, explains tradeoffs with numbers, acknowledges misses, changes tone, or relies mainly on vague external excuses.
   - Insider ownership or incentives when relevant.
   - Buybacks, dilution, M&A, capex, and R&D allocation.

5. **Valuation / 估值分析：当前股价贵不贵？**
   - Show **one compact two-column valuation table**, optionally one short methodology/date note, and **one 2–4-sentence 总结： paragraph**. Do not expand into 6.1 股数、6.2 当前估值、6.3 公式和情景、6.4 价格纪律 mini-essays.
   - Use the reader's language. In Chinese the single table is **关键指标 | 估算结果**. Model rows (format-only placeholders, never reported company data):
     | 关键指标 | 估算结果 |
     |---|---|
     | 当前参考股价 | 已核实股价、币种、报价日期 |
     | 公司整体市值 | 包含全部有经济权益股份的正确总市值 |
     | 当前适用估值指标 | 如市盈率/市销率，只有适用且核实才列 |
     | 保守情景估值 | 估算每股区间；可在行名简述不利假设 |
     | 基础情景估值 | 估算每股区间；可在行名简述主要假设 |
     | 乐观情景估值 | 估算每股区间；可在行名简述有利假设 |
   - Select relevant rows. If evidence cannot establish market cap or trustworthy bear/base/bull ranges, **do not invent them**: state **无法可靠估值** and identify missing inputs. Base scenarios on defensible operating assumptions; never use user-provided examples as verified prices.
   - Include at most **one short note below the table** to explain forecast year and whether scenarios are **discounted estimates of today's value** or **undiscounted future scenario prices**, quote/value dates and material methodological limitations. Never confuse future with present value, omit economically entitled shares, or treat forecasts as guarantees.
   - Provide **one concise summary paragraph starting 总结：**. In 2–4 plain-language sentences judge expensive/reasonable/cheap conditionally on the scenarios and identify the main revenue/profit/capital-spending/dilution assumptions that could alter the conclusion.
   - Default report **must not contain** standalone Forward P/E historical extrema tables, full A/B/N share-class calculations, EV-to-equity formula bridges, peer/parameter/sensitivity grids, separate price zones, or pages of valuation notes. When the user explicitly requests those details, give them.
   - **Underlying research remains complete and auditable:** preserve direct sources, price/evidence dates, scenario assumptions, full economic share counts, EV-to-equity bridge, debt/lease/cash and forecast dilution, discounting, comparable multiples where meaningful, sensitivity and arithmetic checks under [valuation discipline](valuation.md) in `tracker.md` or linked calculation records.

6. **Future Events to Watch / 未来值得关注的事件**
   - Reader-facing output is **one concise two-column table of normally 3–5 key upcoming events**, then **one 2–3-sentence 总结： paragraph**. Select only material events that could change the investment view; fewer rows are fine.
     | 重要事件 | 为什么值得关注 |
     |---|---|
     | Upcoming earnings / actual relevant event (use confirmed timing only) | In a single plain-language sentence, specify what business result would matter and why |
     | Customer usage, product commercialization or cash/financing milestone | Distinguish a paid/completed result from a plan, and name the investment implication |
   - These table rows are **format examples, not required events or confirmed schedules**. Events may be positive or negative. Prioritize the next earnings release, verified major commercial results, important capital/stock dilution developments, policy or regulatory decisions when relevant. Group overlapping AMD/AWS/chip launches or similar items if they test the same thesis; do not mechanically repeat the earlier 3–5 ongoing projects.
   - A date is optional: **include it only if officially confirmed** and label company targets/estimated dates properly; do not invent deadlines or treat estimated calendar dates as issuer announcements. Use sourced evidence concisely. Exclude already-past events as of the report cutoff.
   - **No eight-item dense lists, project-status recaps, 7.1/7.2 detailed subsections or extra watchlists**. Do not copy earlier progress table entries or repeat valuation numbers. Under the table write **one 2–3-sentence paragraph beginning 总结：** explaining the main one or two proof points or risk events to watch.
   - Keep the full dated monitoring calendar, source links, targets, original commitments and evolving triggers in `tracker.md`, not repeated in the readable report.

7. **Key Investment Risks / 主要投资风险**
   - In full reports, render **one three-column table of normally 4–5 company-specific material risks**, then **one 2–3-sentence 总结： paragraph**. Choose fewer when warranted; do not fill the table with generic risks just to hit a count.
     | 主要风险 | 可能产生什么影响 | 需要警惕的信号 |
     |---|---|---|
     | A material company-specific risk in plain language | In one sentence, explain a plausible consequence for sales, earnings, funding or valuation | One observable factual warning or disclosure that would prompt reassessment |
   - These are format placeholders, **not verified risks for a named company**. Explain risk pathways in everyday language: for example, a major customer leaving might lower revenue; delayed delivery could defer income; financing may dilute shareholders; weak results can cause an expensive stock's valuation to fall. Include financial/competition/regulatory risks when company-specific evidence makes them important.
   - **No reader-facing "判断/严重度", "机制", "可观察红线", probability or scoring columns**. Assess severity, likelihood (qualitatively only unless statistically defensible), supporting evidence, downside scenarios and invalidation triggers in the underlying risk register/`tracker.md`, not in extra public tables.
   - Distinguish current adverse facts from hypothetical downside risks. Do not duplicate the three-item opening "主要风险", upcoming events, operating project progress or valuation chapter; the table adds concrete consequences and **observable warning signals**.
   - Beneath the table, write **one 2–3-sentence paragraph starting 总结：** about the principal ways the investment thesis could fail and the one or two warning signs to monitor. No 8.1/8.2 subsections, seven-row dense matrix, second checklist, long severity debate or row-by-row essays.
   - Retain traceable risk origins, assessed severity, management incentives, cash/dilution exposure, measurable thesis-invalidating thresholds and updates in `tracker.md` or the valuation/monitoring evidence. Expand the risk inventory only on explicit user request.

8. **Four Investment Perspectives / 四种投资视角：怎么看这家公司？**
   - Present **exactly one compact three-column table with four rows**, then **one 2–3-sentence 总结： paragraph**. This is an evidence-based comparison of four thinking styles, not opinions attributed to the actual investors:
     | 投资视角 | 最关注什么 | 对公司的判断 |
     |---|---|---|
     | 巴菲特式 | 企业能否长期持续赚钱，当前估值是否有余地 | One concise judgment tied to this company's proven or missing evidence |
     | 芒格式 | 哪个错误假设可能带来最大损失 | One different concrete weakness or evidence gap |
     | 段永平式 | 客户为何愿意长期付钱，产品与管理是否可靠 | One plain-language assessment |
     | 李录式 | 长期行业趋势、最坏情况与资金安全 | One plain-language assessment |
   - Use 1 short sentence per cell wherever possible; each viewpoint must add a **distinct insight**, not a copy of the risk, operating-progress, finance or valuation sections. A plain statement such as "仍需观察，因为尚未证明设备投入能转化为持续现金收入" is better than an opaque "Needs further observation" without explanation.
   - **After the table**, include only **one 2–3-sentence paragraph beginning 总结：** describing what the combined checks imply and the single most important unknown. Do not restate the opening three-item investment judgment in different words.
   - Default output **must not include** stand-alone Anti-bias A/B/C rating, four separate investor essays, each investor's support/counterargument/follow-up bullets, 1–10 score table, integrated decision memo, position-sizing/action table, or a second table. Perform critical thinking and source checks internally using [investor lenses](investor-lenses.md), preserving substantial contradictory evidence and key question(s) in `tracker.md` / research notes; expand only if explicitly requested.

9. **Final Research Framework**
   - Add only distinct, measurable conditions that would materially invalidate or change the thesis and are **not already covered** in the future-events table, risk-warning-signal column or four-perspective summary.
   - Never regenerate an upcoming-events list or repeat the opening summary. If nothing new is added, omit this redundant section.

## Post-Earnings Tracking Template

Read this section for earnings or material-event updates. Load [data rules](data-verification.md) and [execution progress](operating-agenda-execution-progress.md); load [valuation rules](valuation.md) when updating values. For non-earnings events, replace earnings-specific fields with event facts and implications; do not force a beat/miss verdict.

Open with **exactly three brief, reader-facing items** in the user's language. For Chinese reports use **投资观点**, **核心逻辑**, **主要风险**; for English reports use **Investment view**, **Core thesis**, **Key risks**. Do not print both languages together.

- **Investment view / 投资观点:** In 1–2 plain-language sentences, say how the company looks as an investment at the current valuation; reflect the supported research-view category without using unexplained labels.
- **Core thesis / 核心逻辑:** In 1–2 sentences, explain the main business and cash-generation drivers behind the investment view.
- **Key risks / 主要风险:** In 1–2 sentences, identify the most important realistic ways the thesis could fail, translating jargon into everyday language.

The bilingual labels above specify meaning only: render each heading in the user's language. **Do not add standalone Confidence or Time horizon fields.** Evaluate evidence strength internally and discuss decision-critical uncertainty where it matters. State the research cutoff, quote timestamp/session, latest fiscal period/end date and valuation target year(s) once in a compact metadata line or relevant valuation section.

Do **not** create a separate or numbered executive overview under any name (including **Executive View**, **Executive Summary**, **执行摘要**, or **先给结论**). The three short items above are the only opening verdict; do not append a second recap, "three most important judgments", lengthy quote/price discussion, or "changes since last report" digest. Relocate unique details to the relevant sections: prices and share-count assumptions → **Valuation Work** (or relevant valuation analysis); product and customer progress → **Segment, Product and Execution Progress** (or the relevant progress section); changes versus previous reports → **Updated Thesis and Tracking Plan** or the pertinent update section. Later sections should add original evidence, numbers, and conditions, not rewrite the initial summary.

1. **Post-Earnings Verdict**
   - Better than expected / mixed / worse than expected only against an identified pre-release benchmark. Separate management guidance from consensus; if pre-release consensus is missing, write “consensus surprise unverified.”
   - What materially changed in the investment judgment, if anything, and the new evidence behind it. Do not repeat the opening investment-view statement.
   - Whether the quarter strengthened or weakened the long-term thesis, and why.

2. **Headline Results / 本期财务发生什么变化**
   - Follow the same **period-comparison table → small-font definitions → one summary paragraph** layout. Compare latest quarter/interim against the matching prior-year quarter/interim; include older years or TTM only if needed to interpret a trend. Normally 3–6 materially relevant metrics, with periods in columns and metrics in rows.
   - Directly below the single table use 1–3 compact small-font lines (<small class="financial-glossary">…</small>) to explain unfamiliar financial terms used. Then a single 2–4-sentence **总结：** paragraph about the meaning of results, one-time gains, cash implications and risks. Disclose only verified guidance/consensus information where relevant.
   - Do not add a second historical grid, multiple financial subsections or extended line-by-line reconciliation essays.

3. **Guidance, Management Commentary and Progress**
   - Keep the same compact three-column progress format (**项目 / 为什么做、希望达到什么结果 / 当前进展与下一步**), usually **3–5 top items**, focusing on important changes since the last period. Explain the customer problem and intended business outcome even in updates; indicate previous-to-current change briefly inside the last column. Distinguish verified delivery or paid use from plans.
   - Highlight only decision-relevant guidance changes, missed promises and management answers; no per-project 3.1/3.2 essays or repetition of the progress table. Preserve complete original dates and evidence in `tracker.md`.
   - Put earnings and cash consequences in the financial/valuation sections, not another broad operating recap.

4. **Quality of the Quarter**
   - Add **only new interpretation, not a repeated set of the Headline Results table**. In at most 2–3 concise sentences, call out any single decisive nonrecurring gain, deteriorating margins, cash conversion or customer/sector indicator that changes the apparent results.
   - If the key insight has already been clearly explained next to a number above, omit this separate subsection entirely. Keep complete verification and calculation records in the tracker or research notes instead of adding a lengthy accounting audit trail.

5. **Market Reaction in Context**
   - Assess whether the post-earnings market reaction is consistent with changes in fundamentals, guidance, and valuation.
   - Separate fundamental changes from sentiment, positioning, and valuation reset only as needed for the earnings conclusion.

6. **Updated Thesis and Tracking Plan**
   - Briefly identify the one or two most important changed assumptions, including any triggered red line and the evidence behind it; do not reiterate the opening view or the earlier business-progress table.
   - When future events matter, use at most the same **重要事件 | 为什么值得关注** two-column format with 3–5 rows (fewer if warranted), followed by **one 2–3-sentence 总结： paragraph**. If the future-events material adds nothing beyond the operating-progress section, omit the redundant table and give only the new change or next verification point.
   - Preserve detailed event dates, original targets and prior-to-current status changes in `tracker.md`; do not invent exact dates or add another long monitoring checklist.

### Required before/after bridge

Read the previous dated memo/tracker before updating. Include this table for decision-driving changes, with source links or locators:

| Item / basis | Prior assumption + date | New fact + evidence date | Revised estimate or unchanged assumption | Valuation impact | View / next proof |
|---|---|---|---|---|---|
| Revenue / margin / shares / initiative / multiple | Prior recorded value or no prior baseline | Actual versus target, not hindsight | Analyst estimate separately from company guidance | Quantified if defensible; otherwise direction and missing input | Confirmed / weakened / invalidated / unverified |

- On first coverage, establish an initial baseline; do not invent prior assumptions, upgrades or downgrades.
- Separate changes in market price, earnings expectations, net claims/share count and valuation method/multiple. An unchanged thesis can still have a changed expected return.
- If a material change affects an old valuation, recompute the affected scenarios or explicitly mark the old valuation stale; do not silently carry it forward. Reuse unchanged assumptions with their original dates.
- Describe market reaction using named price observations (pre-release close, after-hours, next regular close) and benchmark context when available. Do not infer sentiment or causality solely from a price move.
- Preserve the old snapshot, save the new update and link it from the tracker. For non-earnings events, compare pre-event expectations with dated event evidence.
