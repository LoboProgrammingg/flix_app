import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione Uma opcao',
        ['Inicio', 'Generos', 'Atores/Atrizes', 'Filmes', 'Avaliacoes']
    )

    if menu_option == 'Inicio':
        st.write('Inicio')

    if menu_option == 'Generos':
        show_genres()

    if menu_option == 'Atores/Atrizes':
        show_actors()

    if menu_option == 'Filmes':
        show_movies()

    if menu_option == 'Avaliacoes':
        show_reviews()

if __name__ == '__main__':
    main()
