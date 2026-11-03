import assert from "node:assert/strict";
import test from "node:test";
import { findMatchingStocks } from "../src/lib/stock-search.js";

const stocks = [
  { symbol: "PL", companyName: "Planet Labs PBC" },
  { symbol: "AAPL", companyName: "Apple" },
  { symbol: "SPCX", companyName: "Space Exploration Technologies" },
  { symbol: "HOOD", companyName: "Robinhood Markets" },
  { symbol: "INTC", companyName: "Intel" },
];

test("exact ticker PL takes precedence over other company names containing pl", () => {
  assert.deepEqual(findMatchingStocks(stocks, "pl").map((s) => s.symbol), ["PL"]);
  assert.deepEqual(findMatchingStocks(stocks, " PL ").map((s) => s.symbol), ["PL"]);
});

test("company names and partial stock symbols are searchable case-insensitively", () => {
  assert.deepEqual(findMatchingStocks(stocks, "INTEL").map((s) => s.symbol), ["INTC"]);
  assert.deepEqual(findMatchingStocks(stocks, "appl").map((s) => s.symbol), ["AAPL"]);
  assert.deepEqual(findMatchingStocks(stocks, "SPC").map((s) => s.symbol), ["SPCX"]);
});

test("unrelated research descriptions are never searched", () => {
  assert.deepEqual(findMatchingStocks(stocks, "投资观点"), []);
  assert.deepEqual(findMatchingStocks(stocks, "半导体"), []);
  assert.deepEqual(findMatchingStocks(stocks, "ai"), []);
});

test("empty search returns every stock", () => {
  assert.deepEqual(findMatchingStocks(stocks, "  "), stocks);
});
