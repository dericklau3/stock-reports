import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

import { buildReportIndex, extractValuationRanges } from "../scripts/report-index.mjs";

const page = await readFile(new URL("../src/pages/valuations.astro", import.meta.url), "utf8");
const layout = await readFile(new URL("../src/layouts/BaseLayout.astro", import.meta.url), "utf8");

test("valuation overview has three scenario columns, source report links, search, and mobile styling", () => {
  for (const label of ["悲观情景", "基础情景", "乐观情景", "股票估值总览", "valuation-search", "valuation-result-count"]) {
    assert.ok(page.includes(label), label);
  }
  assert.ok(page.includes("import index from \"../data/report-index.json\""));
  assert.ok(page.includes("company.valuation?.[key]"));
  assert.ok(page.includes("reportUrl(base, company.symbol, company.reports[0].fileName)"));
  assert.ok(page.includes("data-valuation-filter=\"missing\""));
  assert.ok(page.includes("@media (max-width: 760px)"));
  assert.ok(layout.includes("pageType === \"valuations\""));
});

test("valuation parser reads scenario prices instead of financial metrics in the same table", () => {
  const report = [
    "# Mock report",
    "## 6. 估值分析",
    "| 情景 | 经营依据 | 合理价 |",
    "| --- | --- | --- |",
    "| **悲观** | 营业利润 $12.30–$18.40bn | **$42.42–$53.61** |",
    "| **基础** | 收入 $20.0–$24.0bn | **$55.92–$70.02/股** |",
    "| **乐观** | 增长假设 | **$83.00–$95.75** |",
    "## 7. 风险提示",
    "| 悲观 | $1.00–$2.00 |",
  ].join("\n");
  assert.deepEqual(extractValuationRanges(report), {
    bear: { low: 42.42, high: 53.61 },
    base: { low: 55.92, high: 70.02 },
    bull: { low: 83, high: 95.75 },
    currency: "USD",
    unit: "股",
  });
});

test("unquantified scenarios are explicitly missing, and ADS units are preserved", () => {
  const missing = extractValuationRanges([
    "## 6. 估值分析",
    "| 情景 | 合理价格区间 |",
    "| --- | --- |",
    "| 悲观 | **未能可靠量化** |",
    "| 基础 | **未能可靠量化** |",
    "| 乐观 | **未能可靠量化** |",
  ].join("\n"));
  assert.equal(missing.bear, null);
  assert.equal(missing.base, null);
  assert.equal(missing.bull, null);

  const ads = extractValuationRanges([
    "## 6. 估值分析",
    "| **悲观** | **$65.12–$81.83 / ADS** |",
    "| **基础** | **$98.47–$129.10 / ADS** |",
    "| **乐观** | **$145.37–$166.76 / ADS** |",
  ].join("\n"));
  assert.equal(ads.unit, "ADS");
  assert.deepEqual(ads.base, { low: 98.47, high: 129.1 });
});

test("latest reports provide report-derived valuation data, without made-up SPCX prices", async () => {
  const companiesDir = fileURLToPath(new URL("../../research/COMPANIES/", import.meta.url));
  const reportIndex = await buildReportIndex(path.resolve(companiesDir));
  assert.ok(reportIndex.companies.length >= 19);
  const companyBySymbol = new Map(reportIndex.companies.map((company) => [company.symbol, company]));

  for (const symbol of "AAPL AMZN AVAV CRCL GOOG HOOD INTC LMND META MSFT NVDA ORCL PL RKLB SKHY TEM TSLA VST".split(" ")) {
    const company = companyBySymbol.get(symbol);
    assert.ok(company, symbol + " missing from index");
    for (const scenario of ["bear", "base", "bull"]) {
      const range = company.valuation?.[scenario];
      assert.ok(range && range.low > 0 && range.high >= range.low, symbol + " " + scenario + " missing or invalid");
    }
  }

  const spcx = companyBySymbol.get("SPCX");
  assert.ok(spcx);
  assert.equal(spcx.valuation.bear, null);
  assert.equal(spcx.valuation.base, null);
  assert.equal(spcx.valuation.bull, null);
  assert.equal(companyBySymbol.get("SKHY").valuation.unit, "ADS");
});
