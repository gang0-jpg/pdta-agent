import pandas as pd
from backends import xp
from config import RISK_FREE_RATE


class OptimizerAgent:
    def evaluate(self, returns: pd.DataFrame, portfolios: pd.DataFrame):
        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252

        weights = xp.array(portfolios.values)
        mean_values = xp.array(mean_returns.values)
        cov_values = xp.array(cov_matrix.values)

        portfolio_returns = weights @ mean_values

        portfolio_risks = xp.sqrt(
            xp.einsum("ij,jk,ik->i", weights, cov_values, weights)
        )

        sharpe_ratios = (portfolio_returns - RISK_FREE_RATE) / portfolio_risks

        results = portfolios.copy()
        results["return"] = portfolio_returns
        results["risk"] = portfolio_risks
        results["sharpe"] = sharpe_ratios

        results.to_csv("data/portfolio_results.csv", index=False)

        print("Saved data/portfolio_results.csv")

        print()
        print("Best Sharpe Portfolio:")
        print(results.loc[results["sharpe"].idxmax()])

        print()
        print("Minimum Risk Portfolio:")
        print(results.loc[results["risk"].idxmin()])

        print()
        print("Maximum Return Portfolio:")
        print(results.loc[results["return"].idxmax()])

        return results
