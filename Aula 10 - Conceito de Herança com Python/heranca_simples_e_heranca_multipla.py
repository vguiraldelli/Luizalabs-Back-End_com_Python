import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Herança simples:
print(" Herança Simples ".center(50, "=") + "\n")
class A:
    pass

class B(A):
    pass


# Herança Múltipla
print(" Herança Múltipla ".center(50, "=") + "\n")
class Animal():
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def __str__(self):
        return f"Animal {self.__class__.__name__}: {'. '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        self.cor_do_bico = cor_do_bico
        super().__init__(**kw)

class Ornitorrinco(Mamifero, Ave):
    pass

ornitorrinco = Ornitorrinco(numero_de_patas=4, cor_do_pelo="marrom", cor_do_bico="laranja")
print(ornitorrinco)
print("\n")