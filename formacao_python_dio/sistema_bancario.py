menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Qual o valor a ser depositado?"))
        if deposito <= 0:
            print("Não foi possível realizar o depósito")
        else:
            saldo += deposito

    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Quanto você deseja sacar?"))
            if saque > 0 and saque <= saldo and saque <= limite:
                saldo -= saque
                numero_saques += 1
            else:
                print("Saque inválido")
        else:
            print("Limite de saques atingidos")

    elif opcao == "e":
        print("Extrato")
        print(f"Saldo em conta: R$ {round(saldo, 2)}")
        print(f"Foram realizados {numero_saques} saques.")

    elif opcao == "q":
        break

    else:
        print("Opção não existe")
