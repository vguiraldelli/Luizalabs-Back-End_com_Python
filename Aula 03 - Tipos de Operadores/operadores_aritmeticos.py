import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Operadores Aritméticos:")
print("=" * 60 + "\n")

numero1 = 10
numero2 = 3

print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Soma: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Divisão: {numero1 / numero2}")
print(f"Divisão inteira: {numero1 // numero2}")
print(f"Módulo: {numero1 % numero2}")
print(f"Exponenciação: {numero1 ** numero2}")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)