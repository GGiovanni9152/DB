import streamlit as st
from pages.store import show_store_page
from pages.library import show_library_page
from pages.game_detail import show_search_games_page
import repositories.users
from services.auth import Authotize
import services.user
import services.users
import repositories.admin
import pandas as pd

auth = Authotize()
users = services.users.get_users()

def login():
    st.title("Авторизация")
    st.write("Введите почту и пароль:")

    email = st.text_input("Почта")
    password = st.text_input("Пароль", type="password")
    if st.button("Войти"):
        if auth.auth(email, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = email
            st.success(f"Добро пожаловать, {email}!")
            st.session_state.user = services.user.get_user(email)
            st.session_state["admin"] = repositories.admin.get_admins(st.session_state.user["user_id"].item())
            print(st.session_state["admin"])
            st.rerun()
        else:
            st.error("Неверная почта или пароль!")

def register():
    st.title("Регистрация")
    st.write("Введите почту")
    email = st.text_input("Почта")
    st.write("Введите пароль")
    password = st.text_input("Пароль", type="password")
    st.write("Подтвердите пароль")
    second_password = st.text_input("Подтверждение пароля", type="password")
    st.write("Введите ник")
    nickname = st.text_input("Ник")

    if st.button("Зарегистрироваться"):
        if (not(email) or not(password) or not(second_password) or not(nickname)):
            st.error("Введите требуемые значения!")
        else:
            if (password != second_password):
                st.error("Пароли не совпадают!")
            else:
                if users["email"].isin([email]).any():
                    st.error("Данная почта уже зарегистрирована!")
                elif users["nickname"].isin([nickname]).any():
                    st.error("Пользователь с данным именем уже существует")
                else:
                    st.success("Успешная регистрация")
                    st.session_state["authenticated"] = True
                    #st.session_state.user = pd.DataFrame({})
                    st.rerun()




def main():

    if not st.session_state["authenticated"]:
        pg = st.radio("Войдите или зарегистрируйтесь", ["Вход", "Регистрация"])
        if pg == "Вход":
            login()
        elif pg == "Регистрация":
            register()
        #login()
    else:
        page = st.sidebar.radio(
            "Перейти к странице",
            ["Магазин", "Библиотека", "Игры"],
        )

        if page == "Магазин":
            show_store_page()

        elif page == "Библиотека":
            show_library_page()
        elif page == "Игры":
            show_search_games_page()
    

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "admin" not in st.session_state:
    st.session_state["admin"] = False

if "user" not in st.session_state:
    st.session_state.user = pd.DataFrame(
        columns = ["user_id", "nickname", "email", "money"]
    )

if __name__ == "__main__":
    main()