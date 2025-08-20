nm1 = int(input("digite seus numero 1 \n"))
nm2 = int(input("digite seu numero 2 \n"))
nm3 = int(input("digite seu numero 3 \n"))

if nm1 > nm2 and nm1 > nm3:
    print (f"""o maior numero e {nm1}""")
elif nm2 > nm1 and nm2 > nm3:
    print (f"""o maior numero e {nm2}""")
elif nm3 > nm2 and nm3 > nm1:
    print (f"""o maior numero e {nm3}""")
elif nm1 == nm2 and nm1 == nm3:
    print (f"""os tres numeros sao iguais {nm1}""")
elif nm1 == nm2:
    print (f"""o numero 1 e o numero 2 sao os maiores {nm1}""")
else:
    print(f"""o numero 2 e o numero 3 sao maiores que o 1 {nm2}""")