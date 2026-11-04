import assert from "node:assert/strict";
import { mkdtemp, mkdir, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";

import { renderMarkdown, reportUrl, withBase } from "../src/lib/markdown.js";
import { buildReportIndex, extractInvestmentView, slugForReport } from "../scripts/report-index.mjs";

test("slugForReport preserves report names", () => {
  assert.equal(slugForReport("2026-07-22-deep-research.md"), "2026-07-22-deep-research");
});
test("withBase keeps GitHub Pages links under the repository base path", () => {
  assert.equal(withBase("/stock-reports", "stocks/TSLA/"), "/stock-reports/stocks/TSLA/");
  assert.equal(reportUrl("/stock-reports", "TSLA", "2026-07-22-deep-research.md"), "/stock-reports/reports/TSLA/2026-07-22-deep-research/");
});

test("buildReportIndex discovers reports without any tracker.md", async () => {
  const root = await mkdtemp(path.join(tmpdir(), "stock-reports-"));
  const dir = path.join(root, "COMPANIES", "TSLA", "deep-research");
  await mkdir(dir, { recursive: true });
  await writeFile(path.join(dir, "2026-11-04-deep-research.md"),
    "# Tesla（TSLA）完整深度研究\n\n- **投资观点：**中性偏谨慎。现金流仍有压力。\n- **核心逻辑：**汽车与储能需要继续验证。\n- **主要风险：**高资本开支。\n");
  const index = await buildReportIndex(path.join(root, "COMPANIES"));
  assert.equal(index.companies.length, 1);
  const company = index.companies[0];
  assert.equal(company.symbol, "TSLA");
  assert.equal(company.companyName, "Tesla");
  assert.equal(company.lastUpdated, "2026-11-04");
  assert.equal(company.investmentView, "中性偏谨慎");
  assert.equal(company.reports.length, 1);
  assert.equal(company.reports[0].slug, "2026-11-04-deep-research");
  assert.ok(!("tracker" in company));
});

test("index uses latest report date and excludes companies without reports", async () => {
  const root = await mkdtemp(path.join(tmpdir(), "stock-reports-dates-"));
  const companyDir = path.join(root, "COMPANIES", "PL");
  const reports = path.join(companyDir, "deep-research");
  await mkdir(reports, { recursive: true });
  await mkdir(path.join(root, "COMPANIES", "EMPTY"), { recursive: true });
  await writeFile(path.join(reports, "2026-11-01-deep-research.md"), "# Old report\n");
  await writeFile(path.join(reports, "2026-11-04-deep-research.md"), "# Planet Labs PBC（NYSE: PL）深度研究\n\n**投资观点：**谨慎看好。\n");
  const index = await buildReportIndex(path.join(root, "COMPANIES"));
  assert.equal(index.companies.length, 1);
  assert.equal(index.companies[0].companyName, "Planet Labs PBC");
  assert.equal(index.companies[0].lastUpdated, "2026-11-04");
  assert.equal(index.companies[0].investmentView, "谨慎看好");
  assert.equal(index.companies[0].reports.length, 2);
});

test("business sections are default-closed and retain rendered Markdown", () => {
  const source = [
    "## 1. 公司到底是做什么生意的？",
    "",
    "公司整体定位保持直接可见。",
    "",
    '<details class="business-detail">',
    "<summary>① 芯片业务｜本季已核实收入</summary>",
    "",
    "客户购买芯片并付款。[官方来源](https://example.com/source)。",
    "",
    "**举例假设（非真实订单）：** 设备厂向制造商下单。",
    "</details>",
    "",
    "| 业务 | 最新季 |",
    "|---|---:|",
    "| 芯片 | 100 |",
  ].join("\n");

  const html = renderMarkdown(source);
  assert.match(html, /<details class="business-detail">/);
  assert.doesNotMatch(html, /<details[^>]+\sopen(?:\s|=|>)/);
  assert.match(html, /<summary>① 芯片业务｜本季已核实收入<\/summary>/);
  assert.match(html, /<div class="business-detail-content">/);
  assert.match(html, /<strong>举例假设（非真实订单）：<\/strong>/);
  assert.match(html, /<a href="https:\/\/example.com\/source">官方来源<\/a>/);
  assert.match(html, /<table>/);
});


test("monthly event roadmap keeps grouped cards and detailed evidence", () => {
  const source = [
    "## 2. 近期已公布的重大事件",
    "",
    '<div class="event-roadmap" aria-label="重大事件时间轴">',
    '<section class="event-month" data-month="2026-04">',
    '<h3 class="event-month-heading">2026-04</h3>',
    '<details class="event-entry">',
    "<summary>",
    '<span class="event-entry-title">资产交易</span>',
    '<span class="event-entry-preview">一句话介绍。</span>',
    "</summary>",
    '<div class="event-detail-content">',
    "",
    "**公告日期：** 2026-04-23",
    "",
    "**公布了什么：** 已公布实质交易。",
    "",
    "**对公司的实际意义：** 影响现金。",
    "",
    "**原始来源：** [IR公告](https://example.com/ir)",
    "",
    "</div>",
    "</details>",
    "</section>",
    "</div>",
  ].join("\n");

  const html = renderMarkdown(source);
  assert.match(html, /<div class="event-roadmap"/);
  assert.match(html, /<section class="event-month" data-month="2026-04">/);
  assert.match(html, /<h3 class="event-month-heading">2026-04<\/h3>/);
  assert.match(html, /<details class="event-entry">/);
  assert.doesNotMatch(html, /<details class="event-entry"[^>]*\sopen(?:\s|=|>)/);
  assert.match(html, /<summary>\s*<span class="event-entry-title">资产交易<\/span>/);
  assert.match(html, /<div class="event-detail-content">[\s\S]*<strong>公告日期：<\/strong>/);
  assert.match(html, /<a href="https:\/\/example.com\/ir">IR公告<\/a>/);
});


test("view extraction reads only report conclusions and not long metadata", () => {
  assert.equal(extractInvestmentView("# Intel\n\n- **投资观点：**中性偏谨慎。Xeon盈利强劲。\n- **研究截止：**2026-11-02"), "中性偏谨慎");
  assert.equal(extractInvestmentView("# NVDA\n\n**谨慎看好。** 数据中心增长强劲。"), "谨慎看好");
  assert.equal(extractInvestmentView("# ABC\n\n- **核心逻辑：**增长中。"), "研究中");
});
