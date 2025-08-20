class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
        else:
            print(f"O livro {livro} não está emprestado por este aluno.")


class Biblioteca:
    livros_disponiveis = []

    @classmethod
    def emprestar(cls, livro, aluno):
        if livro in cls.livros_disponiveis:
            print(f"O livro {livro} foi retirado do sistema.")
            cls.livros_disponiveis.remove(livro)
            aluno.emprestar_livro(livro)
        else:
            print(f"O livro {livro} não está disponível.")

    @classmethod
    def devolver(cls, aluno, livro):
        if livro not in cls.livros_disponiveis:
            print(f"O livro {livro} foi devolvido com sucesso.")
            cls.livros_disponiveis.append(livro)
            aluno.devolver_livro(livro)
        else:
            print(f"O livro {livro} já foi devolvido ou não foi emprestado.")

    @classmethod
    def adicionar(cls, novo):
        if novo not in cls.livros_disponiveis:
            print(f"{novo} foi adicionado a biblioteca")
            cls.livros_disponiveis.append(novo)
        else:
            print(f"o livro {novo} já se encontra na biblioteca")

    @staticmethod
    def consultar( livro):
        if livro in Biblioteca.livros_disponiveis:
            return f"o livro esta disponivel"
        else:
            return f"o livro nao esta disponivel"
        


# Criando objetos de aluno e biblioteca
aluno1 = Aluno("João", "12345")
biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adicionar("Python para Iniciantes")
biblioteca.adicionar("Estruturas de Dados")

# Consultando a disponibilidade de um livro
print(Biblioteca.consultar("Python para Iniciantes"))

# Emprestando um livro
Biblioteca.emprestar("Python para Iniciantes", aluno1)

# Consultando novamente
print(Biblioteca.consultar("Python para Iniciantes"))

# Devolvendo o livro
Biblioteca.devolver(aluno1, "Python para Iniciantes")


