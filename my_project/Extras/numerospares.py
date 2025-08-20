contador = 0
numeros = ""

for num in range(0,201,2):
    if num == 200:
        numeros += str(num)
    else:
        numeros += str(num) + ","
    
    if num % 2 == 0:
        contador += 1
        
print(numeros)
print(f"""a quantidade de numeros pares sao {contador}""")