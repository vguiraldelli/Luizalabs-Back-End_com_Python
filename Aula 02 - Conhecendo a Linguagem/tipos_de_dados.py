import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()
from utils.tipos_de_dados import formatar_tipo


# Imprime os tipos de dados em Python
print("Tipos de dados em Python:\n")

print(f"Tipo de 10: {formatar_tipo(type(10))}")
print(f"Tipo de 10.5: {formatar_tipo(type(10.5))}")
print(f"Tipo de 'Hello World': {formatar_tipo(type("Hello World"))}")
print(f"Tipo de True: {formatar_tipo(type(True))}")
print(f"Tipo de False: {formatar_tipo(type(False))}")
print(f"Tipo de 10 + 5j: {formatar_tipo(type(10 + 5j))}")
print(f"Tipo de [1, 2, 3]: {formatar_tipo(type([1, 2, 3]))}")
print(f"Tipo de (1, 2, 3): {formatar_tipo(type((1, 2, 3)))}")
teste = {"name": "John", "age": 30};print(f"Tipo de {teste}: {formatar_tipo(type(teste))}")
teste = {1, 2, 3}; print(f"Tipo de {teste}: {formatar_tipo(type(teste))}")  
print(f"Tipo de None: {formatar_tipo(type(None))}")


