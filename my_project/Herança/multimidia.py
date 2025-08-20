class Midia:
    def __init__(self, titulo, genero, ano_lancamento, formato, tamanho):
        self.arquivo = titulo
        self.genero = genero
        self.ano = ano_lancamento
        self.formato = formato
        self.tamanho = tamanho

    def remover(self):
        pass
    def acessar(self):
        pass
    def renomear(self):
        pass

class Livro(Midia):
    
    def __init__(self, titulo, genero, ano_lancamento, formato, paginas):
        super().__init__(titulo, genero, ano_lancamento, formato)
        self.paginas = paginas

    def passar_paginas():
        pass


class Musica(Midia):
    
    def __init__(self, titulo, genero, ano_lancamento, formato, album):
        super().__init__(titulo, genero, ano_lancamento, formato,)
        self.album = album


    def aumentar_volume():
        pass

class Filme(Midia):
    def __init__(self, titulo, genero, ano_lancamento, formato, tamanho, resolucao):
        super().__init__(titulo, genero, ano_lancamento, formato, tamanho)
        self.resolucao = resolucao

    def fullscreen():
        pass