import streamlit as st
from pages.store import show_store_page
from pages.library import show_library_page
from pages.game_detail import show_search_games_page
from pages.addgame import show_add_game_page
import repositories.users
from services.auth import Authotize
import services.user
import services.users
import services.regist
import repositories.admin
import pandas as pd
import redis_client
import atexit
import jwt_utils
import adm_listener


auth = Authotize()
users = services.users.get_users()
registr = services.regist.Registration()

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
            user = services.user.get_user(email)
            st.session_state.user = user
            redis_client.save_current_user(user)
            st.session_state["admin"] = repositories.admin.get_admins(st.session_state.user["user_id"].item())
            print(st.session_state["admin"])
            st.rerun()
            token = jwt_utils.create_token(user["user_id"].item(), email, st.session_state["admin"])
            st.session_state["jwt"] = token
            redis_client.redis_client.save_token(user["user_id"].item(), token)
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
                    #user = pd.DataFrame({"nickname" : nickname, "email" : email, "password" : password})
                    user_id = registr.registr(pd.DataFrame({"nickname": [nickname], "email": [email], "password": [password]}))
                    redis_client.clear_users()
                    #user["user_id"] = user_id
                    user = pd.DataFrame({"user_id": [user_id], "nickname": [nickname], "email": [email], "password": [password]})
                    st.session_state.user = user
                    redis_client.save_current_user(user)
                    token = jwt_utils.create_token(user_id, email, False)
                    st.session_state["jwt"] = token
                    redis_client.redis_client.save_token(user_id, token)
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
        if "jwt" in st.session_state:
            payload = jwt_utils.decode_token(st.session_state["jwt"])
            if payload:
                token_from_redis = redis_client.load_token(payload["user_id"])
                if token_from_redis == st.session_state["jwt"]:
                    st.session_state["authenticated"] = True
                    st.session_state["admin"] = payload.get("admin", False)
                    st.session_state["user"] = services.user.get_user(payload["email"])
                else:
                    st.warning("token_comparison_failed")
                    st.session_state["authenticated"] = False
                    st.session_state["admin"] = False
                    st.session_state["user"] = pd.DataFrame()
                    redis_client.clear_current_user()
                    st.rerun()
            else:
                st.session_state["authenticated"] = False
                st.session_state["admin"] = False
                st.session_state["user"] = pd.DataFrame()
                redis_client.clear_current_user()
                st.rerun()

        if st.session_state["admin"]:
            if st.sidebar.button("Выйти"):
                st.session_state["authenticated"] = False
                st.session_state["admin"] = False
                st.session_state["user"] = pd.DataFrame()
                redis_client.clear_current_user()
                st.rerun()

            if "listener_started" not in st.session_state:
                adm_listener.start_list()
                st.session_state["listener_started"] = True

            page = st.sidebar.radio(
                "Перейти к странице",
                ["Магазин", "Библиотека", "Игры", "Добавить игру"],
            )

            if page == "Магазин":
                show_store_page()

            elif page == "Библиотека":
                show_library_page()
            elif page == "Игры":
                show_search_games_page()
            elif page == "Добавить игру":
                show_add_game_page()

        else:
            if st.sidebar.button("Выйти"):
                st.session_state["authenticated"] = False
                st.session_state["admin"] = False
                st.session_state["user"] = pd.DataFrame()
                redis_client.clear_current_user()
                st.rerun()
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

user = redis_client.load_current_user()
if user is None or user.empty:
    st.session_state.user = pd.DataFrame(
        columns = ["user_id", "nickname", "email", "money"]
    )
else:
    st.session_state.user = user

#if "user" not in st.session_state:
#    st.session_state.user = pd.DataFrame(
#        columns = ["user_id", "nickname", "email", "money"]
#    )

if __name__ == "__main__":
    main()

def exit_handler():
    redis_client.clear_current_user()
    redis_client.clear_users()

atexit.register(exit_handler)