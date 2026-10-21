# Malaysia charts: source data and reproduction

These are original plots of published numbers, with no publisher artwork copied. The chart PNG/PDF/SVG files and downloadable CSVs are in site/content/posts/work-meaning-ai-malaysia/. Research inputs are kept here.

malaysia-income-shares.csv: DOSM GDP Income Approach 2025 overview, with 2024 comparative figures. Percent of nominal GDP. Each row totals 100. GOS includes mixed income, depreciation and statistical discrepancy; it is not pure corporate profit. Data do not estimate AI effects.

malaysia-ai-exposure.csv: IMF Country Report 25/57 Annex IV paragraphs 9–10. Percent of employed people, with sex-specific denominators where marked. Employment data extrapolated to 2018 with fixed detailed occupational shares from 2000. Values 27,20,40,20 are quoted individually; no overall total inferred from rounded inconsistent totals. Not job-loss probabilities.

Use Python 3.12 with matplotlib (versions in malaysia-plot-environment.json). From the repository root, run the generator in this folder. If plotting packages are installed normally the script uses them; it also checks the local ignored .tools/research-figure/python-packages folder. Layout positions are not empirical data. Export files were visually inspected before inclusion, and their hashes are in assets.json.
