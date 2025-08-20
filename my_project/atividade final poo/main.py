import classes  # Importa as classes que você definiu

def menu():
    funcionarios_logados = []  # lista para guardar os funcionários logados

    while True:
        print("\nSelecione uma opção:")
        print("1 - Login")
        print("2 - Registrar")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "3":
            print("Saindo...")
            break

        elif escolha == "2":
            nome = input("Digite um nome de usuário: ").strip()
            senha = input("Digite uma senha: ").strip()
            funcao = input("Selecione a função: 1 - Recepcionista  2 - Instrutor: ").strip()

            if funcao == "1":
                funcao = "recepcionista"
            elif funcao == "2":
                funcao = "instrutor"
            else:
                print("Função inexistente")
                continue

            try:
                with open("registro.txt", "r") as arquivo:
                    registros = arquivo.readlines()
                    usuarios = [linha.split(":", 2)[0].strip() for linha in registros if ":" in linha]
            except FileNotFoundError:
                usuarios = []

            if nome in usuarios:
                print("O usuário já existe. Tente outro nome.")
            else:
                with open("registro.txt", "a") as arquivo:
                    arquivo.write(f"{nome}:{senha}:{funcao}\n")
                print(f"Usuário '{nome}' registrado com sucesso!")
                # Criando a instância do funcionário
                if funcao == "recepcionista":
                    funcionario = classes.Recepcionista(nome, senha)
                elif funcao == "instrutor":
                    funcionario = classes.Instrutor(nome, senha)
                funcionarios_logados.append(funcionario)

                # Chama o menu da instância do funcionário imediatamente após o registro
                funcionario.menu()

        elif escolha == "1":
            nome = input("Digite um nome de usuário: ").strip()
            senha = input("Digite uma senha: ").strip()

            try:
                with open("registro.txt", "r") as arquivo:
                    registros = arquivo.readlines()
                    encontrado = False

                    for linha in registros:
                        linha = linha.strip()
                        if linha == "" or linha.count(":") < 2:
                            continue

                        usuario, senha_registrada, funcao_registrada = linha.split(":", 2)
                        if usuario == nome and senha == senha_registrada:
                            print(f"Bem-vindo, {nome}! Função: {funcao_registrada}")
                            encontrado = True
                            # Agora, ao fazer o login, chama o menu adequado
                            if funcao_registrada == "recepcionista":
                                funcionario = classes.Recepcionista(nome, senha)
                                funcionario.menu()  # Chama o menu do Recepcionista
                            elif funcao_registrada == "instrutor":
                                funcionario = classes.Instrutor(nome, senha)
                                funcionario.menu()  # Chama o menu do Instrutor
                            break

                    if not encontrado:
                        print("Nome de usuário ou senha incorretos.")

            except FileNotFoundError:
                print("Nenhum usuário registrado ainda.")

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu()