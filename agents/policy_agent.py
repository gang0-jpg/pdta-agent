import pandas as pd

from config import INVESTMENT_POLICY


class PolicyAgent:
    def apply(self, recommendation: pd.DataFrame):
        policy = INVESTMENT_POLICY

        adjusted = recommendation.copy()

        adjusted["AdjustedDifference"] = adjusted["Difference"].clip(
            lower=-policy["max_trade_per_asset"],
            upper=policy["max_trade_per_asset"]
        )

        # Asset-specific constraints
        for idx, row in adjusted.iterrows():
            asset = row["Asset"]
            current = row["Current"]
            diff = row["AdjustedDifference"]

            # GOLD max
            if asset == "GOLD":
                max_weight = policy.get("gold_max", 1.0)
                if current >= max_weight and diff > 0:
                    adjusted.at[idx, "AdjustedDifference"] = 0.0

            # JREIT max
            if asset == "JREIT":
                max_weight = policy.get("reit_max", 1.0)
                if current >= max_weight and diff > 0:
                    adjusted.at[idx, "AdjustedDifference"] = 0.0

            # USBOND max
            if asset == "USBOND":
                max_weight = policy.get("bond_max", 1.0)
                if current >= max_weight and diff > 0:
                    adjusted.at[idx, "AdjustedDifference"] = 0.0

            # USDJPY max
            if asset == "USDJPY":
                max_weight = policy.get("usd_max", 1.0)
                if current >= max_weight and diff > 0:
                    adjusted.at[idx, "AdjustedDifference"] = 0.0

            # JPY minimum cash
            if asset == "JPY":
                cash_min = policy.get("cash_min", 0.0)
                if current + diff < cash_min:
                    adjusted.at[idx, "AdjustedDifference"] = cash_min - current

        adjusted["AdjustedAction"] = adjusted["AdjustedDifference"].apply(
            lambda x: "HOLD" if abs(x) < 0.01 else ("BUY" if x > 0 else "SELL")
        )

        adjusted.to_csv("data/policy_recommendation.csv", index=False)

        print()
        print("=" * 60)
        print("Policy Adjusted Recommendation")
        print("=" * 60)
        print(adjusted)

        print()
        print("Saved data/policy_recommendation.csv")

        return adjusted
