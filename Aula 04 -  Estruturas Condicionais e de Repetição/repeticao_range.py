import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Range:")
print("=" * 60 + "\n")

for i in range(10):
    print(i, end=" ")

print("\n\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)