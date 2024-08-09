import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Acao'
    },
    {
        'id': 2,
        'name': 'Comedia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_genres():
    st.write('Lista de Generos')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        enableSorting=True,
        key='genres_grid',
        height=200,
    )

    st.title('Cadastrar Novo Genero')
    name = st.text_input('Nome do Genero')
    if st.button('Cadastrar'):
        st.success(f'Genero "{name}" Cadastrado com sucesso')
