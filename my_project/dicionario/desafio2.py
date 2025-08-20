
estoque = {"linguiça": 24, "banana": 69, "ovo": 0}

def lista():
    for items in estoque:
        print("\n", items, "\n")

def adicionar():
    add = input("digite o produto \n").strip().lower()
    if add in estoque:
        print("este produto ja existe")
        
    else:
        try:
            n = int(input("digite a quantidade \n"))
            if n < 0:
                print("a quantidade nao pode ser negativa")
            else:
                estoque[add] = n

        except ValueError:
            print("Por favor, digite apenas números inteiros.")

def quantidade():
    pe = input ("digite o produto existente \n").strip().lower()
    if pe in estoque:
        escolha = input(f"""1 - somar produto 2 - subtrair produto \n""")
        if escolha == "1":
            try:
                q = int(input("digite o quanto quer somar \n"))
                
                estoque[pe] += q
            except ValueError:
                print("Por favor, digite apenas números inteiros.")
        elif escolha == "2" and estoque[pe] > 0:
            try:
                q = int(input("digite o quanto quer subtrair \n"))
            
                if q <= estoque[pe]:
                    estoque[pe] -= q
                else:
                    print(f"a quantidade do produto {pe}({estoque[pe]}) é menor que a subtraçao")
            except ValueError:
                print("Por favor, digite apenas números inteiros.")
        elif escolha == "2" and estoque[pe] == 0:
            print("o produto ja esta esgotado")
        else:
            print("invalido")
    else:
        print("o produto nao existe")

def remocao():
    remover = input("digite o nome do produto \n").strip().lower()
    if remover in estoque:
        del estoque[remover]
    else:
        print("produto inexistente")

def produtos():
    Product = input("digite o produto \n").strip().lower()
    if Product in estoque:
        if estoque[Product] > 0:
            print(f"o produto {Product} ainda tem {estoque[Product]}")
        
        elif estoque[Product] == 0:
            print(f"{Product} esgotado")
    else:
        print(f"{Product} nao existe no estoque")

def menu():
    while True:
        outro = input(f"""selecione uma opçao
                    1 - checar estoque
                    2 - adicionar produto
                    3 - remover produto
                    4 - somar ou subtrair a quantidade de um produto \n \n""").strip().lower()
        if outro == "1":
            lista()
            produtos()
        if outro == "2":
            lista()
            adicionar()
        if outro == "3":
            lista()
            remocao()
        if outro == "4":
            lista()
            quantidade()

menu()