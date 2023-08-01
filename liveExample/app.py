# Import necessary libraries
import pandas as pd # Data manipulation library
import dash # Framework for building web applications
from dash import dcc # Dash Core Components, allows you to create interactive components
from dash import html # HTML components to structure the layout of the app

# Load CSV file into a pandas DataFrame
df = pd.read_csv('sample.csv') # "df" is a common alias for a DataFrame object

# Create a new Dash application
app = dash.Dash(__name__)

# Define the layout of the application, i.e., what the user will see
app.layout = html.Div([ # Div function is used to create a division on the webpage
    dcc.Graph( # Graph function is used to create a plot
        id='example-graph', # ID for the graph, useful for callbacks
        figure={ # Contains the data and layout for the plot
            'data': [ # List of plots to include in the graph
                {'x': df['Year'], 'y': df['Sales'], 'type': 'bar', 'name': 'Sales'}, # First plot
                {'x': df['Year'], 'y': df['Expenses'], 'type': 'bar', 'name': 'Expenses'}, # Second plot
            ],
            'layout': { # Layout for the plot
                'title': 'Sales and Expenses over Time' # Title of the plot
            }
        }
    )
])

# "__main__" is the name of the scope in which top-level code executes
if __name__ == '__main__':
    # Runs the application
    # debug=True allows for possible Python errors to appear on the web page
    app.run_server(debug=True)
