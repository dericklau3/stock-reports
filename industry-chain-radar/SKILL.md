---
name: industry-chain-explosion-radar
description: Use when discovering US-stock opportunities by starting from already-exploded industries or leading stocks, mapping supply-chain bottlenecks and second/third-order beneficiaries, and identifying the next potential industry or stock group to research. Avoid simple rule-based stock screening as the primary approach.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, equity-research, industry-chain, thematic-investing, us-stocks]
    related_skills: [us-equity-research]
---

# Industry Chain Explosion Radar

## Overview

Use this skill to find potential US-stock opportunities through industry-chain transmission rather than simple technical stock screening.

The core pattern is:

1. A leading stock or industry proves demand is real.
2. The market asks which bottleneck the leader's growth creates.
3. Second-order supply-chain beneficiaries begin to re-rate.
4. Third-order suppliers, infrastructure providers, or hidden beneficiaries may follow.
5. The agent identifies what has already exploded, what is in second-wave confirmation, and what deserves next deep research.

Example pattern:

- AI GPU demand explodes → NVDA validates the primary trend.
- GPU scale creates HBM/DRAM demand → MU, WDC, STX, SNDK re-rate.
- AI clusters need high-speed interconnect → ANET, MRVL, COHR, LITE, AAOI, CIEN become relevant.
- Bigger data centers need power, cooling, construction, and grid upgrades → VRT, GEV, PWR, ETN, EME, HUBB, GRID become next-chain candidates.

The goal is not to ask “which stock is up today?” The goal is to ask:

> Which industry has already been validated by a leader, where is the next bottleneck, and which companies have not yet been fully priced for that bottleneck?

## When to Use

Use this skill when the user asks for:

- “下一轮爆发行业” / next explosive industry.
- Opportunities after a leader or sector has already rallied.
- Industry-chain mapping after a major stock such as NVDA, LLY, AVGO, VRT, or another leader breaks out.
- Identifying second-order beneficiaries, hidden suppliers, bottleneck links, or follow-on trades.
- Distinguishing already-exploded themes from next-wave candidates.
- A document or watchlist under `/home/ubuntu/stock-reports` about industry/theme opportunity discovery.

Do not use this as the main framework when the user asks only for a deep research memo on a specific company; use `us-equity-research` for that.

## Required Output Discipline

The user does **not** want a report that is mostly methodology, generic buckets, or disconnected ticker lists. The required shape is a **causal industry-chain explosion map**:

1. **Start with the already-exploded leader/industry** and explain in plain language why it exploded: demand shock, customer capex, shortage, regulation, technology transition, margin expansion, or guidance/backlog evidence.
2. **Trace the transmission chain step by step**: “Because A exploded, B becomes scarce/necessary; because B scales, C becomes the next bottleneck; because C bottlenecks, D companies may see orders/pricing/margin.” Do not jump from theme to tickers without the causal link.
3. **Explain why the next industry could explode**: name the specific bottleneck, who must buy it, why supply cannot instantly respond, and what evidence would confirm it.
4. **Name representative tickers only after the chain logic is clear**. For each ticker, explain what the company actually does in one beginner-friendly sentence and exactly where it sits in the chain.
5. **End with a visual summary table**. The final table is mandatory and should let the user compare: chain link, why it may explode, representative tickers, what each company does, current stage, confirmation evidence, key risk, and next action.

Always separate these five buckets:

1. **Already exploded**: the primary leader or chain has already been re-rated. It can remain a signal source, but avoid presenting it as early discovery.
2. **Second-wave confirmation**: related companies have already moved but may have a second leg if earnings confirm.
3. **Current next-chain focus**: the most plausible next bottleneck or supply-chain layer.
4. **Early observation**: plausible but not yet confirmed by price, orders, or fundamentals.
5. **Concept risk / avoid chasing**: stocks or themes rising mainly on narrative without evidence.

Never present “strong price momentum” alone as the thesis. Momentum is only a confirmation signal after industry logic and fundamental transmission are identified.

### Mandatory Causal-Chain Output Template

Every saved radar document or substantial answer must include these sections in this order:

