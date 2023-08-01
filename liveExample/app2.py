# Import necessary modules
import pandas as pd
import dash
from dash import dcc
from dash import html

# Load the data from a CSV file
df = pd.read_csv('wages.csv')

# Create a new Dash web app
app = dash.Dash(__name__)

# Define the layout of the app
# Our app will have a single Graph component from Dash core components.
app.layout = html.Div([
    dcc.Graph(
        id='wage-comparison-graph',
        figure={
            'data': [
                {'x': df['Year'], 'y': df['Male'], 'type': 'bar', 'name': 'Male Wages'},
                {'x': df['Year'], 'y': df['Female'], 'type': 'bar', 'name': 'Female Wages'},
            ],
            'layout': {
                'title': 'Comparison of Male and Female Wages over Time'
            }
        }
    )
])

# The entry point for running our app
if __name__ == '__main__':
    app.run_server(debug=True)
