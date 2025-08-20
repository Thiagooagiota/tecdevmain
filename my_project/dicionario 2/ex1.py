contatos = {}

def menu():
    escolha = input(f"""selecione uma opção
    1 - adicionar contatos
    2 - listar todos os contatos
    3 - sair do programa
                    """)
    
    if escolha == "1":
        add()
    elif escolha == "2":
        print(contatos)
    elif escolha == "3":
        quit()


def add():
    while True:
        try:
            nome = input("digite o nome do seu contato \n")
            numero = int(input("digite o numero do seu contato\n"))
            contatos[nome] = numero
            break
        except ValueError:
            print("digite o numero corretamente")


while True:
    menu()

