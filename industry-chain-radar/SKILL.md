---
name: industry-chain-radar
description: Use when the user asks to discover current hot industries, find the next industry-chain transmission, map bottlenecks, second-order beneficiaries, hidden suppliers, substitutes, losers, or build an industry-chain watchlist from a theme, leader, policy, capex cycle, technology shift, or adoption curve.
license: MIT
metadata:
  hermes:
    tags: [industry-chain, supply-chain, thematic-research, bottleneck-analysis, investment-research]
---

# Industry Chain Radar

## Purpose

Turn a validated demand or narrative change into a falsifiable industry-chain map: who must spend, what becomes constrained, who supplies the constraint, who can substitute it, who loses, and which entities deserve deeper research. The radar finds links and candidates; it never turns a hot theme, token cycle, asset move, or media narrative into an investment conclusion.

## Non-negotiable evidence rules

- Verify current facts whenever the answer uses current prices, recent earnings, backlog, capex, policy, contracts, or market stage. State the as-of date.
- Cite factual claims with direct links. Prefer primary sources: company/project disclosures, filings, protocol documentation, customer disclosures, regulators, standards bodies, technical architecture, and procurement or budget documents. Use news or industry research only for context.
- For each promoted chain, include an evidence pack with several independent current sources. Explain what each source proves, what it does not prove, and how recent the source is. Thin evidence is a downgrade, not a reason to write a shorter answer.
- Keep four labels distinct: **fact** (sourced), **inference** (reasoned from facts), **assumption** (not yet verified), and **unknown** (required evidence is missing).
- Do not call an entity a beneficiary merely because it is "AI", "crypto", "metaverse", "power", "defense", or otherwise theme-adjacent. Establish the product or service, buyer/user, exposure path, and measurable confirmation metric.
- Do not use price momentum, TVL, social attention, search interest, or funding hype as the thesis. Market signals can confirm or challenge a thesis only after the causal evidence exists.
- Do not manufacture a precise theme-revenue percentage, order number, wallet/user count, customer relationship, market-share claim, or protocol usage claim. If disclosure does not isolate the exposure, say so.
- An entity can be a direct beneficiary, an indirect proxy, a signal source, a substitute, a loser, or a narrative-only name. Do not present those categories as equivalent.
- Show complete entity names. If a public company has a ticker, write the full company name first and put the ticker in parentheses, e.g. `Vertiv Holdings Co. (VRT)`. Never show only the ticker in tables or queues. For protocols, projects, private companies, and assets, use the full project/entity name and put symbols only as secondary identifiers.

## Source order and claim ledger

For every high-priority chain link, assemble the smallest useful claim ledger before ranking names:

| Required claim | Minimum proof | Examples of usable evidence |
|---|---|---|
| Demand driver is real | One primary-demand source | customer capex, budget, utilization, regulation, product adoption, on-chain usage, developer adoption |
| Bottleneck is plausible | Constraint plus reason supply cannot respond quickly | lead time, qualification, capacity, scarce input, standards, distribution, liquidity, trust, engineering cycle |
| Entity benefits | Product/service and buyer/user are connected to the bottleneck | segment disclosure, product/customer announcement, filing, protocol docs, technical architecture |
| Transmission | A metric that should move and expected lag | bookings, backlog, revenue, margin, utilization, active users, transaction volume, fees, retention, attach rate |
| Disproof | Observable failure condition | demand cut, lead-time normalization, lost design win, oversupply, substitution, fee compression, usage decay |

Use this source order:

1. Primary entity material: company/project disclosures, filings, earnings material, protocol documentation, whitepapers, technical docs, governance posts, product specifications.
2. Buyer, customer, user, or regulator material: capex, projects, budgets, procurement, policy, adoption data, chain data, developer docs, standards.
3. Technical primary material: architecture/vendor documentation, standards bodies, benchmark data, supply specifications, integration guides.
4. Competitor, substitute, and ecosystem data for cross-checking.
5. Market-data and news sources for price, breadth, attention, timing, and context.

If any of the first four ledger claims is missing, classify the link as **early observation** or **concept risk**; do not rank it as the current focus.

## Workflow

### 1. Decide discovery mode or theme mode

Use **discovery mode** when the user asks to "run this skill", "find current hot industries", "find the next industry to position for", "what comes after the current hot theme", or gives no specific starting theme.

In discovery mode, first identify 3-7 currently hot industry candidates, then choose 1-3 with the strongest transmission potential for full chain mapping. Use current sources and state the as-of date. Do not rely on attention alone.

Screen candidates across these signal buckets:

