import pandas as pd
import streamlit as st
import repositories.game_detail
import repositories.games
from st_clickable_images import clickable_images
from streamlit_modal import Modal
import base64

if 'close' not in st.session_state:
    st.session_state.close = False

if "current_game" not in st.session_state:
    st.session_state.games_table = pd.DataFrame()

def close_callback():
    st.session_state.close = True

#@st.cache_data
def get_games() -> pd.DataFrame:
    print('Получение списка игр')
    games = pd.DataFrame(repositories.games.get_games())

    return games

@st.cache_data
def get_game_detail(game_id):
    detail = repositories.game_detail.get_game_detail(game_id)

    return detail

games = get_games()

def search(text_search):
    m1 = games["name"].str.contains(text_search, case= False)
    m2 = games["game_id"].astype(str).str.contains(text_search, case = False)

    return games[m1 | m2]

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"

def show_search_games_page():
    #print(get_games())

    games = get_games()

    text_search = st.text_input("Введите название или id игры", value = "")

    df_search = search(text_search)

    N_cards_per_row = 1

    if text_search:

        details = []

        for n_row, row in df_search.reset_index().iterrows():
            i = n_row % N_cards_per_row
            
            if i==0:
                st.write("---")
                cols = st.columns(N_cards_per_row, gap="large")
            
            with cols[n_row%N_cards_per_row]:
                st.markdown(f"**{row['name'].strip()}**")
                #st.markdown(f"*{row['price'].strip()}*")
                
                game_name = row['name']
                game_id = games['game_id'].loc[games["name"] == game_name]

                #print(games['game_id'].loc(games["name"] == game_name))
                detail = get_game_detail(game_id.item())

                details.append(detail)

                print(details)

                image = [detail['picture_code'].item()]

                clicked = clickable_images(
                    image,
                    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                    img_style={"margin": "5px", "height": "200px"},)

                if clicked != -1:
                    print(clicked)
                    st.session_state.current_game = details[n_row]
                    st.switch_page(page = "pages/current_game.py")

                #if clicked != -1:
                #    while (st.session_state.close != True):
                #        show_game_page(detail)
                #    st.session_state.close = False

#show_search_games_page()        



