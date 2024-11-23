import streamlit as st
from pages.store import show_store_page
from pages.library import show_library_page

def main():
    st.sidebar.title("Навигация")
    page = st.sidebar.radio(
        "Перейти к странице",
        ["Магазин", "Библиотека"],
    )

    if page == "Магазин":
        show_store_page()

    elif page == "Библиотека":
        show_library_page()

if __name__ == "__main__":
    main()