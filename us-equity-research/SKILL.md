---
name: us-equity-research
description: Use this skill to perform professional US equity research for selected US-listed public companies, while explaining every researched company's products, technical terms, business model, and profit engine in plain beginner-friendly language. Default every ticker or company request to deep company research. Use post-earnings tracking when the user asks about earnings, quarterly results, guidance, 10-Q, shareholder letters, or earnings calls. Trigger on prompts such as "Analyze TICKER", "Deep analysis of COMPANY", "Analyze TICKER's latest earnings", "Track COMPANY after earnings", or "Explain how COMPANY makes money".
---

# US Equity Research Skill

## Purpose

Use this skill to analyze selected US-listed public companies for medium-term and long-term investment research. The user has already chosen the stocks worth studying. The default output is a deep company research memo. If the prompt is about earnings, quarterly results, guidance, or a recent filing, use post-earnings tracking.

Default supported tasks:

- Produce a deep company research memo for a selected stock.
- Track the company after earnings or major financial updates.
- Reassess the thesis, valuation, risks, and monitoring points.
- Estimate valuation ranges when assumptions and sources are clear. For deep research, the default expectation is that bear/base/bull scenarios include explicit implied share-price or valuation ranges, unless the security type or missing data makes a range unreliable.

Default investment horizons:

- Medium term: several weeks to several months.
- Long term: more than one year.

## Guardrails

Follow these rules strictly:

- Do not invent financial data, valuation multiples, management quotes, guidance, analyst ratings, or news.
- Do not use stale financials when the user asks for current analysis, latest earnings, or valuation.
- Browse or otherwise verify current facts for market price, recent company materials, earnings dates, guidance, valuation multiples, SEC filings, and analyst updates whenever the answer depends on recent information.
- Cite the sources used for factual claims. Prefer primary sources over secondary commentary.
- Separate facts, estimates, assumptions, and opinion.
- Do not give a price target, fair value, or valuation range without showing the assumptions behind it.
- Do not use one valuation method for every company. Match the valuation method to the company's stage, profitability, cyclicality, and sector.
- Do not treat adjusted EBITDA, non-GAAP EPS, or free cash flow as clean without checking stock-based compensation, working capital, capitalized costs, and one-time items.
- Do not ignore downside scenarios, dilution, debt, competitive pressure, margin risk, customer concentration, regulation, or management credibility.
- Do not frame the output as personalized financial advice. Present it as research support and decision framing.
- When using named investor perspectives, frame them as Buffett-style, Munger-style, Duan Yongping-style, and Li Lu-style analytical lenses. Do not claim to know what those investors would personally buy, sell, or think today unless directly sourced.

## Source Priority

Use the best available sources for the question:

1. Company investor relations: earnings release, shareholder letter, presentation, 10-K, 10-Q, 8-K, annual report, guidance.
2. SEC filings and official transcripts where available.
3. Market data sources for price, market cap, valuation multiples, and historical performance.
4. Reputable financial news for recent catalysts.
5. Analyst rating changes only as supporting context, not as the core thesis.
6. Industry data and competitor filings when needed to benchmark growth, margins, and valuation.

If a required source is unavailable, say what is missing and lower confidence accordingly.

### SEC Filing Retrieval Pattern

For newly listed companies, recent IPOs, post-earnings updates, or cases where the earnings release is filed as an exhibit rather than embedded in the 8-K body:

- Use SEC company tickers to resolve the CIK, then inspect `https://data.sec.gov/submissions/CIK##########.json` for recent filings.
- For a filing accession, check the filing directory `index.json`, because earnings releases and presentations often appear as `EX-99.1`, `final_*.htm`, `ex99*.htm`, or similar exhibits that are not obvious from the primary 8-K document.
- Extract text from the exhibit and quote the filing/exhibit source in the memo when using KPI, guidance, or management-commentary data.
- For recent IPOs, compare S-1 / 424B4 disclosures with the first 10-Q/10-K after listing, and explicitly flag share-count/SBC discontinuities caused by IPO conversion, lockups, and one-time vesting triggers.

