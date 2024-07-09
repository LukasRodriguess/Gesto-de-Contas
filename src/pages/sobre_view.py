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
###### [![Em desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)](https://github.com/seu-usuario/sites_management) - [![My Skills](https://skillicons.dev/icons?i=django,python,supabase,aws,docker)](https://skillicons.dev) 👈🏻 Tecnologias pensadas para o projeto
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

--------------------------------------------------------------------------------
# Topicos de Melhorias gerias ↓
1.  Modularização e Reutilização de Código:
      - **Funções e validações**: estudar a possbilidade de transformar o controlador e suas funções em uma classe validadora
      - **Classe modelo**: Adicionar os métodos atualizar_dados e excluir_conta.

2. Tratamento de erros:
   - **Mensagens de Erro Personalizadas**: As mensagens de erro genéricas podem ser melhoradas para fornecer informações mais específicas ao usuário sobre o problema encontrado.
   - **Log de Erros**: Implemente um sistema de log para registrar erros e exceções, facilitando a depuração e manutenção do código.


3. Segurança:
   - **Hashing de Senhas:** Implementar hashing de senhas antes de armazenar no banco de dados. Utilizar bibliotecas como bcrypt ou Argon2
   - **Sanitização de Dados:** Sanitizar os dados de entrada do usuário para evitar ataques de injeção SQL ou XSS.

4. Interface do Usuário (UI):
   - **Feedback Visual:** Utilizar elementos visuais para fornecer feedback ao usuário sobre as ações realizadas, como animações, mensagens de sucesso ou erro.
   - **Layout Responsivo:** Me certificar de que a interface do usuário seja responsiva e se adapte a diferentes tamanhos de tela.

5. Banco de Dados:
   - **Relacionamentos:** Explorar a possibilidade de criar relacionamentos entre as tabelas do banco de dados (ex: uma tabela de usuários e uma tabela de sites associados a cada usuário).
   - **Índices:** Criar uma especie de índices nas colunas mais utilizadas nas consultas para otimizar o desempenho do banco de dados.

6. Testes:
   - **Testes Unitários:** Implementar testes unitários para garantir o funcionamento correto das funções e classes do meu projeto.

7. Documentação:
   - **Docstrings:** Adicionar docstrings às funções e classes para documentar o código.
   - **Readme:** Manter o arquivo README.md com informações sobre o projeto, como instalação, uso e contribuições.

8. API Logo.Dev:
   - **Cache:** Implementar um sistema de cache para armazenar as URLs das logos geradas pela API Logo.Dev, evitando chamadas repetidas à API.

9. Melhorias Específicas:
   - **Cadastro de Sites:**
      - **Campos Obrigatórios:** Utilizar o atributo `required` nos campos de formulário para garantir que os campos obrigatórios sejam preenchidos.
      - **Validação em Tempo Real:** Implementar validações em tempo real para os campos de formulário, fornecendo feedback imediato ao usuário sobre a validade dos dados.
   - **Exibição de Dados:**
      - **Paginação:** Implementar paginação para exibir grandes quantidades de dados de forma mais eficiente.
      - **Filtros e Ordenação:** Permitir que o usuário filtre e ordene os dados exibidos na tabela.

10. Ferramentas:
   - **Linters:** Utilizar linters como `pylint` ou `flake8` para identificar erros e problemas de estilo no código.
   - **Formatadores de Código:** Utilizar formatadores de código como `black` ou `yapf` para garantir a consistência do estilo de código.


    """
)