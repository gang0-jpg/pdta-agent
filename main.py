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
    results = optimizer.evaluate(returns, portfolios)

    current_agent = CurrentPortfolioAgent()
    current = current_agent.evaluate(returns)

    report = ReportAgent()
    report.plot_frontier(results, current=current)

    print()
    print(f"Scenario count: {len(scenarios)}")
    print("PDTA v0.6 completed.")


if __name__ == "__main__":
    main()
