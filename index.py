import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import sys,requests,json,hashlib
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime

from app import app
from apps import threegraph,table,bar

page_ids = ['home', 'threegraph', 'table', 'bar']

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        html.P(
            "Navigate to dashboards", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink('Home', href='/', id=f'{page_ids[0]}-link'),
                dbc.NavLink("Multi graph example", href="/threegraph", id=f'{page_ids[1]}-link'),
                dbc.NavLink("Table example", href="/table", id=f'{page_ids[2]}-link'),
                dbc.NavLink("Bar graph example", href="/bar", id=f'{page_ids[3]}-link'),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    },
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id='page-content', style={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    })
])

index_page = html.Div([
    html.H1('Home Page', id='index-header'),
    html.Img(src=app.get_asset_url('dash_img.jpg'))
])


@app.callback(
    [dash.dependencies.Output(f"{i}-link", "active") for i in page_ids],
    [dash.dependencies.Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False, False
    return [pathname == f'/{i}' for i in page_ids]


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/threegraph':
        return threegraph.layout
    elif pathname == '/table':
        return table.layout
    elif pathname == '/bar':
        return bar.layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)
