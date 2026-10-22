# Validation — first-job article revision, 23 October 2026

Owner requested implementation of the recommended first-job focus. Article date remains24October2026at09:00MYT; source remains draft=true for scheduled release preparation. Review and schedule digest: `0a534852480c428d0718ac332be8a056b234c591ae8ae2dabcb9e82d314449c9` (identical in primary workspace and staging worktree).

- Primary journal check passed:4public,6draft. Hugo0.167.0 production build passed:36pages. Output checks passed:31HTML,17sitemapURLs, links, source boundary, draft exclusion, SEO metadata, sitemap consistency and article discovery.
- Staging worktree check passed:2public,2draft. Production build passed:28pages. Its narrower output checker passed:23HTML, links, source boundary and draft exclusion.
- Full current publication gate passed for an isolated scratch copy with draft=false and as_of24October2026. Actual article remains draft=true. No validator or theme modifications.
- Preview rebuilt in C: output folder served on loopback1338. Browser verified new title,24Octoberdate, all5article images loaded, and no horizontal overflow. Screenshot saved in task visualization folder as first-job-article-preview.png. The Singapore image initially awaited lazy loading; scrolling to its section confirmed it loaded.
- New charts visually compared with source transcription: US approximate -11/+10, Singapore19/14/8/6. CSVs, vector PDFs, code and environment record retained. Missing Singapore fieldwork dates explicitly disclosed.

Existing theme warnings concern LanguageDirection/LanguageCode deprecations. These checks establish structure/rendering, not truth, causal identification, generalisability or policy effectiveness. No main merge or production deployment performed.
