import streamlit as st
from src.db.supabase import exibir_dados_tabela

st.title("Tabela")
exibir_dados_tabela()