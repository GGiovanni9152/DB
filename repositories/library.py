from pandas import DataFrame
import psycopg2
import psycopg2.extras
from settings import DB_CONFIG

def get_user_games(user_id: int) -> DataFrame:
    query = """
        SELECT games.game_id, name, rating
        FROM user_games 
        LEFT JOIN games
        ON user_games.game_id = games.game_id
        WHERE user_games.user_id = %(user_id)s
        ORDER BY name
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, {"user_id": user_id})
            return DataFrame(cur.fetchall())