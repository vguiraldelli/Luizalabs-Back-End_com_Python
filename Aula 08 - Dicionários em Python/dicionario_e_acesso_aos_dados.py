import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho 
print(" Dicionários em Python \n".center(50, "=") + "\n")

# Criando um dicionário
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "altura": 1.68,
    "is_estudante": True
}
print(f"Pessoa: {pessoa}")
print(f"Tipo da variável: {type(pessoa)}\n")

# Acessando elementos
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Altura: {pessoa['altura']}")
print(f"É estudante? {pessoa['is_estudante']}\n")

# Adicionando elementos
pessoa["cidade"] = "São Paulo"
print(f"Pessoa após adicionar cidade: {pessoa}")

# Modificando elementos
pessoa["idade"] = 26
print(f"Pessoa após modificar idade: {pessoa}\n")

# Removendo elementos
del pessoa["altura"]
print(f"Pessoa após remover altura: {pessoa}")

# Verificando se uma chave existe
print(f"A chave 'nome' existe? {'nome' in pessoa}")
print(f"A chave 'peso' existe? {'peso' in pessoa}\n")

# Obtendo o tamanho do dicionário
print(f"Quantidade de elementos no dicionário: {len(pessoa)}\n")

# Iterando sobre o dicionário
print("Iterando sobre o dicionário:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")