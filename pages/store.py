from datetime import date
import pandas as pd

import streamlit as st
from services.addgame import StoreService
from services.buy import BuyService
import repositories.games
import repositories.users
import random

if "games_table" not in st.session_state:
    st.session_state.games_table = pd.DataFrame(
        columns = ["Имя пользователя", "User_id", "Название игры", "Game_id"]
    )

@st.cache_data
def get_games() -> dict[str, str]:
    print('Получение списка игр')
    games = repositories.games.get_games()

    return {game["name"]: game["game_id"] for game in games}

@st.cache_data
def get_users() -> dict[str, str]:
    print("Получение списка пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["user_id"] for user in users}

def add_game_event(user_name, user_id, game_name, game_id):
    new_row = pd.DataFrame(
        {
            "Имя пользователя": [user_name],
            "User_id": [user_id],
            "Название игры": [game_name],
            "Game_id": [game_id],
        }
    )

    st.session_state.games_table = pd.concat(
        [st.session_state.games_table, new_row], ignore_index=True
    )

def clear_table_event():
    st.session_state.games_table = pd.DataFrame(
        columns = ["Имя пользователя", "User_id", "Название игры", "Game_id"]
    )

def upload_games(games_table: pd.DataFrame) -> None:
    BuyService().process_buy(games_table)
    st.write("Игра добавлена на ваш аккаунт!")

games = get_games()
users = get_users()

def show_store_page():
    st.title("Магазин")
    
    selected_game = st.selectbox("Выберите игру", games.keys())
    selected_user = st.selectbox("Выберете пользователя", users.keys())

    add_game_btn = st.button("Добавить игру")
    clear_table_btn = st.button("Очистить таблицу")
    apply_btn = st.button("Подтверить добавление игры")

    if (add_game_btn):
        add_game_event(selected_user, users[selected_user], selected_game, games[selected_game])

    if (clear_table_btn):
        clear_table_event()
    
    if (apply_btn and len(st.session_state.games_table) > 0):
        upload_games(st.session_state.games_table)
        st.success("Игра успешно добавлена!")
        clear_table_event()
    
    st.write("Добавленные игры:")
    st.dataframe(st.session_state.games_table)
