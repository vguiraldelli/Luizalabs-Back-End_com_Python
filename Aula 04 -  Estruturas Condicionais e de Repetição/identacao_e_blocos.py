def sacar():
    saldo = 5000.0
    
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor_saque
        print(f"Valor de R${valor_saque} sacado com sucesso!")
    print(f"Saldo atual: R${saldo}")

sacar()