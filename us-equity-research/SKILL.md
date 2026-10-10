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

The reader-facing financial section is **财务状况：收入、利润和现金** in Chinese (or **Financial Position: Revenue, Profit and Cash** in English), not a long "Financial Deep Dive". Answer in simple language: **is the business growing, is it making a profit, is it generating or consuming cash, and does it have enough cash/debt capacity to continue?** If the issuer type warrants it (e.g., banks or biotechnology), adapt the key indicators rather than imposing unrelated corporate metrics.

- Default to **one compact three-column table, normally 4–6 meaningful indicators** (fewer if supported data is sparse): **关键指标 | 最新数据（注明期间） | 这说明什么**. Choose revenue and comparable growth, reported profit/loss, cash from operations, investment/capital spending and/or cash remaining after investment, and cash balance/main debt or runway when material. Do not force all rows for every industry; use one row only once for closely related measures when possible.
- Use **one or two recent, comparable periods** per metric and show year-over-year change only using like-for-like time windows. Avoid the default FY2024/FY2025/H1/TTM all-in-one grid. A half-year figure is not an annual total; distinguish latest quarter/half-year from fiscal year. Prefer understandable units in Chinese (e.g., 亿美元, 万美元) with sensible rounding; keep precise original numbers and period definitions internally for calculations.
- Translate each number into its economic meaning in one short sentence. Explain special accounting terms only when decision-critical; do **not** lead with GAAP, TTM, EBITDA, SBC, FCF, OCF or unexplained acronyms. Distinguish reported accounting profit from operational cash generation, investment spending and unrestricted available cash.
- Finish with **one short 2–3-sentence financial interpretation**, highlighting growth, profit, cash sustainability and the single most consequential financial risk. **Do not** follow the table with multiple 4.1/4.2 subchapters, repeated metric descriptions, full accounting reconciliation essays or a second raw historical-data table.
- Critical exceptions still matter: if a headline profit is dominated by a one-time/nonoperating gain, adjusted measure, accounting conflict or unusual financing, explain the consequence in **one concise note adjacent to the affected metric** (and give the exact source). Keep material reconciliations and reproducible calculations in the relevant valuation/financial-quality analysis or dated `tracker.md`, rather than presenting them as a long beginner-facing audit trail. Do not hide facts that reverse the reader's understanding.
- Preserve primary-source validation, comparable reporting periods, fiscal/GAAP basis, currency, key data citations and essential cash/debt/dilution risks. If critical data are unavailable, explicitly say so, avoid invented confidence or false precision, and identify what the missing fact prevents one from judging.

## Required workflow and references

Read only the references needed for the selected task; the shared data rules apply to every non-trivial research pass.

1. Resolve issuer, ticker, exchange, share class and reporting period. Read the previous tracker/memo on repeat coverage and set the research cutoff and quote timestamp.
2. Load [data verification](references/data-verification.md): source retrieval, time/period definitions, critical-number provenance and confidence.
3. Explain the business using the mandatory five-part beginner-first business model and a concrete customer/payment example. For full research or material updates, load [operating agenda and execution progress](references/operating-agenda-execution-progress.md). Research all important initiative histories and preserve stable names, commitments and statuses in the tracker; **only the top 3–5 milestones appear in a three-column, no-deep-dive progress table with project purpose/desired result and actual progress/next verification** in the reader-facing report.
4. Load [company types and conditional checks](references/company-types.md) when choosing metrics/methods, including foreign issuers/ADRs, peer comparability and material financial-quality bridges. Investigate detailed financial quality internally, but write the financial section as the mandatory short beginner-readable snapshot rather than a multi-year data dump.
5. For any valuation, load [valuation discipline](references/valuation.md). Full research normally includes bear/base/bull per-share ranges and a current/1-year high/1-year low forward P/E table, with explicit unavailable/not-meaningful fields where necessary.
6. For full memos or earnings/material-event updates, use the relevant section of [report templates](references/report-templates.md). Updates require a prior-assumption → new-fact → revised-estimate → valuation-impact bridge; first coverage establishes a baseline.
7. For full deep research, load [four investor-style lenses](references/investor-lenses.md) as a concise evidence-based pressure test. Do not repeat earlier sections or turn qualitative scores into mechanical buy signals.
8. Verify calculations, sources, limits and view-changing conditions. Save using the rules below and update the tracker.

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
- In full research, include understandable business economics, evidenced operating progress, material financial risks, suitable scenarios, the forward P/E table or justified gaps, four lenses and thesis invalidation conditions.
- Every valuation needs reproducible inputs/formula, a value date, suitable shares, explicit net claims and sensitivity. Recompute arithmetic with a calculator or code. A future scenario price is not today's fair value without a consistent discounting method.
- Updates must preserve original commitments and explain what changed. Mark invalidated old estimates stale; do not silently rewrite prior snapshots.
- Start the chat response with the concise three-item summary (投资观点 / 核心逻辑 / 主要风险 in Chinese), not a five-field technical block. Include a brief **正在做什么 / 最新进度 / 下一关** summary for material initiatives, the main valuation condition and material verification limits; link the saved memo. For narrow questions, keep delivery proportionate to the request.
- End with concise **What would change my view / 什么会改变我的观点** conditions.
