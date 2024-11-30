import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from pandas import DataFrame

def get_game_name(game_id : int) -> str:
    query = "SELECT name FROM games WHERE game_id = %(game_id)s"

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"game_id": game_id})
            return cur.fetchone()[0]

def get_games() -> list[dict]:
    print("Receiving games")
    query = "SELECT game_id, name, price FROM games;"
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def add_game(name : str) -> int:
    query = """
        INSERT INTO games(name)
        VALUE (%(name)s) RETURNING sale_id;
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"name": name})
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
