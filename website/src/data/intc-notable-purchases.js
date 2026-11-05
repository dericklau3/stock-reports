// INTC 历史公开交易。家庭申报不等于本人下单；收盘参考价并非实际成交价。
const trumpBuys = [
  ["2026-03-02", 45.50], ["2026-03-11", 47.98], ["2026-03-13", 45.77],
  ["2026-03-17", 44.06], ["2026-03-23", 44.01], ["2026-03-25", 47.18],
  ["2026-04-07", 52.91], ["2026-04-15", 64.94],
];
const trumpSales = [
  ["2026-04-27", 84.99], ["2026-05-18", 108.17], ["2026-08-21", 90.07],
];
const referenceMean = (rows) =>
  Math.round((rows.reduce((sum, [, price]) => sum + price, 0) / rows.length) * 100) / 100;

export const intcNotablePurchases = {
  asOf: "2026-11-02",
  people: [
    {
      id: "lip-bu-tan",
      name: "陈立武",
      identity: "Intel CEO · 家族信托",
      average: 95,
      averageLabel: "成交均价",
      summary: "2026-08-11 主动买入 105,263 股，约 1,000 万美元。",
      averageBasis: "SEC Form 4 披露的实际每股成交价，单笔买入。",
      trades: [{ date: "2026-08-11", kind: "股票买入", price: 95, detail: "105,263 股 · Form 4 代码 P" }],
      note: "申报确认这笔主动买入，但不代表截至今日仍完整持有。",
      sources: [
        { label: "SEC Form 4", url: "https://www.sec.gov/Archives/edgar/data/50863/000005086326000177/xslF345X05/form4.xml" },
      ],
    },
    {
      id: "trump",
      name: "特朗普申报账户",
      identity: "家庭 / 申报账户 · 非政府持股",
      average: referenceMean(trumpBuys),
      averageLabel: "参考均价",
      summary: "公开披露包含 8 笔普通股买入和 3 笔卖出。",
      averageBasis: "8 个买入交易日收盘价的简单算术平均，非实际成交均价；各笔精确成交价与买入股数未披露，无法计算真实成本。",
      trades: [
        ...trumpBuys.map(([date, price]) => ({ date, kind: "股票买入", price })),
        ...trumpSales.map(([date, price]) => ({ date, kind: "股票卖出", price })),
      ],
      note: "方向及日期来自公开财务申报；表中价格是对应交易日 INTC 的收盘参考价，并非成交价格。申报无法确定具体交易家庭成员或剩余持股数。",
      sources: [
        { label: "交易披露汇总", url: "https://wallstreettoday.com/tracking-trump/stocks/intc/" },
        { label: "OGE 原始申报", url: "https://extapps2.oge.gov/201/Presiden.nsf/PAS%2BIndex/0BDCCCE7DE13AEFA85258E8A002DE2B5/$FILE/Donald-J-Trump.09.17.2026-278T.pdf" },
      ],
    },
    {
      id: "pelosi",
      name: "佩洛西家庭",
      identity: "Paul Pelosi · 配偶申报",
      average: 92.32,
      averageLabel: "股票参考价",
      summary: "2026-07-24 买入 10,000 股普通股；另外披露两笔看涨期权买入。",
      averageBasis: "仅以 7 月 24 日这笔普通股交易的当日收盘价作参考，非实际成交价；期权不计入普通股均价。",
      trades: [
        { date: "2026-05-29", kind: "期权买入", price: null, detail: "200 张看涨期权 · 行权价 $50 · 2027-03-19 到期" },
        { date: "2026-07-24", kind: "股票买入", price: 92.32, detail: "10,000 股 · 当日收盘参考价" },
        { date: "2026-07-24", kind: "期权买入", price: null, detail: "50 张看涨期权 · 行权价 $50 · 2027-06-17 到期" },
      ],
      note: "期权权利金未核实，“—”不是 $0；未披露卖出也不等于确定仍持有，期权不等于股票。",
      sources: [
        { label: "5 月国会申报", url: "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20034836.pdf" },
        { label: "7 月国会申报", url: "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035143.pdf" },
      ],
    },
  ],
};