## Data Verification Checklist

Before issuing a thesis, valuation range, or post-earnings view, verify and state the date or period for:

- Current share price, market cap, enterprise value, and diluted share count.
- Latest fiscal quarter and trailing twelve-month financials.
- Revenue growth, gross margin, operating margin, net income or loss, free cash flow, and cash balance.
- Debt, lease obligations, maturity schedule, and net cash or net debt.
- Stock-based compensation, share dilution, buybacks, and major equity issuance.
- Latest guidance, consensus context when available, and management commentary.
- Next known earnings date or major catalyst when relevant.

If data is unavailable or inconsistent across sources, flag the uncertainty instead of forcing precision.

For decision-critical numbers, use a two-source check whenever practical:

- Cross-check revenue, net income or loss, cash, debt, diluted shares, market cap, enterprise value, free cash flow, and major KPIs against at least two reputable sources.
- Prefer company filings or investor relations as the source of record when third-party data conflicts with company materials.
- If an investor-relations site blocks automation or returns bot-detection/access-denied pages, do not stall: use SEC filings/exhibits, company press releases mirrored in 8-Ks, market-data pages such as StockAnalysis/Yahoo chart APIs, and reputable secondary sources; explicitly state the IR access limitation and lower confidence for any unavailable materials such as Investor Day PDFs.
- If the difference is small and explainable, state the likely reason, such as reporting date, TTM versus fiscal-year period, GAAP versus non-GAAP, or basic versus diluted share count.
- If the difference is material or cannot be reconciled quickly, flag the exact conflict, lower confidence, and avoid making the conflicted number carry the thesis or valuation conclusion.

## Mode Selection

Use only these two modes:

- **Deep company research**: default for every ticker or company analysis request, even if the user only gives a ticker or company name.
- **Post-earnings tracking**: use when the user mentions earnings, quarterly results, latest quarter, guidance, 10-Q, shareholder letter, investor presentation, or earnings call.

Do not create additional modes. If the user asks another shape of question about a selected stock, adapt the closest of the two modes.

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

Do not overwrite older deep research files. Treat each file as a point-in-time thesis snapshot. Create a new version only when the company logic changes enough to require a fresh full research memo.

### earnings-tracking/

Save each post-earnings tracking memo in `research/COMPANIES/TICKER/earnings-tracking/`.

Prefer `YYYY-QN-earnings-tracking.md` when the fiscal quarter is clear. Use `YYYY-MM-DD-earnings-tracking.md` when the quarter is unclear or the update is not tied to a regular quarter.

### tracker.md

Maintain `research/COMPANIES/TICKER/tracker.md` as the current state file. Update it after every deep research memo and every post-earnings tracking memo.

The tracker should summarize:

- Current research view.
- Current main thesis.
- Key risks.
- Latest earnings or company update.
- What changed since the prior view.
- Core thesis assumptions that must remain true.
- Red-line conditions that would force a thesis review or downgrade.
- Management promises, targets, or strategic milestones that need follow-up.
- Metrics or events to monitor next.
- What would change the research view.

Treat `tracker.md` as the active monitoring dashboard, not a shorter copy of the latest memo. Keep the current state concise, but make it easy to check later whether the original thesis is being confirmed or disproved.

### Update Rules

- Small change: update only `tracker.md`.
- Earnings change: create a new `earnings-tracking/...md`, then update `tracker.md`.
- Major company logic change: create a new `deep-research/...-v2.md`, then update `tracker.md`.
- Standalone scenario-valuation refreshes, current-price valuation updates, or single-event valuation implications normally count as a small change: update `tracker.md` with a dated valuation snapshot, bear/base/bull ranges, practical price zones, sources, and what changed since the prior view. Do **not** create a new deep-research memo unless the business thesis, company logic, or valuation framework materially changed.

## Core Research Workflow

For every non-trivial analysis:

