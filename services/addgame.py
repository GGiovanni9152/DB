from datetime import datetime
from repositories.games import add_game, add_game_detail
from pandas import DataFrame
import time

class StoreService:
    def process_add_game(self, name: str, items: DataFrame) -> int:
        game_id = add_game(name)

        items["game_id"] = game_id
        add_game_detail(items)

        return game_id
        