import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
import repositories.users
import repositories.library
from st_clickable_images import clickable_images
import base64
from services.auth import Authotize
import repositories.admin
import services.users


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


'''users = get_users()

user_games = repositories.library.get_user_games(users['GGiovanni'])


print(users['GGiovanni'])

print(user_games)

print(user_games.info())
'''
#auth = Authotize()

#print(auth.auth('ggiovanni@gmail.com', '123'))

#print(repositories.admin.get_admins(1))

#print(repositories.users.get_user_by_email("ggiovanni@gmail.com"))

import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from pandas import DataFrame
import repositories.users

def get_user(email) -> DataFrame:

    user = repositories.users.get_user_by_email(email)

    result = DataFrame()

    for dic in user:
        for key in dic.keys():
            #result.insert(0, column=key, value=dic[key])
            result[key] = [dic[key]]
            print(key, dic[key])

    return result

print(get_user("ggiovanni@gmail.com"))
#detail = get_game_detail(game_id.item())
#print(detail)