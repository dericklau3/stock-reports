import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { intcConversation } from "../src/data/intc-conversation.js";

const page = await readFile(new URL("../src/pages/stocks/INTC/conversation.astro", import.meta.url), "utf8");
const stockPage = await readFile(new URL("../src/pages/stocks/[symbol].astro", import.meta.url), "utf8");
const reportPage = await readFile(new URL("../src/pages/reports/[symbol]/[report].astro", import.meta.url), "utf8");
const intcReport = await readFile(new URL("../../research/COMPANIES/INTC/deep-research/2026-11-06-deep-research.md", import.meta.url), "utf8");

test("Intel conversation combines related topics into seven sourced sections", () => {
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
  assert.match(page, /withBase\(base, "reports\/INTC\/2026-11-06-deep-research\/"\)/);
  assert.match(page, /renderMarkdown\(item\.answer\)/);
});

test("Intel company and report pages link back to the topic without changing navigation", () => {
  assert.match(stockPage, /company\.symbol === "INTC"/);
  assert.match(stockPage, /stocks\/INTC\/conversation\//);
  assert.match(reportPage, /company\.symbol === "INTC"/);
  assert.match(reportPage, /stocks\/INTC\/conversation\//);
});

test("in-answer research link resolves within the GitHub Pages base directory", () => {
  assert.match(page, /withBase\(base, "reports\/INTC\/2026-11-06-deep-research\/"\)/);
});

test("dated prices and holdings are described as historical, not real-time", () => {
  assert.equal(intcConversation.researchCutoff, "2026-11-02");
  assert.match(intcConversation.entries.find((item) => item.id === "nvidia").answer, /假设/);
});


test("removed the trading Q&A and preserved the other topics in order", () => {
  assert.deepEqual(intcConversation.entries.map(item => item.id), ["ceo", "nvidia", "intel-18a", "fab34-apollo", "classiq-quantum", "substrate-supply-2026", "terafab-14a"]);
  assert.equal(intcConversation.entries.some(item => item.id === "politicians"), false);
  const ceo = intcConversation.entries[0].answer;
  assert.match(ceo, /经营改革|重要行动/);
  assert.match(ceo, /105,263股INTC/);
  assert.doesNotMatch(page, /question-one-valuation/);
});

test("18A discussion integrates the process, Panther Lake, yield, and industry baseline", () => {
  const topic = intcConversation.entries.find(item => item.id === "intel-18a");
  assert.ok(topic);
  assert.equal(topic.researchCutoff, "2026-11-05");
  for (const keyword of ["RibbonFET", "PowerVia", "Core Ultra Series 3", "80%", "85%", "行业标准", "良率", "第三方"]) {
    assert.ok(topic.answer.includes(keyword), "Missing " + keyword);
  }
  assert.match(topic.answer, /未公布具体百分比/);
  assert.match(topic.answer, /没有适用于所有芯片/);
  assert.match(page, /item\.researchCutoff \|\| intcConversation\.researchCutoff/);
});


test("Fab 34 discussion accurately distinguishes share ownership, deal prices and trade-off", () => {
  const topic = intcConversation.entries.find((item) => item.id === "fab34-apollo");
  assert.ok(topic);
  assert.equal(topic.researchCutoff, "2026-11-05");
  for (const term of ["112亿美元", "142亿美元", "30亿美元", "49%", "51%", "净所得", "INTC", "65亿美元过桥贷款", "2026年4月8日"]) {
    assert.ok(topic.answer.includes(term), "Missing " + term);
  }
  assert.match(topic.answer, /不等于阿波罗实际净利润/);
  assert.match(topic.answer, /不是INTC股票|不是INTC的49%/);
  assert.match(page, /\$14\.2B/);
  assert.match(page, /Fab 34股权回购/);
  assert.match(stockPage, /topic\.researchCutoff \|\| topicCutoff/);
});


test("Classiq discussion covers deal, CEO investment, and Intel quantum commercialization with careful caveats", () => {
  const item = intcConversation.entries.find((topic) => topic.id === "classiq-quantum");
  assert.ok(item);
  assert.equal(item.researchCutoff, "2026-11-05");
  for (const keyword of ["19亿美元", "3.5亿美元", "22.5亿美元", "2027年上半年", "陈立武", "2022年2月17日", "Tunnel Falls", "95%", "量子比特", "尚未完成", "尚未证实实现规模化商用QPU"]) {
    assert.ok(item.answer.includes(keyword), "Missing " + keyword);
  }
  assert.match(item.answer, /不是创始人/);
  assert.match(item.answer, /匿名人士/);
  assert.match(item.answer, /不直接带来18A良率提高/);
  assert.match(page, /Classiq/);
});


test("substrate supply discussion correctly separates commitments, payments and bottlenecks", () => {
  const item = intcConversation.entries.find((topic) => topic.id === "substrate-supply-2026");
  assert.ok(item);
  assert.equal(item.researchCutoff, "2026-11-05");
  for (const keyword of ["53亿—61亿美元", "33亿美元", "封装基板", "晶圆", "2027年下半年", "40%", "现金流", "12亿美元预付款"]) {
    assert.ok(item.answer.includes(keyword), "Missing " + keyword);
  }
  assert.match(item.answer, /并非收购基板厂/);
  assert.match(item.answer, /不能认定12亿美元就是两份新合同已付款/);
  assert.match(item.answer, /sec\.gov\/Archives\/edgar/);
});

test("Terafab collaboration appears in the Q&A and April 2026 roadmap without claiming a binding order", () => {
  const topic = intcConversation.entries.find((item) => item.id === "terafab-14a");
  assert.ok(topic);
  assert.equal(topic.researchCutoff, "2026-11-07");
  for (const word of ["2026-04-07", "2026-04-22", "14A", "SpaceX", "xAI", "不负有必须继续参与的义务", "合同金额", "良率", "1太瓦"]) {
    assert.ok(topic.answer.includes(word), "Missing Terafab evidence: " + word);
  }
  assert.match(topic.answer, /sec\.gov\/Archives\/edgar/);
  const april = intcReport.match(/<section class="event-month" data-month="2026-04">([\s\S]*?)<\/section>/);
  assert.ok(april, "April 2026 roadmap group missing");
  assert.match(april[1], /Intel加入Terafab合作/);
  assert.match(april[1], /2026-04-07/);
  assert.match(april[1], /2026-04-22/);
  assert.match(april[1], /<div class="event-detail-content">/);
  assert.match(april[1], /没有持续参与义务/);
  assert.equal((intcReport.match(/<span class="event-entry-title">Intel加入Terafab合作/g) || []).length, 1);
});
