class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor
    
    def calcArea(self):
        pi = 3.14159
        raio = self.circunferencia / (2 * pi)
        area = 4 * pi * raio ** 2
        return area

bola = Bola(cor="vermelha", circunferencia=60, material="plástico")

print(f"A cor da bola é: {bola.mostraCor()}")
bola.trocaCor("azul")
print(f"A nova cor da bola é: {bola.mostraCor()}")
area = bola.calcArea()
print(f"A área da bola é: {area:.2f} unidades quadradas")