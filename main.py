import pandas as pd
import uuid
from database.db import init_db, save_pdta_run
from db.repository import (
    init_db,
    save_run,                 # ← これを追加
    save_portfolio_snapshot,
    save_portfolio_result,
    save_scenario_summary,
    save_recommendation,
    save_decision_log,
    save_policy,
)

from config import PDTA_VERSION
from agents.policy_agent import PolicyAgent
from agents.decision_agent import DecisionAgent
from agents.market_agent import MarketAgent
from agents.return_agent import ReturnAgent
from agents.scenario_agent import ScenarioAgent
from agents.portfolio_generator_agent import PortfolioGeneratorAgent
from agents.optimizer_agent import OptimizerAgent
from agents.current_portfolio_agent import CurrentPortfolioAgent
from agents.report_agent import ReportAgent


def main():
    init_db()
    run_id = str(uuid.uuid4())

    print("=" * 60)
    print(f"Run ID : {run_id}")
    print("=" * 60)
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

    summary = pd.DataFrame(scenario_results)

    summary.to_csv(
        "data/scenario_summary.csv",
        index=False
    )

    best_portfolio = normal_results.loc[
        normal_results["sharpe"].idxmax()
    ]

    decision = DecisionAgent()

    recommendation = decision.recommend(
        current,
        best_portfolio
    )
    policy = PolicyAgent()
    policy_recommendation = policy.apply(recommendation)
    save_pdta_run(
        version="v0.1-postgres",
        recommendation=recommendation,
        policy_recommendation=policy_recommendation,
    )


    report = ReportAgent()

    report.plot_frontier(
        normal_results,
        current=current
    )

    report.plot_risk_reward_map(
        normal_results,
        current=current,
        policy_recommendation=policy_recommendation
    )

    report.plot_scenario_summary(summary)

    print()
    print("=" * 60)
    print(f"PDTA v{PDTA_VERSION} completed.")
    print("=" * 60)
    print("Generated files:")
    print("- data/prices.csv")
    print("- data/returns.csv")
    print("- data/portfolios.csv")
    print("- data/portfolio_results.csv")
    print("- data/scenario_summary.csv")
    print("- data/recommendation.csv")
    print("- data/policy_recommendation.csv")
    print("- output/frontier.png")
    print("- output/scenario_summary.png")
    print("- output/risk_reward_map.png")

    init_db()
    save_run(
        run_id,
        PDTA_VERSION
    )

    current_portfolio = {
        "Gold": {
            "weight": 4.91,
            "mission": "Inflation hedge",
        },
        "REIT": {
            "weight": 3.94,
            "mission": "Income",
        },
        "US Bond": {
            "weight": 8.22,
            "mission": "Defense",
        },
        "Japan Inflation Linked Bond": {
            "weight": 1.18,
            "mission": "Inflation protection",
        },
        "Equity": {
            "weight": 14.35,
            "mission": "Growth / buy the dip",
        },
        "Foreign Currency": {
            "weight": 27.38,
            "mission": "USD cash for US equity correction",
        },
        "JPY Cash": {
            "weight": 40.01,
            "mission": "Cash reserve for Japan equity correction",
        },
    }

    save_portfolio_snapshot(
        run_id,
        current_portfolio
    )
    # シナリオ評価結果保存
    save_scenario_summary(
        run_id,
        summary.to_dict("records")
    )

    # 最適ポートフォリオ保存
    save_portfolio_result(
        run_id,
        {
            "expected_return": float(best_portfolio["return"]),
            "risk": float(best_portfolio["risk"]),
            "sharpe_ratio": float(best_portfolio["sharpe"]),
            "max_drawdown": None,
        }
    )
    # Recommendation保存
    save_recommendation(
        run_id,
        {
            "current_policy": "Mission-based portfolio policy",
            "recommendation": "BUY NASDAQ100, GOLD, USDJPY / SELL TOPIX, JREIT, USBOND, JPY",
            "reason": "DecisionAgent recommendation based on current portfolio and optimized portfolio",
            "confidence": None,
        }
    )

    # Decision の要約を作成
    buy_assets = policy_recommendation[
        policy_recommendation["AdjustedAction"] == "BUY"
    ]["Asset"].tolist()

    sell_assets = policy_recommendation[
        policy_recommendation["AdjustedAction"] == "SELL"
    ]["Asset"].tolist()

    hold_assets = policy_recommendation[
        policy_recommendation["AdjustedAction"] == "HOLD"
    ]["Asset"].tolist()

    decision_summary = (
        f"BUY {', '.join(buy_assets)} / "
        f"SELL {', '.join(sell_assets)} / "
        f"HOLD {', '.join(hold_assets)}"
    )

    # Decision Log保存
    save_decision_log(
        run_id,
        {
            "decision": decision_summary,
            "reason": "PolicyAgent applied investment policy to DecisionAgent recommendation",
            "executed": False,
            "result_note": "Not executed yet",
        }
    )

    save_policy(
        run_id,
        {
            "policy_name": "Mission-based Portfolio Policy",
            "policy_text": decision_summary,
        }
    )


if __name__ == "__main__":

    main()
