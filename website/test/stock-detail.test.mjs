import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const detail = await readFile(new URL("../src/pages/stocks/[symbol].astro", import.meta.url), "utf8");

test("stock detail header only shows short investment view and an optional glossary", () => {
  assert.match(detail, /class="investment-summary"/);
  assert.match(detail, /\{investmentView\}/);
  assert.match(detail, /<details class="view-glossary">/);
  assert.match(detail, /研究中/);
  assert.match(detail, /中性偏建设性 \/ 中性偏谨慎/);
  assert.doesNotMatch(detail, /\{company\.currentView\}/);
  assert.doesNotMatch(detail, /Source: research\/COMPANIES/);
});

test("stock detail renders questions instead of a tracker panel", () => {
  assert.match(detail, /class="topic-panel"/);
  assert.match(detail, /<details class="topic-entry"/);
  assert.match(detail, /topics\.map/);
  assert.match(detail, /intcConversation\.entries/);
  assert.match(detail, /renderMarkdown\(topic\.answer\)/);
  assert.doesNotMatch(detail, /trackerHtml|tracker-body|company\.tracker/);
});
