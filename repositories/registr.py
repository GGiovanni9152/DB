from pandas import DataFrame
import psycopg2
from settings import DB_CONFIG
import bcrypt
from redis_client import redis_client

def registration(user : DataFrame) -> None:
    query = """
        INSERT INTO users (nickname, email, password, money)
        VALUES (%s, %s, %s, 0)
        RETURNING user_id
    """
    hashed_password = bcrypt.hashpw(user["password"].item().encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    user["password"] = hashed_password
    params = (user["nickname"].loc[0], user["email"].loc[0], user["password"].loc[0])
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            redis_client.delete("users:list")
            redis_client.delete("users_pass:list")
            return cur.fetchone()[0]