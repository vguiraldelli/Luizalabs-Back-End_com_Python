import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Construtores e Destrutores ".center(50, "=") + "\n")

# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Objeto {self.nome} criado.")

    def __del__(self):
        print(f"Objeto {self.nome} destruído.")

# Criando objetos
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Bruno", 30)

# Chamando métodos
pessoa1.apresentar()
pessoa2.apresentar()

# Imprimindo objetos
print(pessoa1)
print(pessoa2)
