class Livros:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("\033c")
            print(f"\no livro '{self.titulo}' foi emprestado com sucesso.\n")
            input("Pressione Enter para continuar...")
            return True
        else:
            print("\033c")
            print(f"\no livro '{self.titulo}' não está disponível no momento.\n")
            input("Pressione Enter para continuar...")
            return False
        
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("\033c")
            print(f"\no livro '{self.titulo}' foi devolvido com sucesso.\n")
            input("Pressione Enter para continuar...")
            return True
        else:
            print("\033c")
            print(f"\no livro '{self.titulo}' não estava emprestado.\n")
            input("Pressione Enter para continuar...")
            return False
        
    def exibir_info(self):
        status = "disponível" if self.disponivel else "indisponível"
        return f"\nTítulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}\n"
    


livro1 = Livros("Don quixote e os flamingos", "Eiichiro Oda", 1501)
livro2 = Livros("Biografia de alguém", "Um cara aí", 2099)
livro3 = Livros("AAAAAAAAAAAAAA", "Um homem louco", 2015)