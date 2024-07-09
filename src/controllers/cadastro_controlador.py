import streamlit as st
import re
import requests
from src.db.supabase import adicionar_novo_email, adicionar_nova_tag

# icons = ⚠️ / 🚨 / 👍

# TODO: Observações Gerais  # [fixme]
# - Tratar melhor as saidas de erros de todas as funções para serem diretas e não genericas

# ---------------------------------------------------------------
def validar_nome(nome: str):
    """ Validação de nome """
    if not nome:
        return False

    # Remove espaços em branco no início e no fim
    nome = nome.strip()  

    # Ignora espaços em branco extras (mantém apenas 1 espaço entre as palavras)
    nome = " ".join(nome.split())

    # Verifica se o nome tem pelo menos uma letra e não só numero
    if not any(char.isalpha() for char in nome):
        st.toast(":orange[O nome deve conter pelo menos uma letra.]", icon="⚠️")
        return False

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
            st.toast(":orange[Nome inválido: O nome deve conter apenas letras, números, hífens e apóstrofos.]", icon="⚠️")
            return False
        
    # Verifica o comprimento do nome
    if len(nome_formatado) < 4 or len(nome_formatado) > 15:
        st.toast(":orange[Nome inválido: O nome deve ter de 4 há 15 caracteres.]", icon="⚠️")
        return False
    return True, nome_formatado
# ---------------------------------------------------------------

# TODO: Email: Correções e melhorias
# * procurar uma forma de validar os dominios_permitidos melhor, com api ou coisa do tipo!
def validar_email(email): #OK
    if not email:
        st.toast(":orange[O campo de email não pode estar vazio.]", icon="⚠️")
        return False

    # Verifica se o email segue o padrão de @ e .com
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        st.toast(":orange[Por favor, utilize um formato como 'nome@dominio.com'.]", icon="⚠️")
        return False

    # 3. Extrai o domínio do email
    partes = email.split('@')
    if len(partes) != 2:
        st.toast(":orange[Por favor, utilize um formato como 'nome@dominio.com'.]", icon="⚠️")
        return False
    dominio = partes[1]

    # 4. Verifica se o domínio está na lista permitida
    dominios_permitidos = ["gmail.com", "hotmail.com", "icloud.com", "outlook.com"]
    if dominio in dominios_permitidos:
        adicionar_novo_email(email)
        return True
    else:
        st.toast(":orange[Por favor, utilize um domínio como Gmail, Hotmail, iCloud ou Outlook.]", icon="⚠️")
        return False

#---------------------------------------------------------------
#TODO: URL: Correções e melhorias
# - Adicionar API para validar os TLD https://api.domainsdb.info/v1/domains/tld/{tld}
# - Adicionar um filtro para por as urls em lowercase
def validar_url(url): #OK
    if not url:
        st.toast(':orange[O campo URL não pode estar vazio.]', icon="⚠️")
        return False

    url = url.strip().lower()

    # 2. Adiciona "https://" se não estiver presente
    if not url.startswith("https://"):
        url = "https://" + url

    # 3. Adiciona "www." se "https://" estiver presente e "www." não
    if url.startswith("https://") and not url.startswith("https://www."):
        url = url[:8] + "www." + url[8:]

    # 4. Verifica se a URL termina com ".com" ou ".com.br"
    if not re.match(r'^https://www\.[a-zA-Z0-9.-]+\.(com|com\.br|io|gov\.br|org|net)$', url):
        st.toast(":orange[Por favor, utilize um formato como 'exemplo.com' ou 'exemplo.com.br']", icon="⚠️")
        return False
    # 5. (Opcional) Verifica se a URL existe
    try:
        response = requests.get(url)
        if response.status_code != 200:
            st.toast(":red-background[A URL não foi encontrada.]", icon="⚠️")
            return False
    except requests.exceptions.RequestException:
        st.toast(f":red-background[ERROR: A URL não existe.]", icon="🚨")
        return False

    # Se todas as verificações forem aprovadas, retorna True
    return True, url

#---------------------------------------------------------------
#TODO: Senha: Correções e melhorias
# - Adicionar HASH e criptografia as senhas 
def validar_senha(senha): #OK
    if len(senha) < 8:
        return False,  st.toast(':orange[Senha inválida: mínimo de 8 caracteres.]', icon="⚠️")
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', senha):
        return False,  st.toast(':orange[Senha inválida: deve conter letras maiúsculas, minúsculas, números e caracteres especiais.]', icon="⚠️")
    # Adicione a verificação de senhas fracas
    return True

# #---------------------------------------------------------------
def validar_tags(tag): #OK
    if not tag:
        return True

    tag = tag.strip().upper()

    if not re.match(r'^[A-Z]+$', tag):  # Verifica se a tag contém apenas letras
        st.toast(':orange[A tag deve conter apenas letras.]', icon="⚠️")
        return False

    if len(tag) < 4 or len(tag) > 15:
        st.toast(':orange[Deve ter entre 4 há 15 caracteres.]', icon="⚠️")
        return False

    if " " in tag:
        st.toast(':orange[A tag não pode conter espaços.]', icon="⚠️" )
        return False
    return True, adicionar_nova_tag(tag)
