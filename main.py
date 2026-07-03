from agents.market_agent import MarketAgent
from agents.return_agent import ReturnAgent
from agents.scenario_agent import ScenarioAgent
from agents.portfolio_generator_agent import PortfolioGeneratorAgent
from agents.optimizer_agent import OptimizerAgent
from agents.current_portfolio_agent import CurrentPortfolioAgent
from agents.report_agent import ReportAgent


def main():
    market = MarketAgent()
    prices = market.download()
    prices.to_csv("data/prices.csv")
    print("Saved data/prices.csv")

    return_agent = ReturnAgent()
    returns = return_agent.calculate_returns(prices)

    scenario_agent = ScenarioAgent()
    scenarios = scenario_agent.generate()

    generator = PortfolioGeneratorAgent()
    portfolios = generator.generate(returns.columns)

    optimizer = OptimizerAgent()

    print()
    print("Scenario Evaluation Summary:")

    scenario_results = []

    for scenario in scenarios:
        shocked_returns = scenario_agent.apply_shock(returns, scenario)
        results = optimizer.evaluate(shocked_returns, portfolios)

        best_sharpe = results.loc[results["sharpe"].idxmax()]

        scenario_results.append({
            "scenario": scenario["name"],
            "return": best_sharpe["return"],
            "risk": best_sharpe["risk"],
            "sharpe": best_sharpe["sharpe"]
        })

        print(
            f"{scenario['name']}: "
            f"return={best_sharpe['return']:.4f}, "
            f"risk={best_sharpe['risk']:.4f}, "
            f"sharpe={best_sharpe['sharpe']:.4f}"
        )

    normal_results = optimizer.evaluate(returns, portfolios)

    current_agent = CurrentPortfolioAgent()
    current = current_agent.evaluate(returns)

    report = ReportAgent()
    report.plot_frontier(normal_results, current=current)

    print()
    print("Scenario count:", len(scenarios))
    print("PDTA v0.7 completed.")


if __name__ == "__main__":
    main()
