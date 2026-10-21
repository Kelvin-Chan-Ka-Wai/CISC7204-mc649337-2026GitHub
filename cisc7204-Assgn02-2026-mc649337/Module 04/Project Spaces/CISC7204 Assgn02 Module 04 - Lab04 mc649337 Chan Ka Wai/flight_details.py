"""CISC7204 Assignment 02 - Module 04 Lab04 - PRACTICE TASK: Flight Details Statistics Dashboard.

Dashboard: five line charts of the monthly average delays (carrier, weather, NAS, security and
late aircraft) per reporting airline for the selected year (2010-2020).
The title was changed from "Flight Delay Time Statistics" (font-size 30) to
"Flight Details Statistics Dashboard" (font-size 35) and the file was renamed to flight_details.py.
Run:  python flight_details.py
"""

# ---------------------------------------------------------------- TASK 1 - Import libraries and read the data
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
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

# ---------------------------------------------------------------- TASK 2 - Create the application
app = dash.Dash(__name__)

# ---------------------------------------------------------------- TASK 3 - Build the layout
# Title, the input year and the five graphs split into three segments (2 + 2 + 1)
app.layout = html.Div(children=[
    # PRACTICE TASK: new title, font-size 35 (was "Flight Delay Time Statistics" / 30)
    html.H1("Flight Details Statistics Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 35}),
    html.Div(["Input Year: ", dcc.Input(
        id="input-year", value="2010", type="number",
        style={"height": "35px", "font-size": 30})],
        style={"font-size": 30}),
    html.Br(),
    html.Br(),
    # Segment 1: carrier delay and weather delay side by side
    html.Div([
        html.Div(dcc.Graph(id="carrier-plot")),
        html.Div(dcc.Graph(id="weather-plot")),
    ], style={"display": "flex"}),
    # Segment 2: NAS delay and security delay side by side
    html.Div([
        html.Div(dcc.Graph(id="nas-plot")),
        html.Div(dcc.Graph(id="security-plot")),
    ], style={"display": "flex"}),
    # Segment 3: late aircraft delay
    html.Div(dcc.Graph(id="late-plot"), style={"width": "65%"}),
])

# ---------------------------------------------------------------- TASK 4 - Supporting function
def compute_info(airline_data, entered_year):
    """Compute the average delay dataframes for the selected year."""
    df = airline_data[airline_data["Year"] == int(entered_year)]
    avg_car = df.groupby(["Month", "Reporting_Airline"])["CarrierDelay"].mean().reset_index()
    avg_weather = df.groupby(["Month", "Reporting_Airline"])["WeatherDelay"].mean().reset_index()
    avg_NAS = df.groupby(["Month", "Reporting_Airline"])["NASDelay"].mean().reset_index()
    avg_sec = df.groupby(["Month", "Reporting_Airline"])["SecurityDelay"].mean().reset_index()
    avg_late = df.groupby(["Month", "Reporting_Airline"])["LateAircraftDelay"].mean().reset_index()
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

# ---------------------------------------------------------------- TASK 5 - Callback decorator
@app.callback(
    [Output(component_id="carrier-plot", component_property="figure"),
     Output(component_id="weather-plot", component_property="figure"),
     Output(component_id="nas-plot", component_property="figure"),
     Output(component_id="security-plot", component_property="figure"),
     Output(component_id="late-plot", component_property="figure")],
    Input(component_id="input-year", component_property="value"),
)

# ---------------------------------------------------------------- TASK 6 - Callback function
def get_graph(entered_year):
    # Compute the required information from the data
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, entered_year)
    # Five line plots of the different delay types
    carrier_fig = px.line(avg_car, x="Month", y="CarrierDelay", color="Reporting_Airline",
                          title="Average carrier delay time (minutes) by airline")
    weather_fig = px.line(avg_weather, x="Month", y="WeatherDelay", color="Reporting_Airline",
                          title="Average weather delay time (minutes) by airline")
    nas_fig = px.line(avg_NAS, x="Month", y="NASDelay", color="Reporting_Airline",
                      title="Average NAS delay time (minutes) by airline")
    sec_fig = px.line(avg_sec, x="Month", y="SecurityDelay", color="Reporting_Airline",
                      title="Average security delay time (minutes) by airline")
    late_fig = px.line(avg_late, x="Month", y="LateAircraftDelay", color="Reporting_Airline",
                       title="Average late aircraft delay time (minutes) by airline")
    return [carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]

# ---------------------------------------------------------------- TASK 7 - Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8054)
