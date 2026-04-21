import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Repetição For:")
print("=" * 60 + "\n")

texto = input("Digite um texto: ")
VOGAIS = "AEIOUaeiou"
CONSOANTES = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

vogais = 0
consoantes = 0

# Contagem de vogais e consoantes
for letra in texto:
    if letra in VOGAIS:
        vogais += 1
    elif letra in CONSOANTES:
        consoantes += 1
else:
    print("Fim da repetição!")

print(f"\nVogais: {vogais}")
print(f"Consoantes: {consoantes}")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)