- market leadership, breadth, volume, relative strength, or funding momentum;
- leader earnings, guidance, backlog, capex, pricing, utilization, or margin expansion;
- policy, procurement, budget, regulation, standards, or subsidy changes;
- product adoption, customer deployment, app ranking, developer activity, or technical architecture change;
- on-chain usage, TVL, fees, active users, stablecoin flow, protocol revenue, or infrastructure load where relevant;
- supply stress: lead times, shortages, capacity, qualification, permitting, liquidity, distribution, or trust bottlenecks.

For each candidate, write: **why hot now**, **what first-order demand is proven**, **what could transmit next**, **what evidence is missing**, and **whether it is already too crowded**. Promote only candidates with a plausible next bottleneck; park themes that are hot but lack a transmission path.

Use **theme mode** when the user names a theme, leader, technology, policy, or capex cycle. Skip the broad scan and start from that supplied anchor.

### 2. Choose the correct starting point

Start from one observable event, not a preselected list of names:

- demand shock or customer capex cycle;
- technology transition or architecture change;
- capacity, permitting, qualification, or supply constraint;
- regulation, budget, or procurement change; or
- already-confirmed leader earnings/backlog acceleration.

Separate independent themes from true causal descendants. For example, crypto exchange revenue, AI data-center power, and metaverse devices may all be valid themes in different cycles, but one is not downstream of another unless the spending path proves it.

### 3. Map the mechanism before naming candidates

Write the causal chain in this form:

```text
Demand driver or narrative catalyst → buyer/user behavior → physical/economic/technical constraint
→ required product, service, protocol, or distribution channel → supplier/enabler/substitute
→ measurable transmission
```

For each arrow, give a concise but substantive explanation of the mechanism and one source or clearly marked inference. Ask:

- What breaks first if demand grows faster than expected?
- Why cannot supply, substitution, self-build, open-source alternatives, or protocol forks solve it quickly?
- Who actually pays, uses, stakes, deploys, or integrates, and on what cadence?
- Is the link a bottleneck with pricing power, a volume/usage beneficiary, a toll collector, a distribution gate, or only a proxy?
- What can break the transmission before it reaches this entity?

Do not force every theme into a linear chain. Branches, substitutes, and losing links belong on the map when material.

### 4. Classify entities by evidence, not familiarity

For every named company, project, protocol, product, asset, or private supplier, write the full entity name and a plain-language paragraph covering what it provides, its chain link, who buys or uses it, why it could benefit, what would prove the benefit, and what would break the thesis. Then classify it:

| Classification | Meaning | Required next step |
|---|---|---|
| Signal source | Validates upstream demand; may already be crowded | Monitor the leading metric |
| Direct beneficiary | Sells a necessary bottleneck product/service with disclosed or strongly evidenced exposure | Verify orders, revenue, margins, valuation |
| Indirect proxy | Benefits if the chain expands but exposure or pricing power is not isolated | Verify segment exposure and alternatives |
| Substitute / workaround | Benefits if the bottleneck is painful enough to force substitution | Verify adoption trigger and switching friction |
| Loser / pressure point | Hurt by the constraint, substitution, regulation, or margin shift | Verify exposure and timing |
| Early observation | Plausible mechanism, but one ledger claim is missing | Name the missing proof and monitoring date |
| Concept risk | Theme association without a proven product-to-buyer path | Do not promote without new primary evidence |

### 5. Assign stage and confidence

Assign a stage to each **link**, not just each named entity:

1. **Already exploded** — fundamentals and/or valuation have already re-rated; use as a signal source, not an early discovery claim.
2. **Second-wave confirmation** — transmission is visible, but the next operating, usage, ordering, or adoption cycle must confirm durability.
3. **Current focus** — all material ledger claims are supported and the next data point can validate or falsify the thesis.
4. **Early observation** — mechanism is plausible but evidence is incomplete.
5. **Concept risk / avoid chasing** — narrative or price leads evidence.

Use **high / medium / low** confidence. Confidence measures evidence quality and completeness, not expected return.

### 6. Use attention, market, and valuation discipline

For high-priority links, record available attention and market signals that fit the domain: public-market price and volume, private funding, search interest, app/store ranking, developer activity, on-chain usage, TVL, fees, or procurement cadence. Record the data date and do not call old data current.

Before suggesting an entity for deeper research, state the question that could invalidate an otherwise correct industry-chain thesis: peak-cycle margins, backlog conversion, customer concentration, token/value capture, unit economics, supply response, regulation, dilution, or multiple compression. Do not issue precise valuation targets or buy/sell guidance inside this skill.

## Required output contract

For a substantial radar, write and save a markdown document first, then summarize the saved result for the user with the file path. Use this order in the saved document:

