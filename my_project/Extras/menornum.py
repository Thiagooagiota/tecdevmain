
for i in range(5):
    numeros = float(input("digite o numero"))

    if i == 0:
        menor = numeros
    else:
        if numeros < menor:
            menor = numeros
print(menor)