import autos

def menu():
    print("seleciona um carro")
    print("1 - Fusca, 2 - ferrari \n")

    escolha = input("Escolha o carro: ")

    if escolha == "1":
        print("Você escolheu o Fusca!")
        escolha = autos.fusca
    elif escolha == "2":
        print("Você escolheu a Ferrari!")
        escolha = autos.ferrari
    else:
        print("Opção inválida. Tente novamente.")
        return menu()
    while True:
        print("1 - Acelerar, 2 - Frear, 3 - Exibir Velocidade")
        acao = input("Escolha a ação: ")

        if acao == "1":
            if escolha == autos.fusca and autos.fusca.velocidade < 100:
                escolha.acelerar(20)
            elif escolha == autos.fusca and autos.fusca.velocidade >= 100:
                print("O Fusca já está na velocidade máxima")
            elif escolha == autos.ferrari and autos.ferrari.velocidade < 200:
                escolha.acelerar(50)
            elif escolha == autos.ferrari and autos.ferrari.velocidade >= 200:
                print("A Ferrari já está na velocidade máxima")

        elif acao == "2":
            if escolha.velocidade > 0:
                escolha.frear(20)
            else:
                print(f"{escolha.modelo} já está parado.")

        elif acao == "3":
            escolha.exibir_velocidade()

        else:
            print("Ação inválida. Tente novamente.")
            return menu()
    
menu()