# SEO improvements that fit this personal journal

This is the baseline audit. The approved workflow and technical fixes have since been implemented locally; see [implementation results](implementation.md).

Prepared 18 October 2026, Asia/Kuala_Lumpur. Status: researched recommendation, not implemented or published. This is a bounded technical audit and workflow review, not a ranking experiment.

## Recommendation

Keep the existing capture → brief → research → think → write → review → author approval → publish workflow. Add a reader-search question in the brief, a discovery check before approval, and a manual measurement loop after publishing. Preserve the broad personal journal and its separate genres.

The largest current constraint is the lack of published journal entries: the content check reports **0 public posts and 1 draft**. That is an observed baseline. My judgment is that finishing useful, author-approved entries deserves priority over extensive template tuning. It is not a measured prediction of traffic growth.

Your source appraisal, honest first-person boundaries, About page and editorial review are useful foundations. They align with Google's emphasis on original value, reliable information and clear authorship. A private claim ledger or passing validator is not itself a demonstrated ranking benefit. [People-first guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

## What I verified

- All six URLs in the current sitemap were fetched successfully. HTTPS works; HTTP and the www host redirect to the HTTPS apex. Robots allows crawling and names the sitemap. A deliberately missing URL returns 404.
- Home, About and Journal carry self-referencing HTTPS canonicals and index directives. Search has noindex, appropriately for a utility page, but is also listed in the sitemap.
- Tags and Categories return 200 and are indexable despite having no public entries. The empty Journal listing is expected at this stage.
- The homepage title is only “Meor Ajrul”. Its structured data calls Meor an Organization. The About and Search pages are marked as BlogPosting; Search also emits year-0001 dates. These are semantic cleanup opportunities, not evidence of a ranking penalty.
- Existing checks pass: content validation; Hugo 0.167.0 production build; nine generated HTML files checked for local links, canonical-domain presence, source boundaries and draft exclusion. Two existing PaperMod language-property deprecation warnings remain.

Full observations are in [observations.json](observations.json). Local checks are stronger than nothing, but do not verify exact canonical-to-page matching, every index directive, sitemap consistency, schema meaning, Google indexing or page speed.

## Priorities and acceptance criteria

Priority reflects my judgment about this small journal, not measured search impact. “Owner” identifies who would perform a later action.

| Priority | Observation or gap | Recommended action | Owner and verification |
| --- | --- | --- | --- |
| 1 | No public posts | Finish a real entry through the existing author-review process; keep later entries driven by personal interest and reader value | Meor and editor: approved article, current digest, production URL visible from Journal and in sitemap |
| 1 | Search performance unavailable to this audit | Use an existing Search Console property, or verify one if absent; submit the sitemap and inspect the first published URL | Meor/account owner: property access, sitemap status, URL Inspection result and initial performance export |
| 2 | Brief asks who the reader is but not how they would search | Add optional discovery fields to brief.md; make search intent explicit for explainers and reviews | Editor: one clear question and a distinct contribution; no invented demand or keyword volume |
| 2 | Search is noindex but in sitemap | Exclude noindex utility pages from the sitemap while keeping them crawlable so directives can be seen | Site maintainer: generated and live sitemap contain only intended indexable canonical URLs; Search remains noindex |
| 2 | Empty Tags and Categories are indexable | Keep them out of search/sitemap until they offer useful navigation; reassess when entries accumulate | Site maintainer: no empty archive submitted; meaningful populated archives can later be indexed |
| 2 | Output check covers only part of SEO | Extend automated checks for exact canonicals, intended robots directives, sitemap agreement and metadata presence | Maintainer: valid fixtures pass; deliberately broken fixtures fail; existing checks stay green |
| 3 | Homepage title gives only the name | Consider “Meor Ajrul — A Personal Journal”; review the snippet for clarity | Meor/editor: rendered title and description match the site's actual purpose |
| 3 | Generic theme schema misclassifies utility/profile pages | Use Person for author identity; link article authors to About; emit BlogPosting only for actual posts and omit unset dates | Site maintainer: generated JSON parses, types match pages, applicable live articles checked with Rich Results Test |
| Measure first | Mobile experience and real-world speed not tested | Check Home and the first real article on mobile and with PageSpeed Insights; fix observed problems | Site maintainer: dated results, lab/field distinction and any field-data absence recorded |

