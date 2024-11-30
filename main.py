import streamlit as st
from pages.store import show_store_page
from pages.library import show_library_page
from pages.game_detail import show_search_games_page
from services.auth import Authotize

auth = Authotize()

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
            st.rerun()
        else:
            st.error("Неверная почта или пароль!")



def main():

    if not st.session_state["authenticated"]:
        login()
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

if __name__ == "__main__":
    main()