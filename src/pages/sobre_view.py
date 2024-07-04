import streamlit as st
from src.controllers.cadastro_controlador import validar_tags

#testando possibilidades e funções↓

# opt = [".com", ".br"]

# col1, col2 = st.columns(2)
# name = col1.text_input("add")
# fim = col2.selectbox("", opt)
# if fim == ".com":
#     name = "www." + name + ".com"
# else:
#     name = "www." + name + ".com.br"

# img = f"https://img.logo.dev/{name}?token=pk_CAf7oMuYSwOwXAq2vzGCdg"
# st.image(img)
# st.divider()
# #---------------------------------------------------------------


# st.title("Festando Funções ↓")
# texto1 = st.text_input("",placeholder="add URL",label_visibility='collapsed')

# validar_tags(texto1)

st.header("Cadastro de Sites: Teste de Validações", divider='red')

st.markdown(
    """
# [![Em desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)](https://github.com/seu-usuario/sites_management)
##### O projeto está no inicio e tem muita coisa para ser feita principalmente a tratativa de erros e coisas do tipo, mas espero que vocês possam testar e me dar uns feedbacks 
---
**Objetivo:**

Este projeto demonstra a criação de uma aplicação web simples usando Streamlit para cadastrar sites. O foco principal é mostrar como implementar funções de validação de dados para campos.

**Funcionalidades:**

* **Formulário de Cadastro:** A aplicação apresenta um formulário para o usuário cadastrar um novo site, incluindo campos para:
    * Nome do Site
    * URL do Site
    * Tags do Site
    * Senha Cadastrada
    * Email Cadastrado
* **Validação de Dados:**  As funções de validação implementadas verificam se os dados inseridos pelo usuário estão no formato correto. Por exemplo:
    * **Nome:** O nome deve conter pelo menos uma letra, ter entre 4 e 15 caracteres e deve estar no formato "Primeira Letra Maiúscula". 
    * **URL:** A URL deve seguir o padrão "www.exemplo.com" ou "www.exemplo.com.br".
    * **Email:** O email deve ser válido e seguir o formato "nome@dominio.com". 
    * **Senha:** A senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
    * **Tags:** A tag deve conter apenas letras, ter entre 4 e 15 caracteres e não pode conter espaços.
* **Testar as Funções:** A aplicação inclui uma seção para testar as funções de validação individualmente, permitindo que o usuário experimente diferentes entradas e veja como as validações funcionam.

**Como Usar:**

1. **Experimente o formulário:** Use o formulário de cadastro para inserir dados de um site e clique em "Cadastrar Site". Observe as mensagens de validação exibidas caso os dados inseridos não estejam no formato correto.
2. **Teste as validações:**  Experimente inserir valores nos campos de teste e clique nos botões "Validar Nome", "Validar URL", etc. para testar como as funções de validação funcionam.

    """
)