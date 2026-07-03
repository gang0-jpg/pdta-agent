import matplotlib.pyplot as plt
import pandas as pd


class ReportAgent:
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
            plt.scatter(
                current["risk"],
                current["return"],
                marker="o",
                s=260,
                color="purple",
                edgecolor="black",
                linewidth=1.5,
                label="Current Portfolio"
            )
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

    def plot_scenario_summary(self, summary: pd.DataFrame):
        plt.figure(figsize=(10, 6))

        plt.bar(summary["scenario"], summary["sharpe"])

        plt.title("PDTA Scenario Sharpe Ratio")
        plt.xlabel("Scenario")
        plt.ylabel("Sharpe Ratio")
        plt.xticks(rotation=30, ha="right")
        plt.grid(axis="y")

        plt.savefig("output/scenario_summary.png", dpi=220, bbox_inches="tight")
        plt.close()

        print("Saved output/scenario_summary.png")

    def plot_risk_reward_map(self, results: pd.DataFrame, current=None, policy_recommendation=None):
        best_sharpe = results.loc[results["sharpe"].idxmax()]
        min_risk = results.loc[results["risk"].idxmin()]
        max_return = results.loc[results["return"].idxmax()]
        min_drawdown = results.loc[results["max_drawdown"].idxmax()]

        plt.figure(figsize=(12, 7))

        # PDTA Robust Zone
        plt.axhspan(1.1, results["sharpe"].max() + 0.1, alpha=0.10, color="green")
        plt.axvspan(-10, 0, alpha=0.10, color="green")

        plt.scatter(
            results["max_drawdown"] * 100,
            results["sharpe"],
            s=6,
            alpha=0.30,
            color="steelblue",
            label="Portfolios"
        )

        plt.scatter(
            best_sharpe["max_drawdown"] * 100,
            best_sharpe["sharpe"],
            marker="*",
            s=420,
            color="gold",
            edgecolor="black",
            linewidth=1.2,
            label="Best Sharpe"
        )

        plt.scatter(
            min_risk["max_drawdown"] * 100,
            min_risk["sharpe"],
            marker="s",
            s=210,
            color="green",
            label="Minimum Risk"
        )

        plt.scatter(
            max_return["max_drawdown"] * 100,
            max_return["sharpe"],
            marker="^",
            s=210,
            color="red",
            label="Maximum Return"
        )

        plt.scatter(
            min_drawdown["max_drawdown"] * 100,
            min_drawdown["sharpe"],
            marker="D",
            s=210,
            color="mediumpurple",
            label="Minimum Drawdown"
        )

        if current is not None:
            plt.scatter(
                current["max_drawdown"] * 100,
                current["sharpe"],
                marker="o",
                s=340,
                color="purple",
                edgecolor="black",
                linewidth=2,
                label="Current Portfolio"
            )

            plt.annotate(
                "Current",
                xy=(current["max_drawdown"] * 100, current["sharpe"]),
                xytext=(12, 12),
                textcoords="offset points",
                fontsize=11
            )

            plt.annotate(
                "",
                xy=(best_sharpe["max_drawdown"] * 100, best_sharpe["sharpe"]),
                xytext=(current["max_drawdown"] * 100, current["sharpe"]),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="black")
            )

        plt.annotate(
            "Best Sharpe",
            xy=(best_sharpe["max_drawdown"] * 100, best_sharpe["sharpe"]),
            xytext=(12, 12),
            textcoords="offset points",
            fontsize=11
        )

        plt.annotate(
            "Min DD",
            xy=(min_drawdown["max_drawdown"] * 100, min_drawdown["sharpe"]),
            xytext=(12, 12),
            textcoords="offset points",
            fontsize=11
        )

        plt.axvline(-10, linestyle="--", linewidth=1)
        plt.axhline(1.1, linestyle="--", linewidth=1)

        plt.text(-9.7, 1.12, "PDTA Robust Zone", fontsize=11)

        plt.title("PDTA Portfolio Evaluation Map")
        plt.xlabel("Max Drawdown (%)")
        plt.ylabel("Sharpe Ratio")
        plt.legend()
        plt.grid(True)

        plt.savefig("output/risk_reward_map.png", dpi=220, bbox_inches="tight")
        plt.close()

        print("Saved output/risk_reward_map.png")
