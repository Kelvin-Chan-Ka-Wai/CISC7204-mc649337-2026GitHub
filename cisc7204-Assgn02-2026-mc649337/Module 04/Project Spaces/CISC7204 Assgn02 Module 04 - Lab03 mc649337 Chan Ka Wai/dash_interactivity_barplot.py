"""CISC7204 Assignment 02 - Module 04 Lab03 - TASK 4 practice exercise (bar chart dashboard).

Dashboard: total number of flights to each destination state for the selected year.
Run:  python dash_interactivity_barplot.py
"""

# ---------------------------------------------------------------- TASK 1 - Import libraries and read the data
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

airline_data = pd.read_csv(
    "data/airline_data.csv",
    encoding="ISO-8859-1",
    dtype={"Div1Airport": str, "Div1TailNum": str,
           "Div2Airport": str, "Div2TailNum": str},
)

# ---------------------------------------------------------------- TASK 2 - Application layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Total number of flights to the destination state split by reporting airline",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40}),
    html.Div(["Input Year: ", dcc.Input(
        id="input-year", value="2010", type="number",
        style={"height": "50px", "font-size": 35})],
        style={"font-size": 40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id="bar-plot"), style={"font-size": 35}),
])

# ---------------------------------------------------------------- TASK 3 - Callback decorator
@app.callback(
    Output(component_id="bar-plot", component_property="figure"),
    Input(component_id="input-year", component_property="value"),
)

# ---------------------------------------------------------------- TASK 4 - Callback function
def get_graph(entered_year):
    # Select the data for the entered year
    df = airline_data[airline_data["Year"] == int(entered_year)]
    # Group by destination state and reporting airline, and count the flights
    bar_data = df.groupby(["DestState", "Reporting_Airline"])["Flights"].sum().reset_index()
    # Plotly express bar chart
    fig = px.bar(bar_data, x="DestState", y="Flights", color="Reporting_Airline",
                 title="Total number of flights to the destination state split by reporting airline")
    fig.update_layout(xaxis_title="DestState", yaxis_title="Flights")
    return fig

# ---------------------------------------------------------------- TASK 5 - Run the application
if __name__ == "__main__":
    app.run(debug=True, port=8052)
