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

// Marked preserves raw HTML blocks verbatim. Parse the Markdown body of our
// native, default-closed <details> elements before handing the page to Marked.
export function renderMarkdown(markdown) {
  const renderedDetails = markdown.replace(
    /(<details class="business-detail">\s*<summary>[\s\S]*?<\/summary>)([\s\S]*?)(<\/details>)/g,
    (_whole, opening, body, closing) =>
      `${opening}\n<div class="business-detail-content">\n${marked.parse(body.trim())}\n</div>\n${closing}`,
  );
  // Event Roadmap bodies live inside raw HTML <details>. Parse their Markdown
  // once so GitHub's source keeps readable text while website dialogs have rich HTML.
  const renderedEvents = renderedDetails.replace(
    /(<div class="event-detail-content">)([\s\S]*?)(<\/div>)/g,
    (_whole, opening, body, closing) =>
      `${opening}\n${marked.parse(body.trim())}\n${closing}`,
  );
  return marked.parse(renderedEvents);
}
