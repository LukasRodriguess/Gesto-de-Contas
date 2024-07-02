## Documentação do Projeto: Gerenciador de Contas de Sites (em Desenvolvimento)

**Este documento descreve a estrutura, funcionalidades e progresso atual do projeto "Gerenciador de Contas de Sites", desenvolvido com Streamlit e Supabase.**

**Observação Importante:** Este projeto está em desenvolvimento ativo. Muitas funcionalidades, incluindo validações no controlador, ainda não foram implementadas. 

### 1. Objetivo

O objetivo deste projeto é criar uma aplicação web simples e intuitiva para gerenciar contas de sites. A aplicação permite:

* Cadastrar novos sites com informações relevantes (nome, URL, email, senha, tags).
* Visualizar os sites cadastrados em uma tabela interativa. 
* (Em desenvolvimento) Editar e excluir sites existentes.

### 2. Tecnologias Utilizadas

* **Streamlit:** Framework Python para desenvolvimento rápido de aplicações web.
* **Supabase:** Plataforma de banco de dados como serviço (DBaaS) com backend PostgreSQL e funcionalidades adicionais.
* **Pandas:**  Biblioteca Python para manipulação e análise de dados.
* **Python:** Linguagem de programação principal.

### 3. Estrutura do Projeto

```
sites_management/
├── src/
│   ├── 0 - docs/    
│   │   └── documentação.md   
│   ├── controllers/    
│   │   └── cadastro_controlador.py   
│   ├── db/    
│   │   └── supabase.py   
│   ├── models/    
│   │   └── Conta_modelo.py   
│   ├── pages/    
│   │   ├── sobre_view.py   
│   │   ├── exibir.py   
│   │   └── cadastrar_view.py              
├── requirements.txt
├── app.py.txt
└── README.md     
```

**Descrição dos Arquivos:**

- **`app.py`:** Arquivo principal do Streamlit, define a estrutura básica da aplicação, como barra lateral, navegação e layout.
- **`src/`:** Diretório que contém o código-fonte do projeto.
   - **`controllers/`:** Lógica de controle da aplicação, gerencia as interações entre a interface do usuário (views) e o banco de dados (models).
      - **`cadastro_controlador.py`:** Gerencia o processo de cadastro de novas contas de sites. **(Em desenvolvimento - Validações pendentes)**
   - **`db/`:**  Código relacionado ao acesso e interação com o banco de dados Supabase.
      - **`supabase.py`:** Define funções para conexão com o Supabase, cadastro, consulta e manipulação de dados.
   - **`models/`:**  Definição da estrutura de dados (classes e modelos).
      - **`Conta_modelo.py`:** Define a classe `Conta` que representa uma conta de site.
   - **`pages/`:**  Páginas ou telas da aplicação Streamlit.
      - **`cadastrar_view.py`:**  Contém a interface do usuário para cadastro de novas contas.
      - **`exibir.py`:**  Exibe os sites cadastrados em uma tabela interativa.
      - **`sobre_view.py`:**  Página "Sobre" com informações sobre o projeto.
- **`requirements.txt`:** Lista as dependências do projeto.
- **`README.md`:**  Arquivo principal de documentação (este arquivo).

### 4. Funcionalidades Implementadas

* **Interface de Cadastro de Sites:** Formulário para inserir os dados da conta.
* **Exibição em Tabela:**  Listagem de sites cadastrados em uma tabela interativa com informações básicas (nome, URL, email, senha, tags).
* **Conexão com o Supabase:**  Integração com o banco de dados Supabase para armazenar as contas.
* **Geração de Logotipo (Usando `logo.dev`):**  Exibe o logotipo do site na tabela, recuperado dinamicamente usando a API do `logo.dev`. 

### 5. Funcionalidades em Desenvolvimento

* **Validações no Controlador:**
    - Verificar se os campos obrigatórios foram preenchidos corretamente.
    - Validar o formato do email.
    - Verificar a força da senha e aplicar Hash nela.
    - Tratar erros de forma mais robusta e amigável ao usuário. 
* **Edição de Contas:** Permitir que os usuários editem as informações das contas de sites existentes.
* **Exclusão de Contas:** Implementar a funcionalidade de excluir contas de sites. 
* **Busca e Filtragem:** Permitir que os usuários busquem e filtrem os sites cadastrados por diferentes critérios. 

### 6. Próximos Passos

- Implementar as validações no controlador `cadastro_controlador.py`.
- Criar as funcionalidades de edição e exclusão de contas de sites.
- Implementar recursos de busca e filtragem na tabela de exibição.
- Melhorar a interface do usuário e a experiência geral da aplicação.
- Adicionar Docker e FastApi ao projeto 

### 7. Observações

- As credenciais do Supabase (URL e chave) devem ser armazenadas de forma segura em variáveis de ambiente (.env) para não serem expostas publicamente.
- O uso da API `logo.dev` para gerar logotipos está sujeito aos termos de uso e disponibilidade da plataforma.
- A documentação será atualizada conforme o projeto evoluir. 


