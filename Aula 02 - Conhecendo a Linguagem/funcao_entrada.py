import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()
from utils.tipos_de_dados import formatar_tipo

# Função de entrada
print("=" * 60)
print("Função de entrada:")
print("=" * 60 + "\n")

nome = input("Digite seu nome: ")
print(f"Tipo da variável nome: {formatar_tipo(type(nome))}\n")

idade = input("Digite sua idade: ")
print(f"Tipo da variável idade: {formatar_tipo(type(idade))}\n")

idade = int(idade)
print(f"Olá, {nome}! Você tem {idade} anos.", end="\nAté logo!\n")

print("\nfim","do","programa", sep="-", end="\n")