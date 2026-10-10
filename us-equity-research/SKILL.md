---
name: us-equity-research
description: Use when researching a selected US-listed company, its business model, operating progress, valuation or buyability, or tracking earnings, guidance and material company events. Applies to deep research and focused follow-up questions, including foreign issuers and ADRs listed in the US.
---

# US Equity Research

## Scope and routing

Support medium-term (weeks/months) and long-term (over one year) research on selected companies. A bare ticker or broad “analyze this company” request defaults to deep company research. Preserve the user's language and requested scope.

Use only these two modes:

- **Deep company research:** full initial/reassessment memo, or focused business/valuation follow-up using the relevant subset.
- **Post-earnings tracking:** earnings, guidance, filings and material-event updates, compared with prior research where available.

A narrow price or business question does not require a full memo or all four lenses. Reuse prior research only after checking decision-critical changes; do not treat old prices or assumptions as current. These modes do not authorize trades, messages, publication or scheduled monitoring.

## Essential research contract

- Verify time-sensitive facts; never invent financials, consensus, quotes, sources, progress, probabilities or valuation ranges. Separate facts, management targets, analyst assumptions, estimates and opinion.
- Explain the business to a reader with zero industry background **before** any technical or financial analysis. Answer what the company actually does, which customer problem it solves, exactly who buys/pays for what, why they buy, and how payment becomes profit or cash. Show a concrete customer-use/payment example and separate verified facts from illustrations. Follow the beginner-first rules below; avoid unexplained jargon or acronym dumps.
- Present **公司正在做什么、做到哪一步 / Operating Progress** before valuation as a short, plain-language overview: normally one three-column table with 3–5 material items (or fewer if justified), showing **the project, why it exists and the concrete outcome it aims to deliver, plus verified progress and the next proof to watch**. For each initiative, name the customer/operational problem it addresses, how the initiative helps solve it, and the intended business result (e.g., new paid use, lower cost, more capacity) in everyday language; distinguish goals from achieved results. Avoid wide inventories and **never add serial per-project deep dives by default**. Preserve comprehensive dated milestone analysis and stage/economic distinctions in `tracker.md`; locate relevant figures in financial/valuation/risk sections, not repeated here.
- Use primary filings/IR materials as the financial source of record, with independent cross-checks where practical. Key facts need direct links and document/table/page locators, not just source names. A mirror of one release is not another independent source.
- Match valuation to company stage, sector and security structure. Inspect cash conversion, SBC/dilution, debt, leases, reinvestment, accounting adjustments, concentration, competition, regulation and management credibility. **Research all critical financial details, but show only a short, understandable financial snapshot in the reader-facing report** as specified below; do not equate many rows of accounting data with a better explanation.
- Support each view with evidence, the strongest counterargument, downside and observable conditions that would change it. Lower confidence for decision-critical gaps; do not replace missing evidence with precision.
- Frame conclusions as research support. Investor-style lenses describe analytical approaches, not those investors' actual opinions or endorsements.

## Beginner-first business model (mandatory for full deep research)

Before describing products, segments, industry structure, or technical advantages, explain the company as if the reader knows **nothing** about its industry. The "beginner version" must actually be understandable without searching for terminology:

1. **What does it do?** Start with one concrete sentence naming the everyday product/service and what it enables someone to do; avoid abstract sector labels.
2. **What problem does it solve?** Explain the customer's situation before the product, what improves after buying, and why that improvement matters (time, cost, revenue, risk, convenience, etc.). Explain comparisons only where supported.
3. **Who buys and who pays?** Name the real buyer types and, when verified, one or two recognizable actual customers. Distinguish direct paying customers from users, channel partners, suppliers, financiers, prospective customers and merely announced collaborations. If customer/payment status is undisclosed, say so.
4. **What exactly is delivered and how does money change hands?** For each material revenue stream, describe the deliverable, the paying party, the charging model (one-off equipment, subscription, usage, transaction fee, etc., only if supported), major company-paid costs, and how this could yield profit. Separate current sales from plans not yet monetized.
5. **Make it tangible.** Include one short end-to-end example: customer need → product/service used → benefit → who pays the company and for what. Mark invented illustrative scenarios clearly as hypothetical; never invent customer names, contract terms, prices, or proven performance.

