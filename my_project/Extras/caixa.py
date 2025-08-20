n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

valorOriginal = float(input("digite o valor de saque: \n"))

valorrestante = valorOriginal

if valorrestante >= 100:
    n100 = int(valorrestante / 100)
    valorrestante = valorrestante - (n100 * 100)

if valorrestante >= 50:
    n50 = int(valorrestante / 50)
    valorrestante = valorrestante - (n50 * 50)
if valorrestante >= 20:
    n20 = int(valorrestante / 20)
    valorrestante = valorrestante - (n20 * 20)
if valorrestante >= 10:
    n10 = int(valorrestante / 10)
    valorrestante = valorrestante - (n10 * 10)
if valorrestante >= 5:
    n5 = int(valorrestante / 5)
    valorrestante = valorrestante - (n5 * 5)
if valorrestante >= 2:
    n2 = int(valorrestante / 2)
    valorrestante = valorrestante - (n2 * 2)

print(f""" as notas retiradas foram:
    
    notas de 100 : {n100}
    notas de 50 : {n50}
    notas de 20 : {n20}
    notas de 10 : {n10}
    notas de 5 : {n5}
    notas de 2 : {n2}

    troco: {valorrestante:.2f}""")