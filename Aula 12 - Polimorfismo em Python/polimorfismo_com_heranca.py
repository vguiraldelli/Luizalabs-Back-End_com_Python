import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Polimorfismo com Herança ".center(50, "=") + "\n")

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError("Subclasse deve implementar este método")

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Pato(Animal):
    def falar(self):
        return "Quack!"

# Criando objetos
cachorro = Cachorro("Rex")
gato = Gato("Mimi")
pato = Pato("Donald")

# Função falar
def falar(animal):
    print(f"{animal.nome} diz: {animal.falar()}")

# Chamando métodos
falar(cachorro)
falar(gato)
falar(pato)
