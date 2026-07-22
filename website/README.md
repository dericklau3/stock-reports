# Stock Reports Website

This Astro site renders the Markdown research files under `../research/COMPANIES`.

## Local Development

```bash
bun install
bun run dev
```

## Build

```bash
bun run test
bun run build
```

The build script regenerates `src/data/report-index.json` before Astro renders the static site.
