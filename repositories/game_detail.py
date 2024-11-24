from pandas import DataFrame
import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def get_game_detail(game_id: int) -> DataFrame:
    query = """
        SELECT name, rating, release_date, version, description, picture_name, picture_code
        FROM game_detail
        LEFT JOIN developers
        ON game_detail.developer_id = developers.developer_id
        WHERE game_id = %(game_id)s
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, {"game_id": game_id})
            return DataFrame(cur.fetchall())