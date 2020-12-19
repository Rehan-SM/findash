import plotly.express as px
import plotly.graph_objs as go
from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas_datareader.data as pdr
from pandas.api.types import CategoricalDtype
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd



v = 10

for i in range(10):
	if v == +1:
		print("Hello")
	else:
		print("No")
		v =+ 1