# Chosen comparative essay

The owner selected outline 1, “Can Malaysia merge its way to better MSME support?”, on 19 October 2026 and requested a hero image and charts.

- [Offline essay preview](to_human/essay-preview.html)
- [Editable Hugo essay](../../../site/content/posts/can-malaysia-merge-msme-support/index.md)
- [Editorial review](review.md) and [verification](verification.md)
- [Model notes](model-notes.md), [source register](sources.json), [claim ledger](claims.json), [asset provenance](assets.json)
- [Hero prompt and generation mode](hero-prompt.md)
- [Upstream regional research and outlines](../ai-native-malaysia-government/msme/regional/README.md)

Three charts have original data, transformations, 300 dpi PNG and vector PDF outputs. The quadrant combines reported 2024 programme performance with explicitly qualitative analyst judgments. The fiscal chart shows conditional scenarios, not observed savings.

Rebuild evidence snapshots with src/prepare_packet.py, figures with src/build_charts.py, and asset provenance with src/assemble_artifacts.py. The offline copy uses src/build_preview.py after a separate Hugo draft build in .cache/msme-essay-preview-build. Matplotlib is needed for figures; the local dependency target is .cache/msme-plot-deps.

The owner subsequently approved the delivered illustrated version for release on 20 October 2026 at 09:00 Malaysia time. See schedule.json and review.json. The article remains technically a draft before the scheduled release preparation. The owner handles the final main merge and production deployment; approval is not evidence of a live release.
