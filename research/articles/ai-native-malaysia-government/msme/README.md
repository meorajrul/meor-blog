# MSME support review

Start with [the readable briefing](to_human/msme-agency-review.html), or its [editable Markdown](to_human/msme-agency-review.md).

Follow-up: [Singapore, Thailand and Indonesia comparison](regional/to_human/regional-comparison.html), with [three essay outlines](regional/to_human/essay-outlines.html).

- [Agency records and classification rationale](data/agencies.json)
- [Selected KPI records with target years and scope](data/kpi-records.json)
- [Savings assumptions](data/savings-assumptions.csv) and [calculated scenarios](data/savings-scenarios.csv)
- [Sources](sources.json), [claims](claims.json), [actual recorded searches](search-log.csv), [review limitations](review.md)
- [Verification](verification.md)

The quadrant is an original conceptual classification paired with reported programme scores. The horizontal axis is analyst judgement; it is not a validated or official relevance rating. Unknown scores are not zero. No whole-agency KPI failure or current cash saving is established. The scenario is not a forecast. All publication and author-approval flags remain false.

Reproduction: run `src/build_outputs.py` with Python (standard library only), then `src/validate_outputs.js` with Node. The local-copy quadrant is the portable fallback if the conversation's inline source is unavailable. The interaction preflight uses an isolated DOM substitute and does not verify browser rendering. Original PDFs were inspected locally and identified by SHA256 in the source register, without redistributing them.
