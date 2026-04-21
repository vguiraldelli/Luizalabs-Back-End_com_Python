import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("Fatiamento de Strings\n".center(90, "=") + "\n")

texto = "Testando fatiamento de Strings" # 35 caracteres

print(texto[0:8]) # Testando
print(texto[9:19]) # fatiamento
print(texto[20:22]) # de
print(texto[23:30]) # Strings
print(texto[:8]) # Testando
print(texto[9:]) # fatiamento de Strings
print(texto[:]) # Testando fatiamento de Strings
print(texto[::-1]) # sgnirtS ed otnemaitaf otnatseT