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
    .replace(/[，。]\s*$/u, (match) => match.trim())
    .trim();
}

function normalizeParagraph(value) {
  return stripMarkdown(value.replace(/\s+/g, " "));
}

const VIEW_LABELS = [
  "中性偏建设性", "中性偏谨慎", "中性偏积极", "谨慎中性",
  "建设性但谨慎", "谨慎看好", "谨慎观察", "积极看好",
  "研究中", "待研究", "看多", "看空", "看好", "中性",
  "建设性", "谨慎", "乐观", "观望", "偏多", "偏空",
];

function ratingFromText(value) {
  const text = stripMarkdown(value).replace(/^\s*[-–]\s*/, "").replace(/^[“"「]+/, "").trim();
  for (const label of VIEW_LABELS) {
    if (text.startsWith(label)) return label === "待研究" ? "研究中" : label;
  }
  // Legacy reports sometimes state a directional view in prose rather than a tag.
  const opening = text.split(/[。；;\n]/u, 1)[0].slice(0, 105);
  if (/保持建设性/.test(opening)) return "建设性";
  if (/仍需谨慎|需要谨慎|需谨慎/.test(opening)) return "谨慎观察";
  return "";
}

/** Extract only a short, explicitly supported view label, never a whole Tracker section. */
export function extractInvestmentView(trackerMarkdown, newestReportMarkdown = "") {
  for (const markdown of [trackerMarkdown, newestReportMarkdown]) {
    const head = markdown.slice(0, 3000);
    const match = head.match(/^\s*(?:[-*]\s*)?\*{0,2}(?:当前)?(?:投资观点|观点)\s*[：:]\s*\*{0,2}\s*(.+)$/m);
    if (match) {
      const label = ratingFromText(match[1]);
      if (label) return label;
    }
    const sectionText = extractSection(head, ["Current Research View", "Current view"]);
    const label = sectionText ? ratingFromText(sectionText) : "";
    if (label) return label;
  }
  return "研究中";
}

function extractTitle(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? stripMarkdown(match[1]) : fallback;
}

function extractCompanyName(title, symbol) {
  const withoutTracker = title
    .replace(/\s*Tracker\b.*$/i, "")
    .replace(/\s*Research\s+Tracker\b.*$/i, "")
    .trim();
  const parenMatch = withoutTracker.match(/^(.+?)[（(]\s*[A-Z.]+[）)]/);
  if (parenMatch) return stripMarkdown(parenMatch[1]);
  if (!withoutTracker || withoutTracker.toUpperCase() === symbol) return symbol;
  return stripMarkdown(withoutTracker);
}

function extractLastUpdated(markdown) {
  const patterns = [
    /Last updated:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})/i,
    /\*\*Last updated\*\*:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})/i,
    />\s*Last updated:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})/i,
    /-\s+\*\*Last updated\*\*:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})/i,
  ];

  for (const pattern of patterns) {
    const match = markdown.match(pattern);
    if (match) return match[1];
  }

  return "";
}

function extractSection(markdown, names) {
  const normalizedNames = new Set(names.map((name) => name.toLowerCase()));
  const lines = markdown.split("\n");
  const sectionLines = [];
  let inSection = false;

  for (const rawLine of lines) {
    const line = rawLine.trim();
    const heading = line.match(/^##\s+(.+)$/);

    if (heading) {
      if (inSection) break;
      inSection = normalizedNames.has(heading[1].trim().toLowerCase());
      continue;
    }

    if (inSection && line && !line.startsWith("---")) {
      sectionLines.push(line);
    }
  }

  return normalizeParagraph(sectionLines.slice(0, 4).join(" "));
}

function firstReadableParagraph(markdown) {
  const lines = markdown
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith("#") && !line.startsWith(">"));

  return normalizeParagraph(lines.slice(0, 3).join(" "));
}

async function pathExists(filePath) {
  try {
    await stat(filePath);
    return true;
  } catch {
    return false;
  }
}

async function readMarkdownFile(filePath) {
  const content = await readFile(filePath, "utf8");
  return {
    content,
    title: extractTitle(content, path.basename(filePath, ".md")),
  };
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
    const filePath = path.join(reportsDir, fileName);
    const markdown = await readMarkdownFile(filePath);
    const slug = slugForReport(fileName);
    const dateMatch = fileName.match(/[0-9]{4}-[0-9]{2}-[0-9]{2}/);
    reports.push({
      slug,
      fileName,
      title: markdown.title,
      date: dateMatch ? dateMatch[0] : "",
      content: markdown.content,
    });
  }

  return reports;
}

export async function buildReportIndex(companiesDir) {
  const entries = await readdir(companiesDir, { withFileTypes: true });
  const symbols = entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .filter((name) => !name.startsWith("."))
    .sort((a, b) => a.localeCompare(b));

  const companies = [];

  for (const symbol of symbols) {
    const companyDir = path.join(companiesDir, symbol);
    const trackerPath = path.join(companyDir, "tracker.md");
    if (!(await pathExists(trackerPath))) continue;

    const tracker = await readMarkdownFile(trackerPath);
    const reports = await readReports(path.join(companyDir, "deep-research"));
    const title = tracker.title;
    const currentView =
      extractSection(tracker.content, ["Current Research View", "Current view", "Current research view"]) ||
      firstReadableParagraph(tracker.content);

    // Prefer the newest known research date; a Tracker header can be absent
    // (e.g. the Chinese PL first-coverage Tracker) or stale after a new report.
    const trackerDate = extractLastUpdated(tracker.content);
    const reportDates = reports.map((report) => report.date).filter(Boolean);
    const lastUpdated = [trackerDate, ...reportDates].filter(Boolean).sort().at(-1) || "";

    companies.push({
      symbol,
      companyName: extractCompanyName(title, symbol),
      title,
      lastUpdated,
      currentView,
      investmentView: extractInvestmentView(tracker.content, reports[0]?.content || ""),
      summary: extractSection(tracker.content, ["Current Main Thesis", "Main thesis"]) || currentView,
      keyRisks: extractSection(tracker.content, ["Key Risks", "Key risks"]),
      tracker: {
        fileName: "tracker.md",
        title,
        content: tracker.content,
      },
      reports,
    });
  }

  companies.sort((a, b) => {
    const dateCompare = (b.lastUpdated || "").localeCompare(a.lastUpdated || "");
    return dateCompare || a.symbol.localeCompare(b.symbol);
  });

  return {
    generatedAt: new Date().toISOString(),
    companies,
  };
}
