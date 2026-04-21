import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Métodos de Classe e Estáticos ".center(50, "=") + "\n")

class Calculadora:
    # Método de classe (cls)
    @classmethod
    def somar(cls, a, b):
        return a + b

    # Método estático (não recebe cls nem self)
    @staticmethod
    def multiplicar(a, b):
        return a * b

# Chamando métodos
print(f"Soma: {Calculadora.somar(10, 5)}")
print(f"Multiplicação: {Calculadora.multiplicar(10, 5)}")

# Quando utilizar:
# Método de classe: quando precisa acessar ou modificar variáveis de classe
# Método estático: quando não precisa acessar nem modificar variáveis de classe nem de instância