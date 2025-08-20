class Caixa:

    def __init__(self):
        self.carrinho = {} #dicionario com {produto: preço}


    def adicionar(self, produto, valor): #adicionar produtos

        self.carrinho[produto] = valor #adiciona produto no carrinho como item e o valor como valor


    def remover(self,produto): #remover itens do carrinho

        del self.carrinho[produto] #remove o produto e o preço pelo nome do produto


    def visualizar(self): #mostra os produtos e preços no carrinho

        print(self.carrinho)





    def finalizar(self): #etapas de finalizaçao de pedido

        if not self.carrinho: #checa se o carrinho esta vazio
            print("sem itens no carrinho")
            return
        else:
            valor = sum(self.carrinho.values()) #soma os valores da lista para saber o preço total dos produtos

        print(f"total {valor:.2f}") #mostra o preço total com só duas casas decimais depois do numero 

        while True:
            try:
                pago = float(input("digite o valor pago\n")) #valor pago pelo cliente

                troco = pago - valor #calcula o troco se o cliente paga a mais

                print(f"troco a ser pago {troco:.2f}") #mostra o troco a ser devolvido

                input("pressione enter para terminar") #espera a confirmaçao para finalizar

                self.carrinho.clear() #apaga os itens do carrinho

                break #quebra o loop para retornar ao menu

            except ValueError:
                print("digite um valor valido")

    def op(self):
        while True:

            try:
                user = int(input(f"""selecione uma opção:
                                
                                1 - adicionar produto
                                2 - remover produto
                                3 - visualizar carrinho
                                
                                0 - finalizar compra \n\n""")) #pede para selecionar uma opçao

                if user == 1:
                    try:
                        prod = input("digite o produto \n").lower() #digita o produto
                        val = float(input("digite o valor\n")) #digita o preço
                        
                        self.adicionar(prod, val) #usa a variavel adicionar para colocar no carrinho (o dicionario)

                    except ValueError:
                        print("invalido")

                elif user == 2:
                    prod = input("digite o produto\n").lower() #pede o produto a ser excluido
                    self.remover(prod) #usa a variavel para remover o produto do carrinho

                elif user == 3:
                    self.visualizar() #printa o carrinho


                elif user == 0:
                    self.finalizar() #finaliza a compra



                else:
                    print("digite um numero valido")
                    continue


            except ValueError:
                print("digite um numero")


caixa = Caixa()
caixa.op()