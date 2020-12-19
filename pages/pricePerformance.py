import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from datetime import date
controls = html.Div([
    dcc.Input(id='ticker', placeholder='Ticker', style={'margin-left':'10px', 'width':'75px', 'font-size':'10px'}, persistence=True),
    dcc.DatePickerRange(id='time-horizon', initial_visible_month=date(2020, 1, 1), display_format='DD MMM YY', with_portal=True, style={'font-size':'10px'}),
    html.Button('Submit', id='submit-val', style={'float':'right'})
], id='content')

def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Div([controls], className='row', style={'margin-top': '40px'}),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Price Metrics"], className="subtitle padded"
                                    ),
                                    html.Table(id='price_metrics'),
                                ],
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Performance", className="subtitle padded"),
                                    html.Div([
                                        dcc.Dropdown(id='drop-down', options=[
                                            {'label': 'by Price', 'value': 'price'},
                                            {'label': 'by Daily Return', 'value': 'returns'}
                                        ], value='price', className='three columns'),
                                        dcc.Input(id='another-ticker', placeholder='vs another Ticker', className='three columns'),
                                        html.Button(['Plot'], id='update-chart')
                                    ], className='row'),

                                    dcc.Graph(
                                        id="performance-graph",
                                        figure={
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=700,
                                                height=400,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 0,
                                                    "b": 0,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Distribution of Returns"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                id="distribution",
                                                figure={
                                                    "layout": go.Layout(
                                                        autosize=True,
                                                        width=700,
                                                        height=500,
                                                        font={"family": "Raleway", "size": 10},
                                                        margin={
                                                            "r": 30,
                                                            "t": 0,
                                                            "b": 0,
                                                            "l": 30,
                                                        },
                                                        showlegend=True,
                                                        titlefont={
                                                            "family": "Raleway",
                                                            "size": 10,
                                                        },
                                                    ),
                                                },
                                                config={"displayModeBar": False},
                                            ),
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )