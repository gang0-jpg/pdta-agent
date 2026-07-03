import pandas as pd


class ReturnAgent:

    def calculate_returns(self, prices: pd.DataFrame):

        prices = prices.ffill()

        returns = prices.pct_change().dropna()

        # 異常値を除外
        returns = returns.clip(lower=-0.2, upper=0.2)

        # 円キャッシュ：リターン0として追加
        returns["JPY"] = 0.0

        returns.to_csv("data/returns.csv")

        print("Saved data/returns.csv")

        return returns
