import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Operadores de Atribuição:")
print("=" * 60 + "\n")

numero = 10
print(f"Número: {numero}")
numero += 5
print(f"Número += 5: {numero}")
numero -= 3
print(f"Número -= 3: {numero}")
numero *= 2
print(f"Número *= 2: {numero}")
numero /= 4
print(f"Número /= 4: {numero}")
numero //= 2
print(f"Número //= 2: {numero}")
numero %= 3
print(f"Número %= 3: {numero}")
numero **= 2
print(f"Número **= 2: {numero}")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)
