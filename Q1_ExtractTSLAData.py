import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

ticker_symbol = 'TSLA'
tesla_ticker = yf.Ticker(ticker_symbol)
tesla_data = tesla_ticker.history(period='max')

tesla_data.reset_index(inplace=True)

tesla_data.head()
