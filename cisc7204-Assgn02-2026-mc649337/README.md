# CISC7204 Assignment 02 - Data visualization with Python

Chan Ka Wai (mc649337) · Class D · University of Macau

Artifacts of my Assignment 02 work: the notebooks executed from top to bottom, the screenshots of
every task with its output, and the Dash project spaces.

- **Live showcase:** <https://kelvin-chan-ka-wai.github.io/CISC7204-mc649337-2026GitHub/>
- **Repository:** <https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub>

## What is in this folder

| Path | Content |
|---|---|
| `Datasets/` | datasets used by the labs (Canada immigration, police incidents, airline data, wildfires, automobile sales, `us-states.json`, `world_countries.json`) |
| `Module 01/` … `Module 05/` | each module has `Jupyter Notebooks/`, `Screen Shots/` and, where required, `Project Spaces/` |
| `Module01.zip` … `Module 05.zip` | each module packaged (notebooks + screenshots + project spaces) |
| `Pair Project Proposal/` | revised pair project proposal (Pair 04) |

## Modules

| Module | Labs | Main tools |
|---|---|---|
| [Module 01](Module%2001) | Lab01 Exploring and pre-processing a dataset with Pandas · Lab02 Introduction to Matplotlib and line plots | pandas, matplotlib |
| [Module 02](Module%2002) | Lab01 Area plots, histograms and bar charts · Lab02 Pie charts, box plots, scatter and bubble plots · Lab03 Plotting directly with Matplotlib | pandas, matplotlib |
| [Module 03](Module%2003) | Lab01 Waffle charts, word clouds and regression plots · Lab02 Maps and geospatial data | pywaffle, wordcloud, seaborn, folium |
| [Module 04](Module%2004) | Lab01 Plotly basics · Lab02 Dash basics · Lab03 Interactivity and callbacks · Lab04 Flight delay statistics dashboard | plotly, dash, Theia |
| [Module 05](Module%2005) | Practice Lab01 Wildfire activities in Australia · Practice Lab02 Creating dashboards · Final Lab01 Visualizations with Matplotlib, Seaborn and Folium · Final Lab02 Dashboard with Plotly and Dash | pandas, seaborn, matplotlib, folium, plotly, dash |

## What I did in each module

1. **Module 01** - cleaned and explored the Canadian immigration dataset with pandas, then drew the
   first line plots with Matplotlib.
2. **Module 02** - area plots, histograms and bar charts, then pie charts, box plots, scatter and
   bubble plots, then plotting straight from the Matplotlib object API.
3. **Module 03** - built waffle charts (by hand and with `pywaffle`), word clouds (including a masked
   cloud), regression plots with seaborn and interactive folium maps with markers and a choropleth.
4. **Module 04** - Plotly basics plus four Dash applications; each script is split into `# TASK n`
   sections and every task has a screenshot taken in the Theia IDE.
5. **Module 05** - the wildfire practice project (time series, distributions, pies, scatter and a
   regional folium map) and the final project (matplotlib/seaborn/folium charts for automobile sales
   and a two-report Plotly + Dash dashboard).

## How to run it

Requirements: Python 3.10+ with

```bash
python -m pip install pandas numpy matplotlib seaborn folium plotly dash pywaffle wordcloud
```

**Notebooks**

```bash
jupyter notebook
```

then open any notebook inside `Module 0X/Jupyter Notebooks/` and run it from top to bottom.

**Dash applications**

```bash
cd "Module 04/Project Spaces/CISC7204 Assgn02 Module 04 - Lab02 mc649337 Chan Ka Wai"
python -m pip install -r requirements.txt
python dash_basics.py
```

The URL is printed in the terminal; `CTRL+C` stops the application. The Module 05 practice and final
project spaces are started the same way (`Dash_wildfire.py`, `Dash_automobile.py`).

## Screenshots

Every task has its own screenshot in `Module 0X/Screen Shots/`. They are named after the task, so the
order in the folder follows the order of the work in the notebook or Dash script. The dashboards were
captured while the application was running in the browser.
