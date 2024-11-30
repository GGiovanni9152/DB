import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
from st_clickable_images import clickable_images
from streamlit_modal import Modal
import repositories.games
import base64

detail = st.session_state.current_game

close = st.button(":red[Закрыть]")

title = repositories.games.get_game_name(int(detail['game_id']))
disc = detail['description'].item()
rating = detail['rating'].item()
version = detail['version'].item()
date = detail['release_date'].item()
pic = detail['picture_code'].item()
dev = detail['name'].item()

st.title(title)
st.image(pic, use_container_width=True, caption="Обложка игры")

st.subheader("Описание")
st.write(disc)

st.subheader("Детали игры")
col1, col2 = st.columns(2)

with col1:
    st.write(f"**Рейтинг:** {rating} ⭐")
    st.write(f"**Дата релиза:** {date}")

with col2:
    st.write(f"**Разработчик:** 👩‍💻 {dev}")
    st.write(f"**Версия:** {version}")

if (close):
    st.switch_page('main.py')

    