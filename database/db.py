import os
import json

import psycopg2
from psycopg2.extras import Json
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
                CREATE TABLE IF NOT EXISTS pdta_memory (
                    id SERIAL PRIMARY KEY,
                    run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    version TEXT,
                    market JSONB,
                    portfolio JSONB,
                    recommendation JSONB,
                    decision JSONB,
                    policy JSONB,
                    investor_note TEXT
                );
            """)


def to_jsonable(obj):
    if obj is None:
        return None

    if hasattr(obj, "to_dict"):
        return obj.to_dict(orient="records")

    try:
        json.dumps(obj)
        return obj
    except TypeError:
        return str(obj)


def save_pdta_memory(
    version,
    market=None,
    portfolio=None,
    recommendation=None,
    decision=None,
    policy=None,
    investor_note=None,
):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pdta_memory
                (
                    version,
                    market,
                    portfolio,
                    recommendation,
                    decision,
                    policy,
                    investor_note
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    version,
                    Json(to_jsonable(market)),
                    Json(to_jsonable(portfolio)),
                    Json(to_jsonable(recommendation)),
                    Json(to_jsonable(decision)),
                    Json(to_jsonable(policy)),
                    investor_note,
                ),
            )
