from db.connection import get_connection


def init_db(schema_path="db/schema.sql"):
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(schema_path, "r", encoding="utf-8") as f:
                cur.execute(f.read())
        conn.commit()

def save_portfolio_snapshot(run_id, portfolio: dict):
    sql = """
    INSERT INTO portfolio_snapshot
    (run_id, asset_name, weight, mission)
    VALUES (%s, %s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            for asset, data in portfolio.items():
                cur.execute(
                    sql,
                    (
                        run_id,
                        asset,
                        data.get("weight"),
                        data.get("mission"),
                    ),
                )
        conn.commit()

def save_portfolio_result(run_id, result: dict):
    sql = """
    INSERT INTO portfolio_result
    (run_id, expected_return, risk, sharpe_ratio, max_drawdown)
    VALUES (%s, %s, %s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (
                    run_id,
                    float(result.get("expected_return")),
                    float(result.get("risk")),
                    float(result.get("sharpe_ratio")),
                    result.get("max_drawdown"),
                ),
            )
        conn.commit()

def save_scenario_summary(run_id, scenarios: list):
    sql = """
    INSERT INTO scenario_summary
    (run_id, scenario_name, expected_return, risk, comment)
    VALUES (%s, %s, %s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            for s in scenarios:
                cur.execute(
                    sql,
                    (
                        run_id,
                        s.get("scenario"),
                        float(s.get("return")),
                        float(s.get("risk")),
                        "",
                    ),
                )
        conn.commit()

def save_recommendation(run_id, recommendation: dict):
    sql = """
    INSERT INTO recommendation
    (run_id, current_policy, recommendation, reason, confidence)
    VALUES (%s, %s, %s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (
                    run_id,
                    recommendation.get("current_policy"),
                    recommendation.get("recommendation"),
                    recommendation.get("reason"),
                    recommendation.get("confidence"),
                ),
            )
        conn.commit()


def save_decision_log(run_id,decision: dict):
    sql = """
    INSERT INTO decision_log
    (run_id, decision, reason, executed, result_note)
    VALUES (%s, %s, %s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (
                    run_id,
                    decision.get("decision"),
                    decision.get("reason"),
                    decision.get("executed", False),
                    decision.get("result_note"),
                ),
            )
        conn.commit()

def save_policy(run_id,policy: dict):
    sql = """
    INSERT INTO policy
    (run_id, policy_name, policy_text)
    VALUES (%s, %s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (
                    run_id,
                    policy.get("policy_name"),
                    policy.get("policy_text"),
                ),
            )
        conn.commit()

def save_run(run_id, version):
    sql = """
    INSERT INTO run_history
    (run_id, version)
    VALUES (%s, %s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (run_id, version))
        conn.commit()