1. Identify the company, ticker, exchange, sector, and business model.
2. Translate the company's products, technical terms, customers, and revenue streams into a beginner-friendly "how the business actually works and makes money" explanation before using industry jargon.
3. Verify current price, market cap, recent performance, and the latest reporting period.
4. Read the latest company materials and recent news if the analysis depends on current facts.
5. Classify the company type before selecting valuation methods.
6. Build the initial thesis from business quality, growth drivers, financial trend, valuation, and catalysts.
7. Identify supporting evidence, disconfirming evidence, and the largest uncertainty.
8. Stress-test downside risk, dilution, balance sheet risk, and valuation multiple compression.
9. Apply the four investor-style decision lenses when producing a deep company research memo.
10. State the research view with confidence level, time horizon, risk/reward, and conditions that would change the thesis.
11. Save the output using the Saving Research Results rules and update `tracker.md`.

## Beginner Business Explanation

Every company research output must include a plain-language explanation of how the company operates and how it earns money now or could earn money in the future. This is required for all researched companies, not only technically complex companies.

Write this for a smart non-specialist investor, not for an industry expert:

- Define important jargon in one sentence before relying on it. For example, explain terms like OCS, coherent optics, RPO, ARR, take rate, GMV, loss ratio, or combined ratio when they matter.
- Describe the value chain: what the company sells, who buys it, why the buyer needs it, who pays, when revenue is recognized if relevant, and what costs must be paid to deliver it.
- Separate "today's profit engine" from "future monetization option" when a business line is early, experimental, cyclical, or not yet profitable.
- For segment-heavy companies, give a one-line plain-language explanation for each major segment before analyzing growth and margins.
- Use simple analogies only when they clarify the mechanism. Do not let analogies replace factual explanation.
- End the explanation with the core economic question: what has to happen for this business to produce durable profits or free cash flow?

## Company-Type Adjustments

Adapt the research and valuation approach to the company:

- **High-growth unprofitable software / internet**: focus on revenue durability, gross margin, net revenue retention, customer acquisition efficiency, operating leverage, cash burn, SBC, dilution, and EV/Sales or path-to-FCF valuation.
- **Profitable compounder**: focus on revenue growth, margin durability, ROIC, free cash flow conversion, reinvestment runway, competitive advantage, and P/E, EV/EBIT, EV/EBITDA, or FCF yield.
- **Cyclical company**: normalize revenue, margins, and multiples across the cycle; do not value peak earnings as normal earnings.
- **Financials / insurance / fintech lenders**: focus on credit quality, loss ratios, funding costs, capital adequacy, regulatory risk, book value, ROE, and reserve adequacy.
- **Biotech / healthcare innovation**: focus on pipeline stage, clinical milestones, probability of success, cash runway, dilution, regulatory path, and addressable market.
- **Turnaround or distressed company**: focus on liquidity, debt maturities, covenant risk, cash burn, asset sales, and whether the turnaround is measurable.
- **Industrial / capital-equipment / infrastructure-cycle companies**: focus on orders, book-to-bill, backlog/RPO, backlog margin quality, equipment versus service mix, project execution risk, warranty/quality reserves, working-capital swings, capex required to expand capacity, installed-base service revenue, and whether current earnings are peak-cycle or normalized. For companies with large one-time tax, M&A, or mark-to-market gains, do not annualize GAAP EPS; use normalized Adjusted EBITDA/EBIT/FCF scenarios and explicitly separate operating improvement from non-operating gains.
- **Capital-intensive multi-segment infrastructure platforms**: for companies that combine a proven infrastructure profit engine with high-optionality segments (space launch, satellite broadband, AI compute, founder-controlled software acquisitions, energy infrastructure, or similar), analyze each segment separately. Identify which segment funds the rest of the company today, incorporate pro forma debt/interest after major financings, separate current cash-flow evidence from future optionality, and explicitly evaluate governance, dilution, and mission-drift risk. Use scenario valuation plus practical price zones rather than a single blended multiple.
- **Digital-asset treasury companies and former miners that pivoted into treasury strategies**: value the common stock as a dated common-equity NAV bridge, not on total token holdings or headline GAAP earnings. Subtract debt, liabilities, preferred liquidation preferences, and other senior claims; reconcile basic and conservative fully diluted shares; calculate token and NAV per share over time; and test whether ATM issuance was accretive at the actual mNAV. Analyze staking as gross yield minus validator/custody/security/compliance costs, reconcile option premium with realized and unrealized derivative P/L, and treat self-treasury validator activity as unproven platform optionality until external AUM and fees are disclosed. Explicitly assess mission drift and whether incentives based on total market cap or total tokens can be achieved through dilution. Use token-price × common-NAV × mNAV bear/base/bull scenarios.

