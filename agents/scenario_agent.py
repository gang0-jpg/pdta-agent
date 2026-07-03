class ScenarioAgent:
    def generate(self):
        scenarios = [
            {
                "name": "Normal",
                "description": "通常市場",
                "shock": {}
            },
            {
                "name": "Bull",
                "description": "株高・リスクオン",
                "shock": {
                    "TOPIX": 1.20,
                    "NASDAQ100": 1.25,
                    "GOLD": 0.95,
                    "USBOND": 0.95
                }
            },
            {
                "name": "Bear",
                "description": "株安・リスクオフ",
                "shock": {
                    "TOPIX": 0.70,
                    "NASDAQ100": 0.65,
                    "GOLD": 1.15,
                    "USBOND": 1.10,
                    "JPY": 1.05
                }
            },
            {
                "name": "High Inflation",
                "description": "インフレ・金利上昇",
                "shock": {
                    "GOLD": 1.25,
                    "USBOND": 0.80,
                    "JREIT": 0.90,
                    "USDJPY": 1.10
                }
            },
            {
                "name": "JPY Weak",
                "description": "円安",
                "shock": {
                    "USDJPY": 1.30,
                    "GOLD": 1.10,
                    "NASDAQ100": 1.10
                }
            },
            {
                "name": "JPY Strong",
                "description": "円高",
                "shock": {
                    "USDJPY": 0.70,
                    "TOPIX": 0.90,
                    "NASDAQ100": 0.90,
                    "JPY": 1.10
                }
            },
        ]

        print()
        print("Generated Market Scenarios:")
        for scenario in scenarios:
            print(f"- {scenario['name']}: {scenario['description']}")

        return scenarios

    def apply_shock(self, returns, scenario):
        shocked_returns = returns.copy()

        for asset, multiplier in scenario["shock"].items():
            if asset in shocked_returns.columns:
                shocked_returns[asset] = shocked_returns[asset] * multiplier

        return shocked_returns
