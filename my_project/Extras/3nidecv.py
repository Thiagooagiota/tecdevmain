nm1 = int(input("digite seus numero 1 \n"))
nm2 = int(input("digite seu numero 2 \n"))
nm3 = int(input("digite seu numero 3 \n"))

numeros = [nm1,nm2,nm3]
numeros.sort(reverse=True)

print(f"""{numeros}""")