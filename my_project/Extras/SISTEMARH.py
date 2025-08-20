while True:
    Cadastro = input(f"""SELECIONE O CADASTRO
                         #1 Cadastro de Vendedor
                         #2 Cadastro de Gerente
                         #3 Cadastro de Cliente
                          """)
    
    if Cadastro == "1":
        nome = str(input("digite o nome"))
        cidade = str(input("digite a cidade"))
        cpf = int(input("digite o cpf"))
        idade = int(input("digite a idade"))

    elif Cadastro == "2":
        nome = str(input("digite o nome"))
        cidade = str(input("digite a cidade"))
        cpf = int(input("digite o cpf"))
        idade = int(input("digite a idade"))
        salario = int(input("digite o salario"))
        
    elif Cadastro == "3":
        nome = str(input("digite o nome"))
        endereço = str(input("digite a cidade"))
        cpf = int(input("digite o cpf"))
        idade = int(input("digite a idade"))
        telefone = int(input("digite o salario"))
    else:
        print("invalido, tente novamente")
