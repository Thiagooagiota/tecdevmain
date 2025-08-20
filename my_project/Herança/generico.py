class Veiculo:
    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self. cor = cor

    def acelerar(self):
        print(f"o {self.modelo} acelera")
    def freiar(self):
        print(f"o {self.modelo} freia")
    def infos(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

class Carro(Veiculo):
    def __init__ (self, marca, modelo, ano, cor):
        super().__init__ (marca, modelo, ano, cor)

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, ronco_do_motor):
        super().__init__(marca, modelo, ano, cor)
        self.ronco_do_motor = ronco_do_motor
    def infos(self):
        super().infos()
        print("ronco do motor:", f"{self.ronco_do_motor}")

v1 = Veiculo("Volkswagen", "Gol", 2010 ,"Azul")
v1.acelerar()
v1.freiar()
v1.infos()


v2 = Carro("Fiat", "Uno", 2009,"Vermelho")
v2.acelerar()
v2.freiar()
v2.infos()

v3 = Moto("Honda", "CBR500R", 2005, "Branca", "VRUUUUUUUUUUUMMMMMMMMMMMMM")
v3.acelerar()
v3.freiar()
v3.infos()