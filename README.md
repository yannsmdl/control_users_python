Esse projeto é uma aplicação desenvolvida para gerenciar usuários e fornecer serviços relacionados a esses usuários. Ele oferece operações básicas de CRUD (Criar, Ler, Atualizar, Excluir) para usuários, gerenciamento de sessões de usuário e as permissões de acesso aos serviços.

Funcionalidades

- CRUD de Users
- CRUD de Routes
- CRUD das Permissões dos usuário para acesso as rotas
- Login
- Sessão do Usuário



Tecnologias Utilizadas Linguagem de programação: Python 
Frameworks e bibliotecas: FastAPI
Banco de dados: PostgreSQL

Como Executar o Projeto

- Clone este repositório em sua máquina local.
- Crie o ambiente virtual usando o venv
- Instale as dependências necessárias utilizando pip freeze > requirements.txt.
- Crie o banco de dados e insira a sua conexão na variavel de ambiente DATABASE_URL.
- Crie uma chave privada para criptografar o token na vaviavel de ambiente SECRET_TOKEN.
- Execute as migrations com o comando alembic upgrade head
- Execute o projeto usando o comando python src/main.py