A sitemap should identify preferred pages for search; submitting it does not guarantee indexing. [Sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

The proposed title is an editorial suggestion. Google recommends descriptive, concise titles and chooses the displayed search title itself. [Title guidance](https://developers.google.com/search/docs/appearance/title-link)

Use the existing theme configuration for supported options, and local layout overrides for the rest. Do not edit the vendored theme. Later source work should use a codex/ branch and a PR to staging under your current instructions; the older documentation's direct-main publishing language should be reconciled then. No branch, commit, PR, account change or deployment was made for this audit.

## Fit SEO into the current workflow

| Existing stage / skill | Small addition | Boundary |
| --- | --- | --- |
| Capture / blog-topics | For ideas with discovery value, write the reader's likely search question beside reader_question | Treat it as a hypothesis; reflection can be selected entirely for personal value |
| Brief / blog-research | Review a few actual search results for intent and missing explanations; record the actual query/date and state your distinct contribution | Search results show existing coverage, not proof of demand or truth; use primary sources for factual claims |
| Think and write / blog-think, blog-write | Make the subject understandable in title, opening and headings; write an accurate description and stable, readable slug | No forced keyword density, word count or change to the author's voice |
| Review / blog-review | Check that the article fulfills its title, credits the author and sources, uses truthful dates, and links naturally to relevant published entries | Search optimization cannot bypass evidence, privacy or author review |
| Approve and publish / blog-publish | Finalize SEO wording before computing the review digest; run existing gates plus proposed SEO checks | Substantive edits require the applicable renewed review/approval; never manufacture author approval |
| Correct and maintain | Inspect discovery and indexing after release; review query/page results when sufficient data accumulates | No rankings promised; keep private performance exports under private/ |

Contextual internal links help readers and crawlers find related pages. Once related entries exist, link a new entry from an older relevant page as well as Journal; do not create links to unfinished drafts. There is no ideal link quota. [Link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)

Keep ordinary source citations. Evidence links serve readers; the original contribution still needs to come from your analysis, experience or useful synthesis.

## Example: the existing Iqra topic

This applies to `editorial/topic-briefs/iqra-in-the-age-of-ai/brief.md`. These are proposed editorial choices, not measured keywords or approved copy.

- Reader-search hypothesis: “How can I read AI-generated documents critically?”
- Intent: understand a practical reading and judgment problem, with a personal reflection on Iqra.
- Existing working title to retain: **Iqra in the Age of AI: Read Before You Decide**.
- Possible description: “A reflection on reading AI-generated documents, checking source context, and staying responsible for the decisions that follow.”
- Distinct contribution: the author's supplied connection between reading, navigation, source context and responsibility. Keep religious interpretation, analogy and empirical claims clearly separated.
- Opening/review question: does the first part make that connection clear without claiming AI causes memory loss or inventing a workplace incident?
- Future related entries: the proposed GPS review, document-reading field note, and output-versus-understanding essay answer different questions. Link them when they exist; these are an emerging theme, not a required AI-only niche.

A description is a concise, page-specific invitation. Google may instead generate a different snippet from the page; there is no fixed description-length rule. [Description guidance](https://developers.google.com/search/docs/appearance/snippet)

## A bounded autoresearch loop

The engineering baseline is measurable now. Search outcomes need published material and actual account data. The following are **prospective observational checks**, not completed or preregistered experiments.

| Hypothesis | Next action | What to measure | Interpretation limit |
| --- | --- | --- | --- |
| Clear, useful entries create opportunities for discovery | Publish the first approved entry and repeat when ready | Public article count (baseline 0), indexability, indexed status, relevant impressions and clicks when available | More published pages alone do not establish usefulness or rankings |
| A clearer title/opening better matches a reader question | After collecting a baseline, revise one eligible article if actual queries reveal a mismatch | Same page/query segment; impressions, clicks, CTR and position before/after | Position, query mix, seasonality and new-site growth can explain changes |
| Related links improve navigation and discovery | Add contextual links between genuinely related published pages | Crawlable inbound links, orphan-page check and subsequent discovery/index status | A structural pass cannot prove reader satisfaction or a causal search effect |

For the inner loop, choose one consequential gap, record the intended change and baseline before editing, make the change, verify the output, and keep a dated result. For the outer loop, review the pattern manually after a few meaningful changes or when enough search data exists; keep, revise or abandon the hypothesis.

A practical starting review window is 4–6 weeks after publication, then compare like-for-like 28-day periods when meaningful. This is a project convention, not a promised time to results. Keep low-volume results inconclusive. Google's guidance says effects can take hours to months. [Timing and cautions](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

Search Console supplies clicks, impressions, CTR and position by dimensions including query and page. Look at indexing first, then relevant non-name discovery alongside searches for Meor's name. CTR must be read in the context of position and query mix. [Performance report](https://support.google.com/webmasters/answer/7576553?hl=en)

The recommended initial dashboard is small: public entries, indexed article URLs, relevant impressions, clicks and unresolved technical issues. No numerical traffic target or upward performance chart is justified by the available evidence.

## What to leave alone for now

Keep the broad personal journal. Do not introduce a publishing quota, artificial minimum length, keyword-density score, mass-produced AI posts or a large taxonomy of empty pages. Google ignores meta keywords and does not prescribe a magic word count. Those shortcuts do not address the current absence of public entries. [Starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

Structured-data cleanup is useful accuracy work; it is not a prerequisite to ordinary search visibility. Google's Article guidance recommends applicable properties and author identification, rather than a universal required-property list. [Article markup](https://developers.google.com/search/docs/appearance/structured-data/article)

Measure real mobile performance before claiming the static site is fast. Core Web Vitals concern loading, responsiveness and visual stability. No scores or real-user measurements were collected here. [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)

## Scope, evidence and stopping decision

Inputs: START-HERE.md, editorial/workflow.md, editorial/topics.csv and the existing Iqra brief; research/findings.md and research-state.yaml; the local blog-research skill and contract; plugin article/brief templates and validator; Hugo configuration, local overrides, theme metadata templates, build workflow and generated output. External guidance is catalogued in [sources.json](sources.json), with actions in [search-log.csv](search-log.csv).

The requested autoresearch skill is adapted to the project's bounded editorial-research process. Initial inspection plus targeted counterchecks established the technical baseline and the recommendation. No SEO changes, ranking tests, reader studies, Search Console inspection, backlink audit, mobile rendering test or Core Web Vitals test were run. No recurring automation was created.

Search Console access and existing setup are unknown; absence of account data is not proof that it is unconfigured. Public tracked research is not a place for private account exports. Source guidance comes from one provider origin group, appropriate for Google-specific behavior but not independent experimental replication.

The website reader could not access the custom domain; direct TLS-verified public requests succeeded, so that tool failure is not reported as a website failure. Existing setup notes still describe pending HTTPS, but the newer direct observations show it working.

Conclude this audit: enough evidence exists to prioritize the workflow changes. Future traffic claims require the publishing and measurement loop above. The site source, workflow, plugin, approval records and publication state remain unchanged.
