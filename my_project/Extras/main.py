numeros = []

qtd = int(input("digite quantos numeros deseja calcular"))
for i in range(qtd):
    num = int(input("digite um numero"))
    numeros.append(num)
    
media = sum(numeros)/len(numeros)

print(f"a media é: {media}")