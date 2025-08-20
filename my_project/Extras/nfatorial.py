while True:
    num = int(input("digite o numero final"))

    resultado = 1

    for i in range(1,num + 1):
        resultado *= i

    print(resultado)

