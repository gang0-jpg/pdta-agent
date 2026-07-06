import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg2.connect(database_url)


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS pdta_runs (
                    id SERIAL PRIMARY KEY,
                    run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    version TEXT,
                    recommendation TEXT,
                    policy_recommendation TEXT
                );
            """)


def save_pdta_run(version, recommendation, policy_recommendation):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pdta_runs
                (version, recommendation, policy_recommendation)
                VALUES (%s, %s, %s)
                """,
                (version, str(recommendation), str(policy_recommendation)),
            )