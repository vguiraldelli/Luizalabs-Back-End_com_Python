import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

# Cabeçalho
print(" Variáveis de Classe e Instância ".center(50, "=") + "\n")

class Pessoa:
    # Variável de classe
    especie = "Homo sapiens"

    def __init__(self, nome, idade):
        # Variáveis de instância
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Bruno", 30)

# Acessando variáveis de classe
print(f"Espécie de {pessoa1.nome}: {pessoa1.especie}")
print(f"Espécie de {pessoa2.nome}: {pessoa2.especie}")

# Acessando variáveis de instância
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")