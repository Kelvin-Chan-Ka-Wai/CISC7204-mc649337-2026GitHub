"""
CISC7204 Assignment 02 - Module 05 Practice Project - Part 02
Creating Dashboards:  Australia Wildfire Dashboard

Student : mc649337 Chan Ka Wai
Course  : CISC7204 - Data Science and Data Visualization
Due     : 2026-OCT-25 23:00

Dataset : Historical_Wildfires.csv  (module Datasets folder)

Run it
------
An IDE is required for this lab (Theia / Spyder / PyCharm). Spyder ships with Anaconda:

    D:\\anaconda3\\Scripts\\spyder.exe          -> open this file, press F5

or straight from a terminal:

    D:\\anaconda3\\python.exe Dash_wildfire.py

Dash prints a local URL (normally http://127.0.0.1:8050/); open it in a browser.

Tasks covered
-------------
TASK 2.1  Application title (html.H1, centered, #503D36, font-size 26)
TASK 2.2  dcc.RadioItems for the Region  +  dcc.Dropdown for the Year
TASK 2.3  Two empty output divisions inside the next inner division
TASK 2.4  @app.callback wiring the two outputs to the two inputs
TASK 2.5  Callback function `reg_year_display` producing the pie + bar figures
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# --------------------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------------------
# Resolve the dataset relative to this file so the app works no matter which directory
# it is launched from.  This file lives in  <unit>/Module05/Project Spaces/  and the data
# in  <unit>/Datasets/Historical_Wildfires.csv.
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

DATASET = find_dataset("Historical_Wildfires.csv")

df = pd.read_csv(DATASET)

# The raw dataset only carries a `Date` column; derive Year and Month from it exactly as
# the Part 1 notebook does, so the dashboard and the notebook agree on the same numbers.
df["Year"] = pd.to_datetime(df["Date"]).dt.year
df["Month"] = pd.to_datetime(df["Date"]).dt.month

# Regions present in the dataset (NSW, NT, QL, SA, TA, VI, WA)
regions = sorted(df["Region"].unique())
years = sorted(df["Year"].unique())

# --------------------------------------------------------------------------------------
# Application
# --------------------------------------------------------------------------------------
app = Dash(__name__)

app.layout = html.Div(
    [
        # TASK 2.1: application title
        html.H1(
            "Australia Wildfire Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 26},
        ),

        # Outer division
        html.Div(
            [
                # First inner division -- the input controls  (TASK 2.2)
                html.Div(
                    [
                        html.H2("Select Region:", style={"margin-right": "2em"}),

                        # Radio items to choose the region
                        dcc.RadioItems(
                            options=[
                                {"label": "New South Wales", "value": "NSW"},
                                {"label": "Northern Territory", "value": "NT"},
                                {"label": "Queensland", "value": "QL"},
                                {"label": "South Australia", "value": "SA"},
                                {"label": "Tasmania", "value": "TA"},
                                {"label": "Victoria", "value": "VI"},
                                {"label": "Western Australia", "value": "WA"},
                            ],
                            value="NSW",
                            id="region",
                            inline=True,
                        ),

                        html.H2("Select Year:", style={"margin-right": "2em"}),

                        # Dropdown to choose the year (2005 - 2020, default 2005)
                        dcc.Dropdown(
                            options=[{"label": str(y), "value": y} for y in range(2005, 2021)],
                            value=2005,
                            id="year",
                            style={"width": "80%"},
                        ),
                    ]
                ),

                # Second inner division -- the outputs  (TASK 2.3)
                html.Div(
                    [
                        html.Div([], id="plot1"),
                        html.Div([], id="plot2"),
                    ],
                    style={"display": "flex", "flex-direction": "row"},
                ),
            ],
            style={"display": "flex", "flex-direction": "column"},
        ),
    ]
)


# --------------------------------------------------------------------------------------
# TASK 2.4: callbacks -- two outputs, two inputs
# --------------------------------------------------------------------------------------
@app.callback(
    [Output(component_id="plot1", component_property="children"),
     Output(component_id="plot2", component_property="children")],
    [Input(component_id="region", component_property="value"),
     Input(component_id="year", component_property="value")],
)
# TASK 2.5: callback function
def reg_year_display(input_region, input_year):
    """Build the two figures for the selected region and year."""
    # Data for the selected region
    region_data = df[df["Region"] == input_region]
    y_r_data = region_data[region_data["Year"] == input_year]

    # Plot one -- Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby("Month")["Estimated_fire_area"].mean().reset_index()
    fig1 = px.pie(
        est_data,
        values="Estimated_fire_area",
        names="Month",
        title="{} : Monthly Average Estimated Fire Area in year {}".format(
            input_region, input_year),
    )

    # Plot two -- Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = y_r_data.groupby("Month")["Count"].mean().reset_index()
    fig2 = px.bar(
        veg_data,
        x="Month",
        y="Count",
        title="{} : Average Count of Pixels for Presumed Vegetation Fires in year {}".format(
            input_region, input_year),
    )

    return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)]


if __name__ == "__main__":
    app.run(debug=True)
