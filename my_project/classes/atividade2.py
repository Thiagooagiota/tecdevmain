class Livro:
    def __init__(self, titulo, autor, rep):
        self.titulo = titulo
        self.autor = autor
        self.rep = rep

    def __str__(self):
        return f"Autor: {self.autor} \nTítulo: {self.titulo} \nReputação: {self.reputacao()}"

    def reputacao(self):
        critica = sum(self.rep) / len(self.rep)

        if critica >= 8:
            return "Reputação excelente"
        elif critica >= 5:
            return "Reputação boa"
        else:
            return "Reputação ruim"

livro1_critico = [10, 5, 5, 6]
livro1 = Livro("Ligma Balls", "Neymar Junior", livro1_critico)

print(livro1)
print("\n")

livro2_critico = [5, 5, 5, 7]
livro2 = Livro("AAAAAA", "Joaquim", livro2_critico)

print(livro2)
print("\n")

livro3_critico = [4, 4, 2, 1]
livro3 = Livro("Amiga da Minha Mulher", "Tim Maia", livro3_critico)

print(livro3)
print("\n")