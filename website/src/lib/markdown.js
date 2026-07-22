import { marked } from "marked";

marked.use({
  gfm: true,
  breaks: false,
});

export function reportUrl(baseUrl, symbol, fileName) {
  const slug = fileName.replace(/\.md$/i, "");
  return withBase(baseUrl, `reports/${symbol}/${slug}/`);
}

export function withBase(baseUrl, pathName = "") {
  const normalizedBase = baseUrl.endsWith("/") ? baseUrl : `${baseUrl}/`;
  const normalizedPath = pathName.startsWith("/") ? pathName.slice(1) : pathName;
  return `${normalizedBase}${normalizedPath}`;
}

export function rewriteResearchLinks(markdown, baseUrl, symbol) {
  return markdown.replace(/\]\(deep-research\/([^)]+\.md)\)/g, (_match, fileName) => {
    return `](${reportUrl(baseUrl, symbol, fileName)})`;
  });
}

export function renderMarkdown(markdown) {
  return marked.parse(markdown);
}
