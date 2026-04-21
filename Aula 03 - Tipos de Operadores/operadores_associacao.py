import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Operadores de Associação:")
print("=" * 60 + "\n")

curso = "Curso de Python"
frutas = ["laranja", "banana", "maçã"]
saques = [1500,300,500,200]

print(f"Curso: {curso}")
print(f"Frutas: {frutas}")
print(f"Saques: {saques}\n")

print(f"Curso em Saques: {curso in saques}")
print(f"Curso não está em Saques: {curso not in saques}")
print(f"Curso em Frutas: {curso in frutas}")
print(f"Curso não está em Frutas: {curso not in frutas}")
print(f"Laranja está em Frutas: {'laranja' in frutas}")
print(f"Mamão está em Frutas: {'mamão' in frutas}")
print(f"O valor 300 está em Saques: {300 in saques}")
print(f"O valor 300 não está em Saques: {300 not in saques}")
print(f"O valor 750 está em Saques: {750 in saques}")
print(f"O valor 750 não está em Saques: {750 not in saques}")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)