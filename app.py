import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load and preprocess the dataset
url = "https://opendatanepal.com/dataset/land-use-statistics-of-nepal/resource/267f2676-71f6-4b8b-ac05-59cfd90ec3c1/download/lsnd-use-statistics.csv"
df = pd.read_csv(url)

# Rename columns for consistency
df.columns = ['Land Use Type', '1967', '1978', '1991', '2000', '2010']

# Melt the DataFrame to long format
df_melted = df.melt(id_vars=['Land Use Type'], var_name='Year', value_name='Percentage')
df_melted['Year'] = df_melted['Year'].astype(int)

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Nepal Land Use Dashboard"

# Define the app layout
app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Nepal Land Use Dashboard",
        color="primary",
        dark=True,
        className="mb-4"
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Select Land Use Types"),
                dbc.CardBody([
                    dcc.Dropdown(
                        id='land-use-dropdown',
                        options=[{'label': l, 'value': l} for l in df['Land Use Type']],
                        value=df['Land Use Type'].tolist(),
                        multi=True
                    )
                ])
            ])
        ], md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Select Year"),
                dbc.CardBody([
                    dcc.Slider(
                        id='year-slider',
                        min=df_melted['Year'].min(),
                        max=df_melted['Year'].max(),
                        step=1,
                        marks={str(year): str(year) for year in df_melted['Year'].unique()},
                        value=df_melted['Year'].min()
                    )
                ])
            ])
        ], md=6)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Land Use Trends Over Years"),
                dbc.CardBody([
                    dcc.Graph(id='line-chart')
                ])
            ])
        ])
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Land Use Distribution for Selected Year"),
                dbc.CardBody([
                    dcc.Graph(id='pie-chart')
                ])
            ])
        ])
    ])
], fluid=True)

# Define callback to update line chart
@app.callback(
    Output('line-chart', 'figure'),
    Input('land-use-dropdown', 'value')
)
def update_line_chart(selected_land_uses):
    filtered_df = df_melted[df_melted['Land Use Type'].isin(selected_land_uses)]
    fig = px.line(
        filtered_df,
        x='Year',
        y='Percentage',
        color='Land Use Type',
        markers=True,
        title="Land Use Trends Over Years"
    )
    fig.update_layout(transition_duration=500)
    return fig

# Define callback to update pie chart
@app.callback(
    Output('pie-chart', 'figure'),
    Input('year-slider', 'value')
)
def update_pie_chart(selected_year):
    filtered_df = df_melted[df_melted['Year'] == selected_year]
    fig = px.pie(
        filtered_df,
        names='Land Use Type',
        values='Percentage',
        title=f"Land Use Distribution in {selected_year}"
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