## Research View Framework

Use research views consistently:

- **Positive**: the thesis is supported by durable or improving fundamentals, valuation is explainable under reasonable assumptions, and the risk/reward looks attractive over the stated horizon.
- **Constructive but watchful**: the company is attractive, but valuation, timing, volatility, or missing confirmation requires more evidence.
- **Neutral / wait for confirmation**: the company may be worth tracking, but the current evidence is not strong enough to support a high-conviction thesis.
- **Negative / thesis weakening**: fundamentals, valuation, dilution, balance sheet risk, or competitive position are moving against the thesis.
- **Insufficient evidence**: use when key data is missing, sources conflict, or the thesis cannot be supported without speculation. State what evidence is needed before upgrading to a directional view.

When giving any research view, include the strongest reason against your own view.

## Valuation Discipline

Always explain why the chosen valuation method fits the company:

- Use EV/Sales or EV/Gross Profit mainly for high-growth or unprofitable companies, and explicitly connect the multiple to expected growth, margin potential, and cash burn.
- Use P/E, PEG, EV/EBITDA, EV/EBIT, or FCF yield for profitable companies, and adjust for cyclicality, one-time items, and quality of earnings.
- Use DCF only when assumptions can be stated clearly; show revenue growth, margin, FCF conversion, discount rate, terminal growth or terminal multiple, and sensitivity.
- Use book value, tangible book, ROE, combined ratio, loss ratio, or credit metrics for financials and insurers where relevant.
- Use scenario valuation for important conclusions: bear, base, and bull. Each scenario must include assumptions, explicit implied value range, and key trigger.
- For common stocks, the implied value should normally be a per-share price range and upside/downside versus the current price. For preferred stocks, bonds, funds, warrants, or unusual securities, use the most relevant range such as price range, yield range, NAV discount/premium, asset-coverage range, recovery range, or liquidation-preference discount.
- Do not replace explicit valuation ranges with vague labels like "upside," "downside," "near fair value," or "price may recover" when current price, share count, financials, and method assumptions are available.
- If an explicit range is not defensible, state "No reliable valuation range" and explain the missing data, source conflict, security structure, or assumption sensitivity that prevents a range. Then provide a bounded proxy, such as the revenue, margin, multiple, yield, or NAV condition that would make the security attractive or unattractive.
- Include dilution and SBC impact when meaningful. Prefer diluted shares and enterprise value over simplistic market-cap math.

## Risk / Reward Framework

For deep research and post-earnings tracking, include:

- Base-case upside and downside case when data allows.
- For deep research, include a concise scenario table with bear/base/bull price or valuation ranges by default. The table should show current price, implied upside/downside, core assumptions, and the trigger that would move the thesis toward that scenario.
- What must go right for the bull case.
- What could break the thesis.
- Whether risk is mainly valuation, execution, balance sheet, competition, regulation, macro, or timing.
- What should be monitored in the next quarter or next major update.

## Four Investor-Style Decision Lenses

For deep company research, include a decision-framing section that evaluates the company through four investor-style lenses. This section must be substantive, not a short checklist. Use it as a final pressure-test of the thesis after the business, financial, valuation, management, and risk sections are complete.

These lenses are not a substitute for source-based financial analysis, and they must not be presented as the actual current opinion of Warren Buffett, Charlie Munger, Duan Yongping, or Li Lu. Frame them only as Buffett-style, Munger-style, Duan Yongping-style, and Li Lu-style analytical lenses.

