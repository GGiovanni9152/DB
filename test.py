import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
import repositories.users
import repositories.library
from st_clickable_images import clickable_images
import base64

def get_games() -> pd.DataFrame:
    print('Получение списка игр')
    games = pd.DataFrame(repositories.games.get_games())

    return games

def get_game_detail(game_id):
    detail = repositories.game_detail.get_game_detail(game_id)

    return detail

#games = get_games()

#game_id = games['game_id'].loc[games["name"] == 'Dota2']


def get_users() -> dict[str, int]:
    print("Получение списка пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["user_id"] for user in users}


users = get_users()

user_games = repositories.library.get_user_games(users['GGiovanni'])


print(users['GGiovanni'])

print(user_games)

print(user_games.info())



#detail = get_game_detail(game_id.item())
#print(detail)