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
├── .gitignore
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


#TODO: Melhorias gerias ↓
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