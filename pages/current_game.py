import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
from st_clickable_images import clickable_images
from streamlit_modal import Modal
import base64

def show_game_page(detail):
    close = st.button(":red[Закрыть]")
    st.image(detail['picture_code'].item())

    