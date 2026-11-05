import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const earnings = JSON.parse(await readFile(new URL("../src/data/earnings-q3-2026.json", import.meta.url), "utf8"));

test("each tracked 2026 Q3 reporting-season stock has a verified date state", () => {
  const symbols = "AAPL AMZN AVAV CBRS CRCL GOOG HOOD INTC LMND MSFT NVDA ORCL PL QCOM RKLB SKHY SPCX TEM TSLA VST".split(" ");
  assert.deepEqual(Object.keys(earnings.entries).sort(), symbols.sort());
  for (const [symbol, info] of Object.entries(earnings.entries)) {
    assert.ok(info.quarter, symbol + " missing fiscal quarter");
    assert.match(info.source, /^https:\/\//, symbol + " missing original source");
    assert.ok(["reported", "scheduled", "unannounced", "not-applicable"].includes(info.status), symbol);
    if (info.status === "reported" || info.status === "scheduled") {
      assert.match(info.date, /^2026-\d{2}-\d{2}$/, symbol + " missing confirmed date");
    } else {
      assert.equal(info.date, null, symbol + " must not invent a date");
    }
  }
});

test("unannounced earnings are not labeled as reported", () => {
  for (const symbol of ["AVAV", "PL"]) assert.equal(earnings.entries[symbol].status, "unannounced");
});

test("deleted IAU research has no earnings entry", () => {
  assert.equal(Object.hasOwn(earnings.entries, "IAU"), false);
});
