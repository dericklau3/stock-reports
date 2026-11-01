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

test("buildReportIndex falls back to the newest report date when Tracker has no canonical update date", async () => {
  const root = await mkdtemp(path.join(tmpdir(), "stock-reports-pl-"));
  const companiesDir = path.join(root, "COMPANIES");
  const plDir = path.join(companiesDir, "PL");
  const reportsDir = path.join(plDir, "deep-research");

  await mkdir(reportsDir, { recursive: true });
  await writeFile(
    path.join(plDir, "tracker.md"),
    "# PL｜Planet Labs PBC 投资研究跟踪\\n创建于2026-10-31，首次覆盖。\\n",
  );
  await writeFile(
    path.join(reportsDir, "2026-10-31-deep-research.md"),
    "# Planet Labs 深度研究\\n",
  );
  await writeFile(
    path.join(reportsDir, "2026-10-20-deep-research.md"),
    "# Earlier Planet Labs 深度研究\\n",
  );

  const index = await buildReportIndex(companiesDir);
  assert.equal(index.companies[0].lastUpdated, "2026-10-31");
  assert.equal(index.companies[0].reports.length, 2);
});

test("buildReportIndex does not keep a stale Tracker date over a newer report", async () => {
  const root = await mkdtemp(path.join(tmpdir(), "stock-reports-updated-"));
  const companiesDir = path.join(root, "COMPANIES");
  const companyDir = path.join(companiesDir, "ABC");
  const reportsDir = path.join(companyDir, "deep-research");

  await mkdir(reportsDir, { recursive: true });
  await writeFile(
    path.join(companyDir, "tracker.md"),
    "# ABC Tracker\\n\\nLast updated: 2026-10-20\\n",
  );
  await writeFile(
    path.join(reportsDir, "2026-10-31-deep-research.md"),
    "# Updated research\\n",
  );

  const index = await buildReportIndex(companiesDir);
  assert.equal(index.companies[0].lastUpdated, "2026-10-31");
});
