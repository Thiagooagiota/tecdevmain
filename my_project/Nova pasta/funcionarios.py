class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

    @classmethod
    def adicionar_funcionario(cls):
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))

        novo_funcionario = cls(nome, cargo, salario)
        cls.funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} cadastrado com sucesso!")

    @classmethod
    def listar_funcionarios(cls):
        if not cls.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print("Lista de Funcionários:")
            for funcionario in cls.funcionarios:
                print(funcionario)