# Practice 09 - Data science portfolio

Archive copy of the Practice 09 deliverable, kept in sync with the two public repositories:

- **Live portfolio website:** https://kelvin-chan-ka-wai.github.io/data-science-portfolio/
- **Project repository:** https://github.com/Kelvin-Chan-Ka-Wai/data-science-project
- **Portfolio repository:** https://github.com/Kelvin-Chan-Ka-Wai/data-science-portfolio

## What is in this folder

| Path | Content |
|---|---|
| `index.md`, `_config.yml`, `assets/` | Source of the portfolio site (Jekyll theme `jekyll-theme-cayman`) |
| `REFLECTION.md` | Submitted reflection: ~200-word version, ~100-word checklist version, feedback-to-commit table and responsible-sharing check |
| `REVIEW.md` | The peer review the work responds to, with immutable commit hashes |
| `project/README.md` | Question, dataset sources and permissions, methods, findings, limitation, run instructions |
| `project/notebooks/` | Three executed notebooks (population, car prices, Olympics dashboard) |
| `project/figures/` | The three labelled visualisations used by the README and the portfolio page |
| `project/data/` | Public datasets (World Bank WDI, UCI Automobile, Rio 2016 athletes) and their permission notes |
| `project/scripts/` | `make_figures.py` (PNG + interactive HTML) and `check_notebooks.py` (execution gate) |
| `project/.github/workflows/` | CI that re-runs every notebook and regenerates the figures |

## Checklist status

- [x] Notebooks, scripts and `requirements.txt` are uploaded and organised
- [x] At least two readable visualisations with titles, labels and units (three provided)
- [x] README covers question, dataset sources/permissions, methods, findings and a limitation
- [x] Run instructions tested: pinned environment, all notebooks execute, CI repeats it
- [x] Findings match the code and the figures (values recomputed from the committed data)
- [x] Site introduces the author and lists technical skills
- [x] Showcase includes title, research question, visualisation, findings, limitation and status
- [x] GitHub Pages site opens; images and links verified
- [x] Feedback recorded with the commit that addresses it (`REVIEW.md`)
- [x] No credentials or restricted data; the individual-level Olympic source is disclosed
- [x] A **classmate** review - already obtained

## Process

1. Built the analysis notebooks against the CISC7204 tutorial material.
2. Wrote the project README and exported three Bokeh figures.
3. Published `data-science-project` and `data-science-portfolio`, then enabled GitHub Pages
   (Settings -> Pages -> Deploy from a branch -> `main` -> `/ (root)`).
4. Checked the live site, images and links, then committed the improvements recorded in
   `REVIEW.md`.
5. Posted the portfolio details in the CISC7204 Practice 09 forum thread
   "My Data Science Portfolio Details".

## Declaration of AI Usage

- Student ID: mc649337
- Student full name: CHAN KA WAI
- Did I use an AI LLM? Yes
- Exact LLM used: DeepSeek-V4.1-Flash
- Web browser used: Google Chrome "https://chat.genai.um.edu.mo/"
- How it was used: reading tutorial pages, drafting and debugging notebook code, generating the
  documentation and performing the GitHub/GitHub Pages steps; all commands and outputs were
  reviewed before publishing.
