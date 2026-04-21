import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("\nInterpolação de Strings\n".center(90, "=") + "\n")

nome = "Victor Guiraldelli"
idade = 35
profissao = "Analista de Sistemas"

dicionario = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao
}

# f-string
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}")

# Método format()
print("Nome: {}, Idade: {}, Profissão: {}".format(nome, idade, profissao))

# Método format() com índices
print("Nome: {2}, Idade: {1}, Profissão: {0}".format(profissao, idade, nome))

# Método format() com dicionário
print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}".format(**dicionario))

# Método format() com dicionário e índices
print("Nome: {0[nome]}, Idade: {0[idade]}, Profissão: {0[profissao]}".format(dicionario))

# Método % (antigo)
print("Nome: %s, Idade: %d, Profissão: %s" % (nome, idade, profissao))

