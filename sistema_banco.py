menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Mostrar contas
[7] Sair

==> """ 

# Configuração
saldo = 0
valor = 0
extrato = ""
numero_saques = 0
limite_saques = 10
limite_valor = 500
usuarios = []
contas = []
agencia = "0001"

# Tempo
import datetime as dt
data_atual = 0
horario = 0
ultimo_saque = 0


def horario_transacao():
    x = dt.datetime.now()
    periodo = x.strftime("%d/%m/%Y, %H:%M")
    return periodo

def depositar(saldo, valor, extrato, /):
    print("\n------Depósito------\n")
    valor = float(input("Digite o valor do depósito: "))

    if valor <= 0:
            print("O valor informado é inválido. Tente novamente")
        
    else:
        saldo += valor
        horario = horario_transacao()
        extrato += f"Depósito de R${valor:.2f} - {horario}\n"
        return saldo, extrato

def sacar(*, saldo, numero_saques, limite_saques, limite_valor, ultimo_saque, extrato):
    print("\n------Saque------\n")
    print("Saldo: ", saldo)
    print(f"Saques efetuados: {numero_saques}/10")
    valor = float(input("Digite o valor do saque: "))
    data_atual = dt.date.today()

    if valor <= 0:
        print("O valor informado é inválido. Tente novamente")

    elif valor > limite_valor:
        print("O saque não pode ultrapassar o valor de R$500.00. Tente novamente")

    elif valor > saldo:
        print("O valor não pode ultrapassar o saldo da conta")

    elif numero_saques >= limite_saques and data_atual == ultimo_saque:
        print("O limite de saques diários (10) foi atingido. Tente outro dia")

    else:
        saldo -= valor
        numero_saques += 1

        ultimo_saque = dt.date.today()
        horario = horario_transacao()

        extrato += f"Saque de R${valor:.2f} - {horario}\n"
    return saldo, numero_saques, ultimo_saque, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n------Extrato------\n")
    print("Não foram realizadas operações" if not extrato else extrato)
    print(f"\nSaldo final: R${saldo:.2f}")

def verificar_duplicados(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
  cliente = dict.fromkeys(["nome", "data_nasc", "cpf", "endereço"])

  cliente["cpf"] = input("\nCPF: ")
  usuario = verificar_duplicados(cliente["cpf"], usuarios)
  if usuario:
    print("Já há um usuário com esse CPF")
    return

  else:
    cliente["nome"] = input("Nome completo: ")
    cliente["data_nasc"] = input("Data de Nascimento: ")
    cliente["endereço"] = input("Digite o endereço(logradouro, nro - bairro - cidade/sigla estado): ")


    usuarios.append(cliente)
    print("Usuário criado")
    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("\nDigite o seu CPF: ")
  usuario = verificar_duplicados(cpf, usuarios)

  if usuario:
    print("Conta criada")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  else:
    print("O usuário não foi encontrado. Tente novamente ou crie o usuário, caso não tenha feito.")

def mostrar_contas(contas):
  for conta in contas:
    linha = f"""\n
      Agência:\t{conta['agencia']}
      C/C:\t{conta['numero_conta']}
      Titular:\t{conta['usuario']['nome']}
    """
    print(linha)

while True:

    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 2:
        saldo, numero_saques, ultimo_saque, extrato = sacar(saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques, limite_valor=limite_valor, ultimo_saque=ultimo_saque, extrato=extrato)
       
    elif opcao == 3:
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 6:
       mostrar_contas(contas)

    elif opcao == 7:
        break

    else:
        print("Opção inválida, tente novamente") 