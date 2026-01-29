# API Cadastro de Usuários

Este é um projeto de API REST desenvolvido em Python com Flask, usando SQLite como banco de dados.
O projeto permite criar, listar, atualizar e remover usuários, sendo totalmente testável via Postman.

---

## Funcionalidades

- **GET /usuarios**: Lista todos os usuários cadastrados
- **POST /usuarios**: Cria um novo usuário (necessário enviar JSON com 'nome' e 'email')
- **PUT /usuarios/<id>**: Atualiza um usuário existente pelo ID
- **DELETE /usuarios/<id>**: Remove um usuário pelo ID

  ---

  ## Tecnologias utilizadas

  - Puthon 3.14
  - Flask
  - SQLite
  - Git/GitHub para versionamento
  - Postman para testes

    ---

    ## Estrutura do projeto

    api-cadastro-python/
    |----app.py         # Arquivo principal que inicia a API
    |----routes.py      # Contém todas as rotas (endpoints)
    |----database.py    # Configuração e manipulação do banco SQLite
    |----venv           # Ambiente virtual Python

    ---

    ## Como rodar o projeto

    1. Clone o repositório:
       '''bash
       git clone https://github.com/stellitaalbernaz/api-cadastro-python.git
