
import streamlit as st
import re
import requests

from src.db.supabase import adicionar_novo_email

#TODO: Observações Gerais
# - Tratar melhor as saidas de erros de todas as funções para serem diretas e não genericas

#---------------------------------------------------------------
def validar_nome(nome): #OK
    if not nome:
        return False, ""

    nome = nome.strip()  # Remove espaços em branco no início e no fim

     # Verifica se o nome tem pelo menos uma letra
    if not any(char.isalpha() for char in nome):
        return False, st.error("Nome inválido: O nome deve conter pelo menos uma letra.")

    # Ignora espaços em branco extras (mantém apenas 1 espaço entre as palavras)
    nome = " ".join(nome.split())

    # Verifica se o nome está no formato correto (primeira letra de cada palavra em maiúscula)
    nome_formatado = ""
    primeira_letra = True
    for i, char in enumerate(nome):
        if char.isalpha() and primeira_letra:  # Se é letra e é a primeira da palavra
            nome_formatado += char.upper()  # Adiciona a primeira letra em maiúscula
            primeira_letra = False
        elif char.isspace():
            nome_formatado += char  # Adiciona espaço
            primeira_letra = True  # Próxima letra é a primeira de uma nova palavra
        elif char.isalnum() or char in "-'":
            nome_formatado += char.lower()  # Adiciona outros caracteres em minúscula
        else:
            return False, st.error("Nome inválido: O nome deve conter apenas letras, números, hífens e apóstrofos.")

    # Verifica o comprimento do nome
    if len(nome_formatado) < 4 or len(nome_formatado) > 15:
        return False, st.error("Nome inválido: O nome deve ter de 4 há 15 caracteres.")

    st.success(f"Nome válido: {nome_formatado}")
    return True, nome_formatado
#---------------------------------------------------------------

#TODO: def validar_email 
# * procurar uma forma de validar os dominios_permitidos melhor, com api ou coisa do tipo!
def validar_email(email): #OK
    if not email:
        st.error("O campo de email não pode estar vazio.")
        return False

    # Verifica se o email segue o padrão de @ e .com
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        st.error("O formato do email é inválido. Por favor, utilize um formato como 'nome@dominio.com'.")
        return False

    # 3. Extrai o domínio do email
    partes = email.split('@')
    if len(partes) != 2:
        st.error("O formato do email é inválido. Por favor, utilize um formato como 'nome@dominio.com'.")
        return False
    dominio = partes[1]

    # 4. Verifica se o domínio está na lista permitida
    dominios_permitidos = ["gmail.com", "hotmail.com", "icloud.com", "outlook.com"]
    if dominio in dominios_permitidos:
        adicionar_novo_email(email)
        st.success("Email válido!")
        return True
    else:
        st.error("O domínio do email não é permitido. Por favor, utilize um domínio como Gmail, Hotmail, iCloud ou Outlook.")
        return False

#---------------------------------------------------------------
def validar_url(url): #OK
    if not url:
        st.error("O campo URL não pode estar vazio.")
        return False

    # 2. Adiciona "https://" se não estiver presente
    if not url.startswith("https://"):
        url = "https://" + url

    # 3. Adiciona "www." se "https://" estiver presente e "www." não
    if url.startswith("https://") and not url.startswith("https://www."):
        url = url[:8] + "www." + url[8:]

    # 4. Verifica se a URL termina com ".com" ou ".com.br"
    if not re.match(r'^https://www\.[a-zA-Z0-9.-]+\.(com|com\.br)$', url):
        st.error("O formato da URL é inválido. Por favor, utilize um formato como 'https://www.exemplo.com' ou 'https://www.exemplo.com.br'.")
        return False

    # 5. (Opcional) Verifica se a URL existe
    try:
        response = requests.get(url)
        if response.status_code != 200:
            st.error("A URL não foi encontrada.")
            return False
    except requests.exceptions.RequestException:
        st.error(f"Erro: A URL não foi encontrada ou está fora do ar.")
        return False

    # Se todas as verificações forem aprovadas, retorna True
    st.success("URL válida! ")
    return True

#---------------------------------------------------------------
def validar_senha(senha): #OK
    if len(senha) < 8:
        return False,  st.error("Senha inválida: mínimo de 8 caracteres.")
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', senha):
        return False,  st.error("Senha inválida: deve conter letras maiúsculas, minúsculas, números e caracteres especiais.")
    # Adicione a verificação de senhas fracas
    return True, st.success("OK")

# #---------------------------------------------------------------
def validar_tags(tag): 
    if not tag:
        return True, ""  

    tag = tag.strip().upper()

    if not re.match(r'^[A-Z]+$', tag):  # Verifica se a tag contém apenas letras
        st.error("A tag deve conter apenas letras.")
        return False, st.write("kk")

    if len(tag) < 4 or len(tag) > 15:
        st.error("A tag deve ter entre 4 há 15 caracteres.")
        return False, ""

    if " " in tag:
        st.error("A tag não pode conter espaços.")
        return False, ""

    st.success(f"Tag válida: {tag}")
    return True, tag