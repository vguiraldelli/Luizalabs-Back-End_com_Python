import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()
from utils.tipos_de_dados import formatar_tipo


# Imprime "Variáveis e Constantes em Python"
print("Variáveis e Constantes em Python\n")

print("Variáveis:\n")
nome_completo = "Victor Guiraldelli"
idade = 25
altura = 1.75

# Imprime o valor das variáveis
print(f"Nome: {nome_completo}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")

print("\nConstantes:\n")
PI = 3.14159
VELOCIDADE_DA_LUZ = 299792458
DIAS_POR_SEMANA = 7
MESES_POR_ANO = 12

# Imprime o valor da constante PI
print(f"PI: {PI}", " - tipo: ", formatar_tipo(type(PI)))

# Imprime o valor da constante VELOCIDADE_DA_LUZ
print(f"Velocidade da luz: {VELOCIDADE_DA_LUZ}", " - tipo: ", formatar_tipo(type(VELOCIDADE_DA_LUZ)))

# Imprime o valor da constante DIAS_POR_SEMANA
print(f"Dias por semana: {DIAS_POR_SEMANA}", " - tipo: ", formatar_tipo(type(DIAS_POR_SEMANA)))

# Imprime o valor da constante MESES_POR_ANO
print(f"Meses por ano: {MESES_POR_ANO}", " - tipo: ", formatar_tipo(type(MESES_POR_ANO)))