In Chinese, prefer straightforward everyday Chinese over English financial/technical language. Explain a technical term **immediately** if unavoidable; do not open with acronyms, chip architectures, metrics, or a glossary. Move only the necessary detailed terminology, market size, unit economics and competitive technology **after** this explanation. Use short paragraphs or a compact five-question structure rather than a long vocabulary list; keep the initial explanation concise while preserving key business distinctions. For material multi-segment companies, explain each major revenue stream separately without repeating the entire introduction. For focused business-model questions, prioritize these answers rather than a full research memo.

## Beginner-readable financial picture (mandatory for full deep research)

The financial section should be clear to nonexperts but **retain the historical comparison table the user wants**. Use this exact order: **one multi-period financial table → a compact small-font glossary directly below → one short plain-language summary**. Do not replace the comparison grid with the recent two-column value-only format.

- **Table:** financial indicators as rows; typically 2 previous fiscal years, latest available half-year/quarter and trailing twelve months as columns (e.g., 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2). Adapt labels and column count to actual periods with verified comparable data; example dates are not fixed. Normally 5–8 important rows: GAAP revenue, GAAP gross profit, operating profit/loss, consolidated net profit/loss, operating cash flow, cash capital spending and free cash flow, as applicable. Include a consistent currency/unit note and cited source(s). Missing items may be marked unavailable; do not invent values or force special-sector companies into irrelevant rows.
- **Accuracy:** show historical years and interim/TTM periods side-by-side only as labeled; do not compare six-month totals directly with twelve-month totals to infer growth. Keep reported GAAP and adjusted values separate, calculate TTM from matched periods, distinguish consolidated net income from common-shareholder income, and preserve exact source inputs internally.
- **Small glossary:** directly after the one table, explain **every unfamiliar financial label actually used** (e.g., GAAP收入、GAAP毛利、GAAP经营损益、GAAP净损益、经营现金流、资本开支、自由现金流, FY, H1 and TTM) in **1–3 short compact lines**. Render each as <small class="financial-glossary">short explanations…</small> in Markdown/HTML. Only define terms here; do not interpret company performance or bury key risks in tiny type. No extra glossary heading, second table or long explanations.
- **Summary:** immediately after these small-font definitions, provide **one 2–4-sentence plain-language paragraph labeled 总结：** in Chinese. Explain what the numbers indicate about revenue, real profitability, use of cash, financial endurance and a key risk. This is where to flag one-time gains, material accounting differences and missing cash/debt evidence, with citations. No financial 4.1/4.2 subsection essays, repetitive metric-by-metric paragraphs, additional tables or lengthy audit-trail footnotes.
- **Research quality remains unchanged:** check original fiscal/accounting bases, cash reconciliations, debt/leases, cash constraints and dilution fully; keep detailed verification and original assumptions in the dated tracker and relevant valuation/risk analyses, not a long reader-facing finance section. Specialized industries may use different metrics while following the same presentation order.

## Required workflow and references

Read only the references needed for the selected task; the shared data rules apply to every non-trivial research pass.

