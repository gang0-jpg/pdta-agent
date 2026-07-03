from agents.market_agent import MarketAgent

def main():

    market = MarketAgent()

    prices = market.download()

    print(prices.tail())

    prices.to_csv("data/prices.csv")

    print()

    print("Saved data/prices.csv")

if __name__ == "__main__":
    main()
