CREATE TABLE IF NOT EXISTS portfolio_snapshot (
    id SERIAL PRIMARY KEY,
    snapshot_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    asset_name TEXT NOT NULL,
    weight NUMERIC NOT NULL,
    mission TEXT
);

CREATE TABLE IF NOT EXISTS portfolio_result (
    id SERIAL PRIMARY KEY,
    run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expected_return NUMERIC,
    risk NUMERIC,
    sharpe_ratio NUMERIC,
    max_drawdown NUMERIC
);

CREATE TABLE IF NOT EXISTS scenario_summary (
    id SERIAL PRIMARY KEY,
    run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scenario_name TEXT NOT NULL,
    expected_return NUMERIC,
    risk NUMERIC,
    comment TEXT
);

CREATE TABLE IF NOT EXISTS recommendation (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_policy TEXT,
    recommendation TEXT NOT NULL,
    reason TEXT,
    confidence NUMERIC
);

CREATE TABLE IF NOT EXISTS decision_log (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    decision TEXT NOT NULL,
    reason TEXT,
    executed BOOLEAN DEFAULT FALSE,
    result_note TEXT
);

CREATE TABLE IF NOT EXISTS policy (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    policy_name TEXT NOT NULL,
    policy_text TEXT NOT NULL
);
