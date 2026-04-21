import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Operadores de Comparação:")
print("=" * 60 + "\n")

numero1 = 10
numero2 = 3

print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Igualdade: {numero1 == numero2}")
print(f"Desigualdade: {numero1 != numero2}")
print(f"Maior que: {numero1 > numero2}")
print(f"Menor que: {numero1 < numero2}")
print(f"Maior ou igual a: {numero1 >= numero2}")
print(f"Menor ou igual a: {numero1 <= numero2}")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)