import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Primeiro Programa com POO ".center(50, "=") + "\n")

# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos e sou do signo de {self.signo}.")

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# Criando objetos
pessoa1 = Pessoa("Ana", 25, "Leão")
pessoa2 = Pessoa("Bruno", 30, "Touro")

# Chamando métodos
pessoa1.apresentar()
pessoa2.apresentar()

# Imprimindo objetos
print(pessoa1)
print(pessoa2)
