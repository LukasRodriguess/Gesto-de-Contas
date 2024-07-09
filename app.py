import streamlit as st

st.set_page_config(page_title="Gerenciador de Contas", page_icon="apple", layout="wide", initial_sidebar_state='collapsed', menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })


#Navegador das paginas
paginas = st.navigation([
    # st.Page("src/pages/exibir.py", title="Pagina de testes", icon="🔥"),
    st.Page("src/pages/cadastrar_view.py", title="Cadastrar Conta"),
    st.Page("src/pages/sobre_view.py", title="Sobre o App")
])
paginas.run()
