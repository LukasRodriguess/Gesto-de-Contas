
import streamlit as st
import re

from db.supabase import cadastrar_site

# Função de validação
def validar_campos(nome_site, url_site, email_cadastrado, nickname, senha_cadastrada, tags):
    """Valida os campos do formulário.

    Args:
        nome_site (str): Nome do site.
        url_site (str): URL do site.
        email_cadastrado (str): Endereço de email.
        senha_cadastrada (str): Senha cadastrada.

    Returns:
        tuple: Uma tupla contendo um booleano indicando se a validação passou 
               e uma string de mensagem de erro, se houver.
    """

    # Validar nome do site
    if not nome_site:
        return st.error("Por favor, insira o nome do site.") 

    # Validar URL do site
    if url_site:
        if not re.match(r"^(https?://)?([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$", url_site):
           return st.error("Por favor, insira uma URL válida.")
    else:
        return st.error("Por favor, insira a URL do site.")

    # Validar email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_cadastrado):
        return st.error("Por favor, insira um endereço de email válido.")

    # Validar senha
    if not senha_cadastrada:
        return st.error("Por favor, insira a senha.")
    
    # Validar Tags do Site
    if not tags:
        return st.error("Por favor Adicionar alguma tag")

    cadastrar_site(nome_site, url_site, email_cadastrado, nickname, senha_cadastrada, tags)
