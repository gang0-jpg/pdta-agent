import numpy as np
import pandas as pd

from config import N_PORTFOLIOS


class PortfolioGeneratorAgent:
    def generate(self, asset_names, n_portfolios=N_PORTFOLIOS):
        """
        ランダムにポートフォリオ配分を生成する。
        各行の合計は 1.0。
        """

        n_assets = len(asset_names)

        weights = np.random.random((n_portfolios, n_assets))
        weights = weights / weights.sum(axis=1, keepdims=True)

        portfolios = pd.DataFrame(weights, columns=asset_names)

        portfolios.to_csv("data/portfolios.csv", index=False)

        print(f"Saved data/portfolios.csv")
        print(f"Generated {n_portfolios:,} portfolios")

        return portfolios
