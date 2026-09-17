---
name: us-options-structure
description: Use when a user provides a US-listed stock or ETF ticker with listed options and asks for today's options structure, unusual option activity, large calls or puts, expiry concentration, 0DTE/1DTE activity, OI-versus-volume analysis, spread detection, or directional options positioning.
---

# US Options Structure Research

## Purpose

Analyze the current trading day's listed-options structure for one US stock or ETF. This is descriptive market-structure research, not a market-wide screener, fundamental analysis, price forecast, or trade recommendation.

If the user gives only a ticker such as `$AAPL`, `NVDA`, `TSLA`, or `SPY`, begin directly without asking follow-up questions.

Use the user's language for the report unless asked otherwise.

## Non-negotiable principles

1. **Never mix trading dates.** Previous-session data may be background only and must never appear inside today's Top Calls, Top Puts, or today's premium totals.
2. **Never confuse contract type with direction.** Call does not automatically mean bullish; Put does not automatically mean bearish.
3. **Never confuse a chain snapshot with a trade print.** Contract-level daily volume is not one trade.
4. **Never infer Buy/Sell from stale quotes.** Side inference requires an execution price and contemporaneous bid/ask, or an explicit side from a reliable source.
5. **Never force ten rows.** If only 3 valid current-day records are verifiable, show 3.
6. **Never fabricate missing fields.** Use `Unavailable` / `暂无可靠公开数据`.
7. **Separate fact, calculation, inference, and missing data.**

## Evidence labels

Use these labels when useful:

- **Verified** — directly reported by a source for the stated trading date.
- **Derived** — calculated from verified inputs using an explicit formula.
- **Inferred** — interpretation based on verified inputs but not directly reported.
- **Unavailable** — cannot be verified from available public data.

Do not present `Inferred` as `Verified`.

## Step 1 — Session gate

Before analyzing options, determine the current **US Eastern Time** and market state:

- pre-market;
- regular session;
- after-hours / post-close;
- weekend or market holiday.

Start every report with:

`As of: YYYY-MM-DD HH:MM ET — [Pre-market / Intraday / Post-close]`

Then state the **options-data cutoff** separately if it differs.

### Session rules

- **Pre-market:** there is no current-day listed-options trading yet. Do not create a "today Top 10" from yesterday's chain. Provide a pre-market setup using prior-session OI and the next expirations, clearly labeled as prior-session context.
- **Intraday:** only records explicitly attributable to the current US trading date may enter today's activity tables.
- **Post-close:** prefer completed-session data and label delayed sources if necessary.
- If a source's date is ambiguous or internally contradictory, do not use it as evidence for today's activity unless independently confirmed.

## Step 2 — Identify the instrument

Verify ticker, company/fund name, exchange, spot price, day change, and whether listed options exist.

For companies, verify the next earnings date when relevant. Flag expirations as pre-earnings, earnings week, or post-earnings only when the earnings date is reliable.

## Step 3 — Source hierarchy

Prefer, in order:

1. exchange / official options data where publicly accessible;
2. primary market-data pages with current option-chain fields;
3. established financial-data providers;
4. secondary unusual-options or aggregation sites as supporting evidence only.

Cross-check decision-critical values when practical.

If two sources materially disagree on trade date, strike, expiration, price, volume, OI, or spot:

- prefer the higher-quality / more primary source;
- state the conflict;
- lower confidence;
- exclude the conflicted item from directional totals if unresolved.

## Step 4 — Classify the available dataset

Choose exactly one primary report mode.

### Mode A — Trade-print mode

Use only when current-day individual prints/trades are available with enough fields to identify separate executions.

Output **Top Trades** ranked by Premium Notional.

### Mode B — Chain-activity mode

Use when only contract-level current-day chain data is available, such as daily Volume, OI, Bid, Ask, Last, IV.

Output **Top Contract Activity**, not "Top Trades".

A contract with Volume = 1,000 means total daily contracts for that contract, not one 1,000-lot trade.

### Mode C — Sparse-data mode

Use when current-day public data is insufficient for a credible Top Trades or Top Contract Activity table.

Output only the verified structure that exists, explicitly say `今日数据不足`, and provide the missing fields needed for a fuller report.

Do not fill gaps with prior-session activity.

## Step 5 — Premium terminology and formulas

Use precise terminology.

### Premium Notional

`Premium Notional = Contracts × Option Price × 100`

