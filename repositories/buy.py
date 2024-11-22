from pandas import DataFrame
import psycopg2
from settings import DB_CONFIG


def buy_game(buy : DataFrame) -> None:
    query = """
        INSERT INTO user_games (user_id, game_id, rating)
        VALUES (%s, %s, NULL)
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.executemany(query,
                            buy[["user_id", "game_id"]].itertuples(
                                index=False, name=None
                            ),
                         )
