import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { intcConversation } from "../src/data/intc-conversation.js";

const page = await readFile(new URL("../src/pages/stocks/INTC/conversation.astro", import.meta.url), "utf8");
const stockPage = await readFile(new URL("../src/pages/stocks/[symbol].astro", import.meta.url), "utf8");
const reportPage = await readFile(new URL("../src/pages/reports/[symbol]/[report].astro", import.meta.url), "utf8");

test("Intel conversation has seven sourced, distinct and substantive questions", () => {
  assert.equal(intcConversation.entries.length, 7);
  assert.equal(new Set(intcConversation.entries.map((item) => item.id)).size, 7);
  for (const item of intcConversation.entries) {
    assert.ok(item.id && item.topic && item.question, "Q&A metadata required");
    assert.ok(item.answer.length > 200, item.id + " should provide useful detail");
    assert.match(item.answer, /https:\/\//, item.id + " requires original source links");
  }
});

test("Intel topic page shares the existing Astro site layout and base-prefixed routes", () => {
  assert.match(page, /import BaseLayout/);
  assert.match(page, /<BaseLayout/);
  assert.match(page, /intcConversation\.entries\.map/);
  assert.match(page, /withBase\(base, "stocks\/INTC\/"\)/);
  assert.match(page, /withBase\(base, "reports\/INTC\/2026-11-02-deep-research\/"\)/);
  assert.match(page, /renderMarkdown\(item\.answer\)/);
});

test("Intel company and report pages link back to the topic without changing navigation", () => {
  assert.match(stockPage, /company\.symbol === "INTC"/);
  assert.match(stockPage, /stocks\/INTC\/conversation\//);
  assert.match(reportPage, /company\.symbol === "INTC"/);
  assert.match(reportPage, /stocks\/INTC\/conversation\//);
});

test("in-answer research link resolves within the GitHub Pages base directory", () => {
  const answer = intcConversation.entries[0].answer;
  const match = answer.match(/\]\((\.\.\/[^)]+deep-research\/)\)/);
  assert.ok(match, "expected a relative link to the full INTC report");
  const url = new URL(match[1], "https://dericklau3.github.io/stock-reports/stocks/INTC/conversation/");
  assert.equal(url.href, "https://dericklau3.github.io/stock-reports/reports/INTC/2026-11-02-deep-research/");
});

test("dated prices and holdings are described as historical, not real-time", () => {
  assert.equal(intcConversation.researchCutoff, "2026-11-02");
  assert.match(intcConversation.entries.find((item) => item.id === "politicians").answer, /不能确认/);
  assert.match(intcConversation.entries.find((item) => item.id === "trade-prices").answer, /不是实际成交/);
  assert.match(intcConversation.entries.find((item) => item.id === "nvidia").answer, /假设/);
});
