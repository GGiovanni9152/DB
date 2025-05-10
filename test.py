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
from redis_client import redis_client
import json

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

def get_all_admins(): #-> list[dict]:
    cache_key = "admins"
    #cached_admins = redis_client.get(cache_key)
    if redis_client.exists(cache_key):
        return [int(admin_id) for admin_id in redis_client.smembers(cache_key)]
    #if cached_admins:
    #    return json.loads(cached_admins)

    query = "SELECT user_id FROM admins;"
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:#(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            admins = cur.fetchall()
            adm = []
            for elem in admins:
                adm.append(elem[0])
            redis_client.sadd(cache_key, *adm)
            redis_client.expire(cache_key, 3600)
            #redis_client.set(cache_key, json.dumps(adm), ex=3600)
            return adm

def get_admins(admin_id) -> bool:
    if redis_client.exists("admins"):
        return bool(redis_client.sismember("admins", str(admin_id)))
    
    admins = get_all_admins()
    return admin_id in admins
    
    #query = """SELECT user_id FROM admins WHERE user_id = %(admin_id)s"""
    
    #with psycopg2.connect(**DB_CONFIG) as conn:
    #    with conn.cursor() as cur:
    #        cur.execute(query, {"admin_id" : admin_id})
    #       return (cur.fetchone() != None)

redis_client.delete("admins")
print(get_admins(6))

#print(get_all_admins())
#admins = get_all_admins()
#print(json.dumps(admins))
#for elem in admins:
#    print(elem[0])
#print(get_user("ggiovanni@gmail.com"))
#detail = get_game_detail(game_id.item())
#print(detail)