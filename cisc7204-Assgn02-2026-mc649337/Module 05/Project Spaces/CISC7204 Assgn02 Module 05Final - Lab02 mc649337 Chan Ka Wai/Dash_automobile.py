"""
CISC7204 Assignment 02 - Module 05 Final Project - Part 02
Creating Dashboards:  XYZAutomotives Recession / Yearly Report Dashboard

Student : mc649337 Chan Ka Wai
Course  : CISC7204 - Data Science and Data Visualization
Due     : 2026-OCT-25 23:00

Dataset : automobile-sales.csv  (module Datasets folder)

Run it
------
An IDE is required for this lab (Theia / Spyder / PyCharm). Spyder ships with Anaconda:

    D:\\anaconda3\\Scripts\\spyder.exe          -> open this file, press F5

or straight from a terminal:

    D:\\anaconda3\\python.exe Dash_automobile.py

Dash prints a local URL (normally http://127.0.0.1:8050/); open it in a browser.

Tasks covered
-------------
TASK 2.1  Create the Dash application with a meaningful title
TASK 2.2  Drop-down menus with titles and options (report type, year, recession period)
TASK 2.3  Output division carrying an id and a classname
TASK 2.4  Callback updating the output container from the selected statistics
TASK 2.5  Graphs for the Recession Report statistics
TASK 2.6  Graphs for the Yearly Report statistics
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# --------------------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------------------
APP_DIR = Path(__file__).resolve().parent

def find_dataset(name: str) -> Path:
    """Locate the dataset without hardcoding how deep this file sits.

    The project space may be run from the unit's `Project Spaces/` folder, from a nested
    per-project folder, or from inside the zipped archive, so walk upwards until the shared
    `Datasets/` folder is found and fall back to a copy sitting next to this script.
    """
    for base in list(APP_DIR.parents)[:4] + [APP_DIR]:
        candidate = base / "Datasets" / name
        if candidate.exists():
            return candidate
    return APP_DIR / name

DATASET = find_dataset("automobile-sales.csv")

df = pd.read_csv(DATASET)

# Report selector value -> label shown in the dropdown
REPORT_TYPES = [
    {"label": "Recession Report Statistics", "value": "recession"},
    {"label": "Yearly Report Statistics", "value": "yearly"},
]

# --------------------------------------------------------------------------------------
# Application
# --------------------------------------------------------------------------------------
app = Dash(__name__)

app.layout = html.Div(
    [
        # TASK 2.1: application title
        html.H1(
            "XYZAutomotives Sales Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 26},
        ),

        # Outer division
        html.Div(
            [
                # First inner division -- the input controls  (TASK 2.2)
                html.Div(
                    [
                        html.H2("Select Report Type:", style={"margin-right": "2em"}),
                        dcc.Dropdown(
                            options=REPORT_TYPES,
                            value="recession",
                            id="report-type",
                            style={"width": "80%"},
                        ),

                        html.H2("Select Year:", style={"margin-right": "2em"}),
                        dcc.Dropdown(
                            options=[{"label": str(y), "value": y}
                                     for y in sorted(df["Year"].unique())],
                            value=1980,
                            id="year",
                            style={"width": "80%"},
                        ),

                        html.H2("Select Recession Period:", style={"margin-right": "2em"}),
                        dcc.Dropdown(
                            options=[{"label": "Recession", "value": 1},
                                     {"label": "Non-Recession", "value": 0}],
                            value=1,
                            id="recession",
                            style={"width": "80%"},
                        ),
                    ],
                    style={"display": "flex", "flex-direction": "column"},
                ),

                # Second inner division -- the output container  (TASK 2.3)
                html.Div(
                    [],
                    id="output-container",
                    className="chart-container",
                    style={"display": "flex", "flex-direction": "column"},
                ),
            ],
            style={"display": "flex", "flex-direction": "column"},
        ),
    ]
)


# --------------------------------------------------------------------------------------
# TASK 2.4: callback -- update the output container from the selected statistics
# --------------------------------------------------------------------------------------
@app.callback(
    Output(component_id="output-container", component_property="children"),
    [Input(component_id="report-type", component_property="value"),
     Input(component_id="year", component_property="value"),
     Input(component_id="recession", component_property="value")],
)
def update_output(report_type, year, recession):
    """Return the figures for the selected report type."""
    if report_type == "recession":
        return recession_report(recession)
    return yearly_report(year)


# --------------------------------------------------------------------------------------
# TASK 2.5: Recession Report statistics
# --------------------------------------------------------------------------------------
def recession_report(recession):
    data = df[df["Recession"] == recession]
    label = "Recession" if recession == 1 else "Non-Recession"

    # 1. Average automobile sales per year
    sales_year = data.groupby("Year")["Automobile_Sales"].mean().reset_index()
    fig1 = px.line(
        sales_year, x="Year", y="Automobile_Sales", markers=True,
        title=f"Average Automobile Sales per Year during {label} Periods",
    )

    # 2. Advertising expenditure split by vehicle type
    ad_exp = data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
    fig2 = px.pie(
        ad_exp, values="Advertising_Expenditure", names="Vehicle_Type",
        title=f"Share of Each Vehicle Type in Total Advertising Expenditure ({label})",
    )

    # 3. Effect of unemployment rate on sales, by vehicle type
    fig3 = px.line(
        data, x="unemployment_rate", y="Automobile_Sales", color="Vehicle_Type",
        markers=True,
        title=f"Effect of Unemployment Rate on Vehicle Type and Sales ({label})",
    )

    # 4. GDP variation during the period
    gdp = data.groupby("Year")["GDP"].mean().reset_index()
    fig4 = px.line(
        gdp, x="Year", y="GDP", markers=True,
        title=f"GDP Variation during {label} Periods",
    )

    return [dcc.Graph(figure=f) for f in (fig1, fig2, fig3, fig4)]


# --------------------------------------------------------------------------------------
# TASK 2.6: Yearly Report statistics
# --------------------------------------------------------------------------------------
def yearly_report(year):
    data = df[df["Year"] == year]

    # 1. Average automobile sales per month for the selected year
    sales_month = data.groupby("Month")["Automobile_Sales"].mean().reset_index()
    fig1 = px.line(
        sales_month, x="Month", y="Automobile_Sales", markers=True,
        title=f"Average Automobile Sales per Month in {year}",
    )

    # 2. Advertising expenditure split by vehicle type for the year
    ad_exp = data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
    fig2 = px.pie(
        ad_exp, values="Advertising_Expenditure", names="Vehicle_Type",
        title=f"Advertisement Expenditure per Vehicle Type in {year}",
    )

    # 3. Seasonality impact -- bubble plot sized by seasonality weight
    fig3 = px.scatter(
        data, x="Month", y="Automobile_Sales",
        size="Seasonality_Weight", color="Vehicle_Type",
        title=f"Seasonality Impact on Automobile Sales in {year}",
    )

    # 4. Consumer confidence vs sales for the year
    fig4 = px.scatter(
        data, x="Consumer_Confidence", y="Automobile_Sales", color="Vehicle_Type",
        title=f"Consumer Confidence and Automobile Sales in {year}",
    )

    return [dcc.Graph(figure=f) for f in (fig1, fig2, fig3, fig4)]


if __name__ == "__main__":
    app.run(debug=True)
