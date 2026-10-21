# SEO within a broad personal journal

Use this reference for search discovery in briefs, writing, review, publication and maintenance. Scale the work to the entry: personal reflection can be worth publishing without a search target. Preserve the author's range and voice.

## Brief: help the right reader find the entry

In brief.md, record whether search discovery matters, the reader's likely search question, intent, and the original contribution. A proposed query is a hypothesis, not measured demand. When helpful, inspect current results for that query and log the actual query, date, platform and gaps. Search-result coverage is not evidence that a claim is true. Keep factual research in the existing source and claim registers.

Record the proposed title, description, stable slug and related published entries. Avoid duplicating an existing entry's purpose. Let themes emerge from real entries; do not impose a single niche, posting quota, keyword density or minimum word count. Do not invent search volume or analytics.

## Write and review: fulfill the promise

Make the subject understandable in the title, opening and descriptive headings. Preserve reflective openings when they fit. Write an accurate, page-specific description; Google may show a different snippet. No fixed title or description length is a publication requirement.

Check that the body fulfills the headline, the byline identifies the actual author, dates reflect real publication or substantive revision, citations support their claims, and meaningful images have accurate alt text and rights records. Use contextual, crawlable links to related published entries and ensure a new entry is reachable from Journal or another page. Do not link to unfinished drafts or fabricate firsthand material to make a page appear authoritative.

Record actual discovery findings in review.md. Finalize SEO wording before the review digest. A substantive title, description, article or packet change requires the affected review to be renewed; author approval must cover the final version. SEO work never authorizes publishing an article.

## Publish: verify the artifact

Keep draft = true until the author explicitly approves that article. Check the actual authorization and final review before changing the flag. Run the project gate, the production Hugo build and check-output. Resolve exact canonical, index-directive, sitemap, structured-data, local-link and draft-leak failures. Preview the result and disclose unperformed QA. Automated checks establish structure, not truth, approval, usefulness or search ranking.

Follow the project's branch and review rules. In this project use codex/ branches and PRs to staging; the owner handles main. Push, merge and deploy only within explicit authorization. Only site/public is deployable; never the repository root or a local CMS.

After an authorized release, verify the live URL, HTTPS, robots and sitemap. If Search Console access is available, inspect indexing and sitemap status; otherwise state that these are unknown. Account verification, DNS changes and recurring monitors are separate actions requiring their applicable authorization.

## Maintain: a manual evidence loop

After real publication and sufficient data, inspect Search Console by page and relevant query. Record the question, baseline, intended change and date before editing; change one consequential issue and verify the output. Review indexing first, then impressions, clicks, CTR and position. Separate name searches from relevant discovery queries where useful. Keep private exports under private/ and out of public packets.

A 4–6 week first review and like-for-like 28-day comparisons are optional local conventions, not guarantees. Interpret CTR with position, query mix and data volume. Keep sparse results inconclusive; changes in seasonality and new-site growth limit causal inference. Record actual outcomes and decide whether to keep, revise or abandon the change. No automatic schedules or fabricated improvement charts.

## Primary guidance

Inspected 18 October 2026; refresh when platform-specific behavior matters. These are Google operational sources, not independent validation of this journal's workflow.

- [People-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): original value, sourcing and truthful authorship.
- [Titles](https://developers.google.com/search/docs/appearance/title-link) and [descriptions](https://developers.google.com/search/docs/appearance/snippet): descriptive page promises; displayed results can differ.
- [Links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) and [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap): discoverable links and preferred indexable URLs; no indexing guarantee.
- [Article metadata](https://developers.google.com/search/docs/appearance/structured-data/article): applicable types, honest dates and author identification; no guaranteed rich result.
- [Search Console performance](https://support.google.com/webmasters/answer/7576553?hl=en): query/page metrics and their interpretation.
- [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): no magic word count, ignored meta keywords, and variable time to results.

## AI search, links and reader sharing

For AI search audits, refresh current platform documentation rather than assume a separate optimization formula. Google documents indexed, snippet-eligible pages as the technical basis for supporting links in AI features; no special AI schema or llms.txt is required. Keep content readable, original and properly sourced without imposing an AI-specific voice, page length or keyword quota.

Check production robots.txt and actual CDN/WAF access separately. Local crawl permission does not establish that a live crawler can reach the site. OpenAI documents independent controls for OAI-SearchBot (search) and GPTBot (training); search visibility does not require opting into training. Preserve the owner's training preference. Report failed fetches as unverified access, not proof that the website is broken.

PageRank is an evolving Google link analysis system, not a social share count or a third-party domain score. Use contextual links between relevant published entries. Do not promise ranking gains from share buttons, schema, backlinks or a technical check. Evaluate outcomes using actual indexing and search data; keep missing or sparse evidence inconclusive.

In this journal, sharing uses site/layouts/_partials/share_icons.html and site/assets/css/extended/sharing.css, with ShowShareButtons enabled in Hugo configuration. Edit local overrides, not the vendored theme. The partial shows labelled platform links only on non-draft posts, uses the canonical URL, and supports the theme's disableShare=true opt-out. No social SDK or automatic posting is needed. Verify decoded query parameters against each post's canonical URL: interpolating an already encoded query into a URL can double-escape it. Check draft exclusion and non-post pages as well as public posts. Distinguish HTML checks from actual browser and platform-composer checks.

Current official references inspected 22 October 2026:
- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), technical requirements and SEO best practices.
- [Google generative AI optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), mythbusting special text files, markup and writing tactics.
- [Google ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide), link analysis and PageRank.
- [OpenAI crawler controls](https://developers.openai.com/api/docs/bots), OAI-SearchBot and GPTBot definitions and independent settings.
