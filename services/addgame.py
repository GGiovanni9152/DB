from datetime import datetime
from pandas import DataFrame
import time
import repositories.addgame
import base64

def encode_image_to_base64(image):
    encoded = base64.b64encode(image.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

class GameAdder():
    def add_game(self, game : DataFrame):

        game_id = repositories.addgame.add_game(game[["name", "price"]])

        #pathname = "picture/" + game["picture_name"]

        game["game_id"] = game_id

        repositories.addgame.add_game_detail(game[["game_id", "developer_id", "release_date", "version", "description", "picture_name", "picture_code"]])



        