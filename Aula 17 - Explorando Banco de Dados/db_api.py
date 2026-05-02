import sqlite3
from sqlite3 import Error
from pathlib import Path

# Definir o caminho do Banco de Dados
ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / "banco_de_dados.db"

# Criar conexão
conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()

# Configurar o cursor para retornar linhas como dicionários
cursor.row_factory = sqlite3.Row

# Executar comandos SQL
# cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)")    

# Criando tabela de clientes
def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL)")
    conexao.commit()

# Inserir dados na tabela
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Vanessa Guiraldelli", [EMAIL_ADDRESS]"))

# Inserindo dados na tabela de clientes
# dados = ("Maria Santos", "maria@gmail.com")
# cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)


# Inserindo dados na tabela de clientes - método recomendado
def inserir_cliente(conexao, cursor, nome: str, email: str):
    dados = (nome, email)
    try:
        cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
        conexao.commit()
    except Error as e:
        print(f"Falha ao inserir o cliente: {e}")
        conexao.rollback()

# Inserindo múltiplos dados na tabela de clientes
def inserir_clientes(conexao, cursor, clientes: list[tuple]):
    try:
        cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)
        conexao.commit()
    except Error as e:
        print(f"Falha ao inserir os clientes: {e}")
        conexao.rollback()

# Atualizar dados na tabela
def atualizar_cliente(conexao, cursor, id: int, nome: str, email: str):
    dados = (nome, email, id)
    try:
        cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', dados)
        conexao.commit()
    except Error as e:
        print(f"Falha ao atualizar o cliente: {e}")
        conexao.rollback()

# Deletar dados da tabela
def deletar_cliente(conexao, cursor, id: int):
    try:
        cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
        conexao.commit()
    except Error as e:
        print(f"Falha ao deletar o cliente: {e}")
        conexao.rollback()
    

# Gravar as alterações
# conexao.commit()

# Consultar os dados
# cursor.execute("SELECT * FROM users")
# resultado = cursor.fetchone()
# print(resultado)

# Consultar um cliente pelo id
def listar_cliente(conexao, cursor, id: int):
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    resultado = cursor.fetchone()
    return resultado

# Listar todos os clientes
def listar_clientes(conexao, cursor):
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()
    for cliente in resultado:
        print(dict(cliente))


# def criar_conexao(db_file: str):
#     """
#     Cria uma conexão com o banco de dados SQLite
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(f"Conectado ao banco de dados: {conn.host}")
#     except Error as e:
#         print(e)
    
#     return conn


# Executando as funções
# criar_tabela(conexao, cursor)
# inserir_cliente(conexao, cursor, "Maria Santos", "maria@gmail.com")
# inserir_cliente(conexao, cursor, "João Silva", "maria@gmail.com")
# inserir_clientes(conexao, cursor, [("Maria Santos", "maria@gmail.com"), ("João Silva", "maria@gmail.com"), ("Vanessa Guiraldelli", "vanessa@gmail.com")])
# atualizar_cliente(conexao, cursor, 1, "Maria Santos Silva", "maria@gmail.com")
# deletar_cliente(conexao, cursor, 1)
print(dict(listar_cliente(conexao, cursor, 1)))
listar_clientes(conexao, cursor)
