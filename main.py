from agents.market_agent import MarketAgent
from agents.return_agent import ReturnAgent
from agents.portfolio_generator_agent import PortfolioGeneratorAgent
from agents.optimizer_agent import OptimizerAgent


def main():
    market = MarketAgent()
    prices = market.download()
    prices.to_csv("data/prices.csv")
    print("Saved data/prices.csv")

    return_agent = ReturnAgent()
    returns = return_agent.calculate_returns(prices)

    generator = PortfolioGeneratorAgent()
    portfolios = generator.generate(returns.columns)

    optimizer = OptimizerAgent()
    results = optimizer.evaluate(returns, portfolios)

    print()
    print("Portfolio results head:")
    print(results.head())


if __name__ == "__main__":
    main()
