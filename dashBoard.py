import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

data = pd.read_csv('walmart_sales_dataset_of_45stores.csv')

# Remove 'Store' and 'Date' columns
dashData = data.drop(['Store', 'Date'], axis=1)

# Create a Dash app
app = dash.Dash(__name__)

# Define available variables for selection
available_variables = dashData.columns

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Walmart Sales Dashboard - Yasser Ashraf Mohammed Gaber"),
    html.Div([
        html.Label("Select X Variable:"),
        dcc.Dropdown(
            id='x-variable',
            options=[{'label': col, 'value': col} for col in available_variables],
            value='Temperature'  # Default X variable
        ),
        html.Label("Select Y Variable:"),
        dcc.Dropdown(
            id='y-variable',
            options=[{'label': col, 'value': col} for col in available_variables],
            value='Weekly_Sales'  # Default Y variable
        ),
        dcc.Graph(id='scatter-plot')
    ])
])

# Define callback to update scatter plot based on user input
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-variable', 'value'),
     Input('y-variable', 'value')]
)
def update_scatter_plot(x_variable, y_variable):
    scatter_fig = px.scatter(dashData, x=x_variable, y=y_variable, title=f'{y_variable} vs {x_variable}')
    return scatter_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
