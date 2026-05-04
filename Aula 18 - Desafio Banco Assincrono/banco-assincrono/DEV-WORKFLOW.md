
1. Criar e entrar na pasta

poetry new banco-assincrono
cd banco-assincrono

2. Adicionar as dependências principais
Use aspas em pacotes que possuem colchetes [] para o terminal não se confundir:

poetry add "fastapi" "uvicorn[standard]" "databases[aiosqlite,asyncpg]" "sqlalchemy" "pyjwt" "psycopg2-binary" "asyncpg"

3. Adicionar as dependências de desenvolvimento (Testes)
É uma boa prática colocar o pytest e pacotes de teste em um grupo separado:

poetry add pytest pytest-asyncio httpx --group dev

4. Configurar o Poetry para não criar pacotes (Importante!)
Como a sua aplicação é um serviço e não uma biblioteca que vai para o PyPI, você precisa avisar para o Poetry não criar aquela estrutura de projeto "instalável" (que exige README, etc.). 

Se você não fizer isso, vai tomar erro no deploy igual aconteceu antes.

Edite o arquivo pyproject.toml e adicione (ou descomente) a linha package-mode = false:

Ini, TOML
[tool.poetry]
name = "banco-assincrono"
version = "0.1.0"
description = ""
authors = ["Seu Nome <[EMAIL_ADDRESS]>"]
readme = "README.md"
requires-python = ">=3.13"
package-mode = false
dependencies = [
    # ... suas dependências
]

[tool.poetry.group.dev.dependencies]
pytest = "^9.0.3"
pytest-asyncio = "^0.24.2"
httpx = "^0.28.1"

5. Instalar tudo
poetry install

6. Criar a estrutura de pastas
Crie a pasta src e, dentro dela, o arquivo main.py:

Bash
mkdir src
touch src/main.py