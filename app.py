import streamlit as st


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione Uma opcao',
        ['Inicio', 'Generos', 'Atores/Atrizes', 'Filmes', 'Avaliacoes']
    )

    if menu_option == 'Inicio':
        st.write('Inicio')

    if menu_option == 'Generos':
        st.write('Lista de Generos')

    if menu_option == 'Atores/Atrizes':
        st.write('Lista de Atores/Atrizes')

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')

    if menu_option == 'Avaliacoes':
        st.write('Lista de Avaliacoes')

if __name__ == '__main__':
    main()
