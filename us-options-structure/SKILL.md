---
name: us-options-structure
description: Use when a user provides a US-listed stock or ETF ticker with listed options and wants a compact current-day options table with strike, expiration, DTE, option price, IV, and Put premium yield / annualized yield.
---

# US Options Structure Research

## Purpose

Analyze the current trading day's listed-options structure for one US stock or ETF and return a **single compact table**.

This is descriptive market-structure research, not fundamental analysis, a price forecast, or a trade recommendation.

If the user gives only a ticker such as `$AAPL`, `NVDA`, `TSLA`, or `SPY`, begin directly without asking follow-up questions.

Use the user's language unless asked otherwise.

## Core rules

1. Never mix trading dates. Previous-session data may be used only when clearly labeled as prior-session context.
2. Never fabricate missing values.
3. Calls and Puts must appear in the **same table**.
4. Keep prose minimal. The table is the main output.
5. Do not output extra analytical sections unless the user explicitly asks for them.
6. If a source date is ambiguous or contradictory, exclude that contract from the main table.
7. If current-day option prices cannot be verified, say `今日数据不足` rather than filling the table with stale prices.

## Session gate

Determine current US Eastern Time and market state first.

Start with one short line:

`As of: YYYY-MM-DD HH:MM ET — Pre-market / Intraday / Post-close`

Rules:

- Pre-market: there is no current-day listed-options trading yet. Use prior-session chain only if clearly labeled.
- Intraday: only current-day prices may enter the main table.
- Post-close: prefer completed-session data.
- If a source's date is unclear, do not use it in the main table.

## Source priority

Prefer, in order:

1. exchange / official option-chain data;
2. primary market-data pages with current option-chain fields;
3. established financial-data providers;
4. unusual-options aggregators only as supporting evidence.

Cross-check current-day option prices when practical.

## Contract selection

The final answer should be useful rather than exhaustive.

Default target: up to 20 contracts total.

Use current-day activity internally to choose the most relevant contracts, considering where available:

- trading activity;
- proximity to spot;
- near-term expirations;
- unusual implied volatility;
- meaningful Call or Put concentration.

These ranking inputs are internal selection signals and should **not** be added as table columns.

Include both Calls and Puts when meaningful contracts exist on both sides.

Do not pad the table with stale contracts just to reach a target count.

## Option price

The `期权价格` column must use a price attributable to the current trading day.

Prefer, in order:

1. a verified current-day trade/last price;
2. a reliable current-day mark or midpoint when clearly identified;
3. another clearly current-day representative option price from a reputable source.

Do not use a stale Last from a prior trading day to calculate Put yield.

If a current-day option price cannot be verified, use `N/A`.

## DTE

`DTE` means calendar days remaining until expiration.

- Expiring today: `DTE = 0`.
- Expiring tomorrow: `DTE = 1`.

Use the US trading date when calculating DTE.

## Put yield calculations

The `收益率` and `年化收益率` columns are **Put-only metrics**.

For Call rows:

- 收益率 = `N/A`
- 年化收益率 = `N/A`

For Put rows, when Strike, valid current-day option price, and DTE are available:

### Put premium yield

`收益率 = Option Price / Strike × 100%`

Example:

- Strike = $50
- Put price = $2

`收益率 = 2 / 50 × 100% = 4.00%`

### Annualized Put premium yield

For `DTE > 0`:

`年化收益率 = 收益率 × 365 / DTE`

Example with DTE = 30:

`年化收益率 = 4.00% × 365 / 30 = 48.67%`

For `DTE = 0`:

`年化收益率 = N/A`

### Interpretation

For a Put, these two fields represent the option premium as a percentage of strike-based cash-secured capital and its simple annualized equivalent.

They are most naturally interpreted from a Sell Put / cash-secured Put perspective, but the table does not need a separate direction column.

These are simple gross yield metrics and do not include commissions, taxes, margin treatment, early assignment, opportunity cost, collateral interest, mark-to-market changes, or compounding.

Only calculate them from a current-day option price. If the price is stale or uncertain, use `N/A`.

## Main output table

The report should primarily consist of **one table** combining Calls and Puts.

Use this exact column order:

| 类型 | Strike | 到期日 | DTE | 期权价格 | IV | 收益率 | 年化收益率 | 数据状态 |
|---|---:|---|---:|---:|---:|---:|---:|---|

### Column rules

- 类型: `Call` or `Put`.
- Strike: option strike.
- 到期日: expiration date.
- DTE: calendar days to expiration.
- 期权价格: verified current-day option price.
- IV: implied volatility when available.
- 收益率: Put only; Calls show `N/A`.
- 年化收益率: Put only; Calls show `N/A`; 0DTE shows `N/A`.
- 数据状态: short labels only, such as `Verified`, `Stale price`, `Date conflict`, or `N/A`.

Do **not** add these columns unless the user explicitly asks:

- 方向;
- Volume;
- OI;
- Vol/OI;
- Premium / Proxy;
- 现货价;
- ITM/OTM.

## Formatting

Keep the answer visually compact.

Default format:

1. one short `As of` line;
2. the single table;
3. at most one short sentence after the table.

Do not create separate Dashboard, Top Calls, Top Puts, Expiry Map, OI analysis, Structural Checks, Raw vs Adjusted, or long narrative sections unless explicitly requested.

When useful, order the table by expiration first and then Strike, or by relevance if current-day activity clearly identifies the most important contracts.

## Failure-prevention checklist

Before finalizing, verify:

- table rows belong to the correct trading date;
- stale option prices are not presented as current-day prices;
- Call yield columns are `N/A`;
- Put yield uses `Option Price / Strike`;
- annualized Put yield uses `Yield × 365 / DTE`;
- 0DTE annualized yield is `N/A`;
- missing values are shown as `N/A` instead of invented;
- no removed columns reappear unless explicitly requested;
- the final answer stays focused on the one compact table.

Prefer a short, accurate table over a long narrative report.