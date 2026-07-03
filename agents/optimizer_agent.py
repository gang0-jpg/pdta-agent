import numpy as np
import pandas as pd

from config import RISK_FREE_RATE


class OptimizerAgent:
    def evaluate(self, returns: pd.DataFrame, portfolios: pd.DataFrame):
        """
        各ポートフォリオの年率リターン、年率リスク、シャープレシオを計算する。
        """

        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252

        weights = portfolios.values

        portfolio_returns = weights @ mean_returns.values

        portfolio_risks = np.sqrt(
            np.einsum("ij,jk,ik->i", weights, cov_matrix.values, weights)
        )

        sharpe_ratios = (portfolio_returns - RISK_FREE_RATE) / portfolio_risks

        results = portfolios.copy()
        results["return"] = portfolio_returns
        results["risk"] = portfolio_risks
        results["sharpe"] = sharpe_ratios

        results.to_csv("data/portfolio_results.csv", index=False)

        print("Saved data/portfolio_results.csv")

        best_sharpe = results.loc[results["sharpe"].idxmax()]
        min_risk = results.loc[results["risk"].idxmin()]
        max_return = results.loc[results["return"].idxmax()]

        print()
        print("Best Sharpe Portfolio:")
        print(best_sharpe)

        print()
        print("Minimum Risk Portfolio:")
        print(min_risk)

        print()
        print("Maximum Return Portfolio:")
        print(max_return)

        return results
