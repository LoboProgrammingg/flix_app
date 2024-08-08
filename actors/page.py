import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id':1,
        'name': 'Leonardo DiCaprio'
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Stallone'
    },
]


def show_actors():
    st.write('Lista de Atores:')

    AgGrid(
        data = pd.DataFrame(actors),
        reload_data=True,
        enableSorting=True,
        key='actors_grid',
        height=200,
    )

    st.title('Cadastrar Novo Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" Cadastrado com sucesso')
