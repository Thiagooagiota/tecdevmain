import conta
        
def menu():
    while True:
        nome = input("Digite seu nome: ").strip().lower()
        if nome == "joaquim":
            usuario = conta.joaquim
        elif nome == "thiago":
            usuario = conta.thiago
        elif nome == "tarik":
            usuario = conta.tarik
        else:
            print("Usuário não encontrado. Por favor, verifique o nome e tente novamente.")
            continue
        
        while True:
            print(f"\nBem-vindo, {usuario.titular}!")
            print(f"Saldo atual: {usuario.saldo:.2f}")
            print("Escolha uma opção: ")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Ver saldo")
            print("4 - Sair")
            escolha = input("Digite sua opção: ")
            if escolha == "1":
                try:
                    deposito = float(input("Digite o valor a depositar: "))
                    usuario.depositar(deposito)
                except ValueError:
                    print("Valor inválido. Tente novamente.")
                    continue
            elif escolha == "2":
                try:
                    saque = float(input("Digite o valor a sacar: "))
                except ValueError:
                    print("Valor inválido. Tente novamente.")
                    continue
                usuario.sacar(saque)
            elif escolha == "3":
                print(f"Saldo atual: {usuario.saldo:.2f}")
            elif escolha == "4":
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
menu()

