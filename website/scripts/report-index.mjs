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

    companies.push({
      symbol,
      companyName: extractCompanyName(title, symbol),
      title,
      lastUpdated: extractLastUpdated(tracker.content),
      currentView,
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
