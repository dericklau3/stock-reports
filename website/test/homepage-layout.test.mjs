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
