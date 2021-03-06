import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from app import app

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


layout = html.Div([
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center'
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

