qtd = int(input("quantos numeros deseja na media"))
soma = 0

for i in range(qtd):
    n = int(input(f"digite o numero {i}: "))
    soma = soma + n
    
media = soma/qtd
print(f"a media é: {media}")