1. **一句话结论**: which chain is most likely to be next, and why.
2. **爆发链条总览**: a compact arrow chain, e.g. `AI 训练/推理需求爆发 → GPU/ASIC → HBM/封装 → 光模块/交换机 → 电力/散热/电网 → 发电资产`.
3. **第一环为什么已经爆发**: evidence from leaders such as revenue, backlog, guidance, capex, shortages, margins, or stock re-rating.
4. **第二环/下一环为什么可能爆发**: the mechanical reason, not just correlation. Use “谁的需求增加 → 哪个瓶颈出现 → 谁卖这个瓶颈 → 订单/利润如何体现”.
5. **代表标的解释**: grouped by chain link. For each ticker include: company does what, revenue exposure, why it benefits, what would confirm, why it could fail.
6. **阶段判断**: classify each link as already exploded, second-wave confirmation, current next-chain focus, early observation, or concept risk.
7. **最终直观总表**: mandatory comparison table with columns:
   - 产业链环节
   - 爆发原因 / 传导逻辑
   - 代表标的
   - 公司是做什么的
   - 当前阶段
   - 需要验证的数据
   - 主要风险
   - 下一步动作
8. **下一步深研清单**: top 3-5 tickers to run `us-equity-research` on, ranked by chain importance + evidence + valuation uncertainty.

Completion criterion: a user should be able to read only the arrow chain plus final table and understand why one industry exploded, why the next industry might explode, what the representative companies actually do, and what data must confirm the thesis.

## Workflow

### 1. Identify validated primary trends

Start with industries or leaders that have already proven demand through:

- Revenue acceleration.
- Order/backlog/bookings growth.
- Guidance raises.
- Capex increases from major customers.
- Product shortages or longer delivery times.
- Margin expansion from tight supply.
- Sustained stock leadership versus SPY/QQQ and peers.

Completion criterion: list the primary leader(s), why the demand is real, and whether the leader is already crowded or still useful as a signal source.

### 2. Map the value chain

For each validated primary trend, draw the chain:

- Customer demand driver.
- Primary product or service.
- Critical suppliers.
- Bottleneck components.
- Manufacturing/equipment dependencies.
- Infrastructure dependencies.
- Energy, logistics, data, software, security, or service layers.
- Companies at each link.

Completion criterion: every candidate company must be tied to a concrete value-chain function, not merely “related to the theme.”

### 3. Ask the bottleneck question

For each chain, ask:

- If the leader doubles demand, what breaks first?
- Which input has limited supply?
- Which component has long qualification cycles?
- Which supplier has pricing power?
- Which service must scale before the primary trend can continue?
- Which company’s revenue should lag the leader by one or two quarters?

Completion criterion: identify one to three bottleneck links that are plausible next-wave candidates.

### 4. Check market transmission

Use current data when possible. Compare:

- 1-month, 3-month, and 6-month returns.
- Performance versus SPY/QQQ and sector ETFs.
- Distance to 52-week highs.
- Whether leaders and second-tier companies are moving together.
- Whether smaller or hidden suppliers are starting to participate.
- Whether volume or breadth is improving.

Completion criterion: classify each link as already exploded, second-wave confirmation, current next-chain focus, early observation, or concept risk.

### 5. Check fundamental confirmation

For each high-priority candidate, look for:

- Revenue from the relevant theme.
- Backlog, bookings, RPO, ARR, book-to-bill, or order growth.
- Management commentary naming the demand driver.
- Guidance raises.
- Gross margin or operating margin improvement.
- Capex and capacity expansion.
- Customer concentration and contract duration.
- Supply constraints or pricing power.

Completion criterion: state whether the thesis is confirmed, partially confirmed, or still speculative.

### 6. Build the radar document

When asked to save a report, use this path pattern:

```text
/home/ubuntu/stock-reports/cn/industry-chain-radar/YYYY-MM-DD-next-wave-industry-chain-radar.md
```

Include:

- Methodology.
- Data sources and limitations.
- Already exploded chains.
- Current next-chain focus.
- Industry-by-industry candidate maps.
- Priority ranking.
- Trigger conditions.
- Failure conditions.
- Next deep-research candidates.

Completion criterion: the saved document must make clear which sectors are already past the early stage and which sector deserves the user's current attention.

## Sector Playbooks

### AI infrastructure playbook

Typical sequence:

1. GPU/accelerators: NVDA, AMD, AVGO, custom ASICs.
2. Foundry/equipment: TSM, ASML, AMAT, LRCX, KLAC.
3. HBM/DRAM/storage: MU, WDC, STX, SNDK and non-US peers.
4. Network/interconnect/optics: ANET, MRVL, AVGO, COHR, LITE, AAOI, CIEN.
5. Power/cooling/data-center infrastructure: VRT, ETN, GEV, PWR, EME, HUBB, GRID.
6. Power generation/assets/grid: CEG, VST, NEE, nuclear/uranium names, grid suppliers.
7. Software/security/app monetization: only upgrade when revenue evidence appears.

Key question: after the current strongest AI link, which physical or economic bottleneck prevents the next scale-up?

### GLP-1 playbook

Primary leaders: LLY, NVO.

Potential second-order links:

- Injection devices.
- CDMO and fill-finish capacity.
- Packaging and cold-chain logistics.
- Pharmacy and distribution.
- Diagnostics and follow-up care.
- Potential losers: insulin, dialysis, obesity-related device/procedure chains, selected food categories.

Key question: which companies show actual revenue exposure to GLP-1 volume growth, not just narrative exposure?

### Defense / aerospace / drone playbook

Primary drivers:

- Defense budgets.
- Missile/interceptor demand.
- Drone and counter-drone demand.
- Radar, sensors, electronic warfare.
- Aerospace engine and component supply chains.

Candidate layers:

- Large primes: LMT, RTX, NOC, GD.
- ETFs/breadth: ITA, XAR, PPA.
- Component suppliers: HWM and other aerospace suppliers.
- Higher-risk small caps: KTOS, AVAV and related drone/electronic-warfare names.

Key question: are smaller suppliers beginning to show order/backlog confirmation, or is the move still concentrated in large primes?

### Nuclear / power playbook

Potential links:

- Nuclear operators and power assets: CEG, VST, NEE.
- Uranium: CCJ, UEC, URA.
- Nuclear equipment/services: BWXT.
- SMR/high-risk concepts: SMR and peers.
- Grid: GRID and electrical equipment suppliers.

Key question: is the market buying direct power/equipment beneficiaries, or has it actually rotated into nuclear/uranium yet?

## Trigger Conditions

Upgrade a theme when several of these appear together:

- Primary leader keeps raising guidance.
- Capex from major customers increases.
- Bottleneck supplier reports order acceleration.
- Gross margin expands rather than contracts.
- Theme ETF or basket beats SPY/QQQ over 1-3 months.
- Second-tier names start outperforming primary leaders.
- Previously ignored suppliers begin mentioning the theme in earnings calls.
- Analyst estimates begin to rise after company evidence, not before.

## Failure Conditions

Downgrade a theme when:

- Primary leader misses guidance or capex slows.
- Bottleneck turns out not to be scarce.
- Revenue does not transmit to second-order suppliers.
- Gross margin compresses from competition or oversupply.
- The move spreads only to low-quality concept stocks while core companies weaken.
- Valuations require unrealistic growth or permanent peak margins.
- Dilution, debt, or weak balance sheets dominate the risk/reward.

## Common Pitfalls

1. **Starting from price screens.** Price strength is confirmation, not the source of the thesis.
2. **Calling an already-exploded chain “early.”** If a basket is up hundreds of percent, classify it as already exploded or second-wave only.
3. **Confusing narrative exposure with revenue exposure.** A company must sell something necessary to the bottleneck.
4. **Ignoring lags.** Second-order revenue may appear one or two quarters after the primary leader’s demand signal.
5. **Overlooking supply response.** If everyone can add capacity quickly, the bottleneck may not produce durable profits.
6. **Forgetting losers.** Some second-order themes create negative read-throughs for incumbents.
7. **Skipping company-level research.** A radar candidate is not buyable until deep research confirms business quality, valuation, risks, and portfolio fit.
8. **Treating a confirmed bottleneck as an immediate buy.** Strong industry transmission can identify the right company but still fail as an investment if valuation already discounts several years of flawless execution. After a candidate is promoted from radar to company research, switch to `us-equity-research` and require explicit bear/base/bull valuation, price zones, one-time item cleanup, and portfolio-fit checks.

## Radar-to-Deep-Research Handoff

When a radar output identifies a top candidate such as an AI data-center power/grid beneficiary, do not stop at the theme. The next step should be a company-level memo under `research/COMPANIES/TICKER/` using `us-equity-research`. For industrial infrastructure names, the deep dive should verify orders, RPO/backlog, book-to-bill, segment margins, project execution risk, capex, cash conversion, and whether GAAP earnings include one-time tax/M&A gains. A useful case-study reference exists in `us-equity-research/references/gev-power-infrastructure-case-study.md`.

## Verification Checklist

Before finalizing an industry-chain radar answer:

- [ ] Identified which industry/leader has already exploded.
- [ ] Explained the value-chain transmission in plain language.
- [ ] Separated already exploded, second-wave, next-chain focus, early observation, and concept risk.
- [ ] Included current market evidence when available, with data limitations stated.
- [ ] Checked or listed the fundamental evidence needed: orders, revenue, margin, guidance, capex.
- [ ] Named trigger conditions and failure conditions.
- [ ] Recommended the next deep-research candidates rather than presenting candidates as immediate buys.
- [ ] If saving a report, wrote it under `/home/ubuntu/stock-reports/cn/industry-chain-radar/`.