### Required Depth and Anti-Bias Check

Start the four-lens section with a short anti-bias note:

- **Information richness rating**: A / B / C.
  - A: long-listed company, rich filings, broad analyst/media coverage. Risk: repeating market consensus and mistaking public narrative for insight.
  - B: moderate disclosure or shorter listing history. Risk: filling gaps with plausible but unverified assumptions.
  - C: sparse disclosure, recent IPO, or niche company. Risk: either overconfidence from thin facts or excessive conservatism because the data is incomplete.
- **Main research blind spot**: the most important thing public data does not prove.
- **Strongest reason smart investors may disagree**: one concise sentence.

Each lens must include:

- **Conclusion**: Suitable / Not suitable / Needs further observation.
- **Key question**: the one question this style would ask first.
- **Evidence supporting the thesis**: source-grounded facts from earlier sections.
- **Evidence against the thesis**: disconfirming evidence or unresolved uncertainty.
- **Decision implication**: what this means for further research, watchlist status, position sizing, or required confirmation.
- **Style-specific follow-up question**: one hard question to monitor later.

Do not write vague praise such as "strong moat" or "good management" unless the supporting mechanism is stated. Every score and conclusion must trace back to prior facts in the memo.

Use concise conclusions:

- Suitable
- Not suitable
- Needs further observation

### Buffett-Style Lens

Evaluate whether the company is a durable, understandable, high-return business available with a margin of safety.

Cover:

1. **Business simplicity and durability**: whether the profit engine can be understood and reasonably projected 10 years out.
2. **Economic moat**: switching costs, brand/pricing power, network effects, scale advantages, regulatory advantages, data advantages, or technology barriers. State whether the moat appears widening or narrowing.
3. **Cash conversion and capital intensity**: whether reported earnings convert into free cash flow after capex, SBC, working capital, leases, financing needs, and one-time items.
4. **Management and capital allocation**: whether management has shown discipline in M&A, buybacks, dilution, leverage, capex, and guidance credibility.
5. **Valuation and margin of safety**: whether the current price is explainable under conservative assumptions, not only bull-case growth.

Required follow-up question:

- "If the stock market closed for five years, what business evidence would make this company comfortable or uncomfortable to own?"

### Munger-Style Lens

Evaluate the company by inversion: how could the thesis fail, and where could an investor be fooled?

Cover:

1. **Failure paths**: list the main ways the company could disappoint. Use a compact table with path, mechanism, and investment consequence when useful.
2. **Fragile assumptions**: identify assumptions that sound plausible but are not yet proven by filings, cash flow, customer behavior, or unit economics.
3. **Incentive structure**: whether management, customers, suppliers, sales teams, and investors are rewarded for durable value creation or short-term optics.
4. **Psychological traps**: narrative bias, anchoring, survivorship bias, TAM intoxication, multiple expansion dependence, or "great product equals great stock" thinking.
5. **Major stupidity risk**: the avoidable mistake that would make the thesis look foolish in hindsight.

Required follow-up question:

- "If this investment is wrong three years from now, what red flag should have been obvious today?"

### Duan Yongping-Style Lens

Evaluate whether this is the right business, run by the right people, at the right price.

Cover:

1. **One-sentence business essence**: define what the company really does for customers in plain language.
2. **User value**: who pays, why they pay, whether the product solves an important recurring problem, and what alternatives customers have.
3. **Product or brand strength**: whether the product, brand, distribution, ecosystem, or customer habit creates repeat purchase and pricing power.
4. **People and culture**: whether management behavior suggests customer focus, long-termism, operating discipline, and honest communication.
5. **Long-term certainty and right price**: whether the business can be held through volatility, and what valuation or evidence would make the price reasonable.

Required follow-up question:

- "Is the company creating durable customer value, or mainly monetizing a temporary cycle, subsidy, regulation, or hype window?"

### Li Lu-Style Lens

Evaluate the company through circle of competence, downside protection, and long-term civilization or industry change.

Cover:

