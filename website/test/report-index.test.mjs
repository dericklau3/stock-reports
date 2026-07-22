import assert from "node:assert/strict";
import { mkdtemp, mkdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";

import { reportUrl, withBase } from "../src/lib/markdown.js";
import { buildReportIndex, slugForReport } from "../scripts/report-index.mjs";

test("slugForReport removes markdown extension and keeps readable report names", () => {
  assert.equal(slugForReport("2026-07-22-deep-research.md"), "2026-07-22-deep-research");
});

test("withBase keeps GitHub Pages links under the repository base path", () => {
  assert.equal(withBase("/stock-reports", "stocks/TSLA/"), "/stock-reports/stocks/TSLA/");
  assert.equal(reportUrl("/stock-reports", "TSLA", "2026-07-22-deep-research.md"), "/stock-reports/reports/TSLA/2026-07-22-deep-research/");
});

test("buildReportIndex scans tracker and deep research files", async () => {
  const root = await mkdtemp(path.join(tmpdir(), "stock-reports-"));
  const companiesDir = path.join(root, "COMPANIES");
  const tslaDir = path.join(companiesDir, "TSLA");
  const reportsDir = path.join(tslaDir, "deep-research");

  await mkdir(reportsDir, { recursive: true });
  await writeFile(
    path.join(tslaDir, "tracker.md"),
    `# Tesla（TSLA）Tracker

Last updated: 2026-07-22

## Current Research View

**中性 / 等待确认**，中等置信度。Amazon zone remains intact.

## Current Main Thesis

- Thesis one.
- Thesis two.
`,
  );
  await writeFile(
    path.join(reportsDir, "2026-07-22-deep-research.md"),
    `# Tesla 深度研究

Report body.
`,
  );

  const index = await buildReportIndex(companiesDir);

  assert.equal(index.companies.length, 1);
  assert.equal(index.companies[0].symbol, "TSLA");
  assert.equal(index.companies[0].companyName, "Tesla");
  assert.equal(index.companies[0].lastUpdated, "2026-07-22");
  assert.equal(index.companies[0].currentView, "中性 / 等待确认，中等置信度。Amazon zone remains intact.");
  assert.equal(index.companies[0].reports.length, 1);
  assert.equal(index.companies[0].reports[0].slug, "2026-07-22-deep-research");
});
