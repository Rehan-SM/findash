# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output, State
from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    market_overview
)

from utils import Stock, make_dash_table, get_stocks


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/price-performance":
        return pricePerformance.create_layout(app)
    elif pathname == "/trends":
        return portfolioManagement.create_layout(app)
    elif pathname == "/social-media":
        return portfolioManagement.create_layout(app)
    elif pathname == "/market":
        return market_overview.create_layout(app)
    elif pathname == "/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            market_overview.create_layout(app),
            portfolioManagement.create_layout(app),
        )
    else:
        return overview.create_layout(app)

# Overview Page - Get Summary
@app.callback(
    [Output('summary', 'children'),
     Output('graph-1', 'figure'),
     Output('summary-table', 'children'),
     Output('graph-2', 'figure'),
     Output('value_now', 'children')],
    [Input('submit-val', 'n_clicks'),
     State('ticker', 'value'),
     State('time-horizon', 'start_date'),
     State('time-horizon', 'end_date')])
def update_summary(clicked, ticker, start, end):
    if clicked:
        stock = Stock(ticker, start, end)
        z = stock.get_company_overview()
        key_metrics = make_dash_table(z)
        business_summary = stock.description
        plot_of_performance = stock.plot_prices()
        investment = stock.plot_initial_investment()
        return business_summary, plot_of_performance, key_metrics, investment, f' would now be worth $ {stock.investment_fv}'

# Price Performance - Summary Page
@app.callback(
    Output('price_metrics', 'children'),
    [Input('submit-val', 'n_clicks'),
     State('ticker', 'value'),
     State('time-horizon', 'start_date'),
     State('time-horizon', 'end_date')]
)
def update_summary(a, ticker, start, end):
    if a > 0:
        stock = Stock(ticker, start, end)
        z = stock.price_performance_summary()
        price_summary = make_dash_table(z)
        return price_summary
    else:
        return ""

@app.callback(Output('performance-graph', 'figure'),
              [Input('update-chart', 'n_clicks'),
               State('drop-down', 'value'),
               State('another-ticker', 'value'),
               State('ticker', 'value'),
               State('time-horizon', 'start_date'),
               State('time-horizon', 'end_date')])
def update_chart(n_clicks, drop_down, a_ticker, ticker, start, end):
    if n_clicks > 0:
        stock = Stock(ticker, start, end)
        data = go.Scatter(x=stock.fin_data.index, y=stock.fin_data['Adj Close'] if drop_down == 'price' else stock.fin_data['d_returns'], name=ticker)
        fig = go.Figure(data)

        if a_ticker is not None:
            another = Stock(a_ticker, start, end)
            fig.add_trace(go.Scatter(x=another.fin_data.index, y=another.fin_data['Adj Close'] if drop_down == 'price' else another.fin_data['d_returns'], name=a_ticker))

        return fig
    else:
        return go.Figure()


@app.callback(Output('distribution', 'figure'),
              [Input('update-chart', 'n_clicks'),
               State('another-ticker', 'value'),
               State('ticker', 'value'),
               State('time-horizon', 'start_date'),
               State('time-horizon', 'end_date')])
def update_chart(n_clicks, a_ticker, ticker, start, end):
    if n_clicks > 0:
        stock = Stock(ticker, start, end)
        chart = stock.plot_return_distribution()

        if a_ticker is not None:
            another = Stock(a_ticker, start, end)
            chart.add_trace(go.Histogram(x=another.fin_data.d_returns, name=a_ticker))
            chart.update_layout(barmode='overlay')
            chart.update_traces(opacity=0.75)

        return chart
    else:
        return go.Figure()


@app.callback(Output('market', 'children'),
              [Input('update-market', 'n_clicks'),
               State('market_cap', 'value'),
               State('sector', 'value'),
               State('sort_by', 'value')])
def market(n_clicks, market_cap, sector, sort_by):
    if n_clicks is not None:
        x = get_stocks(market_cap, sector, sort_by)
        y = make_dash_table(x)
        return y
    else:
        return "Please click the button!"



if __name__ == "__main__":
    app.run_server(debug=True, host='192.168.0.165')