1. **Circle of competence**: which parts of the business are knowable from public data and which parts require more evidence, fieldwork, product work, or expert checks.
2. **Industry or civilization trend**: whether the company is aligned with a durable structural shift, and where it sits in the value chain.
3. **Downside protection**: balance sheet, cash flow, asset value, customer stickiness, regulatory position, and downside-case valuation.
4. **Margin of safety**: whether downside is protected by business quality and price, not just by optimism about growth.
5. **Research depth decision**: whether the company deserves deeper work, watchlist status, or high-conviction allocation under the stated assumptions.

Required follow-up question:

- "Looking back 10-20 years from now, is this likely to be a durable node in an important industry, or a temporary winner during a capital cycle?"

### Four-Lens Composite Score

Use a 10-point scoring table. Scores must be justified by the prior analysis, not by vibes. Add one sentence of rationale for each score after the table.

| Dimension | Score |
|---|---:|
| Business model | /10 |
| Moat | /10 |
| Management | /10 |
| Financial quality | /10 |
| Valuation attractiveness | /10 |
| Long-term certainty | /10 |
| Downside risk control | /10 |

### Integrated Decision Memo

Close the four-lens section with a decision memo table:

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality | | |
| Moat | | |
| Management and capital allocation | | |
| Biggest risk | | |
| Long-term trend | | |
| Valuation and margin of safety | | |

Then include an action-framing table:

| Investor state | Research implication |
|---|---|
| No position | |
| Existing position | |
| Add / upgrade signal | |
| Reduce / downgrade signal | |

Finish with:

- Whether it is worth researching further.
- Whether it appears buyable under the stated assumptions, framed as research support rather than personalized advice.
- Whether it appears suitable for long-term holding.
- Biggest risk.
- Metrics to keep tracking.

## Deep Company Research Template

Use this template by default for every selected stock:

Begin with this fixed summary block:

- **Research view**:
- **Confidence**:
- **Time horizon**:
- **Main thesis**:
- **Key risk**:

1. **Executive View**
   - Research view: Positive / Constructive but watchful / Neutral / Negative / Insufficient evidence.
   - Confidence and time horizon.
   - Core thesis in three bullets.
   - Strongest reason against the view.

2. **Business Model and Industry Structure**
   - Beginner explanation: in plain language, what the company sells, who pays, why customers buy, and how cash eventually becomes profit or free cash flow.
   - Jargon translation: define the important product, accounting, or industry terms needed to understand the business.
   - How the company makes money.
   - Unit economics where available.
   - Market size, penetration, and growth drivers.
   - Competitive landscape and moat.
   - Customer concentration, pricing power, and switching costs.

3. **Segment and Product Analysis**
   - Plain-language explanation of each major segment or product before the professional analysis.
   - Revenue by segment or product when available.
   - Growth, margin, and strategic importance by segment.
   - Product roadmap or innovation pipeline.

4. **Financial Deep Dive**
   - Multi-year revenue growth and growth quality.
   - Gross margin, operating margin, and operating leverage.
   - Free cash flow and capital intensity.
   - Balance sheet strength, debt maturity, cash runway, and dilution risk.
   - Key accounting issues or non-GAAP adjustments if relevant.
   - SBC, share count trend, working capital, and one-time items.

5. **Management and Capital Allocation**
   - Management credibility and execution history.
   - Management promise tracking: prior targets, guidance, strategic claims, product milestones, margin goals, capital allocation promises, and whether they were met, delayed, reframed, or abandoned.
   - Earnings-call answer quality when transcripts are available: whether management answers hard questions directly, explains tradeoffs with numbers, acknowledges misses, changes tone, or relies mainly on vague external excuses.
   - Insider ownership or incentives when relevant.
   - Buybacks, dilution, M&A, capex, and R&D allocation.

6. **Valuation Work**
   - Current multiples and historical context.
   - Peer comparison where useful.
   - Scenario valuation: bear, base, bull.
   - Explicit assumptions for revenue growth, margins, multiples, discount rate, or terminal value.
   - Valuation method selection by company type.

