import pandas as pd
from datetime import datetime
import streamlit as st
import services.addgame
from services.buy import BuyService
import repositories.games
import repositories.users
import repositories.addgame
import os

adder = services.addgame.GameAdder()

def show_add_game_page():
    st.title("Добавление игры")

    with st.form(key="add_game_form", clear_on_submit=True):
        name = st.text_input("Название игры")
        price = st.number_input("Цена", min_value=0.0, step=0.01)
        developer_id = st.text_input("ID разработчика")
        release_date = st.date_input("Дата релиза", value=datetime.now().date())
        version = st.text_input("Версия")
        description = st.text_area("Описание игры")
        picture = st.file_uploader("Загрузить изображение", type=["png", "jpg", "jpeg"])

        submitted = st.form_submit_button(label="Добавить игру")

        if submitted:
            if (not name or not developer_id or not release_date or not version or not description or not picture):
                st.error("Поля обязательны к заполению!")
            else:
                extension = picture.name.split(".")[-1]

                picture_name = f"{name.replace(' ', '_').lower()}.{extension}"
                picture_code = services.addgame.encode_image_to_base64(picture)

                save_path = "pictures/" + picture_name
                with open(save_path, "wb") as f:
                    f.write(picture.getbuffer())

                new_game = {
                "name": [name],
                "price": [price],
                "developer_id": [developer_id],
                "release_date": [release_date],
                "version": [version],
                "description": [description],
                "picture_name": [picture_name],
                "picture_code": [picture_code]
                }

                game = pd.DataFrame(new_game)

                adder.add_game(game)

                st.success(f"Игра '{name}' успешно добавлена!")