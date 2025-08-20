produtos = {}

def menu():
    opc = input(f"""selecione uma opção
1 - adicionar produto
2 - listar produtos
3 - vender produto
4 - sair

""")

    if opc == "1":
        adicionar()
    if opc == "2":
        listar()
    if opc == "3":
        venda()
    elif opc == "4":
        quit()


def adicionar():
    nome =  input("digite o nome do produto:\n")
    if nome in produtos:
        print("o produto ja existe")
    else:
        while True:
            try:
                quantidade = input("digite a quantidade do produto:\n").replace(",", ".")
                preco = input("digite o preço do produto:\n").replace(",", ".")
                
                produtos[nome] = float(quantidade), float(preco)

                break
            except ValueError:
                print("invalido")

def listar():
    for nome, (quantidade, preco) in produtos.items():
        print("produto:", nome,"\nquantidade:", quantidade, "\npreço:", preco    )


def venda():
    produto = input("digite o nome do produto\n")

    if produto in produtos:
        while True:
            try:
                estoque, preco = produtos[produto]
                quantidade = float(input("digite a quantidade\n"))
                
                
                if estoque < quantidade:
                    print("pedido acima da quantidade de estoque")
                else:
                    total = preco * quantidade
                    produtos[produto] = (estoque - quantidade, preco)
                    print(f"sua compra deu: {total:.2f}")
                    break
            except ValueError:
                print("invalido")
            
    else:
        print("o produto nao existe")
while True:
    menu()