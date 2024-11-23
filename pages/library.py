import pandas as pd
import streamlit as st
from services.library import LibraryService
from repositories.library import get_user_games
import repositories.users

@st.cache_data
def get_users() -> dict[str, int]:
    print("Получение пользователей")
    users = repositories.users.get_users()

    return {user["nickname"]: user["user_id"] for user in users}

users = get_users()

def show_library_page():
    st.title("Библиотека")

    selected_user = st.selectbox("Выберете пользователя", users.keys())
    btn_pressed = st.button("Подтвердить выбор пользователя")

    if selected_user and btn_pressed:
        items = get_user_games(users[selected_user])

        if(items.empty):
            st.warning("У выбранного пользователя нет приложений")
        else:
            st.dataframe(items)