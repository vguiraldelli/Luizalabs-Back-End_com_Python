import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Encapsulamento Público e Privado ".center(50, "=") + "\n")

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def sacar(self, delta):
        if delta > 0:
            self.__saldo -= delta
        print(f"Sacando... Saldo atual: {self.__saldo}")

    def depositar(self, delta):
        if delta > 0:
            self.__saldo += delta
        print(f"Depositando... Saldo atual: {self.__saldo}")

    def get_saldo(self):
        return self.__saldo

conta = ContaBancaria("João", 1000)
conta.depositar(100)
conta.sacar(50)
print(f"Saldo atual: {conta.get_saldo()} R$")