1. Resolve issuer, ticker, exchange, share class and reporting period. Read the previous tracker/memo on repeat coverage and set the research cutoff and quote timestamp.
2. Load [data verification](references/data-verification.md): source retrieval, time/period definitions, critical-number provenance and confidence.
3. Explain the business using the mandatory five-part beginner-first business model and a concrete customer/payment example. For full research or material updates, load [operating agenda and execution progress](references/operating-agenda-execution-progress.md). Research all important initiative histories and preserve stable names, commitments and statuses in the tracker; **only the top 3–5 milestones appear in a three-column, no-deep-dive progress table with project purpose/desired result and actual progress/next verification** in the reader-facing report.
4. Load [company types and conditional checks](references/company-types.md) when choosing metrics/methods, including foreign issuers/ADRs, peer comparability and material financial-quality bridges. Investigate detailed financial quality internally, but write the visible section as one historical comparison table, small-font financial definitions and one summary, not a long financial essay.
5. For any valuation, load [valuation discipline](references/valuation.md). Full research checks bear/base/bull per-share values and meaningful forward P/E history, but shows only a compact valuation result table and summary; preserve detailed assumptions, P/E history, formulas, dilution and sensitivity in the tracker or linked valuation record.
6. For full memos or earnings/material-event updates, use the relevant section of [report templates](references/report-templates.md). Show the short upcoming-event table and summary without duplicating operating progress; keep detailed trigger/calendar history in the tracker. Updates require a prior-assumption → new-fact → revised-estimate → valuation-impact bridge; first coverage establishes a baseline.
7. For full deep research, load [four investor-style lenses](references/investor-lenses.md) as a concise evidence-based pressure test. Do not repeat earlier sections or turn qualitative scores into mechanical buy signals.
8. Verify calculations, sources, limits and view-changing conditions. Save using the rules below and update the tracker.

## Concise future events and monitoring (mandatory for full deep research)

In Chinese title the chapter **未来值得关注的事件** rather than "Catalysts and Monitoring Plan". Its job is to answer **what is coming next, why it could change the investment view, and what factual outcome to watch**—not repeat the prior **公司正在做什么、做到哪一步** project progress.

- Show **one brief two-column table**, usually **3–5 high-impact events** (fewer if justified), with headers **重要事件 | 为什么值得关注**. Prefer the next earnings report or relevant guidance, a few real business/commercial tests, financing/dilution, regulatory rulings or shareholder selling restrictions when materially relevant.
- Give each row **one short everyday-language explanation** of the effect investors need to verify (e.g., paid revenue, adoption, cost, profitability, dilution), including potential upside **or downside**, not just "catalyst" jargon. Use verified event dates **only when the organizer/issuer/regulator has confirmed them**; where unconfirmed, do not invent a date or represent a third-party estimate as an official date.
- Rank by potential decision impact and immediacy; **group overlapping initiatives**. Do not recite the project history, delivery stages or already-described collaboration details. Do not mechanically list 8–10 press releases or force a quota.
- **Immediately under the table, write one plain-language 总结： paragraph of 2–3 sentences**, explaining the 1–2 most consequential developments to watch and why those outcomes, not announcements alone, would strengthen or weaken the thesis. No extra numbered 7.1/7.2 subsections, per-event essays, another monitoring checklist or repeated thesis conclusion.
- Continue recording the full calendar, source evidence, event-status changes and monitoring triggers in `tracker.md`. If this is a dated report, exclude events already completed before the research cutoff and distinguish prior history from upcoming events. For earnings/event updates use the same priority filter; don't duplicate the operating-progress table.

## Beginner-readable valuation display (mandatory)

For full written reports, use **one compact valuation table + bear/base/bull estimates + one plain-language summary**, rather than a long "Valuation Work" essay. In Chinese, title this chapter **估值分析：当前股价贵不贵？**

