from datetime import date
import pandas as pd
import streamlit as st

from services.buy import BuyService
import repositories.games
import repositories.users
import repositories.library
from redis_client import save_games_table, load_games_table, clear_games_table, clear_user_library, publish_event
import json


@st.cache_data
def get_games() -> dict[str, int]:
    games = repositories.games.get_games()
    return {game["name"]: game["game_id"] for game in games}

@st.cache_data
def get_users() -> dict[str, int]:
    users = repositories.users.get_users()
    return {user["nickname"]: user["user_id"] for user in users}

def get_games_names() -> dict[int, str]:
    names = repositories.games.get_games()
    return {name["game_id"]: name["name"] for name in names}

def add_game_event(user_name, user_id, game_name, game_id):
    new_row = pd.DataFrame({
        "Имя пользователя": [user_name],
        "User_id": [user_id],
        "Название игры": [game_name],
        "Game_id": [game_id],
    })
    
    if "games_table" not in st.session_state or st.session_state.games_table.empty:
        st.session_state.games_table = pd.DataFrame(columns=new_row.columns)

    st.session_state.games_table = st.session_state.games_table[new_row.columns]

    is_duplicate = (st.session_state.games_table == new_row.values).all(axis=1).any()
    if not is_duplicate:
        st.session_state.games_table = pd.concat([st.session_state.games_table, new_row], ignore_index=True)
        st.session_state.games_table.drop_duplicates(inplace=True, ignore_index=True)

def clear_table_event():
    st.session_state.games_table = pd.DataFrame(columns=["Имя пользователя", "User_id", "Название игры", "Game_id"])

def upload_games(games_table: pd.DataFrame):
    BuyService().process_buy(games_table)
    st.write("Игра добавлена на выбранный аккаунт!")
    
    user_id = list(games_table['User_id'].unique())
    game_id = list(games_table["Game_id"].unique())

    event = {
        "type": "new_game_added",
        "user_id": user_id,
        "game_id": game_id
    }
    #print(event)
    #print(json.dumps(event))

    publish_event("game_updates", json.dumps(event))

def show_store_page():
    st.title("Магазин")

    user = st.session_state.get("user")
    if user is None or user.empty:
        st.error("Вы не авторизованы")
        return

    current_user_id = user["user_id"].item()

    if "games_table" not in st.session_state:
        cached_df = load_games_table(current_user_id)
        if cached_df is not None:
            st.session_state.games_table = cached_df
        else:
            clear_table_event()

    users = get_users()
    games = get_games()
    games_names = get_games_names()

    selected_game = st.selectbox("Выберите игру", games.keys())
    selected_user = st.selectbox("Выберите пользователя", users.keys())

    if st.button("Добавить игру"):
        add_game_event(selected_user, users[selected_user], selected_game, games[selected_game])
        save_games_table(current_user_id, st.session_state.games_table)

    if st.button("Очистить таблицу"):
        clear_table_event()
        clear_games_table(current_user_id)

    if st.button("Подтвердить добавление игры") and len(st.session_state.games_table) > 0:
        already_has = False
        has_game = None
        for uid in st.session_state.games_table['User_id'].unique():
            user_games_df = repositories.library.get_user_games(uid)

            if "game_id" not in user_games_df.columns:
                continue

            owned_game_ids = user_games_df["game_id"].astype(int).tolist()

            for game_id in st.session_state.games_table[
                st.session_state.games_table["User_id"] == uid
            ]["Game_id"]:
                if game_id in owned_game_ids:
                    already_has = True
                    has_game = games_names[game_id]
                    name = st.session_state.games_table.loc[
                        st.session_state.games_table["User_id"] == uid, "Имя пользователя"
                    ].iloc[0]
                    break

        if already_has:
            st.warning(f"У пользователя {name} уже имеется игра: {has_game}", icon="⚠️")
        else:
            upload_games(st.session_state.games_table)
            st.success("Игра успешно добавлена!", icon="🔥")
            affected_user_ids = st.session_state.games_table['User_id'].unique()
            for uid in affected_user_ids:
                clear_user_library(int(uid))
            clear_table_event()
            clear_games_table(current_user_id)

    st.write("Выбранные игры:")
    st.dataframe(st.session_state.games_table)