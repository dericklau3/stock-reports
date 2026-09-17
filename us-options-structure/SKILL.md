---
name: us-options-structure
description: Use when a user provides a US-listed stock or ETF ticker with listed options and asks for current-day option structure, large option activity, expiry concentration, 0DTE activity, spread detection, or call/put positioning analysis.
---

# US Options Structure Research

## Scope

Analyze the current-day listed-options structure for one US stock or ETF. This is descriptive market research only: not a market-wide screener, not fundamental analysis, not a price forecast, and not a recommendation to enter or exit a position.

If the user gives only a ticker such as `$AAPL`, `NVDA`, `TSLA`, or `SPY`, begin directly.

## Core rule

Never infer market direction from contract type alone. A Call is not automatically bullish and a Put is not automatically bearish. Deep-ITM contracts, rolls, hedges, synthetic positions, and multi-leg combinations must be separated from simple directional interpretation.

Analyze:

`trade-side inference × strike × expiration × premium × OI × volume × moneyness × multi-leg relationship`.

## Sources and verification

Use current public web data. Prefer Cboe, Nasdaq, Yahoo Finance, Barchart public pages, company investor-relations pages, SEC filings, and other reputable public options-chain sources.

Do not invent volume, OI, bid, ask, last, IV, trade time, trade price, contract size, earnings date, or premium notional.

If a field cannot be verified, state `暂无可靠公开数据` or `数据不足，无法判断`.

Cite important numeric claims when citations are supported. If true tick-by-tick tape is unavailable, state that the report uses public option-chain, volume, OI, bid/ask, and available trade data and is not equivalent to an institutional real-time options tape.

## Initial snapshot

Report ticker, company/fund name, analysis date, current spot price, day change, next earnings date when applicable, and whether the stock is in or near earnings week.

## Top contracts

Produce Top 10 Calls and Top 10 Puts, ranked primarily by premium notional:

`Premium Notional = Contracts × Option Trade Price × 100`

For each contract include, when available: inferred side, strike, expiration, size/volume, trade or last price, premium notional, spot, ITM/OTM percentage, IV, OI, Volume/OI, time, and source.

### Side inference

Use bid/ask only as an inference:

- price near ask: more consistent with buyer-initiated activity;
- price near bid: more consistent with seller-initiated activity;
- price near midpoint: direction uncertain.

Labels may be `Buy Call`, `Sell Call`, `Buy Put`, `Sell Put`, or `Unknown`. Never present this inference as certain unless the source explicitly identifies the side.

## A. Expiration concentration

Aggregate major premium by expiration:

| Expiration | Call Notional | Put Notional | Net Structure | Event Flag |
|---|---:|---:|---|---|

Flag 0DTE, weekly, monthly, pre-earnings, earnings week, and post-earnings expirations.

## B. OI vs volume

Compare current volume with prior OI. Volume materially above OI can be consistent with fresh positioning but does not prove opening activity. Volume near or below OI may include closing trades, rolls, or activity in existing positions.

Unless stronger evidence exists, state: `无法仅凭公开数据确认开仓/平仓性质。`

## C. Deep ITM handling

Flag clearly deep-ITM Calls and Puts. Possible explanations include delta replacement, stock hedging, synthetic stock, rolls, dividend trades, arbitrage, and risk management.

When appropriate label them `可能为对冲 / 展期 / 套利结构` and do not let them dominate directional interpretation without corroborating evidence.

## D. 0DTE structure

If same-day expiration exists, create a dedicated section with Call premium, Put premium, largest Call strike, largest Put strike, main strike concentration, and ITM/OTM distribution when data permits.

Even if last price is unavailable, identify relevant 0DTE contracts when public data confirms their existence.

## E. Multi-leg detection

Look for possible relationships using same expiration, similar execution time, similar contract count, neighboring/logically paired strikes, and matching size.

Possible structures include Call/Put vertical spreads, risk reversals, collars, straddles, strangles, calendar spreads, diagonal spreads, rolls, covered calls, and protective puts.

Use `疑似` unless evidence is strong enough to establish the relationship.

## F. Raw vs adjusted structure

Report:

- Raw Call Notional;
- Raw Put Notional;
- Adjusted Call Notional;
- Adjusted Put Notional;
- Net Directional Notional;
- Unknown-Direction Notional.

Raw figures include all major observed premium. Adjusted figures should separate or discount clearly ambiguous structures such as deep-ITM trades, hedges, rolls, vertical spreads, collars, multi-leg combinations, and unknown-side activity.

For directional accounting only, treat buyer-initiated Calls and seller-initiated Puts as positive directional exposure, and seller-initiated Calls and buyer-initiated Puts as negative directional exposure. Do not force unknown-side transactions into the net number.

Explain why Raw and Adjusted figures differ.

## Weekly expiry summary

Create one row per relevant expiration week:

| Expiry Week | Call Structure | Put Structure | Net Structure | Data Quality | Reasoning |
|---|---|---|---|---|---|

Allowed Net Structure labels: `看涨`, `看跌`, `中性`, `数据不足`.

Base the label on adjusted net structure, not simple Call/Put volume.

## Final summary

Finish with `今日结构总结` covering:

1. Largest Call structure.
2. Largest Put structure.
3. Expiration with the most concentrated premium.
4. Meaningful 0DTE structure, if any.
5. Suspected multi-leg structures.
6. Notable deep-ITM, hedge, or roll patterns.
7. Difference between Raw and Adjusted Notional.
8. Expiry weeks with the clearest net structure.
9. Data worth monitoring next.

Then provide a 3–6 sentence `结构结论` describing the observed options structure only. Do not give trade recommendations, price targets, stop-loss levels, or instructions to go long or short.

## Data confidence

End with `数据可信度`:

- 高: bid/ask/last/volume/OI/time are broadly available and consistent.
- 中: option-chain, volume, and OI are available but trade-level direction is incomplete.
- 低: public data is insufficient to infer direction or structure reliably.

Always separate verified facts from inference. For institutional intent, opening/closing status, hedging, rolling, and multi-leg attribution, use uncertainty language such as `可能`, `疑似`, `更接近`, or `无法确认`.

Keep the report focused on today's options structure. When data is incomplete, prefer an explicit limitation over a fabricated number.