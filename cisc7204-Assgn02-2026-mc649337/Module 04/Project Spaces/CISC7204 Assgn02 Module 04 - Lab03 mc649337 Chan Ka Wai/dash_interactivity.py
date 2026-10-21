"""CISC7204 Assignment 02 - Module 04 Lab03: Add interactivity (user input and callbacks).

Dashboard: pick a year (2010-2020) and see the average monthly arrival delay of that year.
Run:  python dash_interactivity.py
"""

# ---------------------------------------------------------------- TASK 1 - Import libraries and read the data
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Read the airline data into the pandas dataframe
airline_data = pd.read_csv(
    "data/airline_data.csv",
    encoding="ISO-8859-1",
    dtype={"Div1Airport": str, "Div1TailNum": str,
           "Div2Airport": str, "Div2TailNum": str},
)

# ---------------------------------------------------------------- TASK 2 - Create the application layout
# Create a dash application
app = dash.Dash(__name__)

# Title (H1), input year (dcc.Input) and the output graph (dcc.Graph)
app.layout = html.Div(children=[
    html.H1("Airline Performance Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40}),
    html.Div(["Input Year: ", dcc.Input(
        id="input-year", value="2010", type="number",
        style={"height": "50px", "font-size": 35})],
        style={"font-size": 40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id="line-plot")),
])

# ---------------------------------------------------------------- TASK 3 - Add the callback function
# Callback decorator: input is the year, output is the line chart
@app.callback(
    Output(component_id="line-plot", component_property="figure"),
    Input(component_id="input-year", component_property="value"),
)
def get_graph(entered_year):
    # Select the data for the entered year
    df = airline_data[airline_data["Year"] == int(entered_year)]
    # Group the data by month and compute the average arrival delay
    line_data = df.groupby("Month")["ArrDelay"].mean().reset_index()
    # Line chart of the monthly average arrival delay
    fig = go.Figure(data=go.Scatter(x=line_data["Month"], y=line_data["ArrDelay"],
                                    mode="lines", marker=dict(color="green")))
    fig.update_layout(title="Month vs Average Flight Delay Time",
                      xaxis_title="Month", yaxis_title="ArrDelay")
    return fig

# ---------------------------------------------------------------- TASK 4 - Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8051)
