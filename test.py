import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
from st_clickable_images import clickable_images
import base64

def get_games() -> pd.DataFrame:
    print('Получение списка игр')
    games = pd.DataFrame(repositories.games.get_games())

    return games

def get_game_detail(game_id):
    detail = repositories.game_detail.get_game_detail(game_id)

    return detail

games = get_games()

game_id = games['game_id'].loc[games["name"] == 'Dota2']

detail = get_game_detail(game_id.item())
print(detail)