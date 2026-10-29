---
title: CHAN KA WAI - Data Science Portfolio
---

# CHAN KA WAI

**Data science student, University of Macau — CISC7204 Data Science and Data Visualization.**

I turn messy tabular data into figures that answer one specific question. My work is built on
Python (pandas, NumPy), the Bokeh visualisation stack (both the `plotting` and the `models`
interfaces, `gridplot`, `HoverTool`, colour mappers), ipywidgets for interactive filters, and
Jupyter for reproducible notebooks. I care about the unglamorous parts too: readable axis
labels, stated units, honest limitations, and a README that lets someone else run the analysis.

[GitHub profile](https://github.com/Kelvin-Chan-Ka-Wai) ·
[Project repository](https://github.com/Kelvin-Chan-Ka-Wai/data-science-project) ·
[Course repository](https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub)

## Technical skills

| Area | Tools I have used on real data |
|---|---|
| Data wrangling | pandas (grouping, aggregation, joins, time series, missing values), NumPy |
| Visualisation | Bokeh 3.x (`plotting` + `models`, `gridplot`, `LinearColorMapper`, `HoverTool`, `Tabs`, `Span`, `LabelSet`), matplotlib |
| Interactivity | ipywidgets (`interact`, `IntSlider`), Bokeh widgets and toolbars |
| Statistics | descriptive statistics, distributions, hypothesis testing, confidence intervals, correlation |
| Modelling | scikit-learn basics (regression, classification, cross-validation) |
| Reproducibility | Jupyter, pinned `requirements.txt`, Git/GitHub, GitHub Pages, CI that re-runs the notebooks |

## Project showcase

### Visual analytics of population density, car prices and Olympic performance

**Research question.** Can three very different public datasets — World Bank population density,
the 1985 UCI automobile market, and the Rio 2016 Olympic athletes — be turned into readable
interactive Bokeh visualisations, and what do they actually tell us about convergence, price
skew, and medal efficiency?

**Status: completed** (course project, October 2026). **Repository:**
[data-science-project](https://github.com/Kelvin-Chan-Ka-Wai/data-science-project) — three
notebooks, the datasets, the figure script and a full README.

#### Visualisation 1 — population density converged

![Population density of Germany and Switzerland, 1961-2015, converging from a gap of 72.7 to 23.9 people per square kilometre](assets/population_density_germany_switzerland.png)

Germany's population density rose from **210.2 to 233.6 people/km²** (+11.1%) and Switzerland's
from **137.5 to 209.7** (+52.5%) between 1961 and 2015. The gap between them narrowed from
**72.7 to 23.9 people/km² — a 67% reduction**. Switzerland grew faster from a lower base; the two
countries are converging, not diverging.

#### Visualisation 2 — car prices are skewed, not merely spread out

![Mean car price by manufacturer in the 1985 US market, ranging from 6,007 USD for Chevrolet to 34,600 USD for Jaguar, with the 10,295 USD median marked](assets/car_mean_price_by_make.png)

Mean price per manufacturer spans **6,007 USD (Chevrolet) to 34,600 USD (Jaguar) — a factor of
5.8x** — while the **median car costs only 10,295 USD** and just 14 of the 201 cars cost more than
30,000 USD. The mean is dragged upward by a handful of luxury brands, which is exactly why the
median is the more honest summary of "a typical car" here.

#### Visualisation 3 — medals track delegation size

![Scatter of total medals against athletes sent at Rio 2016 for 207 countries, with a Pearson correlation of 0.87 and Jamaica, Serbia and the USA labelled](assets/olympics_medals_vs_athletes.png)

Medal totals correlate strongly with delegation size at Rio 2016 (**Pearson r = 0.87, n = 207
countries**): the USA sent 567 athletes and won 264 medals. Among countries with at least 20
athletes, **Jamaica** (57 athletes → 30 medals, 0.53 per athlete) and **Serbia** (103 → 53, 0.51)
converted their athletes into medals more efficiently than the USA (0.47).

#### Limitation

**These are descriptive associations from aggregated public data, not causal claims.** The
Olympic dataset counts *athletes*, not medal events, so a single team medal is multiplied across a
whole squad; the population figures are country-level World Bank aggregates that hide internal
regional variation; and the car prices are a 1985 snapshot in unadjusted USD. The "efficiency"
ranking in particular should not be read as a performance measure — it is a ratio computed on a
small sample, and it rewards countries that concentrate athletes in a few successful events.

## Reproducing this work

```bash
git clone https://github.com/Kelvin-Chan-Ka-Wai/data-science-project.git
cd data-science-project
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/          # or, headless:
jupyter nbconvert --to notebook --execute --inplace notebooks/01_population_density.ipynb
python scripts/make_figures.py  # regenerate every figure on this page
```

The datasets are committed under `data/`, so no download step is needed. Versions are pinned;
the repository also has a GitHub Actions workflow that re-runs all three notebooks on every push.

## What I am working on next

- **Depth, not just description:** add a regression with confidence intervals to the Olympic
  analysis, so the r = 0.87 claim comes with an uncertainty range instead of a bare number.
- **Linked views:** brushing the population chart to filter the Olympic dashboard.
- **Written case studies:** a short plain-language narrative per figure for a non-technical reader.

---

*Built with Jupyter, Bokeh and GitHub Pages. Datasets: World Bank WDI (CC BY 4.0), UCI Machine
Learning Repository (CC BY 4.0), [Rio 2016 Olympic athlete statistics](https://github.com/flother/rio2016) (public source; see repository data notes for redistribution scope). No passwords, API
keys, personal contact details or restricted datasets appear on this site or in either
repository. The Olympic source contains public individual athlete records (including names and
birth dates); the published analysis aggregates those records by country.*