This is **option premium dollars**, not underlying stock notional.

### Underlying Notional

`Underlying Notional = Contracts × Spot Price × 100`

Do not call Premium Notional "underlying notional".

### Chain-level premium proxy

In chain-activity mode, only calculate:

`Activity Premium Proxy = Current-day Volume × Representative Current-day Option Price × 100`

when the representative price is demonstrably from the current trading day.

If Last is stale, its timestamp is unknown, or the quote is inconsistent with the trading date, do **not** multiply current volume by that Last. Rank by verified current-day Volume instead and mark premium proxy `Unavailable`.

Always label chain-level figures as a **proxy**, because daily volume may contain many trades at different prices.

## Step 6 — Top Calls and Top Puts

### Trade-print mode columns

| Rank | Evidence | Side | Strike | Expiry | Size | Trade Price | Premium Notional | Spot | Moneyness | IV | Prior OI | Time ET | Source |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|

### Chain-activity mode columns

| Rank | Evidence | Strike | Expiry | Today Volume | Prior OI | Vol/OI | Bid | Ask | Current-day Price | Premium Proxy | Moneyness | IV | Source |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|

Create separate Call and Put tables.

If fewer than 10 valid records exist, show only the available records and state the count.

## Step 7 — Side inference

Allowed labels:

- `Buy Call`
- `Sell Call`
- `Buy Put`
- `Sell Put`
- `Unknown`

Use Buy/Sell only when either:

1. a reliable source explicitly identifies the aggressor side; or
2. trade execution price and contemporaneous bid/ask are available.

For a valid spread with bid < ask, compute execution location:

`Spread Position = (Trade Price - Bid) / (Ask - Bid)`

Default interpretation:

- `>= 0.75`: ask-side / buyer-initiated **inference**;
- `<= 0.25`: bid-side / seller-initiated **inference**;
- between: `Unknown`.

Do not infer side when:

- bid/ask timestamp is not contemporaneous with the trade;
- spread is crossed, locked, zero, or abnormally wide;
- trade price lies materially outside a reliable spread without explanation;
- only daily Last is available.

## Step 8 — OI vs Volume

Treat reported OI during the trading day as the latest published OI, usually reflecting positions through the prior session rather than live intraday opening interest.

Therefore:

- `Volume > Prior OI` can be consistent with fresh activity but does not prove new opening positions;
- `Volume <= Prior OI` does not prove closing activity;
- only next-session OI changes or explicit trade-condition data can materially improve opening/closing inference.

Default wording when unconfirmed:

`无法仅凭当日 Volume 与上一期 OI 确认开仓或平仓。`

## Step 9 — Moneyness and Deep ITM

For Calls:

`Moneyness % = (Strike - Spot) / Spot × 100`

For Puts, describe distance from spot clearly rather than using an ambiguous sign convention.

When delta is available, a practical Deep ITM flag is approximately `|delta| >= 0.85`. Without delta, use strong intrinsic dominance and substantial distance through spot as a qualitative flag; do not invent a fixed threshold if the data does not support one.

Deep-ITM activity may reflect delta replacement, stock hedging, synthetic stock, rolls, dividend trades, arbitrage, or risk management. Exclude clearly ambiguous Deep-ITM activity from directional net calculations unless corroborated.

## Step 10 — Expiration concentration

Aggregate only the activity supported by the available dataset.

| Expiration | Call Premium / Proxy | Put Premium / Proxy | Directional Net | Event Flag | Coverage |
|---|---:|---:|---:|---|---|

Do not imply that a partial public feed represents total market premium.

Flag:

- 0DTE;
- 1DTE;
- weekly;
- monthly;
- pre-earnings;
- earnings week;
- post-earnings.

## Step 11 — 0DTE / 1DTE

If same-day expiration exists, create a dedicated 0DTE section.

If the nearest expiration is tomorrow, explicitly call it **1DTE**, not 0DTE.

When data permits, report:

- verified Call and Put activity;
- largest active strikes;
- spot-relative strike concentration;
- ITM/OTM distribution;
- major OI clusters.

Do not confuse OI concentration with today's traded premium.

## Step 12 — Multi-leg detection

Only call a structure `疑似` multi-leg when the evidence is meaningfully strong.

Prefer at least three of these:

- same or logically related expiration;
- near-identical contract quantity;
- close execution timestamps;
- economically coherent strike relationship;
- compatible trade prices / side pattern;
- source explicitly marks spread/complex activity.

