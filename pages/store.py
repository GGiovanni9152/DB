from datetime import date
import pandas as pd

import streamlit as st
from services.addgame import StoreService
import repositories.games
import repositories.users
import random

@st.cache_data
def get_games() -> dict[str, str]:
    print('Получение списка игр')
    games = repositories.games.get_games()

    return {game["name"]: game["price"] for game in games}

@st.cache_data
def get_users() -> dict[str, str]:
    print("Получение списка пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["email"] for user in users}

games = get_games()
users = get_users()

def show_store_page():
    st.title("Магазин")
    
    selected_game = st.selectbox("Выберите игру", games.keys())
    selected_user = st.selectbox("Выберете пользователя", users.keys())

    add_game_btn = st.button("Добавить игру")
    clear_table_btn = st.button("Очистить игру")
    apply_btn = st.button("Подтверить добавление игры")

    #if (add_game_btn):


