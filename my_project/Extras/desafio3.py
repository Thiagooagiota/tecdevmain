lista = []
for i in range(10):
    numeros = float(input("digite sua temperatura:  "))
    lista.append(numeros)

media = sum(lista) / len(lista)
tempac = []
for temp in lista:
    if temp > media:
        tempac.append(temp)
print(f"temperaturas maior que a media:  {tempac}")
print(f"media de temperatura:  {media}")