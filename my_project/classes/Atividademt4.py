class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, cm):
        self.altura += cm


pessoa = Pessoa(nome="João", idade=20, peso=70, altura=170)

print(f"Antes: {pessoa.nome}, {pessoa.idade} anos, {pessoa.peso} kg, {pessoa.altura} cm")

pessoa.envelhecer()
pessoa.engordar(2)
pessoa.emagrecer(1)
pessoa.crescer(0.3)

print(f"Depois: {pessoa.nome}, {pessoa.idade} anos, {pessoa.peso} kg, {pessoa.altura} cm")
