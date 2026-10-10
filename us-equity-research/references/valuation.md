# Valuation Discipline and Reproducibility

Read whenever issuing or revising a multiple, price zone, fair value or scenario range. Choose methods using [company-type checks](company-types.md); preserve input provenance under [data verification](data-verification.md).

## Choose and label the method

- Use P/E, EV/EBIT, EV/EBITDA or FCF yield for suitable profitable businesses, adjusted for cyclicality, reinvestment and earnings quality. PEG is supporting context only; equal growth rates do not imply equal risk or cash returns.
- Use EV/Sales or EV/Gross Profit for suitable growth/unprofitable companies only with a bridge to sustainable margins, capital needs, cash burn and dilution. Use book/tangible book and ROE/capital measures where appropriate for financials, or a common-equity NAV bridge for asset-backed situations.
- DCF requires explicit growth, margins, reinvestment/FCF conversion, discount rate, terminal assumptions and sensitivity. Match enterprise cash flows with an enterprise discount rate and equity cash flows with an equity rate; avoid deducting debt twice. Check that terminal assumptions are economically plausible and disclose terminal-value dependence.
- Distinguish **today's intrinsic-value estimate** from a **future market-price scenario**. State valuation date, target year, and whether discounted. Future EBITDA times an exit multiple is a future value unless the method explicitly values that forecast at today's date; explain the convention.

## Forward P/E snapshot

For full deep research where earnings-based valuation is meaningful, retain all three rows:

| Metric | Multiple | Observation date / coverage | EPS window and accounting basis | Source / coverage limitation | Interpretation |
|---|---:|---|---|---|---|
| Current forward P/E | Value or unavailable | Quote/estimate timestamps | NTM, FY1 or FY2, fiscal end date; GAAP or adjusted | Provider or price/EPS calculation | Comparable or not comparable |
| 1-year high forward P/E | Value or unavailable | Rolling-year start/end and extreme date if known | Same defined historical convention | Daily series / provider-reported range / sparse sample | Verified range position only if comparable |
| 1-year low forward P/E | Value or unavailable | Rolling-year start/end and extreme date if known | Same defined historical convention | Daily series / provider-reported range / sparse sample | State missing coverage |

- NTM means next twelve months; FY1/FY2 labels vary by provider. State the actual fiscal period, not just the acronym. Record both price and estimate dates and identify stale estimates.
- Historical forward P/E requires the earnings forecast available at each historical observation. **Never divide old share-price highs/lows by today's EPS estimate and label the result historical forward P/E.** Price extrema need not coincide with multiple extrema.
- Keep complete daily extrema, a provider's reported one-year range and sparse monthly/quarterly observations distinct. A sample minimum/maximum is only an observed-sample extreme, not the true one-year extreme. A provider range with unavailable methodology remains a qualified single-source snapshot.
- Align estimate-window conventions, adjusted/GAAP basis and split/share adjustments. Flag fiscal rollovers and denominator discontinuities. Do not force a high/middle/low judgment when periods or definitions are not comparable, or assert “cheapest in a year” from sparse samples.
- If historical data cannot be obtained, write **historical range unavailable** and optionally show labeled sample observations. Missing historical data does not make a valid current P/E meaningless. If earnings are negative/unreliable or the method does not fit the business, write **Forward P/E not meaningful** and explain the alternative method.
- Cross-check when practical; otherwise label the single-source limitation. Explain whether comparable evidence suggests relative cheapness, and whether earnings revisions or business deterioration undermine that conclusion. Lower P/E alone is not a buy signal.

## Reproducible scenario contract

Full research normally includes bear/base/bull ranges; focused updates recompute only affected scenarios. If a reliable range is impossible, state **No reliable valuation range**, identify missing inputs and offer supportable operating/valuation conditions instead. Do not invent probabilities to force an expected value.

For each material scenario show:

1. Value date/horizon, current quote, units/currency, operating assumptions, multiple or discount rate, and why the assumptions are plausible. Label management guidance versus analyst assumptions. Connect execution gates to revenue timing, costs and cash generation.
2. Formula and the method-specific bridge. For an enterprise-multiple model: `enterprise value = operating metric × multiple`; `common equity = EV − debt − preferred claims − minority interests + eligible excess cash/non-operating assets`, adjusted for items already included and the model's conventions. Match claim/asset dates to the value date, and exclude restricted/customer cash unless availability to common holders is established.
3. Denominator reconciliation: current actual shares, historical weighted-average shares and scenario diluted shares, with dates. Use the denominator appropriate to the value being estimated; do not use an old EPS denominator merely because it is labeled diluted. Explain options, RSUs, convertibles and planned issuance/repurchases when material. A conversion scenario changes both claims and shares consistently.
4. SBC treatment: explain whether continuing grants are modeled as an economic expense, future net dilution or offsetting repurchase cash. Existing claims and future grants are different. Do not mechanically deduct the same modeled economic cost twice; a claim that SBC is “included in the multiple” needs an explicit rationale and sensitivity.
5. Per-share range and `(scenario price / current price) − 1`. State endpoints and pair consistent operating/multiple/claim assumptions; do not assemble favorable endpoints from incompatible cases. Future percentage price change is not an annualized return or total return; include holding period and dividends where applicable.
6. Sensitivity to the variables that actually drive the decision (typically margins, multiple/discount rate, financing and shares). Reverse valuation when supportable: what earnings, cash flow or growth does today's price require, and is that consistent with capacity, adoption and funding evidence?
7. Recompute all material arithmetic using a calculator or code. Show enough input/formula detail for replication; preserve a small calculation artifact beside the memo only when complexity warrants it. Check units, signs, endpoint ordering, discount horizon and no double counting of optionality already included in forecasts.

Discount consistently: discount future common-equity proceeds with an appropriate equity return assumption and include interim distributions if modeled; or discount enterprise cash flows to today and reconcile today's claims/assets. Do not mix a discounted future EV with undated balance-sheet figures and call it precise present fair value. If future financing/claims are unknown, label a hold-constant assumption and show its sensitivity.

Practical price zones must derive from these scenarios and business conditions, not arbitrary rounded buy/sell levels. Separate business quality, valuation attractiveness and evidence confidence.
