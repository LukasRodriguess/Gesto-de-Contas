

#utilizando essa pagina para teste enquanto desenvolvo ↓

import streamlit as st


# Exemplo de uso
url = st.text_input("Digite a URL:")
url = url.strip().lower()
st.write(url)


# st.warning('This is a warning', icon="⚠️")
# st.info('This is a purely informational message', icon="ℹ️")
# e = RuntimeError('This is an exception of type RuntimeError')
# st.exception(e)


# "https://api.domainsdb.info/v1/domains/tld/{tld}" conferir melhor como utilizar para aplicar na função validar_url
