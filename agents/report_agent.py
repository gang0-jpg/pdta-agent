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
