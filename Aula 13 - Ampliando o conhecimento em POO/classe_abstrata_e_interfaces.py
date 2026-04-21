import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Classe Abstrata e Interfaces ".center(50, "=") + "\n")

# Quando utilizar:
# Classe abstrata: quando precisa definir um contrato que deve ser implementado por subclasses
# A subclasse é obrigada a implementar os métodos abstratos

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

class Carro(Veiculo):
    def ligar(self):
        return "Carro ligado"

    def desligar(self):
        return "Carro desligado"

carro = Carro()
carro.marca = "Toyota"
print(carro.marca)
print(carro.ligar())
print(carro.deslig())