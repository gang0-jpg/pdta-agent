import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "h100_mcp_demo",
    "user": "demo",
    "password": "demo",
}


def get_connection():
    return psycopg2.connect(
        **DB_CONFIG,
        cursor_factory=RealDictCursor
    )
