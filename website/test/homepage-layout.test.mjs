import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const home = await readFile(new URL("../src/pages/index.astro", import.meta.url), "utf8");
const shell = await readFile(new URL("../src/layouts/BaseLayout.astro", import.meta.url), "utf8");
const css = await readFile(new URL("../src/styles/global.css", import.meta.url), "utf8");

test("homepage no longer contains oversized green hero or promotional illustration", () => {
  assert.doesNotMatch(home, /class="library-hero"/);
  assert.doesNotMatch(home, /hero-finance\.svg|class="hero-art"/);
  assert.match(home, /class="library-intro"/);
  assert.match(home, /class="overview-stats"/);
});

test("navigation links are removed but brand remains a working home link", () => {
  assert.doesNotMatch(shell, /<nav\b/);
  assert.match(shell, /class="brand" href=\{homeHref\}/);
});

test("stock discovery remains functional after compact redesign", () => {
  for (const value of ["stock-search-form", "stock-search", "stock-library", "stock-grid"]) {
    assert.ok(home.includes(value), value);
  }
  assert.match(home, /findMatchingStocks\(/);
  assert.match(home, /data-company-name=/);
  assert.match(home, /data-symbol=/);
  assert.match(home, /data-filter="semiconductors"/);
  assert.match(home, /data-filter="ai"/);
  assert.match(home, /data-view="grid"/);
  assert.match(home, /data-view="list"/);
  assert.doesNotMatch(home, /card-accent-graph/);
});

test("compact layout has responsive rules and keeps detailed report styling", () => {
  assert.match(css, /\.library-intro\s*\{/);
  assert.match(css, /\.library-controls\s*\{/);
  assert.match(css, /@media \(max-width: 680px\)/);
  assert.match(css, /\.event-dialog-content\s*\{/);
});

test("each homepage stock card renders only symbol, company name, rating and verified earnings date", () => {
  const cardMarkup = home.split('<a\n          class="stock-card"')[1]?.split('</a>')[0] || "";
  assert.ok(cardMarkup, "stock card markup must exist");
  assert.match(cardMarkup, /class="stock-identity"/);
  assert.match(cardMarkup, /class="ticker"/);
  assert.match(cardMarkup, /class="stock-company"/);
  assert.match(cardMarkup, /class:list=\{\["view-tag"/);
  assert.match(cardMarkup, /class="stock-card-earnings"/);
  assert.match(cardMarkup, /class="earnings-date"/);
  assert.match(home, /earningsCalendar\.entries/);
  for (const name of ["stock-description", "report-pill", "card-meta", "stock-logo", "card-open"]) {
    assert.doesNotMatch(cardMarkup, new RegExp(name), name + " must not be visible inside stock cards");
  }
  assert.match(home, /data-report-count=\{company\.reports\.length\}/);
  assert.match(home, /card\.dataset\.reportCount/);
  assert.doesNotMatch(home, /querySelector\("\.report-pill"\)/);
});
test("compact cards do not preserve empty space for deleted excerpts", () => {
  assert.match(css, /\.home-page \.stock-card\s*\{[\s\S]*?min-height:\s*164px/);
  assert.doesNotMatch(css, /\.home-page \.stock-description\s*\{/);
});
