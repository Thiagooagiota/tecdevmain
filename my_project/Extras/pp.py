numero = int(input("Digite um número para verificar se é primo: "))

if numero < 2:
    print(f"{numero} não é primo.")
else:
    divisor = 2
    contador = 0

    while divisor <= numero // 2:
        if numero % divisor == 0:
            contador += 1
        divisor += 1

    if contador == 0:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")