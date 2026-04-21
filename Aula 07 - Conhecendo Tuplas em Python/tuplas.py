import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho 
print(" Tuplas em Python \n".center(50, "=") + "\n")

# Criando uma tupla
coordenadas = (10.0, 20.0)
print(f"Coordenadas: {coordenadas}")
print(f"Tipo da variável: {type(coordenadas)}\n")

# Acessando elementos
print(f"Primeira coordenada: {coordenadas[0]}")
print(f"Segunda coordenada: {coordenadas[1]}\n")

# Tuplas são imutáveis
# coordenadas[0] = 15.0  # Isso geraria um erro

# Desempacotamento de tuplas
x, y = coordenadas
print(f"Coordenada X: {x}")
print(f"Coordenada Y: {y}\n")

# Tuplas com diferentes tipos de dados
pessoa = ("Ana", 25, 1.68, True)
print(f"Pessoa: {pessoa}")
print(f"Nome: {pessoa[0]}")
print(f"Idade: {pessoa[1]}")
print(f"Altura: {pessoa[2]}")
print(f"É estudante? {pessoa[3]}\n")

# Contando elementos
print(f"Quantidade de elementos na tupla: {len(pessoa)}\n")

# Verificando se um elemento existe na tupla
print(f"A idade 25 está na tupla? {25 in pessoa}\n")

# Iterando sobre a tupla
print("Iterando sobre a tupla:")
for item in pessoa:
    print(f"- {item}")