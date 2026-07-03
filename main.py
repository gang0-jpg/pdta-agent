from agents.market_agent import MarketAgent
from agents.return_agent import ReturnAgent


def main():

    market = MarketAgent()

    prices = market.download()

    prices.to_csv("data/prices.csv")

    print("Saved data/prices.csv")

    return_agent = ReturnAgent()

    returns = return_agent.calculate_returns(prices)

    print()
    print(returns.tail())


if __name__ == "__main__":
    main()
