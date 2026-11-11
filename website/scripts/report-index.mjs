import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";

export function slugForReport(fileName) {
  return fileName.replace(/\.md$/i, "");
}

function stripMarkdown(value) {
  return value
    .replace(/\*\*/g, "")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
}

const VIEW_LABELS = [
  "中性偏建设性", "中性偏谨慎", "中性偏积极", "谨慎中性",
  "建设性但谨慎", "谨慎看好", "谨慎观察", "积极看好",
  "研究中", "待研究", "看多", "看空", "看好", "中性",
  "建设性", "谨慎", "乐观", "观望", "偏多", "偏空",
];

function ratingFromText(value) {
  const text = stripMarkdown(value).replace(/^[-–]\s*/, "").replace(/^[“"「]+/, "").trim();
  for (const label of VIEW_LABELS) {
    if (text.startsWith(label)) return label === "待研究" ? "研究中" : label;
  }
  const opening = text.split(/[。；;，,\n]/u, 1)[0].slice(0, 105);
  if (/保持建设性|偏向积极/.test(opening)) return "建设性";
  if (/仍需谨慎|需要谨慎|需谨慎/.test(opening)) return "谨慎观察";
  return "";
}

function extractOpeningField(markdown, field) {
  const lines = markdown.slice(0, 5000).split("\n");
  for (const source of lines) {
    const line = source.trim().replace(/^[-*]\s*/, "");
    const cleaned = line.replace(/^\*{0,2}/, "");
    for (const name of field === "投资观点" ? ["投资观点", "当前投资观点", "观点"] : [field]) {
      if (!cleaned.startsWith(name + "：" ) && !cleaned.startsWith(name + ":")) continue;
      return stripMarkdown(cleaned.slice(name.length + 1));
    }
  }
  return "";
}

function firstReadableParagraph(markdown) {
  return stripMarkdown(
    markdown.split("\n")
      .map((line) => line.trim())
      .filter((line) => line && !line.startsWith("#") && !line.startsWith(">"))
      .slice(0, 2).join(" "),
  );
}

/** Stock views come from the latest deep-research report, never Tracker. */
export function extractInvestmentView(reportMarkdown) {
  const view = extractOpeningField(reportMarkdown, "投资观点");
  return ratingFromText(view || firstReadableParagraph(reportMarkdown)) || "研究中";
}

function extractTitle(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? stripMarkdown(match[1]) : fallback;
}

function extractCompanyName(title, symbol) {
  const source = title.replace(/^(?:完整)?(?:中文)?(?:深度)?研究\s*[:：-]\s*/, "").trim();
  const prefix = source.split(/[（(]/u)[0].trim();
  if (prefix && prefix.toUpperCase() !== symbol && prefix.length < 90) {
    return prefix.replace(/\s*(?:完整|中文)?(?:深度|个股)?(?:研究|分析)(?:报告)?(?:[—\-｜].*)?$/u, "").trim() || prefix;
  }
  return symbol;
}


/**
 * Read scenario price ranges from the latest report's valuation section.
 * These are conditional reference prices from the report, not live quotes.
 * Return null for unquantified scenarios; never extrapolate missing values.
 */
export function extractValuationRanges(markdown) {
  const heading = /^##\s+(?:\d+[.、]\s*)?估值[^\n]*$/m.exec(markdown);
  if (!heading) return null;
  const rest = markdown.slice(heading.index + heading[0].length);
  const nextHeading = rest.search(/^##\s+/m);
  const section = nextHeading < 0 ? rest : rest.slice(0, nextHeading);
  const prices = { bear: null, base: null, bull: null };
  const keys = { 悲观: "bear", 基础: "base", 乐观: "bull" };

  for (const line of section.split("\n")) {
    if (!/^\s*\|/.test(line)) continue;
    const cells = line.split("|").slice(1, -1).map((cell) => cell.trim());
    const scenario = cells[0]?.replace(/\*/g, "").trim().match(/^(悲观|基础|乐观)(?:$|\s|[（(])/);
    if (!scenario) continue;
    const key = keys[scenario[1]];
    if (prices[key]) continue;

    // The first part of a table row can contain revenue/profit ranges.
    // The last USD interval in the scenario row is the per-share price range.
    const matches = [...cells.slice(1).join(" | ").matchAll(
      /\$\s*(\d+(?:,\d{3})*(?:\.\d+)?)\s*[–—\-~～至]\s*\$?\s*(\d+(?:,\d{3})*(?:\.\d+)?)/g,
    )];
    const price = matches.at(-1);
    if (price) {
      const low = Number(price[1].replaceAll(",", ""));
      const high = Number(price[2].replaceAll(",", ""));
      if (Number.isFinite(low) && Number.isFinite(high) && low > 0 && high >= low) {
        prices[key] = { low, high };
      }
    }
  }

  return {
    ...prices,
    currency: "USD",
    unit: /\bADS\b/.test(section) ? "ADS" : "股",
  };
}

async function pathExists(filePath) {
  try {
    await stat(filePath);
    return true;
  } catch {
    return false;
  }
}

async function readReports(reportsDir) {
  if (!(await pathExists(reportsDir))) return [];
  const entries = await readdir(reportsDir, { withFileTypes: true });
  const markdownFiles = entries
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => entry.name)
    .sort((a, b) => b.localeCompare(a));

  const reports = [];
  for (const fileName of markdownFiles) {
    const content = await readFile(path.join(reportsDir, fileName), "utf8");
    const dateMatch = fileName.match(/\d{4}-\d{2}-\d{2}/);
    reports.push({
      slug: slugForReport(fileName),
      fileName,
      title: extractTitle(content, path.basename(fileName, ".md")),
      date: dateMatch ? dateMatch[0] : "",
      content,
    });
  }
  return reports;
}

export async function buildReportIndex(companiesDir) {
  const entries = await readdir(companiesDir, { withFileTypes: true });
  const symbols = entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((symbol) => !symbol.startsWith("."))
    .sort((a, b) => a.localeCompare(b));

  const companies = [];
  for (const symbol of symbols) {
    const reports = await readReports(path.join(companiesDir, symbol, "deep-research"));
    if (!reports.length) continue;

    const latest = reports[0];
    const currentView = extractOpeningField(latest.content, "投资观点") || firstReadableParagraph(latest.content);
    companies.push({
      symbol,
      companyName: extractCompanyName(latest.title, symbol),
      title: latest.title,
      lastUpdated: latest.date,
      currentView,
      investmentView: extractInvestmentView(latest.content),
      valuation: extractValuationRanges(latest.content),
      summary: extractOpeningField(latest.content, "核心逻辑") || currentView,
      keyRisks: extractOpeningField(latest.content, "主要风险"),
      reports,
    });
  }

  companies.sort((a, b) =>
    (b.lastUpdated || "").localeCompare(a.lastUpdated || "") || a.symbol.localeCompare(b.symbol),
  );
  return {
    generatedAt: new Date().toISOString(),
    companies,
  };
}