- Show **only one two-column table** (normally 5–7 rows, **关键指标 | 估算结果**): the dated stock price; entire equity market capitalization including all economically entitled share classes; at most one meaningful current valuation multiple; then **保守 / 基础 / 乐观** per-share estimate ranges. State currency and dates; do not invent unknown ratios or ranges.
- Beneath the table, at most **one compact date/method note** must distinguish estimates of value **discounted to today** from **undiscounted future share-price scenarios**, and identify any forecast year. Never imply an assumption is a guaranteed price target.
- Finish with **one 2–4-sentence paragraph starting 总结：**, answering whether the stock appears expensive, fair or cheap **under the assumptions**, why, and which business/financing conditions could materially change that conclusion. If key inputs do not support precise ranges, say **无法可靠估值**, describe missing evidence, and do not force scenarios.
- Do not normally show 6.1/6.2/6.3/6.4 mini-chapters, separate historical Forward P/E tables, capitalization walkthroughs, EV-to-equity equations, peer grids, scenario input tables, sensitivity grids or buy-price ladders. Expand these only if the user requests such detail.
- **Keep analytical depth:** validate all share classes, stock/earnings dates, debt, cash/leases, dilution, scenario assumptions, discounting, forward-P/E comparisons when meaningful and reproducible arithmetic under [valuation rules](references/valuation.md). Retain full inputs, citations and calculations in `tracker.md` or a small linked calculation record; never hide a limitation that reverses the result.

## Research view and confidence

- **Positive:** durable/improving fundamentals and attractive risk/reward under reasonable assumptions.
- **Constructive but watchful:** attractive business with unresolved valuation, timing or execution confirmation.
- **Neutral / wait for confirmation:** no sufficiently supported directional thesis.
- **Negative / thesis weakening:** adverse fundamentals, valuation, dilution, financing or competitive developments.
- **Insufficient evidence:** decision-critical inputs are missing or materially conflicted; name the evidence needed.

Assess confidence in the underlying evidence while researching: high requires reconciled critical inputs and a view robust to plausible sensitivity; medium means bounded uncertainties could alter valuation or conviction; low means unresolved thesis-driving dependencies dominate. Confidence does not predict stock returns and is not determined by report length. Do not present a standalone confidence score or heading by default; instead, identify material evidence gaps in the sections they affect, explain their consequences and name what would resolve them. Provide an explicit confidence rating only if the user asks.

## Reader-facing report summary

For full deep research and post-earnings/material-event updates, open the written report with **exactly three concise, plain-language items**, in the user's language:

- **投资观点 / Investment view**: overall business and valuation judgment, including whether the current price offers an attractive risk/reward when supportable.
- **核心逻辑 / Core thesis**: why that judgment could be right, emphasizing the actual commercial/earnings drivers.
- **主要风险 / Key risks**: the 1–3 most important failure modes, stated clearly rather than as jargon lists.

Use **投资观点、核心逻辑、主要风险** for Chinese output; **Investment view, Core thesis, Key risks** for English output. The bilingual labels above are instructions, not headings to print together. Aim for 1–2 short sentences per item. Explain necessary technical terms in everyday language. Do not add standalone **Confidence** or **Time horizon** fields. State research/quote dates and relevant valuation target years once in compact metadata or the valuation analysis; discuss material uncertainty beside the affected evidence instead of creating a confidence field. Strictly prohibit any additional executive-overview section in full reports, update reports, and chat responses. Never create a standalone or numbered **Executive View**, **Executive Summary**, **执行摘要**, **先给结论**, or equivalent recap under another heading. The three-item opening is the **only** top-level verdict summary; keep it short, without extra paragraphs, lists of judgments, detailed price commentary, or a historical-change digest. Put prices and valuation assumptions in the valuation section, operating progress in the company-progress section, and changes since earlier research in update/tracking sections. Do not repeat the opening verdict at the end; later content must add new evidence, calculations or actionable verification conditions. For narrow questions, answer only the requested scope.

## Saving Research Results

Save research outputs as Markdown files unless the user explicitly asks not to save them. Use one directory per company:

```text
research/
`-- COMPANIES/
    `-- TICKER/
        |-- deep-research/
        |   |-- YYYY-MM-DD-deep-research.md
        |   `-- YYYY-MM-DD-deep-research-v2.md
        |-- earnings-tracking/
        |   |-- YYYY-QN-earnings-tracking.md
        |   `-- YYYY-MM-DD-earnings-tracking.md
        `-- tracker.md
