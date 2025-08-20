for i in range(5):
    numeros = float(input("digite o numero"))

    if i == 0:
        maior = numeros
    else:
        if numeros > maior:
            maior = numeros
print(maior)