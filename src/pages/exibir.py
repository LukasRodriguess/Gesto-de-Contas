""" DocString
# utilizando essa pagina para teste enquanto desenvolvo ↓

# st.warning('This is a warning', icon="⚠️")
# st.info('This is a purely informational message', icon="ℹ️")
# e = RuntimeError('This is an exception of type RuntimeError')
# st.exception(e)

# "https://api.domainsdb.info/v1/domains/tld/{tld}"
# conferir melhor como utilizar para aplicar na função validar_url
    """


import streamlit as st
from src.controllers.cadastro_controlador import validar_nome

# Exemplo de uso

nome = st.text_input("nome", label_visibility='collapsed', placeholder="Digite")

validar_campo = validar_nome(nome)


confirmar = st.button("Confirmação", disabled=not validar_campo)

if confirmar:
    st.write(validar_nome(nome))
