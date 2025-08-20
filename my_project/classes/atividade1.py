
class Aluno:
    def __init__(self,nome,matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    def exibir_informacoes(self):
        print(f"nome: {self.nome}")
        print(f"matricula: {self.matricula}")
        print(f"notas: {self.notas}")

    def mediafinal(self):
        return sum(self.notas) / len(self.notas)
    
    def aprovado_reprovado(self):
        media = self.mediafinal()
        print(f"media final: {media:.2f}")
        if media >= 6:
            print("VOCE PASSOU")
        else:
            print("REPROVADO")

vagabundo_notas = [0,0,5,7]
vagabundo = Aluno("Everton", 12345, vagabundo_notas)

estudioso_notas = [8,10,10,9]
estudioso = Aluno("Jacinto", 54321, estudioso_notas)

vagabundo.exibir_informacoes()
vagabundo.aprovado_reprovado()

estudioso.exibir_informacoes()
estudioso.aprovado_reprovado()