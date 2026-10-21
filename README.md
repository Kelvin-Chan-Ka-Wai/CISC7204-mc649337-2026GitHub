# CISC7204 · Data Science and Data Visualization — coursework showcase

**Chan Ka Wai (mc649337)** · Class D · University of Macau

A public portfolio of the visualisation work done for **CISC7204**. Everything here is the actual
submission material: notebooks executed end to end, screenshots of every task and its output, and
runnable Dash application project spaces.

> **Live showcase:** <https://kelvin-chan-ka-wai.github.io/CISC7204-mc649337-2026GitHub/>
>
> **Assignment 02 folder:** [`cisc7204-Assgn02-2026-mc649337/`](cisc7204-Assgn02-2026-mc649337/)

---

## Assignment 02 — Data visualization with Python (5 modules · 15 labs)

| Module | Focus | Highlights |
|---|---|---|
| **[Module 01](cisc7204-Assgn02-2026-mc649337/Module%2001)** | Introduction to data visualization | Pandas preprocessing + first Matplotlib line plots on the Canadian immigration data |
| **[Module 02](cisc7204-Assgn02-2026-mc649337/Module%2002)** | Basic and specialized tools | Area plots, histograms, bar charts, pies, box plots, scatter and bubble plots |
| **[Module 03](cisc7204-Assgn02-2026-mc649337/Module%2003)** | Advanced & geospatial | Waffle charts, word clouds, regression plots and interactive folium maps |
| **[Module 04](cisc7204-Assgn02-2026-mc649337/Module%2004)** | Plotly & Dash | Plotly basics plus four Dash dashboards developed task by task in the Theia IDE |
| **[Module 05](cisc7204-Assgn02-2026-mc649337/Module%2005)** | Practice & final project | Australian wildfire analysis and a two-report automobile-sales dashboard |

The complete artifact folder is `cisc7204-Assgn02-2026-mc649337/` and follows the required layout:

```
cisc7204-Assgn02-2026-mc649337/
  Datasets/                      datasets used by the labs
  Module 01 … Module 05/         Jupyter Notebooks/ · Screen Shots/ · Project Spaces/
  Module01.zip … Module 05.zip   the packaged modules
  Pair Project Proposal/         revised pair project proposal (Pair 04)
```

**What was done in each module**

1. **Module 01** — explored and pre-processed the Canadian immigration dataset with pandas, then drew
   line plots with Matplotlib (`Exercise 8`-style task-by-task screenshots).
2. **Module 02** — area plots, histograms and bar charts, followed by pie charts, box plots, scatter
   and bubble plots, and finally plotting directly with the Matplotlib object API.
3. **Module 03** — built waffle charts by hand and with `pywaffle`, generated word clouds (including a
   masked cloud), regression plots with seaborn, and interactive folium maps (markers, supermap and a
   choropleth with a GeoJSON layer).
4. **Module 04** — Plotly basics (scatter, line, bar, histogram, bubble, pie, sunburst) and four Dash
   applications: a basic layout, callbacks driven by a year input, and a five-chart flight-delay
   dashboard; each script is split into `# TASK n` sections with screenshots of every task in Theia.
5. **Module 05** — the wildfire practice project (time series, distributions, pies, scatter and a
   regional folium map) and the final project: matplotlib/seaborn/folium visualisations of automobile
   sales plus a two-report Plotly + Dash dashboard (yearly and recession statistics).

### Run the notebooks

```bash
python -m pip install pandas numpy matplotlib seaborn folium plotly dash pywaffle wordcloud
jupyter notebook        # open any notebook in Module 0X/Jupyter Notebooks
```

### Run a Dash application

```bash
cd "cisc7204-Assgn02-2026-mc649337/Module 04/Project Spaces/CISC7204 Assgn02 Module 04 - Lab02 mc649337 Chan Ka Wai"
python -m pip install -r requirements.txt
python dash_basics.py      # then open the URL printed in the terminal (CTRL+C stops it)
```

---

## Other coursework in this repository

| Work | Description |
|---|---|
| [**Assignment 01**](cisc7204-Assgn01-2026-mc649337/) | First assignment: visualising the Canadian immigration dataset |
| [**Practice 09 — data science portfolio**](practice-09-ds-portfolio/) | A small public portfolio project with three notebooks, Bokeh figures and a README |

---

*Built from the actual submissions posted in the CISC7204 personal forums for Modules 01–05.*
