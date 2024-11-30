from pandas import DataFrame
import psycopg2
from settings import DB_CONFIG
import bcrypt


def add_game(game : DataFrame) -> int:
    query = """
        INSERT INTO games (name, price)
        VALUES (%s, %s)
        RETURNING game_id
    """
    params = (game["name"].loc[0], game["price"].loc[0])
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchone()[0]

def add_game_detail(detail: DataFrame) -> None:
    query = """
        INSERT INTO game_detail (game_id, developer_id, rating, release_date, version, description, picture_name, picture_code)
        VALUES (%s, %s, 0, %s, %s, %s, %s, %s)
    """
    params = (int(detail["game_id"].iloc[0]), int(detail["developer_id"].iloc[0]), str(detail["release_date"].loc[0]), str(detail["version"].loc[0]), str(detail["description"].loc[0]), str(detail["picture_name"].loc[0]), detail["picture_code"].loc[0])
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            #return cur.fetchone()[0]