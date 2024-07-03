
import streamlit as st
import re
import requests

#---------------------------------------------------------------
#TODO: def validar_nome:
# * Não permitir espaços
# * Aceitar numeros mas não só numeros
# * Revisar a quantidade de caracteres permitidos, estou achando 15 muinto

def validar_nome(nome): 
    if not nome or len(nome) < 4: 
        return False, st.error("Nome inválido: limite Minimo de 4 caracteres.")
    if len(nome) > 15: 
        return False, st.error("Nome inválido: limite Maximo de 15 caracteres.")
    if not re.match(r'^[a-zA-Z\s\'-]+$', nome): 
        return False, st.error("Nome inválido: Apenas letras, espaços, hífens e apóstrofos.")
    return True, st.success("Ok")
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

#---------------------------------------------------------------

#TODO:def validar_senha
# * Revisar e consertar função inteira
# 
# def validar_senha(senha):
#     if len(senha) < 8:
#         return False,  st.error("Senha inválida: mínimo de 8 caracteres.")
#     if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', senha):
#         return False,  st.error("Senha inválida: deve conter letras maiúsculas, minúsculas, números e caracteres especiais.")
#     # Adicione a verificação de senhas fracas
#     return True, st.success("OK")

# #---------------------------------------------------------------
#TODO:def validar_tags
# * Revisar e consertar função inteira
# * Rever a nescessidade dela existir! 
# def validar_tags(tags):
#     if not tags:
#         return True, st.write("aa")  # Tags opcionais, não há erro
#     tags_limpas = [tag.strip().lower() for tag in tags.split(',')]  # Limpa e converte para minúsculas
#     if len(tags_limpas) > 5:  # Limite de 5 tags
#         return False, st.write("Número máximo de tags excedido.")
#     # Adicione a verificação de lista permitida
#     return True, st.write("bb")