---
title: CHAN KA WAI - Data Science Portfolio
---

# CHAN KA WAI (mc64933)

**Data science student, University of Macau - CISC7204 Data Science and Data Visualization.**

I turn messy tabular data into figures that answer a specific question. My work is built on
Python (pandas, NumPy), the Bokeh visualisation stack (plotting and models interfaces,
`gridplot`, `HoverTool`, colour mappers), ipywidgets for interactive filters, and Jupyter for
reproducible notebooks. I care about the unglamorous parts too: readable axis labels, honest
limitations, and a README that lets someone else run the analysis.

- GitHub: [github.com/Kelvin-Chan-Ka-Wai](https://github.com/Kelvin-Chan-Ka-Wai)
- Email: mc64933@um.edu.mo
- Course repository: [CISC7204-mc649337-2026GitHub](https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub)

## At a glance

| | |
|---|---|
| **Project** | Visual analytics of population density, car prices and Olympic performance |
| **Question** | Can three public datasets - World Bank population density, the 1985 UCI automobile market and Rio 2016 Olympic athletes - be turned into readable interactive Bokeh visualisations, and what do they show? |
| **Main finding** | Population densities converged (Germany-Switzerland gap 72.7 -> 23.9 people/km2), mean car prices span 5.8x (6,007 -> 34,600 USD), and Olympic medals track delegation size (Pearson r = 0.87). |
| **Key limitation** | Descriptive associations only: athletes are counted rather than medal events, population data are country-level aggregates, and car prices are unadjusted 1985 USD from a small sample. |
| **Status** | Completed (October 2026) |

## Technical skills

| Area | Tools |
|---|---|
| Data wrangling | pandas (grouping, aggregation, joins, time series), NumPy |
| Visualisation | Bokeh 3.x (plotting + models interfaces, `gridplot`, `LinearColorMapper`, `HoverTool`, `Tabs`), matplotlib |
| Interactivity | ipywidgets (`interact`, `IntSlider`), Bokeh widgets and toolbars |
| Modelling | scikit-learn basics (regression, classification, cross-validation) |
| Reproducibility | Jupyter, requirements files, Git/GitHub, GitHub Pages |
| Data handling | CSV/Excel, data cleaning, missing-value and outlier treatment |

## Project showcase

### Visual analytics of population density, car prices and Olympic performance

**Research question.** Can three very different public datasets - World Bank population
density, the 1985 UCI automobile market and the Rio 2016 Olympic athletes - be turned into
readable, interactive Bokeh visualisations, and what do they actually tell us about convergence,
price skew and medal efficiency?

[![Population density of Germany and Switzerland](assets/population_density_germany_switzerland.png)](https://github.com/Kelvin-Chan-Ka-Wai/data-science-project)

*Population density, Germany vs Switzerland, 1961-2015 (Bokeh line chart).*

**What the visualisation shows.**

- **Convergence.** Germany's population density rose from 210.2 to 233.6 people/km² (+11.1%)
  and Switzerland's from 137.5 to 209.7 (+52.5%) between 1961 and 2015; the gap narrowed from
  **72.7 to 23.9 people/km²**, a 67% reduction.
- **Price skew.** Mean car prices per manufacturer span 6,007 USD (Chevrolet) to 34,600 USD
  (Jaguar) - a factor of 5.8x - while the median car costs 10,295 USD, so the mean is dragged up
  by a few luxury brands.
- **Medals follow delegation size.** Medal totals correlate strongly with delegation size at Rio
  2016 (Pearson r = 0.87); Jamaica and Serbia converted athletes into medals most efficiently
  among countries with at least 20 athletes.

**Key limitation.** All three results are descriptive associations from aggregated public data,
not causal claims: the Olympic dataset counts athletes rather than medal events (so team sports
inflate a country's medal count), the population figures are country-level aggregates, and the
car prices are unadjusted 1985 USD from a small sample.

**Links.** [Project repository](https://github.com/Kelvin-Chan-Ka-Wai/data-science-project) -
code, datasets, README and three notebooks.

**Status: completed** (course project, October 2026). Next steps: add a reproducible report and
a second visual for the Olympic efficiency ranking.

## What I am working on next

- A reproducibility check that re-runs every notebook from a clean environment in CI.
- More interactive charts: linked brushing between the population and Olympic dashboards.
- Written case studies that put each figure in context for a non-technical reader.

---

*Built with Jupyter, Bokeh and GitHub Pages. Datasets: World Bank WDI (CC BY 4.0), UCI Machine
Learning Repository (CC BY 4.0), Rio 2016 Olympic athletes dataset (public).*
