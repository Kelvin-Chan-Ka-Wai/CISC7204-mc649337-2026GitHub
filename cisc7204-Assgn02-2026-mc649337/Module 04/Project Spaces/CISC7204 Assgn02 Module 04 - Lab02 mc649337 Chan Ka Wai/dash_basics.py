"""CISC7204 Assignment 02 - Module 04 Lab02: Dash Basics (HTML and core components).

Dashboard: proportion of flights in each distance group, for a 500-flight sample.
Run:  python dash_basics.py
"""

# ---------------------------------------------------------------- TASK 1 - Data preparation
# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into a pandas dataframe
airline_data = pd.read_csv(
    "data/airline_data.csv",
    encoding="ISO-8859-1",
    dtype={"Div1Airport": str, "Div1TailNum": str,
           "Div2Airport": str, "Div2TailNum": str},
)

# Randomly sample 500 data points (random_state=42 keeps the result reproducible)
data = airline_data.sample(n=500, random_state=42)

# Pie chart of the distance-group proportion
fig = px.pie(data, values="Flights", names="DistanceGroup",
             title="Distance group proportion by flights")

# ---------------------------------------------------------------- TASK 2 - Create the application
# Create a dash application
app = dash.Dash(__name__)

# ---------------------------------------------------------------- TASK 3 - Build the layout
# H1 title, P description and the core graph component
# PRACTICE TASK: the title was changed from "Airline Dashboard" (font-size 40) to
#                "Airline On-time Performance Dashboard" (font-size 50), as the lab asks.
app.layout = html.Div(children=[
    html.H1("Airline On-time Performance Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 50}),
    html.P("Proportion of distance group (250 mile distance interval group) by flights.",
           style={"textAlign": "center", "color": "#F57241"}),
    dcc.Graph(figure=fig),
])

# ---------------------------------------------------------------- TASK 4 - Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8050)
