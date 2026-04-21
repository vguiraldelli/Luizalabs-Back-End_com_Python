import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Conceitos de Classes e Objetos ".center(50, "=") + "\n")

# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando objetos
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Bruno", 30)

# Chamando métodos
pessoa1.apresentar()
pessoa2.apresentar()