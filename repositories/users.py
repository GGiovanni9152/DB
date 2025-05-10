import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from pandas import DataFrame
import redis
import json


redis_client = redis.Redis(host = 'localhost', port = 6379, db = 0, decode_responses = True)

def get_users() -> list[dict]:
    cache_key = "users:list"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    print("Receiving users")
    query = "SELECT user_id, nickname, email FROM users;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            users = cur.fetchall()
            redis_client.set(cache_key, json.dumps(users), ex=3600)
            return users
            #return cur.fetchall()

def get_users_with_password() -> list[dict]:
    cache_key = "users_pass:list"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    print("Receiving users")
    query = "SELECT password, email FROM users;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            users = cur.fetchall()
            redis_client.set(cache_key, json.dumps(users), ex=3600)
            return users
            #return cur.fetchall()

def get_user_by_email(user_email) -> list[dict]:
    query = "SELECT user_id, nickname, email, money FROM users WHERE email = %(email)s"

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, {"email" : user_email})
            return cur.fetchall()