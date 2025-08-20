class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):

            if valor <= 0:
                print("Valor inválido. O depósito deve ser maior que zero.")
                return
            else:
                self.saldo += valor
                print(f"Depósito realizado com sucesso! Saldo atual: {self.saldo:.2f}")


    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
            return
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso! Saldo atual: {self.saldo:.2f}")


joaquim = Banco("Joaquim", 1000.00)
thiago = Banco("Thiago", 300.00)
tarik = Banco("Tarik", 000.00)