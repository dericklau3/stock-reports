/**
 * Search only stock tickers and company names, never research text.
 * Exact ticker matches take precedence over partial company-name matches.
 */
export function findMatchingStocks(stocks, query) {
  const normalized = String(query ?? "").trim().toLocaleLowerCase();
  if (!normalized) return stocks;

  const exactTickers = stocks.filter(
    (stock) => String(stock.symbol ?? "").toLocaleLowerCase() === normalized,
  );
  if (exactTickers.length > 0) return exactTickers;

  return stocks.filter((stock) => {
    const symbol = String(stock.symbol ?? "").toLocaleLowerCase();
    const companyName = String(stock.companyName ?? "").toLocaleLowerCase();
    return symbol.includes(normalized) || companyName.includes(normalized);
  });
}
