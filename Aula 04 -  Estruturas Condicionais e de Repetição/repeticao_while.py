import sys, os

# Adiciona a pasta "Luizalabs - Back-End com Python" ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.limpar_tela import limpar_tela
limpar_tela()

print("=" * 60)
print("Repetição While:")
print("=" * 60 + "\n")

opcao = -1

while opcao != 0:
    print("\n" + "=" * 60)
    print("Menu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print("=" * 60 + "\n")
    
    opcao = int(input("Digite uma opção: "))
    print("\n")
    if opcao == 0:
        break
    elif opcao == 1:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print(f"A soma de {numero1} e {numero2} é {numero1 + numero2}")
    elif opcao == 2:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print(f"A subtração de {numero1} e {numero2} é {numero1 - numero2}")
    elif opcao == 3:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        print(f"A multiplicação de {numero1} e {numero2} é {numero1 * numero2}")
    elif opcao == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        if numero2 == 0:
            print("Não é possível dividir por zero!")
        else:
            print(f"A divisão de {numero1} e {numero2} é {numero1 / numero2}")
    else:
        print("\nOpção inválida!")
    input("\nPressione Enter para continuar...")


print("\n\n" + "=" * 60)
print("Fim do programa")
print("=" * 60)