import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Métodos Úteis de String:")
print("=" * 60 + "\n")

texto = "  Olá, Mundo!  "

# Maiúsculo, Minúsculo, Capitalizado e Title
print(f"Texto original: {texto}\n")
print(f"Texto em maiúsculo: {texto.upper()}")
print(f"Texto em minúsculo: {texto.lower()}")
print(f"Texto com primeira letra maiúscula: {texto.capitalize()}")
print(f"Texto com primeira letra de cada palavra maiúscula: {texto.title()}")

# Remove espaços no início e no fim
print(f"Texto sem espaços no início: {texto.lstrip()}")
print(f"Texto sem espaços no fim: {texto.rstrip()}")
print(f"Texto sem espaços no início e no fim: {texto.strip()}\n")

# Junções e Centralizações
lista_palavras = ["Olá", "Mundo", "Python"]
print(f"Lista de palavras: {lista_palavras}")
print(f"Junção de palavras: {' '.join(lista_palavras)}")
print(f"Texto centralizado: {texto.center(10, "#")}")