import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print(" Métodos da Classe List \n".center(50, "=") + "\n")

# Criando uma lista
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
print(f"Lista de produtos: {produtos}")
print(f"Tipo da variável: {type(produtos)}\n")

# Adicionando elementos
produtos.append("Headset")
print(f"Lista após adicionar 'Headset': {produtos}")

produtos.insert(1, "Microfone")
print(f"Lista após adicionar 'Microfone' no índice 1: {produtos}")

# Removendo elementos
produtos.remove("Teclado")
print(f"Lista após remover 'Teclado': {produtos}")

produtos.pop()
print(f"Lista após remover o último elemento: {produtos}")

# Ordenando a lista
produtos.sort()
print(f"Lista ordenada: {produtos}")

# Invertendo a ordem da lista
produtos.reverse()
print(f"Lista invertida: {produtos}")

# Verificando se um elemento existe na lista
print(f"O 'Mouse' está na lista? {'Mouse' in produtos}")

# Contando elementos
print(f"Quantidade de produtos na lista: {len(produtos)}")

# Limpando a lista
produtos.clear()
print(f"Lista após limpar: {produtos}")
