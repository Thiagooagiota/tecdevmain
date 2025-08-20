# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         pass

# pessoa0 = Pessoa("joao",30)
# pessoa1 = Pessoa("maria",25)

# print(f"a primeira pessoa é {pessoa0.nome} e possui {pessoa0.idade} anos")
# print(f"a primeira pessoa é {pessoa1.nome} e possui {pessoa1.idade} anos")

class Cavalo:
    def __init__(self, raca, cavalgada):
        self.raca = raca
        self.cavalgada = cavalgada
        pass

cavalo1 = Cavalo("mustangue", "excelente")

print(f"o cavalo {cavalo1.raca} te da uma cavalgada {cavalo1.cavalgada}")

class Heli:
    def __init__(self, modelo, e):
        self.modelo = modelo
        self.e = e
        pass

heli1 = Heli("Apache", "Camuflado")

print(f"o {heli1.modelo} é {heli1.e}")

class Metralhadora:
    def __init__(self, modelo, tem):
        self.modelo = modelo
        self.tem = tem
        pass

    def __str__(self):
        return f"{self.modelo}, {self.tem}"

metralhadora1 = Metralhadora("uzi", "trava de segurança")

print(f"a metralhadora {metralhadora1.modelo} tem {metralhadora1.tem}")
print(metralhadora1.__str__())