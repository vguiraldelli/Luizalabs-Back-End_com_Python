import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

programa = input("1 - Verificação de idade\n2 - Saque de valores\n\nDigite o número do programa que deseja executar: ")

if programa == "1":
    print("\n" + "=" * 60)
    print("Verificação de idade:")
    print("=" * 60 + "\n")

    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

    print("\n" + "=" * 60)
    print("Fim do programa")
    print("=" * 60)

elif programa == "2":

    print("\n" + "=" * 60)
    print("Saque de valores:")
    print("=" * 60 + "\n")

    conta_normal = True
    conta_universitaria = False
    
    saldo = 5000.0
    cheque_especial = 2000.0


    valor_saque = float(input("Digite o valor do saque: "))

    if conta_normal:
        if saldo >= valor_saque:
            print("Saque realizado com sucesso!")
        elif valor_saque <= cheque_especial:
            print("Saque realizado com cheque especial!")
        else:
            print("Saldo insuficiente!")
    elif conta_universitaria:
        if saldo >= valor_saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Conta inválida!")

    print(f"Saldo atual: R${saldo}")

else:
    print("\nPrograma inválido!\n")

print("\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)