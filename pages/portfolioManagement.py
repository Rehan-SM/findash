import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_equity_char = pd.read_csv(DATA_PATH.joinpath("df_equity_char.csv"))
df_equity_diver = pd.read_csv(DATA_PATH.joinpath("df_equity_diver.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            html.Img(
                src=app.get_asset_url("ohno.gif"),
                className='twelve columns'
            ),
        ],
        className="page",
    )