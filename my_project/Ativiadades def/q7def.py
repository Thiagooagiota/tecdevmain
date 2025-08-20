def maiusculas(frase):
    frase = frase
    contador = 0

    for letra in frase:
        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            contador += 1

    return contador

texto = str(input("digite seu texto ou frase: \n"))
contmaius = maiusculas(texto)
print(f"sua frase tem {contmaius} maiusculas ")