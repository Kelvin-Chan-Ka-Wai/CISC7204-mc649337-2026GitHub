# Practice 09 - Data science portfolio

Archive copy of the Practice 09 deliverable: a public project repository, a portfolio page and a
GitHub Pages deployment.

- **Live portfolio website:** https://kelvin-chan-ka-wai.github.io/data-science-portfolio/
- **Project repository:** https://github.com/Kelvin-Chan-Ka-Wai/data-science-project
- **Portfolio repository:** https://github.com/Kelvin-Chan-Ka-Wai/data-science-portfolio

## What is in this folder

| Path | Content |
|---|---|
| `index.md`, `_config.yml`, `assets/` | Source of the portfolio site (GitHub Pages, Jekyll theme `jekyll-theme-cayman`) |
| `project/README.md` | Project documentation: question, datasets and permissions, methods, findings, limitation, run instructions |
| `project/notebooks/` | Three executed analysis notebooks (population, car prices, Olympics dashboard) |
| `project/figures/` | The three visualisations embedded in the README and the portfolio page |
| `project/data/` | The public datasets used by the notebooks (World Bank WDI, UCI Automobile, Rio 2016 athletes) |
| `project/requirements.txt` | Pinned environment (bokeh 3.4.3, pandas 2.1.4, numpy 1.26.4, ipywidgets 8.1.9) |

## Requirements checklist

- [x] Portfolio website is accessible - https://kelvin-chan-ka-wai.github.io/data-science-portfolio/ (HTTP 200)
- [x] Project code and documentation are organised - `notebooks/`, `data/`, `figures/`, `scripts/` and a README with the required sections
- [x] Findings are supported by readable visualizations - three Bokeh figures (population convergence, mean car price by manufacturer, medals vs delegation size)
- [x] Analysis can be reproduced using the README instructions - datasets committed, versions pinned, `pip install -r requirements.txt` then run the notebooks
- [x] All links work, and no sensitive information is exposed - no passwords, API keys, personal data or restricted datasets in any of the three repositories

## Process

1. Built the analysis notebooks against the two CISC7204 tutorial pages (Suggested Exercise 09).
2. Wrote the project README (problem, data sources and permissions, methods, findings,
   limitation, run instructions) and exported three Bokeh figures.
3. Created the public `data-science-project` repository and committed the content.
4. Created the public `data-science-portfolio` repository with `index.md` and published it with
   GitHub Pages (Settings -> Pages -> Deploy from a branch -> `main` -> `/ (root)`).
5. Checked the live site, images and links, then made one improvement based on review feedback:
   an **At a glance** table that puts the research question, main finding and key limitation on
   the first screen (commit: *Add at-a-glance question / finding / limitation summary to the
   showcase*).
6. Posted the portfolio details in the CISC7204 Practice 09 forum thread
   "My Data Science Portfolio Details".

## Declaration of AI Usage

- Student ID: mc64933
- Student full name: CHAN KA WAI
- Did I use an AI LLM? Yes
- Exact LLM used: DeepSeek (V3.2 / V4 flash-class models served through the DeepSeek Harness)
- Web browser used: Google Chrome via https://www.deepseek.com/en/
- How it was used: reading the tutorial pages, drafting and debugging the notebook code,
  generating the documentation and performing the GitHub/GitHub Pages steps; all commands and
  outputs were reviewed before publishing.
