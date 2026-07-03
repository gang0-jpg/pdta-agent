import pandas as pd


class ReturnAgent:

    def calculate_returns(self, prices: pd.DataFrame):

        # 欠損値を前方補完
        prices = prices.ffill()

        # 日次リターン
        returns = prices.pct_change().dropna()

        returns.to_csv("data/returns.csv")

        print("Saved data/returns.csv")

        return returns
