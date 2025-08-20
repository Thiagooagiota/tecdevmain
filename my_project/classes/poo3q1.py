class Quarto:
    def __init__ (self, numero, tipo, disponibilidade = True):
        self.numero = numero
        self.tipo = tipo
        self.disponibilidade = disponibilidade


    def reservar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"Quarto {self.numero} reservado com sucesso")
        else:
            print(f"Quarto {self.numero} ja esta reservado.")

    def liberar(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f"Quarto {self.numero} liberado com sucesso!")
        else:
            print(f"Quarto {self.numero} já está livre.")

class Hotel:
    
    quartos = []

    @classmethod
    def adicionar(cls, quarto):
        cls.quartos.append(quarto)
        print(f"Quarto {quarto.numero} adicionado")

    @classmethod
    def disponivel(cls):
        disponiv = False

        for quarto in cls.quartos:
            if quarto.disponibilidade:
                print(f"Quarto {quarto.numero}, Tipo: {quarto.tipo}")
                disponiv = True
        
        if not disponiv:
            print("nao há quartos disponiveis")



quarto1 = Quarto(101, 'Single')
quarto2 = Quarto(102, 'Double', False)
quarto3 = Quarto(103, 'Suite')


Hotel.adicionar(quarto1)
Hotel.adicionar(quarto2)
Hotel.adicionar(quarto3)


Hotel.disponivel()


quarto1.reservar()
quarto1.reservar()


Hotel.disponivel()