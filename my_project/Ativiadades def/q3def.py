def vogais(frase):
    frase = frase.lower()
    contador = 0

    for letra in frase:
        if letra in "aeiou":
            contador += 1

    return contador

texto = str(input("digite seu texto ou frase: \n"))
contvogais = vogais(texto)
print(f"sua frase tem {contvogais} vogais ")