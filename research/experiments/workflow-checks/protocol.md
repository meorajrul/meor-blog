# Workflow checks — protocol

Locked before running by the bootstrap commit. These are engineering and editorial scenario checks, not a scientific evaluation of writing quality.

H1: Create a reflection with no external claims. Prediction: the draft can have empty evidence arrays, but cannot publish without an actual author review.
H2: Create an essay with an uninspected source, missing locator, unsupported claim, or duplicated source IDs. Prediction: each invalid packet is rejected.
H3: Try to publish with unresolved issues, pending author approval, expired freshness, unsafe article IDs, or a changed article after review. Prediction: reject. A complete synthetic fixture is accepted structurally; this does not prove truth.
H4: Build production with draft canaries. Prediction: drafts, local admin, research, private notes, and plugin sources do not appear in the served artifact. Check canonicals, sitemap, RSS, relative assets, internal links, CNAME and empty-site behavior.

Record exact outcomes and repairs in results.md after execution. Changes to protocol after tests must be labeled exploratory. No benchmark superiority, preregistered reader study, or quantitative research claim is implied.
