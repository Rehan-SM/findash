import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from datetime import date
from utils import Header, make_dash_table, Stock

controls = html.Div([
    dcc.Input(id='ticker', placeholder='Ticker', style={'margin-left':'10px', 'width':'75px', 'font-size':'10px'}, persistence=True),
    dcc.DatePickerRange(id='time-horizon', initial_visible_month=date(2020, 1, 1), display_format='DD MMM YY', with_portal=True, style={'font-size':'10px'}),
    html.Button('Submit', id='submit-val', style={'float':'right'})
], id='content')

def create_layout(app):
    # Page layouts
    return html.Div(
        [

            html.Div(
                [
                    html.Div([Header(app)]),
                    html.Div([controls], className='row', style={'margin-top':'40px'}),

                    # page 1
                    html.Div(
                        [

                            # Row 3
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H5("Business Summary"),
                                            html.Br([]),
                                            html.P(
                                                "A summary of the financial instrument shall be provided here once you input a ticker.",
                                                style={"color": "#ffffff"},
                                                className="row",
                                                id='summary'
                                            ),
                                        ],
                                        className="product",
                                    )
                                ],
                                className="row",
                            ),
                            # Row 4
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(
                                                ["Instrument Facts"], className="subtitle padded"
                                            ),
                                            html.Table(id='summary-table'),
                                        ],
                                        className="six columns",
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Price Chart",
                                                className="subtitle padded",
                                            ),
                                            dcc.Graph(
                                                id="graph-1",
                                                figure={'layout': go.Layout(
                                                    autosize=False,
                                                    font={'family':'Raleway', "size": 10},
                                                    height=270, width=380)},
                                                config={"displayModeBar": False},
                                                style={'margin-top': '-15px'}
                                            ),
                                        ],
                                        className="six columns",
                                    ),
                                ],
                                className="row",
                                style={"margin-bottom": "35px"},
                            ),
                            # Row 5
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(
                                                "Hypothetical growth of $10,000",
                                                className="subtitle padded",
                                            ),
                                            html.H6(id="value_now"),
                                            dcc.Graph(
                                                id="graph-2",
                                                figure={'layout': go.Layout(
                                                    autosize=False,
                                                    font={'family':'Raleway', "size": 10},
                                                    height=270, width=380)},
                                                config={"displayModeBar": False},
                                                style={'margin-top': '-5px'}
                                            ),
                                        ],
                                        className="six columns",
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Risk Reward Metrics - (WIP)", className="subtitle padded"
                                            ),
                                            html.Img(
                                                src=app.get_asset_url("risk_reward.png"),
                                                className="risk-reward",
                                            ),
                                        ],
                                        className="six columns",
                                    ),
                                ],
                                className="row ",
                            ),
                        ],
                        className="sub_page",
                    ),
                ],
                        className="page",
                    ),
                ]
            )


