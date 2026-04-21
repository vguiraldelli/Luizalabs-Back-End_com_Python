import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Historico():
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })

    def listar_transacoes(self):
        for transacao in self._transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")