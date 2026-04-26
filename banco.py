saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(saldo, extrato):
    valor = float(input("Digite o valor para depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f'+ Depósito: R${valor:.2f}\n'
        print("Depósito realizado!")
    else:
        print("Valor inválido!")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Digite o valor para saque: "))

    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques atingido!")

    elif valor > 500:
        print("Limite por saque é R$500")

    elif valor > saldo:
        print("Saldo insuficiente!")

    elif valor > 0:
        saldo -= valor
        extrato += f'- Saque: R${valor:.2f}\n'
        numero_saques += 1
        print("Saque realizado!")

    else:
        print("Valor inválido!")

    return saldo, extrato, numero_saques


def mostrar_saldo(saldo):
    print(f"\nSaldo: R${saldo:.2f}")


def mostrar_extrato(extrato):
    print("\n--- EXTRATO ---")
    print(extrato if extrato else "Sem movimentações")


while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Extrato")
    print("5 - Sair")

    op = input("Escolha: ")

    if op == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif op == "2":
        saldo, extrato, numero_saques = sacar(
            saldo, extrato, numero_saques, LIMITE_SAQUES
        )

    elif op == "3":
        mostrar_saldo(saldo)

    elif op == "4":
        mostrar_extrato(extrato)

    elif op == "5":
        break
