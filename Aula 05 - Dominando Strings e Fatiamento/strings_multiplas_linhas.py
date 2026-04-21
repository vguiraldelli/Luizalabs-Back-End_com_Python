import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("Strings de Múltiplas Linhas\n".center(90, "=") + "\n")

texto = """
Este é um texto
de múltiplas
linhas.
"""

print(texto)


menu = """
================================== MENU ==================================
1 - Cadastrar
2 - Listar
3 - Sair
==========================================================================
"""

print(menu)