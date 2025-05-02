menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==> """ 


saldo = 0
extrato = ""
numero_saques = 0
limite_saques = 3
limite_valor_saques = 500


while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("\n------Depósito------\n")
        valor = float(input("Digite o valor do depósito: "))

        if valor <= 0:
            print("O valor informado é inválido. Tente novamente")
        
        else:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"


    elif opcao == 2:
        print("\n------Saque------\n")
        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("O valor informado é inválido. Tente novamente")

        elif valor > limite_valor_saques:
            print("O saque não pode ultrapassar o valor de R$500.00. Tente novamente")

        elif valor > saldo:
            print("O valor não pode ultrapassar o saldo da conta")

        elif numero_saques == limite_saques:
            print("O limite de saques diários (3) foi atingido. Tente outro dia")

        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de R${valor:.2f}\n"

        
    elif opcao == 3:
        print("\n------Extrato------\n")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nSaldo final: R${saldo:.2f}")


    elif opcao == 4:
        break


    else:
        print("Opção inválida, tente novamente")