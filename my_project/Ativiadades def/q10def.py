def lm( lim, mul):
    contador = 0
    for i in lim:
        if i % mul == 0:
            contador += 1
    return contador

limite = int(50)
multiplo = int(2)
total = lm(limite, multiplo)
print(f"a quantidade de numeros divisiveis por {multiplo} que vao ate {limite} é: {total}")