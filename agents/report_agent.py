import matplotlib.pyplot as plt
import pandas as pd


class ReportAgent:
    def plot_risk_reward_map(self, results: pd.DataFrame, current=None):
        """
        Sharpe Ratio と Max Drawdown の関係を可視化する。
        横軸: Max Drawdown
        縦軸: Sharpe Ratio
        """

        best_sharpe = results.loc[results["sharpe"].idxmax()]
        min_risk = results.loc[results["risk"].idxmin()]
        max_return = results.loc[results["return"].idxmax()]
        min_drawdown = results.loc[results["max_drawdown"].idxmax()]

        plt.figure(figsize=(10, 6))

        plt.scatter(
            results["max_drawdown"] * 100,
            results["sharpe"],
            s=6,
            alpha=0.35,
            label="Portfolios"
        )

        plt.scatter(
            best_sharpe["max_drawdown"] * 100,
            best_sharpe["sharpe"],
            marker="*",
            s=300,
            label="Best Sharpe"
        )

        plt.scatter(
            min_risk["max_drawdown"] * 100,
            min_risk["sharpe"],
            marker="s",
            s=180,
            label="Minimum Risk"
        )

        plt.scatter(
            max_return["max_drawdown"] * 100,
            max_return["sharpe"],
            marker="^",
            s=180,
            label="Maximum Return"
        )

        plt.scatter(
            min_drawdown["max_drawdown"] * 100,
            min_drawdown["sharpe"],
            marker="D",
            s=180,
            label="Minimum Drawdown"
        )

        if current is not None:
            plt.scatter(
                current["max_drawdown"] * 100,
                current["sharpe"],
                marker="o",
                s=240,
                label="Current Portfolio"
            )

            plt.annotate(
                "Current",
                xy=(current["max_drawdown"] * 100, current["sharpe"]),
                xytext=(10, 10),
                textcoords="offset points"
            )

        plt.axvline(-10, linestyle="--", linewidth=1)
        plt.axhline(1.0, linestyle="--", linewidth=1)

        plt.title("PDTA Sharpe Ratio vs Max Drawdown")
        plt.xlabel("Max Drawdown (%)")
        plt.ylabel("Sharpe Ratio")
        plt.legend()
        plt.grid(True)

        plt.savefig("output/risk_reward_map.png", dpi=220, bbox_inches="tight")
        plt.close()

        print("Saved output/risk_reward_map.png")
    def plot_scenario_summary(self, summary: pd.DataFrame):
        """
        シナリオ別 Sharpe Ratio を棒グラフで出力する。
        """

        plt.figure(figsize=(10, 6))

        plt.bar(
            summary["scenario"],
            summary["sharpe"]
        )

        plt.title("PDTA Scenario Sharpe Ratio")
        plt.xlabel("Scenario")
        plt.ylabel("Sharpe Ratio")
        plt.xticks(rotation=30, ha="right")
        plt.grid(axis="y")

        plt.savefig("output/scenario_summary.png", dpi=220, bbox_inches="tight")
        plt.close()

        print("Saved output/scenario_summary.png")

    def plot_frontier(self, results: pd.DataFrame, current=None):
        best_sharpe = results.loc[results["sharpe"].idxmax()]
        min_risk = results.loc[results["risk"].idxmin()]
        max_return = results.loc[results["return"].idxmax()]

        plt.figure(figsize=(11, 7))

        scatter = plt.scatter(
            results["risk"],
            results["return"],
            c=results["sharpe"],
            s=6,
            alpha=0.55
        )

        plt.colorbar(scatter, label="Sharpe Ratio")

        plt.scatter(best_sharpe["risk"], best_sharpe["return"], marker="*", s=350, label="Best Sharpe")
        plt.scatter(min_risk["risk"], min_risk["return"], marker="X", s=220, label="Minimum Risk")
        plt.scatter(max_return["risk"], max_return["return"], marker="^", s=220, label="Maximum Return")

        if current is not None:
            plt.scatter(current["risk"], current["return"], marker="o", s=260, label="Current Portfolio")
            plt.annotate(
                "Current",
                xy=(current["risk"], current["return"]),
                xytext=(10, 10),
                textcoords="offset points"
            )

        plt.annotate("Best Sharpe", xy=(best_sharpe["risk"], best_sharpe["return"]), xytext=(10, 10), textcoords="offset points")
        plt.annotate("Min Risk", xy=(min_risk["risk"], min_risk["return"]), xytext=(10, -15), textcoords="offset points")
        plt.annotate("Max Return", xy=(max_return["risk"], max_return["return"]), xytext=(10, 10), textcoords="offset points")

        plt.title("PDTA Efficient Frontier with Current Portfolio")
        plt.xlabel("Annualized Risk")
        plt.ylabel("Annualized Return")
        plt.legend()
        plt.grid(True)

        plt.savefig("output/frontier.png", dpi=220, bbox_inches="tight")
        plt.close()

        print("Saved output/frontier.png")
