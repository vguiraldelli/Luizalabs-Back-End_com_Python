import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Operadores Lógicos:")
print("=" * 60 + "\n")

variavel1 = 10
variavel2 = 3
variavel3 = 7

print(f"Variável 1: {variavel1}")
print(f"Variável 2: {variavel2}")
print(f"Variável 3: {variavel3}\n")

print(f"Variável 1 é maior ou igual à Variável 2 E à Variável 3: {variavel1 >= variavel2 and variavel1 >= variavel3}")
print(f"Variável 1 é maior ou igual à Variável 2 OU à Variável 3: {variavel1 >= variavel2 or variavel1 >= variavel3}")
print(f"Variável 1 NÃO é maior ou igual à Variável 2: {not (variavel1 >= variavel2)}\n")

print(f"Variável 2 é maior ou igual à Variável 1 E à Variável 3: {variavel2 >= variavel1 and variavel2 >= variavel3}")
print(f"Variável 2 é maior ou igual à Variável 1 OU à Variável 3: {variavel2 >= variavel1 or variavel2 >= variavel3}")
print(f"Variável 2 NÃO é maior ou igual à Variável 1: {not (variavel2 >= variavel1)}\n")

print(f"Variável 3 é maior ou igual à Variável 1 E à Variável 2: {variavel3 >= variavel1 and variavel3 >= variavel2}")
print(f"Variável 3 é maior ou igual à Variável 1 OU à Variável 2: {variavel3 >= variavel1 or variavel3 >= variavel2}")
print(f"Variável 3 NÃO é maior ou igual à Variável 1: {not (variavel3 >= variavel1)}\n")


print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)
