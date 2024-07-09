import streamlit as st
import pandas as pd
from supabase import create_client, Client
import os
from dotenv import load_dotenv

from src.models.conta_modelo import Conta

load_dotenv()

# Substitua com suas informações da Supabase
URL_SUPABASE = os.getenv('URL_SUPABASE')
KEY_SUPABASE = os.getenv('KEY_SUPABASE')

supabase: Client = create_client(URL_SUPABASE, KEY_SUPABASE)

# Cadastrar o site ao banco de dados
def cadastrar_site(conta: Conta):
    try:
        supabase.table("contas").insert(
            {
                "nome_site": conta.nome_site,
                "url_site": conta.url_site,
                "email_cadastrado": conta.email_cadastrado,
                "senha_cadastrada": conta.senha_cadastrada,
                "tags": conta.tags_site,
            }
        ).execute()

        st.success("Site cadastrado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao cadastrar o site: {e}")
# -----------------------------------

# Referente a exibição da tabela
def exibir_dados_filtrados():
    data = supabase.table("contas").select("*").execute().data

    # Verificar se há dados para exibir
    if data:
        for row in data:
            st.divider()
            col1, col2, col3, col4 = st.columns(4)
            col1.markdown(f"Nome Site: [**{row['nome_site']}**]({row['url_site']})")
            col2.write(f"Email: {row['email_cadastrado']}")
            col3.write(f"Senha: {row['senha_cadastrada']}")
            col4.write(f"Tags: {', '.join(row['tags'])}")
    else:
        st.info("Nenhum site cadastrado ainda.")

def exibir_dados_tabela():
    data = supabase.table("contas").select("url_site", "email_cadastrado", "senha_cadastrada", "tags").execute().data
    df = pd.DataFrame(data)

    # Formatar 'url_site' para exibir www. e remover apenas https://
    df['url_site'] = df['url_site'].str.replace(r'https://', '', regex=True)
    df.insert(0, 'Logo', df['url_site'].apply(gerar_url_logo))

    st.data_editor(
        df,
        column_config={
            "Logo": st.column_config.ImageColumn("Logo", width="small"),
            "url_site": st.column_config.LinkColumn("Url", width='medium', disabled=True),
            "email_cadastrado": st.column_config.Column("Email", width='medium', disabled=True),
            "senha_cadastrada": st.column_config.Column("Senha", width='small', disabled=True),
            "tags": st.column_config.ListColumn("Tags do Site", width='large')
        },
        hide_index=True,
        num_rows='fixed'
    )
# -----------------------------------

# Referente as tags↓
def exibir_tags():
        data = supabase.table("tags").select('nome_tag').execute().data
        df = pd.DataFrame(data)
        return df

def adicionar_nova_tag(nova_tag):
    try:
          supabase.table('tags').insert({"nome_tag": nova_tag}).execute()
    except Exception as e:
         st.error(f"Error ao cadastrar nova tag: {e}")
# -----------------------------------

# Referente aos Emails
def exibir_emails():
     data = supabase.table("emails").select('email').execute().data
     df = pd.DataFrame(data)
     return df

def adicionar_novo_email(novo_email):
    try:
          supabase.table('emails').insert({"email": novo_email}).execute()
    except Exception as e:
         st.error(f"Error ao cadastrar novo EMAIL: {e}")

# -----------------------------------
# Api Logo.Dev ↓
def gerar_url_logo(url_site):
    return f"https://img.logo.dev/{url_site}?token=pk_CAf7oMuYSwOwXAq2vzGCdg"
