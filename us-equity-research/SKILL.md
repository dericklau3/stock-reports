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
- Explain every company's products and jargon in plain language: what is sold, who pays, why they buy, major costs, revenue recognition where material, and how revenue becomes profit/cash. Explain major segments separately; distinguish today's earnings engine from future monetization.
- Present **公司正在做什么、做到哪一步 / Operating Agenda & Execution Progress** before valuation in full research. Distinguish technical/regulatory readiness, paid adoption and economics. Verified early progress matters even without disclosed revenue; a launch or contract does not establish profitable adoption.
- Use primary filings/IR materials as the financial source of record, with independent cross-checks where practical. Key facts need direct links and document/table/page locators, not just source names. A mirror of one release is not another independent source.
- Match valuation to company stage, sector and security structure. Inspect cash conversion, SBC/dilution, debt, leases, reinvestment, accounting adjustments, concentration, competition, regulation and management credibility.
- Support each view with evidence, the strongest counterargument, downside and observable conditions that would change it. Lower confidence for decision-critical gaps; do not replace missing evidence with precision.
- Frame conclusions as research support. Investor-style lenses describe analytical approaches, not those investors' actual opinions or endorsements.

## Required workflow and references

Read only the references needed for the selected task; the shared data rules apply to every non-trivial research pass.

1. Resolve issuer, ticker, exchange, share class and reporting period. Read the previous tracker/memo on repeat coverage and set the research cutoff and quote timestamp.
2. Load [data verification](references/data-verification.md): source retrieval, time/period definitions, critical-number provenance and confidence.
3. Explain the business in beginner-friendly terms. For full research or material updates, load [operating agenda and execution progress](references/operating-agenda-execution-progress.md). Discover current work, compare original commitments and show prior stage → new evidence → current stage. Retain stable initiative names and distinguish no new disclosure from no progress.
4. Load [company types and conditional checks](references/company-types.md) when choosing metrics/methods, including foreign issuers/ADRs, peer comparability and material financial-quality bridges.
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

Report confidence separately: high requires reconciled critical inputs and a conclusion robust to plausible sensitivity; medium means bounded uncertainties could change valuation/conviction; low means unresolved critical dependencies dominate. High confidence is not certainty of returns. Information richness or a long report does not establish high confidence. Identify mixed confidence across operating progress and valuation when relevant.

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
- Start the chat response with the research view. Include a brief **正在做什么 / 最新进度 / 下一关** summary for material initiatives, the main valuation condition and material verification limits; link the saved memo. For narrow questions, keep delivery proportionate to the request.
- End with concise **What would change my view / 什么会改变我的观点** conditions.
