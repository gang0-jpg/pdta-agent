class ScenarioAgent:
    def generate(self):
        scenarios = [
            {
                "name": "Normal",
                "description": "通常市場"
            },
            {
                "name": "Bull",
                "description": "株高・リスクオン"
            },
            {
                "name": "Bear",
                "description": "株安・リスクオフ"
            },
            {
                "name": "High Inflation",
                "description": "インフレ・金利上昇"
            },
            {
                "name": "JPY Weak",
                "description": "円安"
            },
            {
                "name": "JPY Strong",
                "description": "円高"
            },
        ]

        print()
        print("Generated Market Scenarios:")
        for scenario in scenarios:
            print(f"- {scenario['name']}: {scenario['description']}")

        return scenarios
