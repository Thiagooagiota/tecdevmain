pacientes = {}
nlista = 1

def menu():
    escolha = input(f"""selecione uma opçao:
1 - cadastrar paciente
2 - buscar paciente
3 - sair do programa \n""")

    if escolha == "1":
        cadastro()
    elif escolha == "2":
        busca()
    elif escolha == "3":
        quit()

def cadastro():
    nome = input("nome do paciente\n")
    while True:
        try:
            cpf = int(input("digite o cpf\n"))
            idade = int(input("digite a idade\n"))
            pacientes[cpf] = nome, idade
            break
        except ValueError:
            print("invalido")


def busca():
    while True:
        try:
            cpf = int(input("digite o cpf \n"))
            if cpf in pacientes:
                nome, idade = pacientes[cpf]
                print("paciente:", nome, "\nidade:", idade )
            else:
                print("paciente nao encontrado")
            break
        except ValueError:
            print("erro")


while True:
    menu()