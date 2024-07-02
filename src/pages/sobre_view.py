import streamlit as st

#testando possibilidades e funções↓

opt = [".com", ".br"]

col1, col2 = st.columns(2)
name = col1.text_input("add")
fim = col2.selectbox("", opt)
if fim == ".com":
    name = "www." + name + ".com"
else:
    name = "www." + name + ".com.br"


img = f"https://img.logo.dev/{name}?token=pk_CAf7oMuYSwOwXAq2vzGCdg"
st.image(img)
st.divider()


