class Cliente:
    def __init__(self, nome, cpf, data_do_cadastro):
        self.nome = nome
        self.cpf = cpf
        self.data_de_cadastro = data_do_cadastro
        self.plano = None  # Atributo para armazenar o plano do cliente

    def mostrar_infos_de_cadastro(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nData de Cadastro: {self.data_de_cadastro}\nPlano: {self.plano if self.plano else 'Nenhum plano'}"

    def registrar_assinatura(self):
        print(f"Selecione um plano:")
        print("1 - 3 meses por 600 R$")
        print("2 - 1 ano por 1000 R$")

        escolha = input("Digite a opção: ").strip()

        if escolha == "1":
            self.plano = "3 meses por 600 R$"
            print(f"Plano {self.plano} registrado com sucesso!")
        elif escolha == "2":
            self.plano = "1 ano por 1000 R$"
            print(f"Plano {self.plano} registrado com sucesso!")
        else:
            print("Opção inválida. Nenhum plano registrado.")

    def cancelar_assinatura(self):
        if self.plano:
            print(f"Plano {self.plano} cancelado para o cliente {self.nome}!")
            self.plano = None
        else:
            print("Nenhum plano para cancelar.")

        
class Funcionarios:
    def __init__(self, nome, senha, funcao):
        self.nome = nome
        self.senha = senha
        self.funcao = funcao

    def checar_cliente(self):
        cpf = input("Digite o CPF do cliente: ").strip()

        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip() == "":
                    continue
                nome, cpf_c, data_do_cadastro = linha.strip().split(":")
                if cpf_c == cpf:
                    cliente = Cliente(nome, cpf_c, data_do_cadastro)
                    print(cliente.mostrar_infos_de_cadastro())  # Exibe as informações do cliente
                    return cliente
            print("Cliente não encontrado!")
            return None

    def menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("1 - Checar cliente")
            print("2 - Sair do menu")

            opcao = input("Digite a opção: ").strip()

            if opcao == "1":
                self.checar_cliente()
            elif opcao == "2":
                print("Saindo do menu do funcionário...")
                break
            else:
                print("Opção inválida. Tente novamente.")


class Recepcionista(Funcionarios):
    def __init__(self, nome, senha):
        super().__init__(nome, senha, funcao="recepcionista")

    def registrar_cliente(self):
        nome = input("Digite o nome do cliente: ").strip()
        cpf = input("Digite o CPF do cliente: ").strip()
        data = input("Digite a data de registro do cliente (opcional): ").strip()

        # Verificar se o CPF já existe
        try:
            with open("clientes.txt", "r") as arquivo:
                for linha in arquivo:
                    if linha.strip() == "":
                        continue
                    _, cpf_c, *_ = linha.strip().split(":")
                    if cpf_c == cpf:
                        print("Cliente com esse CPF já está registrado!")
                        return  # Sai do método para não registrar duplicado
        except FileNotFoundError:
            pass  # Arquivo não existe, pode registrar normalmente

        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"{nome}:{cpf}:{data}\n")

        print(f"Cliente {nome} registrado com sucesso!")

    def remover_cliente(self):
        cpf_remover = input("Digite o CPF do cliente que deseja remover: ").strip()

        try:
            with open("clientes.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            encontrado = False
            with open("clientes.txt", "w") as arquivo:
                for linha in linhas:
                    if linha.strip() == "":
                        continue
                    nome, cpf, *resto = linha.strip().split(":")
                    if cpf == cpf_remover:
                        encontrado = True
                        continue  # Pula a linha a ser removida
                    arquivo.write(linha)

            if encontrado:
                print("Cliente removido com sucesso!")
            else:
                print("Cliente com esse CPF não foi encontrado.")

        except FileNotFoundError:
            print("Nenhum cliente foi registrado ainda.")

    def atribuir_plano(self):
        cpf = input("Digite o CPF do cliente para atribuir o plano: ").strip()

        try:
            with open("clientes.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            for linha in linhas:
                if linha.strip() == "":
                    continue
                nome, cpf_c, data_cadastro = linha.strip().split(":")
                if cpf_c == cpf:
                    cliente = Cliente(nome, cpf, data_cadastro)
                    cliente.registrar_assinatura()
                    return

            print("Cliente não encontrado!")

        except FileNotFoundError:
            print("Clientes ainda não registrados!")

    def remover_plano(self):
        cpf = input("Digite o CPF do cliente para remover o plano: ").strip()

        try:
            with open("clientes.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            for linha in linhas:
                if linha.strip() == "":
                    continue
                nome, cpf_c, data_cadastro = linha.strip().split(":")
                if cpf_c == cpf:
                    cliente = Cliente(nome, cpf, data_cadastro)
                    cliente.cancelar_assinatura()
                    return

            print("Cliente não encontrado!")

        except FileNotFoundError:
            print("Clientes ainda não registrados!")

    def menu(self):
        while True:
            print("\nEscolha a opção:")
            print("1 - Checar infos de cadastro")
            print("2 - Registrar cliente")
            print("3 - Remover cliente")
            print("4 - Atribuir plano a cliente")
            print("5 - Remover plano de cliente")
            print("6 - Sair")

            escolha = input("Selecione uma opção: ").strip()

            if escolha == "1":
                self.checar_cliente()
            elif escolha == "2":
                self.registrar_cliente()
            elif escolha == "3":
                self.remover_cliente()
            elif escolha == "4":
                self.atribuir_plano()
            elif escolha == "5":
                self.remover_plano()
            elif escolha == "6":
                print("Saindo do menu do recepcionista...")
                break
            else:
                print("Opção inválida. Tente novamente.")


class Instrutor(Funcionarios):
    def __init__(self, nome, senha):
        super().__init__(nome, senha, funcao="instrutor")

    def registro_de_treinos(self):
        treino = input("Digite o treino a ser registrado: ").strip()
        print(f"Treino '{treino}' registrado com sucesso.")

    def definir_rotina(self):
        rotina = input("Defina a rotina para o cliente: ").strip()
        print(f"Rotina definida: {rotina}")

    def menu(self):
        while True:
            print("\nEscolha a opção:")
            print("1 - Registrar treino")
            print("2 - Definir rotina")
            print("3 - Sair")

            escolha = input("Selecione uma opção: ").strip()

            if escolha == "1":
                self.registro_de_treinos()
            elif escolha == "2":
                self.definir_rotina()
            elif escolha == "3":
                print("Saindo do menu do instrutor...")
                break
            else:
                print("Opção inválida. Tente novamente.")
