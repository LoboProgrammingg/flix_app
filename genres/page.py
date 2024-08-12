import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Generos')
        genres_dr = pd.json_normalize(genres)
        AgGrid(
            data=genres_dr,
            reload_data=True,
            enableSorting=True,
            key='genres_grid',
            height=200,
        )
    else:
        st.warning('Nenhum genero encontrado.')

    st.title('Cadastrar Novo Genero')
    name = st.text_input('Nome do Genero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(
            name=name,
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar um genero. Verifique os campos')
