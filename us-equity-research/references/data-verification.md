# Data Verification and Evidence

Read for every non-trivial research pass. Keep provenance proportional to the decision: track critical inputs, not every incidental number.

## Cutoff and identity

State the research date/cutoff, quote timestamp/time zone and regular/extended session, fiscal year/quarter and period end date. On non-trading days, identify the last available session rather than implying a live quote. For a historical-as-of request, use only information available by that cutoff; later restatements belong in a separately labeled subsequent-information note.

Confirm legal issuer, ticker, exchange, share class, currency and corporate actions. For ADRs/foreign issuers, load [company-type checks](company-types.md). Never combine an ordinary-share denominator with an ADS quote without conversion.

## Retrieval

Prefer company filings, earnings releases, shareholder letters, presentations and official call materials; supplement with market-data providers for quotes/estimates, competitor filings and industry sources for benchmarks, and reputable news for catalysts. Analyst ratings are supporting context, not the thesis.

- Resolve the CIK using SEC company tickers, then inspect `https://data.sec.gov/submissions/CIK##########.json`.
- For a selected accession, inspect the filing directory `index.json` and relevant exhibits (often EX-99.1/ex99/final files); the 8-K body may not contain the earnings tables. Record accession, document/exhibit and table/page/section where usable.
- For recent IPOs, compare S-1/424B4 with the first periodic filings. Flag conversion, share-count, lockup and vesting/SBC discontinuities. Use the applicable foreign-issuer filings rather than forcing a domestic schedule.
- If IR/SEC retrieval is blocked, use a legitimate alternate official filing, mirrored issuer release, or reputable secondary source and disclose the missing coverage. Respect access limits; avoid repeated retries of the same blocked endpoint. A search snippet is a discovery lead, not a substitute for a decision-critical table.
- A mirrored issuer release supports what the issuer reported, not independent corroboration. Product documentation, customer disclosures and regulatory records support only the specific operational facts they establish.

## Critical-data record

Place a compact source/input table in the memo or alongside the relevant calculation; no separate database is required.

| Metric | Value / unit / currency | Period or as-of time | Definition / basis | Source link + locator / disclosure date | Status / reconciliation |
|---|---|---|---|---|---|
| Decision-critical input | Raw value or unavailable | Fiscal/TTM/instant/estimate horizon | GAAP/adjusted; reported/calculated; share class | Filing table, exhibit, page or provider observation | Single source / corroborated / conflict; formula if derived |

Cover the inputs that carry the conclusion: price, actual shares/market cap, EV bridge, revenue/growth, margins, income, cash flow/capex, cash/restricted cash, debt/leases/maturities, SBC/dilution/buybacks, guidance, estimates and thesis-driving KPIs. State the next earnings/catalyst date if verified; distinguish announced from provider-estimated dates.

## Period and accounting reconciliation

- Distinguish fiscal from calendar years, quarterly from cumulative cash-flow figures, TTM from annual forecasts, and millions from billions. Derive standalone quarters or TTM only from comparable periods; label calculations and adjust for fiscal changes/restatements.
- Preserve reported and adjusted values separately with material adjustments. Do not blend GAAP earnings with an adjusted consensus benchmark.
- Market cap normally uses current actual shares of the relevant equity classes, with class treatment explained; EPS weighted-average shares are a period measure. Valuation may require forecast dilution. Keep these denominators separate.
- Separate consolidated cash from restricted/customer cash, debt from other claims, and balance-sheet date from quote date. Reflect material subsequent financing with a dated pro forma bridge.
- Record the timestamp and earnings window of consensus. For earnings surprises, use a snapshot demonstrably available before release. Data captured afterward is not evidence of pre-release expectations; unavailable pre-release consensus means the consensus beat/miss is unverified.

## Cross-checks and confidence

Cross-check decision-critical figures against another reputable source when practical, but identify source lineage. Two aggregators using the same feed or a release and its mirror are not two independent confirmations. Direct filing evidence plus a transparent arithmetic reconciliation can be more useful than an unexplained second number.

When figures differ, reconcile date, currency, fiscal/TTM window, adjusted/GAAP definitions, consolidated/common attribution and actual/weighted-average/diluted shares. Do not average conflicting values. Prefer the applicable primary filing (including a relevant amendment); explain what was excluded and why. If still material and unresolved, do not let that number carry a precise valuation.

Assess confidence in the specific claim: confidence that an issuer reported a number is different from independent verification of operating outcomes. Describe inaccessible evidence and the decision it prevents; a missing non-critical document need not invalidate verified results. Use the main skill's confidence rubric and identify the weakest thesis-driving input.
