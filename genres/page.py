import streamlit as st


genres = [
    {
        'id':1,
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

    st.table(genres)

    st.title('Cadastrar Novo Genero')
    name = st.text_input('Nome do Genero')
    if st.button('Cadastrar'):
        st.success(f'Genero "{name}" Cadastrado com sucesso')
