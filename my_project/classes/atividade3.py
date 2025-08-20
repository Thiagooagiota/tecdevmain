class Carro:
    def __init__(self, marca, modelo, porta):
        self.marca = marca
        self.modelo = modelo
        self.porta = porta  

    def __str__(self):
        return f"marca: {self.marca}\nmodelo: {self.modelo}\nporta: {self.estadop()}"

    def estadop(self):
        return "porta aberta" if self.porta else "porta fechada"

    def abrirp(self):
        if self.porta == 0:
            self.porta = 1
            return "Você abriu a porta."
        else:
            return "A porta já está aberta."

    def fecharp(self):
        if self.porta == 1:
            self.porta = 0
            return "Você fechou a porta."
        else:
            return "A porta já está fechada."


def menu():
    carro = Carro("Fiat", "Uno", 0)

    while True:
        print("1 - Ver estado do carro")
        print("2 - Abrir porta")
        print("3 - Fechar porta")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n", carro)
        elif escolha == "2":
            print("\n", carro.abrirp())
        elif escolha == "3":
            print("\n", carro.fecharp())
        elif escolha == "4":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


menu()