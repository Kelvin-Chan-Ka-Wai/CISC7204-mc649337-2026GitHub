# CISC7204 Assignment 01 - Data analysis with Python

Chan Ka Wai (mc649337) · Class D · University of Macau

Artifacts of my Assignment 01 work: six modules of data-analysis labs (data importing, wrangling,
exploratory analysis, model development and model evaluation) and the pair preliminary project.

- **Repository:** <https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub>
- **Live showcase of Assignment 02:** <https://kelvin-chan-ka-wai.github.io/CISC7204-mc649337-2026GitHub/>

## What is in this folder

| Path | Content |
|---|---|
| `Module 01.zip` … `Module 06.zip` | each module packaged with its notebooks, screenshots and datasets (self-contained) |
| `Pair Preliminary Project/` | the Cambridgeshire road-collision pair project: proposal, analysis notebook, verification notebook, data and figures |
| `README.md` | this file |

## Modules

| Module | Topic | Labs |
|---|---|---|
| Module 01 | Importing datasets | Lab01 Importing a dataset · Lab02 Practice lab: laptop pricing |
| Module 02 | Data wrangling | Lab01 Missing values and data formats · Lab02 Practice lab: data wrangling |
| Module 03 | Exploratory data analysis | Lab01 Correlation and grouping · Lab02 Practice lab: laptop pricing EDA |
| Module 04 | Model development | Lab01 Simple and multiple linear regression, polynomial regression and pipelines · Lab02 Practice lab |
| Module 05 | Model evaluation and refinement | Lab01 Train/test split, cross-validation and ridge regression · Lab02 Practice lab |
| Module 06 | Practice and final project | Practice Project: insurance cost analysis · Final Project: house sales analysis and price prediction |

Each module ZIP contains:

```
Module 0X/
  CISC7204 Assgn01 Module 0X - Lab01 mc649337 Chan Ka Wai.ipynb
  CISC7204 Assgn01 Module 0X - Lab02 mc649337 Chan Ka Wai.ipynb   (where the module has a practice lab)
  lab1_1.png … lab1_N.png            screenshots of every task
  jupyter notebook folder ....png    the folder view of the notebooks
  *.csv                              the datasets used
```

Module 06 also contains `Final Project.zip` and `Practice Project.zip` with the two project notebooks
and their screenshots.

## What I did in each module

1. **Module 01** - imported the car-price and laptop datasets with pandas, inspected types and basic
   statistics and noted the first insights about the data.
2. **Module 02** - identified and handled missing values (mean/median replacement, dropping columns),
   corrected data formats and saved the cleaned data frame.
3. **Module 03** - exploratory data analysis: correlation tables and heatmaps, grouping by categorical
   variables (drive wheels, body style) and box plots to see how price changes between groups.
4. **Module 04** - built regression models with `scikit-learn`: simple and multiple linear regression,
   polynomial features, and pipelines with standardisation.
5. **Module 05** - evaluated and refined the models: train/test split, cross-validation with
   `cross_val_score`, ridge regression, and used `GridSearchCV` to tune the parameters.
6. **Module 06** - two complete projects: the insurance cost analysis (practice project) and the house
   sales final project, following the full workflow: import the data, wrangle it, explore it, build a
   model and evaluate/refine it.

## Datasets

| Dataset | Used in |
|---|---|
| `auto.csv`, `usedcars.csv`, `module_5_auto.csv` | modules 01–05 (car price analysis) |
| `laptops.csv`, `laptop_pricing_dataset_base.csv`, `laptop_pricing_dataset_mod2.csv` | practice labs of modules 01–05 (laptop pricing) |
| `clean_df.csv` | module 02 (cleaned data frame) |
| `housing.csv`, `kc_house_data_NaN.csv` | module 06 final project (house sales) |
| `medical_insurance_dataset.csv` | module 06 practice project (insurance cost analysis) |

All datasets are included inside the module ZIPs, so each module can be run on its own.

## How to run it

Requirements: Python 3.10+ with

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn
```

Unzip the module you want, open its folder in a terminal and start Jupyter:

```bash
jupyter notebook
```

Then open the Lab01/Lab02 notebook and run it from top to bottom.

## Pair Preliminary Project

The pair project (Chan Ka Wai, mc649337 + Liu Haixiang, mc649298) studies **Cambridgeshire road
collision patterns (2012–2017)**: how recorded collisions vary by district and month and how severity
differs across road-surface and weather conditions.

| File | What it is |
|---|---|
| `CISC7204-Assgn01-mc649337-PreliminaryProjectProposal.docx` | the project proposal (topic, research questions, data sources, plan) |
| `collision_patterns_analysis.ipynb` | the analysis notebook: data acquisition, cleaning/harmonisation, primary and supplementary analysis and the figures |
| `CISC7204_Verification_Notebook.ipynb` | verification notebook: source log, data audit, cleaning checks and re-computation of the analysis |
| `collision_patterns_analysis.py` | the same analysis as a plain Python script |
| `data.zip` | the raw datasets used by the notebooks |
| `figures.zip` | the exported figures |
| `README.md` | short note about the pair project files |

Run the pair notebooks the same way: unzip `data.zip`, `python -m pip install pandas numpy matplotlib
seaborn`, then `jupyter notebook` and run the analysis notebook from the top.
