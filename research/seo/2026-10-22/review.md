# Search discovery and sharing review — 22 October 2026

Scope: local source inspection and current official guidance. No Search Console data, backlink inventory, user research or ranking baseline was available. Live robots.txt and sitemap retrieval through the web tool failed; this does not establish a live-site fault. No publication, deployment or change to article approval.

Applied the requested brainstorming skill's problem-first, simplicity and boundary-check questions as review prompts. These are organizing questions, not an empirically validated SEO model. Priorities below are implementation judgments, not estimated ranking effects. Preserve the broad personal journal.

## Observations

Existing local source has canonical/index directives, sitemap overrides, BlogPosting/author metadata, RSS, static HTML and a search workflow (see 18 October implementation). The production check will establish current output consistency. Share buttons were disabled. The current gate reports three public articles and four drafts; no performance baseline was obtained. Existing uncommitted articles, About edits, policy edits and analytics configuration were present before this work and retained.

## Candidate register

| Candidate | Decision and evidence boundary |
| --- | --- |
| Verify Search Console indexing and sitemap after release | First priority; access/data unavailable in this review |
| Publish original entries after real author approval | First priority; approval requirements are an observed constraint, not permission to publish |
| Accurate title, description and descriptive headings | Retain existing editorial checks; no automatic rewriting of approved voice |
| Contextual links among related published entries | Apply as entries become available; Google link guidance supports crawlable anchors |
| Crawl access for AI search | Verify live robots and Cloudflare access; local production wildcard allows crawling; edge rules uninspected |
| Lightweight social sharing | Implemented locally as reader convenience; no claim of PageRank gain |
| Open Graph image per article | Later, using relevant rights-cleared assets; no fabricated default article image |
| Performance and mobile accessibility review | Measure real pages before deciding on fixes; no speed failure established |
| Topic index pages | Defer until actual entries justify useful groupings; no invented niche or thin keyword pages |
| Backlink acquisition | Seek voluntary editorial references through useful original work; no paid-link scheme or promised result |
| llms.txt or special AI schema | No implementation: Google says these are unnecessary for its AI visibility; other services need their own evidence |
| Mass FAQ pages and keyword variants | Reject without distinct reader needs and evidence; no arbitrary word count or keyword density |

## Recommended next work

1. Release the already reviewed infrastructure through the owner's staging/main process, then inspect live index directives, canonical, sitemap and crawler access. Verify the Search Console property and use URL Inspection on an actual approved article. No account verification or DNS change was performed.
2. Finish one author-selected entry with a distinct contribution, truthful byline/dates, precise title/description and readable source links. Related entries should use normal anchors. Preserve reflection as a valid genre without compulsory keyword targeting.
3. Check AI search eligibility separately from training preferences. OpenAI identifies OAI-SearchBot as search and GPTBot as training; allowing training is not a prerequisite for search. Inspect actual edge/WAF blocks before changing access rules. Google requires indexed, snippet-eligible pages for supporting links in AI features, without special AI markup.
4. Record indexing, queries, pages, impressions, clicks, CTR and position from real data after release. Review AI visibility using reports actually available in the property and record their scope. A manual 4–6 week review is only a local working convention. Sparse data cannot establish that an edit caused improvement. Keep account exports private.

PageRank is one of Google's evolving link analysis systems; it is not equivalent to share counts or a third-party domain score. This work makes no forecast of ranking, indexing or AI citation gains. Meaningful editorial references are a reasonable long-term aim; their effect on this journal remains unknown.

## Inspected sources and locators

Accessed 22 October 2026. Official operational documentation supports platform behavior, not an independent outcome study of this journal.

- Google, [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features), “Technical requirements” and “SEO best practices”: index/snippet eligibility; no extra technical requirements; no indexing guarantee.
- Google, [Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), “Mythbusting generative AI search”: no special text file/schema requirement, no ideal length, no need to rewrite for AI; “Measure visibility” for reporting guidance. This counterchecks the special-AI-file candidate.
- Google, [Ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide), “Link analysis systems and PageRank”: PageRank remains part of core ranking systems and has evolved.
- Google, [Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), crawlable anchor and descriptive internal-link guidance (search extract inspected).
- OpenAI, [Overview of crawlers](https://developers.openai.com/api/docs/bots), introduction and OAI-SearchBot/GPTBot rows: independent search/training controls and crawler access recommendations.

## Search log

Web search, 22 October 2026, no recency filter:
- site:developers.google.com/search AI features website SEO best practices
- site:platform.openai.com OAI-SearchBot robots.txt
- site:developers.google.com/search ranking systems PageRank links
Selected official Google/OpenAI pages for platform-specific claims and opened the four principal documents. Live https://meorajrul.com/robots.txt and /sitemap.xml fetches returned tool access errors. No search volume, search ranking, referral traffic or crawl-log measurements obtained.

## Implementation

Local share partial overrides the theme without modifying vendor files. Enables links on non-draft posts only, uses the canonical URL and encoded query parameters, labels each platform, wraps on mobile, and uses existing keyboard focus styling. No SDK, external font, share counter or automatic social posting. disableShare=true remains the theme's per-page opt-out. Links open the platform's compose/share interface; the reader completes sharing.

Validation results are recorded in validation.txt. UI screenshot review and authenticated platform composer checks were not performed; generated HTML checks do not prove third-party service behavior.

PR scope note: this review originally inspected the local journal-seo-workflow checkout, including uncommitted articles. The staging-based PR includes only this review, sharing controls and skill guidance. Earlier metadata/validator changes are outside this PR. The share partial resolves canonicalURL directly with Permalink fallback to avoid depending on the earlier unmerged canonical helper. See pr-validation.txt for validation of this exact staging-based candidate.

Sharing layout revision: moved the sharing row into the post header below the metadata, with inline Share this entry: label and accessible bundled SVG icons for WhatsApp, LinkedIn, Facebook, X, Telegram and Threads. Local single.html overrides the theme placement; vendor files remain unchanged. Threads uses https://www.threads.com/intent/post with encoded text and url parameters. The official Meta documentation URL https://developers.facebook.com/documentation/threads/threads-web-intents could not be retrieved; authenticated composer behavior was not verified.