Possible structures include vertical spreads, risk reversals, collars, straddles, strangles, calendars, diagonals, rolls, covered calls, and protective puts.

If individual trade timestamps are unavailable, do not claim that two high-volume strikes form a spread merely because sizes look similar. Use `可能相关合约，无法确认组合成交`.

## Step 13 — Raw vs Adjusted directional structure

### Raw observed premium

Report the gross observed Premium Notional or chain-level Premium Proxy separately for Calls and Puts.

### Adjusted directional premium

Exclude from directional net by default:

- `Unknown` side;
- clearly Deep-ITM ambiguous activity;
- suspected hedges;
- suspected rolls;
- confirmed or suspected multi-leg structures unless the net economics are modeled;
- stale or date-conflicted records.

### Signed directional premium proxy

For independent trades with reliable side inference:

- Buy Call = `+premium`
- Sell Put = `+premium`
- Sell Call = `-premium`
- Buy Put = `-premium`

Then:

`Net Directional Premium = Σ signed eligible premium`

This is a **directional premium proxy**, not delta exposure, gamma exposure, or expected P&L.

Also report:

- Raw Call Premium;
- Raw Put Premium;
- Eligible Directional Premium;
- Net Directional Premium;
- Unknown / Excluded Premium;
- percentage of observed premium excluded from directional inference.

If most premium is Unknown/Excluded, the final directional label must be `数据不足` even if Calls greatly exceed Puts.

## Step 14 — Weekly / expiry summary

Use one row per relevant expiration week:

| Expiry Week | Main Structure | Net Label | Evidence Quality | Why |
|---|---|---|---|---|

Allowed Net Labels:

- `看涨`
- `看跌`
- `中性`
- `数据不足`

Only use 看涨/看跌 when adjusted directional evidence is sufficiently complete. Call/Put volume or OI alone is not enough.

## Required output format

Keep the report compact and data-first.

### 1. Session & Data Coverage

State ET time, market state, spot timestamp, options-data date, report mode (A/B/C), and overall data confidence.

### 2. Structure Dashboard

Show at most 6–8 high-value items, such as:

- Spot;
- nearest expiry and DTE;
- largest verified Call activity;
- largest verified Put activity;
- most active expiration;
- Raw Call/Put premium or proxy;
- Net Directional Premium when valid;
- Unknown/Excluded share.

### 3. Top Calls

Use the correct table for the active report mode.

### 4. Top Puts

Use the correct table for the active report mode.

### 5. Expiry Map

Show expiration concentration and event flags.

### 6. Structural Checks

Cover only relevant items:

- OI vs Volume;
- 0DTE/1DTE;
- Deep ITM;
- suspected multi-leg;
- Raw vs Adjusted.

Do not create long empty sections.

### 7. Today's Structure Summary

End with 3–5 concise bullets answering:

- What is the largest verified Call activity?
- What is the largest verified Put activity?
- Where is activity concentrated by expiration/strike?
- Is there credible directional evidence after exclusions?
- What key missing data prevents stronger conclusions?

Then give one final line:

`结构标签：看涨 / 看跌 / 中性 / 数据不足`

The label must follow the evidence rules above, not intuition.

## Data confidence

Use:

- **High** — current-day trade-level prints plus contemporaneous quotes, volume, OI, and timestamps are broadly available and internally consistent.
- **Medium** — current-day chain activity is reliable, but print-level side/combination information is incomplete.
- **Low** — current-day public data is sparse, stale, contradictory, or insufficient for directional inference.

## Failure-prevention checklist

Before finalizing, verify all of the following:

- today's tables contain only today's records;
- prior-session data is clearly separated;
- no chain Volume is described as one trade;
- no stale Last is multiplied by current Volume;
- Premium Notional is not confused with underlying notional;
- Buy/Sell labels have contemporaneous evidence;
- OI is not described as live intraday OI unless the source truly provides that;
- 0DTE and 1DTE are not confused;
- suspected multi-leg structures meet the evidence threshold;
- Unknown/Excluded premium is not forced into Net Directional Premium;
- fewer than 10 valid rows are never padded with older records;
- source conflicts are disclosed and unresolved conflicted records are excluded from directional conclusions.

When public data cannot support a complete current-day report, a short accurate Mode C report is better than a detailed but misleading one.