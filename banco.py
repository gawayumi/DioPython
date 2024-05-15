operacoes = saldo = limiteS = totalS = saldos = 0
extrato = []

print("Seja vem-vindo ao Banco Python. Qual operação gostaria de realizar hoje?")

while True:
    print("Digite 'd' para depósito; 's' para saque e 'e' para extrato.")
    menu = input()
    menu = menu.upper()
    
    if menu == "D":
        deposito = float(input("Você iniciou o menu de DEPÓSITO. Qual valor gostaria de depositar? "))
        if deposito <= 0:
            print("O valor informado não pode ser depositado. Tente novamente.\n")
        else:
            print(f"Foi realizado um depósito na sua conta de R${deposito:.2f}\n")
            extrato.append(deposito)
            operacoes += 1
            saldo += deposito
    elif menu == "S":
        saque = (float(input("Você iniciou o menu de SAQUE. Qual valor gostaria de sacar? ")))
        if limiteS < 3:
            if saldo >= saque:
                if saque <= 0 or saque > 500:
                    print("O valor informado não pode ser sacado. Tente novamente.\n")
                else:
                    print(f"Foi realizado um saque na sua conta de R${saque:.2f}\n")
                    extrato.append(-saque)
                    saldo -= saque
                    operacoes += 1
                    limiteS += 1
                    if totalS < 1500:
                        totalS += saque
                    else:
                        print("Valor excede o limite monetário diário. Tente novamente.\n")
            else:
                print("Saldo insuficiente. Não foi possível efetuar o saldo.\n")
        else:
            print("Limite de saques diários excedido. Não foi possível realizar o saque\n")
    elif menu == "E":
        print("\n")
        for i in range(operacoes):
            if extrato[i] > 0:
                print(f"Depósito: R${extrato[i]:.2f}")
            elif extrato[i] < 0:
                print(f"Saque: R${extrato[i]:.2f}")
            saldos += extrato[i]
        print(f"\nO seu saldo atual é: {saldo:.2f}")
        break
    else:
        print("Comando inválido. Tente novamente.")