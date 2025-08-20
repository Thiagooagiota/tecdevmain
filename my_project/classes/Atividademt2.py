class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarLado(self, novo_lado):
        self.lado = novo_lado
    
    def verificarLado(self):
        return self.lado
    
    @staticmethod
    def calcularArea(self):
        return self.lado ** 2

# Exemplo de uso da classe
quadrado = Quadrado(lado=4)

print(f"O tamanho do lado do quadrado é: {quadrado.retornarLado()}")
quadrado.mudarLado(6)
print(f"O novo tamanho do lado do quadrado é: {quadrado.retornarLado()}")
area = quadrado.calcularArea()
print(f"A área do quadrado é: {area} unidades quadradas")