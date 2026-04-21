import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Herança em POO ".center(50, "=") + "\n")

# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Objeto {self.nome} criado.")

    def __del__(self):
        print(f"Objeto {self.nome} destruído.")

# Criando uma classe
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        print(f"Objeto {self.nome} criado.")

    def __del__(self):
        print(f"Objeto {self.nome} destruído.")

# Criando objetos
funcionario1 = Funcionario("Ana", 25, 1000)
funcionario2 = Funcionario("Bruno", 30, 2000)

# Chamando métodos
funcionario1.apresentar()
funcionario2.apresentar()

# Imprimindo objetos
print(funcionario1)
print(funcionario2)
