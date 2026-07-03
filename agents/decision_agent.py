import pandas as pd


class DecisionAgent:

    def recommend(self,
                  current_portfolio: pd.Series,
                  target_portfolio: pd.Series):

        print()
        print("=" * 60)
        print("PDTA Recommendation")
        print("=" * 60)

        recommendations = []

        assets = [
            c for c in target_portfolio.index
            if c not in ["return", "risk", "sharpe", "max_drawdown"]
        ]

        for asset in assets:

            current = float(current_portfolio.get(asset, 0))
            target = float(target_portfolio.get(asset, 0))

            diff = target - current

            if abs(diff) < 0.01:
                action = "HOLD"

            elif diff > 0:
                action = "BUY"

            else:
                action = "SELL"

            recommendations.append({
                "Asset": asset,
                "Current": current,
                "Target": target,
                "Difference": diff,
                "Action": action
            })

        recommendation_df = pd.DataFrame(recommendations)

        print(recommendation_df)

        recommendation_df.to_csv(
            "data/recommendation.csv",
            index=False
        )

        print()
        print("Saved data/recommendation.csv")

        return recommendation_df