1. **Research thesis and layout judgment** — several paragraphs, not a compressed summary. Explain the selected chains, why they rank above rejected hot themes, what is already proven, what is still uncertain, and how a patient investor/operator would monitor the next transmission step. Do not use a short standalone verdict section.
2. **Scope and as-of date** — market, geography, horizon, sources checked, and material data gaps.
3. **Hot-industry scan** — if in discovery mode, list candidates screened and why the final focus was chosen.
4. **Causal chain overview** — compact arrows, with parallel themes explicitly labeled.
5. **Evidence pack** — detailed source-by-source evidence for each promoted chain. For every important source, state the fact proved, date/as-of period, direct link, limitation, and how it connects to the chain.
6. **Why the starting demand is real** — sourced driver evidence; distinguish history from current facts.
7. **Bottleneck test** — constraint, supply response, buyer, substitute, and earnings/usage transmission.
8. **Candidate map** — direct beneficiary / proxy / substitute / loser / signal source / early observation / concept risk. For each high-priority entity: full name, optional ticker/symbol in parentheses, what it provides, exposure evidence, confirmation metric and date, disproof, and key risk.
9. **Stage, triggers, and failure conditions** — include specific next events or metrics, not generic "watch earnings".
10. **Final comparison table** — the mandatory columns are below.
11. **Next-research queue** — 3-5 full entity names, assets, projects, or chain links ranked by bottleneck importance, evidence quality, uncertainty, and a specific unanswered question.

| Chain link | Causal mechanism | Representative full entity name and role | Stage / confidence | Detailed evidence and source | Next confirmation | Disproof / risk | Action |
|---|---|---|---|---|---|---|---|

Do not compress the evidence into a few short bullets when the user is looking for layout or positioning research. The conclusion must survive this test: a reader can identify what would have to happen operationally or behaviorally for the entity to benefit, which data would prove it, which data would prove it wrong, and where every key factual claim came from.

## Updates and saving

Treat each radar as a dated snapshot. For substantial radar work, save by default in this repository:

```text
research/industry-chain-radar/YYYY-MM-DD-<theme-or-discovery-slug>-industry-chain-radar.md
research/industry-chain-radar/tracker.md
```

Use lowercase hyphenated slugs, e.g. `2026-07-10-current-hot-industries-industry-chain-radar.md`. Do not overwrite old radar files. Create `research/industry-chain-radar/` if it does not exist. Update `tracker.md` with the current stage, as-of date, evidence that changed, next confirmation date/metric, disproof conditions, and links to saved radar files.

Do not write to `research/INDUSTRY-CHAINS/`, `/home/ubuntu/stock-reports`, or other legacy paths unless the user explicitly requests that path.

## Common failures

- **Answer only, no saved document:** substantial radar work must save a markdown file under `research/industry-chain-radar/` and then link it in the final response.
- **Ticker instead of entity:** replace `VRT` with `Vertiv Holdings Co. (VRT)`; replace symbols-only crypto references with full protocol/project names.
- **Thin evidence:** add source-by-source evidence and limitations; if evidence is unavailable, downgrade the chain rather than shortening the analysis.
- **Compressed thesis:** replace with a multi-paragraph research judgment and layout logic.
- **Theme list instead of a chain:** remove names until every remaining entity has a product/service/protocol-to-buyer-or-user path.
- **Cycle-specific tunnel vision:** avoid writing the skill as if the current hot theme is permanent; AI, crypto, metaverse, energy, defense, biotech, and consumer cycles all require the same chain proof.
- **Correlation mistaken for causation:** add the missing mechanism, timing, and substitute; otherwise downgrade it.
- **A product announcement treated as revenue:** separate architecture, qualification, order, shipment, revenue, and margin evidence.
- **Leader's success automatically transferred downstream:** test buyer timing, contract structure, capacity, and supplier competition.
- **Stale snapshot presented as current:** label the old date or refresh primary sources and market data.
- **Correct chain, weak value capture:** keep it in the radar until deeper research proves revenue, fees, margins, token capture, or strategic value.

## Final checklist

- [ ] A markdown radar was saved under `research/industry-chain-radar/` for substantial work.
- [ ] Every high-priority link has a complete claim ledger or is explicitly downgraded.
- [ ] If no starting theme was supplied, a current hot-industry scan was performed and dated.
- [ ] Facts, inferences, assumptions, and unknowns are visibly separated.
- [ ] Every factual claim has a direct source link and current claims have an as-of date.
- [ ] Every promoted chain includes a detailed evidence pack with source limitations.
- [ ] Every named entity uses the full entity name first; ticker/symbol is secondary and parenthetical only.
- [ ] Every named entity has a concrete product/service/protocol, buyer or user, exposure path, confirmation metric, and disproof condition.
- [ ] Independent themes are not presented as downstream beneficiaries.
- [ ] Market, attention, and usage signals are confirmation only.
- [ ] The final table and a ranked next-research queue are present.
