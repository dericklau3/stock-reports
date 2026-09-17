---
name: us-options-structure
description: Use when a user provides a US-listed stock or ETF ticker with listed options and wants a compact current-day options table, including calls, puts, volume, OI, premium, moneyness, IV, and put premium yield / annualized yield.
---

# US Options Structure Research

## Purpose

Analyze the current trading day's listed-options structure for one US stock or ETF and return a **single compact table**.

This is descriptive market-structure research, not a market-wide screener, fundamental analysis, price forecast, or trade recommendation.

If the user gives only a ticker such as `$AAPL`, `NVDA`, `TSLA`, or `SPY`, begin directly without asking follow-up questions.

Use the user's language unless asked otherwise.

## Core rules

1. Never mix trading dates. Previous-session data may be used only as clearly labeled background.
2. Never describe contract-level daily Volume as one trade.
3. Never infer Buy/Sell from stale Last versus current Bid/Ask.
4. Never fabricate missing values.
5. If fewer than 10 valid current-day contracts are available, show only the available rows.
6. Calls and Puts must appear in the **same table**.
7. Keep prose minimal. The table is the main output.

## Session gate

Determine current US Eastern Time and market state first.

Start with one short line:

`As of: YYYY-MM-DD HH:MM ET — Pre-market / Intraday / Post-close`

Rules:

- Pre-market: no current-day listed-options trading yet. Use prior-session chain only if clearly labeled.
- Intraday: only current-day records may enter the main table.
- Post-close: prefer completed-session data.
- If a source date is ambiguous or contradictory, exclude that row from the main table.

## Source priority

Prefer:

1. exchange / official option-chain data;
2. primary market-data pages with current chain fields;
3. established financial-data providers;
4. unusual-options aggregators only as supporting evidence.

If current-day data cannot be verified, say `今日数据不足` rather than filling the table with older activity.

## Dataset modes

### Trade-print mode

Use when current-day individual option executions are available.

Rank primarily by verified Premium:

`Premium = Contracts × Trade Price × 100`

### Chain-activity mode

Use when only current-day option-chain activity is available.

Daily Volume is aggregate contract activity, not one trade.

If a representative current-day option price is verified, calculate:

`Premium Proxy = Today Volume × Current-day Option Price × 100`

Label it as `Premium Proxy`, not as one trade's premium.

If current-day option price cannot be verified, leave Premium as `N/A` and rank primarily by Volume.

## Buy / Sell direction

Allowed labels:

- Buy Call
- Sell Call
- Buy Put
- Sell Put
- Unknown

Only infer Buy/Sell when either:

- a reliable source explicitly identifies the aggressor side; or
- execution price and contemporaneous Bid/Ask are available.

Otherwise use `Unknown`.

Do not infer side from a stale Last price.

## OI and Volume

Treat intraday OI as the latest published OI, normally reflecting positions through the prior session.

`Volume > OI` may indicate fresh activity but does not prove opening positions.

Do not claim opening/closing status unless stronger evidence exists.

## Moneyness

For Calls:

`OTM % = max(Strike - Spot, 0) / Spot × 100`

For Puts:

`OTM % = max(Spot - Strike, 0) / Spot × 100`

If ITM, display `ITM` plus the corresponding percentage distance through spot.

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

Then:

`收益率 = 2 / 50 × 100% = 4.00%`

### Annualized put premium yield

For DTE > 0:

`年化收益率 = 收益率 × 365 / DTE`

Example with DTE = 30:

`年化收益率 = 4.00% × 365 / 30 = 48.67%`

For 0DTE:

`年化收益率 = N/A`

### Interpretation

When the direction is `Sell Put`, this approximates the gross option-premium yield relative to strike-based cash-secured capital.

When the direction is `Buy Put` or `Unknown`, the same numeric ratio may still be displayed for comparison, but it must not be described as an earned return. It is only the option premium as a percentage of strike.

These metrics do not include:

- commissions;
- margin treatment;
- early assignment;
- opportunity cost;
- interest on collateral;
- taxes;
- mark-to-market changes;
- compounding.

Only calculate these metrics using a current-day option price. If the price is stale or its date is unclear, use `N/A`.

## Main output table

The report should primarily consist of **one table** combining Calls and Puts.

Use this exact column order when data is available:

| 类型 | 方向 | Strike | 到期日 | DTE | 期权价格 | Volume | OI | Vol/OI | Premium / Proxy | 现货价 | ITM/OTM | IV | 收益率 | 年化收益率 | 数据状态 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---|

### Column rules

- 类型: `Call` or `Put`.
- 方向: Buy Call / Sell Call / Buy Put / Sell Put / Unknown.
- Strike: option strike.
- 到期日: expiration date.
- DTE: calendar days to expiration.
- 期权价格: verified current-day trade price or current-day representative chain price.
- Volume: current-day volume.
- OI: latest published OI.
- Vol/OI: `Volume / OI`; if OI = 0 or unavailable, use `N/A`.
- Premium / Proxy: real trade Premium in trade-print mode; Premium Proxy in chain mode; otherwise `N/A`.
- 现货价: spot price used for moneyness calculation.
- ITM/OTM: status plus percentage distance.
- IV: implied volatility when available.
- 收益率: Put only; Calls show `N/A`.
- 年化收益率: Put only; Calls show `N/A`; 0DTE shows `N/A`.
- 数据状态: use short labels such as `Verified`, `Derived`, `Unknown side`, `Stale price`, or `Date conflict`.

## Row selection and ordering

Keep the table useful rather than exhaustive.

Default target: up to 20 rows total.

Prefer rows with the strongest combination of:

1. current-day Volume;
2. Premium / Premium Proxy;
3. Volume relative to OI;
4. proximity to spot;
5. near-term expiration relevance;
6. unusual IV or activity when clearly supported.

Include both Calls and Puts when meaningful activity exists on both sides.

Do not pad the table with stale rows merely to reach a target count.

## Optional one-line summary

After the table, add at most 1–2 concise sentences summarizing only the most obvious structure, for example:

- which expiry / strike has the most activity;
- whether activity is concentrated in Calls or Puts;
- which Put contracts have the highest premium yield / annualized yield;
- whether data quality prevents directional interpretation.

Do not create separate Dashboard, Top Calls, Top Puts, Expiry Map, Structural Checks, or long narrative sections unless the user explicitly asks for them.

## Failure-prevention checklist

Before finalizing, verify:

- main-table rows belong to the correct trading date;
- prior-session data is not mixed into today's rows;
- daily Volume is not described as one trade;
- stale Last is not multiplied by current Volume;
- Buy/Sell labels have contemporaneous evidence;
- Call yield columns are `N/A`;
- Put yield uses `Option Price / Strike`;
- annualized Put yield uses `Yield × 365 / DTE`;
- 0DTE annualized yield is `N/A`;
- stale or ambiguous option prices do not produce yield values;
- missing values are shown as `N/A` instead of invented.

Prefer a short, accurate table over a long narrative report.