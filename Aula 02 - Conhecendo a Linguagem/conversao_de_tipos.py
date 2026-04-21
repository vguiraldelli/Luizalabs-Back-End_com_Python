import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()
from utils.tipos_de_dados import formatar_tipo

# Conversão de tipos
print("=" * 60)
print("Conversão de tipos:")
print("=" * 60 + "\n")

numero_str = "123"
print(f"• Variável numero_str: {numero_str}", " - tipo: ", formatar_tipo(type(numero_str)))

print(">> Convertendo variável numero_str para float...\n")
numero_str = float(numero_str)
print(f"• Variável numero_str: {numero_str}", " - tipo: ", formatar_tipo(type(numero_str)))

print(">> Convertendo variável numero_str para int...\n")
numero_int = int(numero_str)
print(f"• Variável numero_int: {numero_int}", " - tipo: ", formatar_tipo(type(numero_int)), "\n")


# Conversão por divisão
print("=" * 60)
print("Conversão por divisão:")
print("=" * 60 + "\n")

numero = 10
print(">> Convertendo variável numero (int) por divisão:\n")
divisao = numero / 2
print(f"• Variável divisao: {divisao}", " - tipo: ", formatar_tipo(type(divisao)), "\n")

print(">> Convertendo variável numero (int) por divisão inteira:\n")
divisao_inteira = numero // 2
print(f"• Variável divisao_inteira: {divisao_inteira}", " - tipo: ", formatar_tipo(type(divisao_inteira)), "\n")

# Conversão de numérico para string
print("Conversão de numérico para string:\n")
numero_str = str(numero)
print(f"• Variável numero_str: {numero_str}", " - tipo: ", formatar_tipo(type(numero_str)), "\n")