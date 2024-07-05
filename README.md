# Gerenciador de Contas em Sites (em Desenvolvimento)

[![Em desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)](https://github.com/seu-usuario/sites_management)


## Tecnologias que estarão no projeto👇🏻
[![My Skills](https://skillicons.dev/icons?i=django,python,supabase,aws,docker)](https://skillicons.dev)

Este projeto em desenvolvimento visa criar uma aplicação web para gerenciar contas de sites de forma simples e intuitiva. A aplicação permite cadastrar, visualizar e, futuramente, editar e excluir contas.

**Funcionalidades Atuais:**

- Cadastro de novos sites (nome, URL, email, senha, tags).
- Exibição em tabela interativa com informações das contas e logotipos.
- Integração com o banco de dados Supabase para armazenamento.
- Geração dinâmica de logotipos usando a API do `logo.dev`.

**Funcionalidades Planejadas:**

- Validações robustas no lado do servidor (backend).
- Edição e exclusão de contas de sites existentes.
- Recursos de busca e filtragem de contas.
- Implementação de uma API RESTful usando FastAPI para maior flexibilidade e escalabilidade.
- Conteinerização com Docker para facilitar a implantação e garantir a consistência entre ambientes.

**Tecnologias Utilizadas:**

- **Frontend:** Streamlit
- **Backend (em desenvolvimento):** FastAPI
- **Banco de Dados:** Supabase (PostgreSQL)
- **Geração de Logotipos:** API do `logo.dev`
- **Conteinerização (planejada):** Docker

**Como Executar o Projeto (Versão Atual):**

1. **Clone o repositório:** `git clone https://github.com/seu-usuario/sites_management.git`
2. **Crie um arquivo `.env` na raiz do projeto** e defina as variáveis de ambiente do Supabase:

   ```
   URL_SUPABASE=sua_url_supabase
   KEY_SUPABASE=sua_chave_supabase
   ```

3. **Instale as dependências:** `pip install -r requirements.txt`
4. **Execute o aplicativo Streamlit:** `streamlit run app.py`

**Contribuições:**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou compartilhar ideias para o desenvolvimento do projeto.

**Aviso:**

Este projeto está em fase inicial de desenvolvimento. A estrutura, as funcionalidades e a documentação estão sujeitas a alterações.


**Próximos Passos:**

- Implementar a API RESTful com FastAPI.
- Migrar a lógica de cadastro e gerenciamento de contas para o backend FastAPI.
- Criar endpoints da API para as funcionalidades existentes e planejadas.
- Dockerizar a aplicação para facilitar a implantação.

---

**Nota:** Substitua `seu-usuario` e `sites_management` pelos seus dados reais do GitHub. 
