import numpy as np
import pandas as pd

from config import CURRENT_PORTFOLIO, RISK_FREE_RATE


class CurrentPortfolioAgent:
    def evaluate(self, returns: pd.DataFrame):
        current = pd.Series(CURRENT_PORTFOLIO)

        # returnsに存在する資産だけに合わせる
        current = current.reindex(returns.columns).fillna(0.0)

        # 合計が1になるよう正規化
        current = current / current.sum()

        mean_returns = returns.mean() * 252
        cov_matrix = returns.cov() * 252

        portfolio_return = float(current.values @ mean_returns.values)
        portfolio_risk = float(
            np.sqrt(current.values @ cov_matrix.values @ current.values)
        )
        sharpe = (portfolio_return - RISK_FREE_RATE) / portfolio_risk

        result = current.copy()
        result["return"] = portfolio_return
        result["risk"] = portfolio_risk
        result["sharpe"] = sharpe

        print()
        print("Current Portfolio:")
        print(result)

        return result
