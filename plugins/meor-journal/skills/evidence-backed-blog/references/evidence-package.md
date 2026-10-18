# Evidence package

## Default layout

Adapt to the user's requested format. Omit unnecessary files with an explanation.

~~~text
article.md
brief.md
research/search-log.csv
research/sources.csv
research/claims.csv
research/extraction-notes.md
sources/
data/raw/
data/derived/
assets/images/
assets/charts/
assets/diagrams/
assets/manifest.csv
references.bib
verification.md
README.md
~~~

Use UTF-8 CSV with properly quoted fields, durable URLs, and standard Markdown. Create directories only when needed. Preserve raw files without overwriting them. Where tools permit, hash successfully saved originals with SHA-256; this detects later changes, not source authenticity.

Article-package README explains navigation, visual reproduction, missing resources, and updating. References.bib contains verified bibliographic fields only.

## Identifiers

S001 for sources, C001 for claims, A001 for assets, V001 for visuals. IDs remain stable within an article package. List multiple linked IDs with a pipe separator inside a quoted CSV field. Record underlying evidence origin to identify duplicate coverage.

Use ISO 8601 dates. Use explicit unknown values for unavailable metadata; never fabricate dates, authors, licenses, or DOI values.

## Search log

Fields:
search_id, queried_at, platform, query, filters, relevant_source_ids, selection_notes

Only record observed counts when reliably available. Log exclusions and reasons in selection_notes or a separate screening register for larger projects.

## Source register

Fields:
source_id, title, authors_or_publisher, published_at, updated_at, accessed_at, canonical_url_or_doi, resource_type, version, evidence_origin_id, inspection_status, locator, relevance, limitations, reuse_status, local_path, capture_status, capture_gap, sha256

inspection_status: discovered | inspected | inaccessible
capture_status: captured | link-only | failed
reuse_status: cleared | restricted | unknown

"Cleared" must include a basis in the notes or asset manifest. A public URL alone is not proof of reuse rights. Keep access and reuse status separate.

## Claim ledger

Fields:
claim_id, exact_claim, claim_type, supporting_source_ids, supporting_locators, contrary_source_ids, qualifications, population, geography, time_period, units, denominator, calculation, confidence_and_reason, article_location, verification_status

claim_type: fact | quotation | calculation | inference | recommendation | illustration
verification_status: verified | qualified | unsupported | pending

A calculation needs source inputs and formula. "Verified" requires actual checking; listing a citation is insufficient.

## Asset and visual manifest

Fields:
asset_id, visual_id, kind, purpose, associated_claim_ids, source_ids, title, creator, original_url, license, license_url, reuse_basis, modifications, attribution, input_paths, transformation_or_formula, editable_source_path, export_path, caption, alt_text, long_description_or_table_path, qa_status, gaps

One row per delivered asset. Use visual_id when the asset conveys a chart, table, or diagram. Include raw/derived dataset references for quantitative visuals. Use caption and attribution in the article, not only the manifest.

qa_status: inspected | pending | failed
Provide a short text identification and a longer equivalent description or table for complex visuals as appropriate to the publication format.

## Verification report

Record:
- Research cutoff and scope.
- Number of material claims checked and how they were identified.
- Citation support, numerical calculations, and quantitative visual reproduction.
- Resource capture completeness and exceptions.
- Asset reuse and attribution status.
- Link and export checks.
- Rendered visual inspection or pending checks.
- Unsupported claims removed, qualifications added, and unresolved gaps.

Do not interpret missing denominators as perfect performance. Separate structural checks from factual and visual verification.
