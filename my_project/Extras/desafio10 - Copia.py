
pedidos = []
pao = 6
suco = 3
while True:
    select = int(input(f"""
                       
                       escolha uma opçao
                        1- pedir algo mais     2 - checar meus pedidos     3 - remover todos os pedidos     4 - finalizar pedido \n"""))
    if select == 1:
        print(f"1 - pao com ovo  {pao}    2 - suco de caju {suco}\n")
        selec = int(input(""))

        if selec == 1 and pao > 0:
            pedidos.append("pao com ovo")
            pao -= 1
            continue
        elif selec == 2 and suco > 0:
            pedidos.append("suco de caju")
            suco -= 1
            continue
        elif pao == 0 or suco == 0:
            print("     esgotado")
            continue
        else:
            print("     invalido")
            continue

    elif select == 2:
        print(f"""seu pedido:
                {pedidos}""")
        continue

    elif select == 3:
        v = pedidos.count("pao com ovo")
        s = pedidos.count("suco de caju")

        pao += v
        suco += s

    
        pedidos.clear()

        continue

    elif select == 4:
        print("espere pelo pedido no balcao")
        break