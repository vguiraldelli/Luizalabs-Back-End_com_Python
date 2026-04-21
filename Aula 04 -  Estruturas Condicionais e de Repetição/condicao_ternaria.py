import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Condição Ternária:")
print("=" * 60 + "\n")

idade = int(input("Digite sua idade: "))

status = "maior" if idade >= 18 else "menor"

print(f"Você é {status} de idade.")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)