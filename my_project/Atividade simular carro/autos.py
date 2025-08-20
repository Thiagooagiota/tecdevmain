class Carros:
    def __init__ (self,marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, aceleracao):
        self.velocidade += aceleracao
        print(f"Acelerando {self.modelo}")

    def frear(self, desaceleracao):
        self.velocidade -= desaceleracao
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Freando {self.modelo}")

    def exibir_velocidade(self):
        print(f"Velocidade atual de {self.modelo}: {self.velocidade} km/h")

fusca = Carros("Volkswagen", "Fusca", 1970, 0)
ferrari = Carros("Ferrari", "488", 2020, 0)