import streamlit as st


from src.db.supabase import cadastrar_site, adicionar_nova_tag, exibir_tags
import src.models.Conta_modelo as Conta

col1, col2, col3, col4, col5 = st.columns([1,1,2,0.5,0.5])
col3.title("Cadastrar Sites")

col1, col2, col3, col4, col5 = st.columns([1,1,1,1,0.6])
adicionar_tag = col5.checkbox("Add Tag")

with st.container(border=True):

    col1, col2 = st.columns(2)

    nome_site = col1.text_input("Nome_site", placeholder="Nome do Site *", label_visibility='collapsed', disabled=adicionar_tag)
    url_site = col2.text_input("url_site", placeholder="URL do Site *", label_visibility='collapsed', disabled=adicionar_tag)
    url_site = "www." + url_site
    email_cadastrado = col1.text_input("email_cadastrado Site", placeholder="Email Cadastrado *", label_visibility='collapsed', disabled=adicionar_tag)

    senha_cadastrada = col1.text_input("senha_cadastrada", placeholder="Senha Cadastrada *", label_visibility='collapsed', type='password', disabled=adicionar_tag)
    tags_site = col2.multiselect("Tags", exibir_tags(), placeholder="Tags do Site", label_visibility='collapsed', disabled= adicionar_tag)
    
    campos_validos = ( nome_site and url_site and email_cadastrado and senha_cadastrada and tags_site)

    

    if adicionar_tag:
        form_nova_tag = col2.form("adicionar nova tag", clear_on_submit=True, border=False)

        with form_nova_tag: 
            col1, col2 = st.columns([0.7,0.3])

            nova_tag = col1.text_input("Nova_tag", placeholder="Adicione uma nova tag", label_visibility="collapsed").upper()
            add_tag = col2.form_submit_button("Adicionar", type='primary')

            if nova_tag:
                adicionar_nova_tag(nova_tag)

    confirmacao_cadastro = st.button('Cadastrar Site', use_container_width=True, type='primary', disabled=adicionar_tag or not campos_validos)
    if confirmacao_cadastro:
        #TODO: Melhorar esse codigo
        Conta.nome = nome_site
        Conta.url_site = url_site
        Conta.email_cadastrado = email_cadastrado
        Conta.senha_cadastrada = senha_cadastrada
        Conta.tags_site = tags_site

        cadastrar_site(Conta)


