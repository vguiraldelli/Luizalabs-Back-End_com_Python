import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

from historico import Historico

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        excedeu_saldo = valor > self._saldo
        if excedeu_saldo:
            print("\n### Operação falhou! Você não tem saldo suficiente.")
        elif valor <= 0:
            print("\n### Operação falhou! O valor informado é inválido.")
        else:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        return False
        
    
    def depositar(self, valor):
        if valor <= 0:
            print("\n### Operação falhou! O valor informado é inválido.")
        else:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        return False


#########################################################################

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1000, limite_saques=5):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        excedeu_limite = valor > self._limite
        excedeu_saques = len(self.historico.transacoes) >= self._limite_saques

        if excedeu_limite:
            print("Operação falhou! Você excedeu o limite de saque.")
            return False
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques.")
            return False
        else:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        return False