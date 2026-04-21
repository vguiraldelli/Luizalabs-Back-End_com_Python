import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print(" Listas: Criação e Acesso aos Dados \n".center(50, "=") + "\n")

# Criando uma lista
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
print(f"Lista de produtos: {produtos}")
print(f"Tipo da variável: {type(produtos)}\n")

# Acessando elementos pelo índice
print("Acessando elementos pelo índice:")
print(f"Primeiro produto (índice 0): {produtos[0]}")
print(f"Terceiro produto (índice 2): {produtos[2]}")
print(f"Último produto (índice -1): {produtos[-1]}\n")

# Acessando um intervalo de elementos (fatiamento)
print("Acessando um intervalo de elementos (fatiamento):")
print(f"Do segundo ao quarto produto: {produtos[1:4]}")
print(f"Do terceiro produto em diante: {produtos[2:]}")
print(f"Até o terceiro produto: {produtos[:3]}\n")

# Verificando o tamanho da lista
print(f"Quantidade de produtos na lista: {len(produtos)}\n")

# Iterando sobre a lista
print("Iterando sobre a lista:")
for produto in produtos:
    print(f"- {produto}")

# Matriz (lista de listas)
print("\nMatriz (lista de listas):\n")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatriz: {matriz}")
print(f"Elemento da primeira linha e segunda coluna: {matriz[0][1]}")

# Iterando sobre a lista com enumerate
print("\nIterando sobre a lista com enumerate:")
carros = ["Fusca", "Gol", "Palio", "Uno"]
print(f"Lista de carros: {carros}")

for indice, carro in enumerate(carros):
    print(f"Índice {indice}: {carro}")

# Separando números pares e ímpares
print("\nSeparando números pares e ímpares:\n")

numeros = [1, 30, 2, 25, 10, 50]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Lista de números: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")

# Ordenando a lista
numeros.sort()
print(f"Lista de números ordenada: {numeros}")

# Invertendo a ordem da lista
numeros.reverse()
print(f"Lista de números invertida: {numeros}")

# Verificando se um elemento existe na lista
print(f"O número 25 está na lista? {25 in numeros}")

# Contando elementos
print(f"Quantidade de números na lista: {len(numeros)}")

# Limpando a lista
numeros.clear()
print(f"Lista de números após limpar: {numeros}")