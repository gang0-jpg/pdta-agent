import matplotlib.pyplot as plt
import pandas as pd


class ReportAgent:
    def plot_frontier(self, results: pd.DataFrame, current=None):
        best_sharpe = results.loc[results["sharpe"].idxmax()]
        min_risk = results.loc[results["risk"].idxmin()]
        max_return = results.loc[results["return"].idxmax()]

        plt.figure(figsize=(10, 6))

        scatter = plt.scatter(
            results["risk"],
            results["return"],
            c=results["sharpe"],
            s=5,
            alpha=0.5
        )

        plt.colorbar(scatter, label="Sharpe Ratio")

        plt.scatter(best_sharpe["risk"], best_sharpe["return"], marker="*", s=300, label="Best Sharpe")
        plt.scatter(min_risk["risk"], min_risk["return"], marker="X", s=200, label="Min Risk")
        plt.scatter(max_return["risk"], max_return["return"], marker="^", s=200, label="Max Return")

        if current is not None:
            plt.scatter(
                current["risk"],
                current["return"],
                marker="o",
                s=200,
                label="Current"
            )

        plt.title("PDTA Efficient Frontier")
        plt.xlabel("Annualized Risk")
        plt.ylabel("Annualized Return")
        plt.legend()
        plt.grid(True)

        plt.savefig("output/frontier.png", dpi=200, bbox_inches="tight")
        plt.close()

        print("Saved output/frontier.png")
