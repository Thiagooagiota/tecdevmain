class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
    
    def retornarLados(self):
        return self.lado_a, self.lado_b
    
    def calcularArea(self):
        return self.lado_a * self.lado_b
    
    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)

def calcular_pisos(area_local, area_piso):
    return area_local / area_piso

def calcular_rodapes(perimetro_local, comprimento_rodape):
    return perimetro_local / comprimento_rodape

largura_local = float(input("Digite a largura do local (em metros): "))
comprimento_local = float(input("Digite o comprimento do local (em metros): "))

area_piso = float(input("Digite a área de um piso (em metros quadrados): "))
comprimento_rodape = float(input("Digite o comprimento de um rodapé (em metros): "))

local = Retangulo(lado_a=largura_local, lado_b=comprimento_local)

area_local = local.calcularArea()
perimetro_local = local.calcularPerimetro()

quantidade_pisos = calcular_pisos(area_local, area_piso)
quantidade_rodapes = calcular_rodapes(perimetro_local, comprimento_rodape)

print(f"A área do local é: {area_local} metros quadrados")
print(f"O perímetro do local é: {perimetro_local} metros")
print(f"Você precisará de aproximadamente {quantidade_pisos:.2f} pisos.")
print(f"Você precisará de aproximadamente {quantidade_rodapes:.2f} rodapés.")
