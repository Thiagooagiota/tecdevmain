while True:
    dc = int(input("escolha o desafio 1 ou 2: "))

    if dc == 2:
    #desafio 2
        listapar = []
        listaimp = []
        listato = []


        for i in range(20):
            numero = int(input("digite seu numero \n"))
            listato.append(numero)
            if numero % 2 == 0:
                listapar.append(numero)
            else:
                listaimp.append(numero)


        print("lista impar:", listaimp)
        print("lista par: ", listapar)
        print("lista total: ", listato)

    #desafio 1
    elif dc == 1:

        lista1 = [1,242,35,94,69,37,72]

        def sub_num(lista):
            for i in range(len(lista)):
                if lista[i] % 2 == 0:
                    lista[i] = 0
            return lista


        
        t = sub_num(lista1)
        print(t)

    else:
        print("invalido")
        continue
