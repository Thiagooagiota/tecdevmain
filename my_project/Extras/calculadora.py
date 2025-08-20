soma = 0
cont = str(input("digite sair se quiser encerrar ou clique enter para continuar \n")).strip().lower()
    
while cont != "sair":
    num1 = float(input("digite o primeiro numero"))
    num2 = float(input("digite o segundo numero"))
    selec = float(input("escolha a sua operaçao \n" \
    "1- adiçao, 2- subtraçao, 3- multiplicaçao, 4- divisao"))

    if selec == 1:

        resultado = num1 + num2

        print(f"""resultado: {resultado}""")

    elif selec == 2:
    
        resultado = num1 - num2

        print(f"""resultado: {resultado}""")

    elif selec == 3:
    
        resultado = num1 * num2

        print(f"""resultado: {resultado}""")

    elif selec == 4:

        if num1 != 0 and num2 != 0:
            resultado = num1 / num2
            print(f"""resultado: {resultado}""")

        elif num1 == 0 or num2 == 0:
            print("é 0, agora nunca mais tente dividir por zero em um codigo meu")

    else:
        print("comando invalido")
        continue
    
    cont = str(input("digite sair se quiser encerrar ou clique enter para continuar \n")).strip().lower()





if cont == "sair":
    print("programa encerrado")

