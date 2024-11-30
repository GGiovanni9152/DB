"""
#Home = st.Page("main.py", title="Home", icon="🏠")
Store = st.Page("pages/store.py", title = "Магазин", icon = "🎈️")
Library = st.Page("pages/library.py", title= "Библиотека", icon = ":books:")
Games = st.Page("pages/game_detail.py", title = "Игры", icon = "🕹️")
Game = st.Page("pages/current_game.py", title = "Выбранная игра")

pg = st.navigation([Store, Library, Games, Game])
pg.run()

"""

#st.sidebar.title("Навигация")
    #nav = get_nav_from_toml(".streamlit/pages.toml")
    #pg = st.navigation(nav)
    #add_page_title(pg)
    #pg.run()
    #st.write("HOME")
    #st.switch_page(page = 'pages/store.py')

    