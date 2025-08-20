class Livro:
    def __init__(self, titulo, autor, ano_publicacao, avaliacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.avaliacao = avaliacao

    def __str__(self):
        return f"""
        Titulo: {self.titulo} 
        por {self.autor} ({self.ano_publicacao})
        Avaliação: {self.avaliacao}
"""