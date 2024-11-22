import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from pandas import DataFrame

def get_users() -> list[dict]:
    print("Receiving games")
    query = "SELECT user_id, nickname, email FROM users;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()