```

Use uppercase ticker symbols for company folders, such as `TICKER`.

### deep-research/

Save each full deep company research memo in `research/COMPANIES/TICKER/deep-research/`.

Do not overwrite older deep research files. Treat each file as a point-in-time thesis snapshot. Create a new version when the user explicitly requests a new full memo or company logic materially changes; use the small-update rule otherwise.

### earnings-tracking/

Save each post-earnings tracking memo in `research/COMPANIES/TICKER/earnings-tracking/`.

Prefer `YYYY-QN-earnings-tracking.md` when the fiscal quarter is clear; YYYY is the fiscal year, and the memo must state the period end date. If a filename already exists, add the update date or a version suffix rather than overwriting it. Use `YYYY-MM-DD-earnings-tracking.md` when the quarter is unclear or the update is not tied to a regular quarter.

### tracker.md

Maintain `research/COMPANIES/TICKER/tracker.md` as the current state file. Update it after every deep research memo and every post-earnings tracking memo.

The tracker should summarize:

- Current research view.
- Current main thesis.
- Key risks.
- Latest earnings or company update.
- **Operating Agenda / Execution Progress**: retain stable initiative names/keys, latest evidenced stage and evidence date, schedule status, the next gate/date, bottleneck and shareholder relevance. Preserve original commitments when targets are changed.
- What changed since the prior view, including each material initiative's prior stage → new evidence → current stage; distinguish no new disclosure from no progress.
- Core thesis assumptions that must remain true.
- Red-line conditions that would force a thesis review or downgrade.
- Management promises, targets, or strategic milestones that need follow-up.
- Metrics or events to monitor next.
- What would change the research view.

Treat `tracker.md` as the active monitoring dashboard, not a shorter copy of the latest memo. Preserve dated assumption/valuation changes and links to their source memos. Keep the current state concise, but make it easy to check later whether the original thesis is being confirmed or disproved.

### Update Rules

- Small change: update only `tracker.md`; append a compact dated change entry with prior and new assumptions so earlier valuation snapshots remain recoverable.
- Earnings change: create a new `earnings-tracking/...md`, then update `tracker.md`.
- Major company logic change: create a new `deep-research/...-v2.md`, then update `tracker.md`.
- Standalone scenario-valuation refreshes, current-price valuation updates, or single-event valuation implications normally count as a small change: update `tracker.md` with a dated valuation snapshot, bear/base/bull ranges, practical price zones, sources, and what changed since the prior view. Create a new deep-research memo only when explicitly requested or when the business thesis, company logic, or valuation framework materially changed.

## Final acceptance and delivery

- Confirm the latest reporting period, quote session/time zone and cutoff; flag older evidence and missing materials. Do not claim to have read blocked documents.
- Check units, fiscal periods, adjusted/GAAP basis, estimate timestamps and share/security definitions. Resolve critical conflicts or disclose their effect.
- In full research, include understandable business economics, evidenced operating progress, material financial risks, suitable valuation scenarios (or explicit evidence gaps), four lenses and thesis invalidation conditions. Forward P/E details are research evidence, not an obligatory extra public table.
- Every valuation still needs reproducible inputs/formula, a value date, suitable shares, explicit net claims and sensitivity in the tracker or linked calculations. Recompute arithmetic with a calculator or code. Explicitly distinguish future share prices from today's discounted fair-value estimates in the short report.
- Updates must preserve original commitments and explain what changed. Mark invalidated old estimates stale; do not silently rewrite prior snapshots.
- Start the chat response with the concise three-item summary (投资观点 / 核心逻辑 / 主要风险 in Chinese), not a five-field technical block. Include a brief **正在做什么 / 最新进度 / 下一关** summary for material initiatives, the main valuation condition and material verification limits; link the saved memo. For narrow questions, keep delivery proportionate to the request.
- End with concise **What would change my view / 什么会改变我的观点** conditions.
