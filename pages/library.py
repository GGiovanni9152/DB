import pandas as pd
import streamlit as st
from services.library import LibraryService
from repositories.library import get_user_games
import repositories.users
from redis_client import save_user_library, load_user_library, clear_user_library

def get_users() -> dict[str, int]:
    print("Получение пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["user_id"] for user in users}

def show_library_page():
    users = get_users()
    st.title("Библиотека")

    selected_user = st.selectbox("Выберете пользователя", users.keys())
    btn_pressed = st.button("Подтвердить выбор пользователя")

    if selected_user and btn_pressed:
        user_id = users[selected_user]
        items = load_user_library(user_id)

        if items is None:
            items = get_user_games(user_id)
            if not items.empty:
                save_user_library(user_id, items)

        if(items.empty):
            st.warning("У выбранного пользователя нет приложений")
        else:
            st.dataframe(items)
            if st.button("Очистить кэш"):
                clear_user_library(user_id)
                st.success("Кэш очищен")

#show_library_page()