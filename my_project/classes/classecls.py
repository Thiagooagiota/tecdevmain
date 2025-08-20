class Pessoa:
    populacao = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1
    
    @classmethod
    def contar_populacao(cls):
        print(f"total:{cls.populacao}")
    
p1 = Pessoa("ana")
p2 = Pessoa("jao")
Pessoa.contar_populacao()

@staticmethod
def idade(self, anonas):
    self.idade = 2025 - anonas