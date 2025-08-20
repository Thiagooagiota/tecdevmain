soma = 0
numero = 0

while numero >= 0:
    numero = int(input(" digite um numero positivo para somar ou um negativo para encerrar \n \n"))
    soma += numero

    if numero >= 0:
        print("\n", soma)
    else:
        print("encerrado")