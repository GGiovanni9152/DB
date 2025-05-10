import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from pandas import DataFrame
import redis
import json

redis_client = redis.Redis(host = 'localhost', port = 6379, db = 0, decode_responses = True)

def get_game_name(game_id : int) -> str:
    cache_key = f"game_name:{game_id}"
    cached_name = redis_client.get(cache_key)
    
    if cached_name:
        return cached_name


    query = "SELECT name FROM games WHERE game_id = %(game_id)s"

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"game_id": game_id})
            result = cur.fetchone()
            if result:
                name = result[0]
                redis_client.set(cache_key, name, ex=3600)
                return name
            return ""

            #return cur.fetchone()[0]

def get_games() -> list[dict]:
    #print("Receiving games")
    cache_key = "games:list"
    cached = redis_client.get(cache_key)

    if cached:
        print("Use cache games")
        return json.loads(cached)
    print("Receiving games")
    query = "SELECT game_id, name, price FROM games;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            games = cur.fetchall()
            redis_client.set(cache_key, json.dumps(games), ex=3600)
            return games
            #return cur.fetchall()

def add_game(name : str) -> int:
    query = """
        INSERT INTO games(name)
        VALUE (%(name)s) RETURNING sale_id;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"name": name})
            redis_client.delete("games:list")
            return cur.fetchone()[0]

def add_game_detail(game: DataFrame):
    query = """
        INSERT INTO games (game_id, developer_id, price, release_date, version)
        VALUES (%s, %s, %s, %s, %s);
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                query,
                game[["game_id", "developer_id", "price", "release_date", "version"]].itertuples(
                    index = False, name = None
                ),
            )
