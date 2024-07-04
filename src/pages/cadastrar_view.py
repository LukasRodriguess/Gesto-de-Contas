import streamlit as st
import src.models.Conta_modelo as Conta
from src.controllers.cadastro_controlador import *
from src.db.supabase import exibir_emails, exibir_tags, cadastrar_site

#Todo o st.columns é unica e exclusivamente visual
col1, col2, col3, col4, col5 = st.columns([1,1,2,0.5,0.5])
col3.title("Cadastrar Sites")
 
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,0.6])
habilitar_adicao = col5.checkbox("Tag/Email") #CheckBox que habilita adicionar novas Tags

with st.container(border=True):

    col1, col2 = st.columns(2)

    nome_site = col1.text_input("Nome_site", placeholder="Nome do Site *", label_visibility='collapsed', disabled=habilitar_adicao)
    if nome_site: validar_nome(nome_site)
    url_site = col2.text_input("url_site", placeholder="URL do Site *", label_visibility='collapsed', disabled=habilitar_adicao)
    if url_site: validar_url(url_site)
    senha_cadastrada = col1.text_input("senha_cadastrada", placeholder="Senha Cadastrada *", label_visibility='collapsed', type='password', disabled=habilitar_adicao)
    if senha_cadastrada: validar_senha(senha_cadastrada)
    email_cadastrado = col1.selectbox("email_cadastrado Site", exibir_emails(), placeholder="Email Cadastrado *",  index=None, label_visibility='collapsed', disabled=habilitar_adicao)
    tags_site = col2.multiselect("Tags", exibir_tags(), placeholder="Tags do Site *", label_visibility='collapsed', disabled= habilitar_adicao)
    
    #Variavel boleana que define os campos obrigatorios
    campos_validos = ( nome_site and url_site and email_cadastrado and senha_cadastrada and tags_site)

    confirmacao_cadastro = st.button('Cadastrar Site', use_container_width=True, type='primary', disabled=habilitar_adicao or not campos_validos)
    if confirmacao_cadastro:
        Conta.nome = nome_site
        Conta.url_site = url_site
        Conta.email_cadastrado = email_cadastrado
        Conta.senha_cadastrada = senha_cadastrada
        Conta.tags_site = tags_site

        cadastrar_site(Conta)

if habilitar_adicao:
    with st.form("form_Adicionar_tag_email",clear_on_submit=True):
        col1, col2 = st.columns(2)

        nova_tag = col1.text_input("nova_tag", placeholder="Uma nova TAG", label_visibility="collapsed").upper()
        novo_email = col2.text_input("novo_email", placeholder="Um novo EMAIL", label_visibility="collapsed")
        
        #TODO: Passar as informações para o Controlador 
        if nova_tag:
            #adicionar_nova_tag(nova_tag) 
            validar_tags(nova_tag)
        if novo_email:
            #adicionar_novo_email(novo_email)
            validar_email(novo_email)


        st.form_submit_button("Confirmar", use_container_width=True, type='primary')


from src.db.supabase import exibir_dados_tabela

st.title("Tabela")
exibir_dados_tabela()