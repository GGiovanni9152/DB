from repositories.buy import buy_game
from pandas import DataFrame

class BuyService:
    def process_buy(self, items: DataFrame) -> None:
        items = items.rename(columns={"User_id": "user_id", "Game_id" : "game_id"})

        buy_game(items)

