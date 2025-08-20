
nsenha = 3
lista = [0,1,2,3]
novo = 0
while True:
    input("pressiona enter para iniciar o programa")
    while True:
        
        selec = input(f"""ESCOLHA UMA OPÇÃO
                    1 - criar nova senha
                    2 - chamar senha
                    3 - encerrar
                    """)
        if selec == "1":
            nsenha += 1
            lista.append(nsenha)
            print("numeros restantes", lista)
            continue
        elif selec == "2":
            # index = lista.index(novo)
            # lista.remove(index)
            # puxado += 1
            # novo += 1
            # nindex = lista.index(puxado)
            # print(f"""NUMERO: {nindex}""")
            # continue
            if len(lista) == 0:
                print("não há mais senhas disponiveis")
            else:
                index = lista.pop(0)
                print(f"""NUMERO: {index}""")
                print("numeros restantes", lista)

        
        elif selec == "3":
            print("programa encerrado")
            break

