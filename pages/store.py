from datetime import date
import pandas as pd

import streamlit as st
from services.addgame import StoreService
from services.buy import BuyService
import repositories.games
import repositories.users
import repositories.library
import random

if "games_table" not in st.session_state:
    st.session_state.games_table = pd.DataFrame(
        columns = ["Имя пользователя", "User_id", "Название игры", "Game_id"]
    )

@st.cache_data
def get_games() -> dict[str, int]:
    print('Получение списка игр')
    games = repositories.games.get_games()

    return {game["name"]: game["game_id"] for game in games}

@st.cache_data
def get_users() -> dict[str, int]:
    print("Получение списка пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["user_id"] for user in users}

def get_games_names() -> dict[int, str]:
    names = repositories.games.get_games()
    return {name["game_id"]: name["name"] for name in names}

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
games_names = get_games_names()


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
        user_games = repositories.library.get_user_games(users[selected_user])

        already_has = False
        has_game = None

        for game_id in st.session_state.games_table["Game_id"]:
            if game_id in user_games["game_id"]:
                already_has = True
                has_game = games_names[game_id]
                break

        if not(already_has):
            upload_games(st.session_state.games_table)
            st.success("Игра успешно добавлена!", icon="🔥")
            clear_table_event()
        else:
            st.warning(f"У пользователя уже имеется игра: {has_game}", icon="⚠️")
    
    st.write("Выбранные игры:")
    st.dataframe(st.session_state.games_table)
