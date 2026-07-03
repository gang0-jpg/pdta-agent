import yfinance as yf
import pandas as pd

from config import ASSETS, START_DATE, END_DATE


class MarketAgent:

    def download(self):

        prices = pd.DataFrame()

        for name, ticker in ASSETS.items():

            print(f"Downloading {name} ({ticker})")

            data = yf.download(
                ticker,
                start=START_DATE,
                end=END_DATE,
                progress=False
            )

            prices[name] = data["Close"]

        return prices
