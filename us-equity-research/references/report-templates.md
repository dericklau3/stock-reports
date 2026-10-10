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
   - Preserve the complete dated initiative inventory, original versus updated deadlines, stage/finance evidence and bottlenecks in `tracker.md`; move material revenue and cost detail to Financial Deep Dive, dilution or price assumptions to Valuation Work, and major risks to Risk Register. Cite key facts in the table.
   - Expand one project only when the user explicitly requests a project deep dive. A short update on a thesis-changing fact belongs in its analytical section instead of recreating the whole project list.

3. **Financial Position / 财务状况：收入、利润和现金**
   - Write for a reader with **zero accounting background**. Explain how much the company sells, whether it earns a sustainable profit, where cash is flowing, and whether it can fund ongoing operations/expansion.
   - Default to **one compact table with three columns and normally 4–6 selected indicators** (fewer if data or sector makes rows inapplicable). A model format:
     | 关键指标 | 最新数据（注明期间） | 这说明什么 |
     |---|---|---|
     | 收入及同比增长 | Latest comparable period, dated | Is customer spending growing? |
     | 净利润或亏损 | Reported figure, dated | Does accounting profit exist, and is it recurring? |
     | 经营产生的现金 | Relevant reported cash flow | Is the business collecting more cash than it spends running operations? |
     | 建设及设备投入 | Material capital expenditures | How much cash goes into expansion or upkeep? |
     | 投入后现金结余（自由现金流） | Only if meaningful/reconcilable | Is cash generated after capital spending, or being consumed? |
     | 现金储备及主要债务 | Same balance-sheet date | Does it have enough liquidity/financing headroom? |
   - **Select rather than mechanically print every example row**: growth/profitability/cash are the default focus; choose sector-specific indicators where important. Show one or two **comparable** periods per indicator, not the old FY2024 + FY2025 + H1 2026 + TTM grid. Do not compare a six-month subtotal with an entire fiscal year as if it were year-over-year growth. Use sensible rounded Chinese units (e.g., 亿美元), retaining exact values in the calculation records.
   - In the final column, explain **what the number means for this specific company**, without simply restating the label. Limit the body after the table to **one 2–3-sentence financial judgment** about growth, sustainable earnings, cash burn/runway and main financial risk.
   - Avoid separate 4.1, 4.2... financial subsections, dense line-by-line reconciling footnotes, professional acronym lists and duplicate metric tables by default. Define necessary concepts at first appearance; replace bare GAAP, TTM, OCF, FCF, SBC and similar jargon with plain language.
   - **Do not simplify away a material contradiction**: if a one-time gain makes profit appear positive despite weak operating earnings, or adjusted figures diverge materially, disclose the actual issue and its interpretation **briefly beside the relevant figure** and cite the filing/table. Keep verified source lineage, unit/period/accounting basis and reproducible calculations in the relevant tracker/valuation work; don't force all audit-trail details into the reading flow.
   - Preserve decision-critical discussion of gross/operating margin quality, working capital, debt maturity, leases, equity compensation/dilution and financing when they change the investment conclusion; surface them in the appropriate valuation/risk section or one concise financial note, rather than generating exhaustive accounting commentary.

4. **Management and Capital Allocation**
   - Management credibility and execution history.
   - Management promise tracking: prior targets, guidance, strategic claims, product milestones, margin goals, capital allocation promises, and whether they were met, delayed, reframed, or abandoned.
   - Earnings-call answer quality when transcripts are available: whether management answers hard questions directly, explains tradeoffs with numbers, acknowledges misses, changes tone, or relies mainly on vague external excuses.
   - Insider ownership or incentives when relevant.
   - Buybacks, dilution, M&A, capex, and R&D allocation.

5. **Valuation Work**
   - Current multiples and historical context.
   - Forward P/E snapshot table: current forward P/E, 1-year high forward P/E, and 1-year low forward P/E, with dates, EPS basis, sources and coverage. Interpret range position only if comparable; explicitly distinguish unavailable history, sparse observations and a method that is not meaningful.
   - Peer comparison where useful.
   - Scenario valuation: bear, base, bull.
   - Reproducible formula, unit/period definitions, EV-to-common-equity bridge, selected shares, value date, sensitivity and arithmetic check under [valuation rules](valuation.md). Include current-price implied operating requirements when supportable.
   - Valuation method selection by company type.

6. **Catalysts and Monitoring Plan**
   - Near-term catalysts.
   - Medium-term thesis milestones.
   - Metrics to monitor in future quarters.

7. **Risk Register**
   - Qualitative likelihood and severity of key risks; numerical probabilities require a defensible basis.
   - Downside case.
   - Thesis invalidation signals.
   - The strongest disconfirming evidence.

8. **Four Investor-Style Decision Lenses**
   - Anti-bias note: information richness rating, main research blind spot, and strongest reason smart investors may disagree.
   - Buffett-style lens: conclusion, key question, evidence for and against, decision implication, and follow-up question covering business durability, moat, cash conversion, management, valuation, and margin of safety.
   - Munger-style lens: conclusion, key question, inversion table or concise failure paths, fragile assumptions, incentives, psychological traps, major stupidity risk, decision implication, and follow-up question.
   - Duan Yongping-style lens: conclusion, one-sentence business essence, user value, product or brand strength, culture/people, long-term certainty, right price, decision implication, and follow-up question.
   - Li Lu-style lens: conclusion, circle of competence, long-term industry or civilization trend, value-chain position, downside protection, margin of safety, research-depth decision, and follow-up question.
   - Scoring table with evidence rationale and coarse anchors from [investor lenses](investor-lenses.md); N/A is permitted. Do not repeat earlier analysis.
   - Integrated decision memo and action-framing table for no position, existing position, add/upgrade signal, and reduce/downgrade signal.

9. **Final Research Framework**
   - Briefly name the measurable assumptions and future events that would strengthen or invalidate the thesis.
   - Do not repeat the opening three-part summary or copy the risk section; focus on observable thresholds and evidence to watch.

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
   - Use a concise **three-column table of 3–5 decision-driving metrics**, showing the actual number and same-period comparable change (when available), plus a one-line plain-language meaning. Prioritize revenue, profit/loss, operating cash and any material financing/capex/sector-specific measure.
   - Explain in one short paragraph whether this quarter reflects better/worse business economics. Only mention guidance and pre-release consensus when verifiable and material. Preserve forecast basis and reporting period, but avoid a second full-year/TTM grid or an exhaustive accounting reconciliation.
   - Distinguish published accounting profit from adjusted measures and one-time gains if they change the conclusion; explain differences briefly near the relevant value.

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
   - What improved.
   - What worsened.
   - Which assumptions changed.
   - Which core thesis assumptions were confirmed or weakened.
   - Whether any red-line condition was triggered.
   - Which management promises or milestones need follow-up.
   - What to monitor before the next earnings report.
   - What would change the research view.

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