7. **Catalysts and Monitoring Plan**
   - Near-term catalysts.
   - Medium-term thesis milestones.
   - Metrics to monitor in future quarters.

8. **Risk Register**
   - Probability and severity of key risks.
   - Downside case.
   - Thesis invalidation signals.
   - The strongest disconfirming evidence.

9. **Four Investor-Style Decision Lenses**
   - Anti-bias note: information richness rating, main research blind spot, and strongest reason smart investors may disagree.
   - Buffett-style lens: conclusion, key question, evidence for and against, decision implication, and follow-up question covering business durability, moat, cash conversion, management, valuation, and margin of safety.
   - Munger-style lens: conclusion, key question, inversion table or concise failure paths, fragile assumptions, incentives, psychological traps, major stupidity risk, decision implication, and follow-up question.
   - Duan Yongping-style lens: conclusion, one-sentence business essence, user value, product or brand strength, culture/people, long-term certainty, right price, decision implication, and follow-up question.
   - Li Lu-style lens: conclusion, circle of competence, long-term industry or civilization trend, value-chain position, downside protection, margin of safety, research-depth decision, and follow-up question.
   - Four-lens composite scoring table with one-sentence rationale for each score.
   - Integrated decision memo and action-framing table for no position, existing position, add/upgrade signal, and reduce/downgrade signal.

10. **Final Research Framework**
   - What the thesis depends on.
   - What would make the thesis stronger.
   - What would change the research view.

## Post-Earnings Tracking Template

Use when the user asks about earnings, latest results, guidance, 10-Q, shareholder letter, investor presentation, or earnings call:

Begin with this fixed summary block:

- **Research view**:
- **Confidence**:
- **Time horizon**:
- **Main thesis**:
- **Key risk**:

1. **Post-Earnings Verdict**
   - Better than expected / mixed / worse than expected.
   - Updated research view: Positive / Constructive but watchful / Neutral / Negative / Insufficient evidence.
   - Key reason.
   - Whether the quarter changed the long-term thesis.

2. **Headline Results**
   - Revenue, growth, EPS or net income, margins, cash flow.
   - Compare with prior year, prior quarter, guidance, and consensus when available.
   - Separate reported results from non-GAAP or adjusted results.

3. **Guidance and Management Commentary**
   - New guidance.
   - Important management comments.
   - Changes from prior narrative.
   - Any change in management tone or strategic priority.
   - Whether management met, missed, delayed, or reframed prior commitments.
   - Quality of Q&A answers when available, especially directness, specificity, consistency with filings, and willingness to address weak spots.

4. **Quality of the Quarter**
   - Was growth high quality or one-off?
   - Margin trend.
   - Cash flow and balance sheet changes.
   - Customer, product, or segment signals.
   - Industry-specific KPIs when relevant, such as ARR, RPO, NRR, GMV, take rate, bookings, backlog, loss ratio, combined ratio, same-store sales, or clinical milestones.

5. **Market Reaction in Context**
   - Assess whether the post-earnings market reaction is consistent with changes in fundamentals, guidance, and valuation.
   - Separate fundamental changes from sentiment, positioning, and valuation reset only as needed for the earnings conclusion.

6. **Updated Thesis and Tracking Plan**
   - What improved.
   - What worsened.
   - Which assumptions changed.
   - Which core thesis assumptions were confirmed or weakened.
   - Whether any red-line condition was triggered.
   - Which management promises or milestones need follow-up.
   - What to monitor before the next earnings report.
   - What would change the research view.

## Output Style

- Start with the research view, not a long setup.
- Match the user's requested language. Keep the formal section labels clear and consistent.
- For every researched company, include a beginner-friendly business explanation before the technical or professional analysis. Avoid assuming the user already understands specialized technical, financial, or industry vocabulary.
- Use tables only when they make comparison or assumptions easier to read.
- Make deep research comprehensive, but keep each section focused on decision-useful evidence.
- Include dates for earnings, filings, prices, and news when relevant.
- Include source links or source names for key facts.
- End with a concise "What would change my view" section.
