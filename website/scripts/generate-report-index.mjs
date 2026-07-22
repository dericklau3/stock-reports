import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildReportIndex } from "./report-index.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const websiteRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(websiteRoot, "..");
const companiesDir = path.join(repoRoot, "research", "COMPANIES");
const outputFile = path.join(websiteRoot, "src", "data", "report-index.json");

const index = await buildReportIndex(companiesDir);

await mkdir(path.dirname(outputFile), { recursive: true });
await writeFile(outputFile, `${JSON.stringify(index, null, 2)}\n`);

console.log(`Generated ${index.companies.length} companies at ${path.relative(repoRoot, outputFile)}`);
