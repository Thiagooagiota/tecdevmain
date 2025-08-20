while True:

    cargo = input("digite seu cargo \n").strip().lower()


    if cargo == "gerente":
        print("voce é o gerente da loja")
        break

    elif cargo == "estoquista":
        print("voce é o estoquista da loja")
        break

    elif cargo == "vendedor":
        print("voce é o vendedor da loja")
        break 


    else:
        print("invalido")

salario = float(input("digite seu salario \n"))

while True:

    if cargo == "gerente" and salario > 0:
        salarioebonus = (salario * 0.15) + (salario)

        break
    elif cargo == "estoquista" and salario > 0:
        salarioebonus = (salario * 0.10) + (salario)
        break
    elif cargo == "vendedor" and salario > 0:
        salarioebonus = (salario * 0.25) + (salario)
        break
    else:
        print("invalido")

print (f"""seu cargo é:
    {cargo}

e seu salario + seu bonus é igual a:

    {salarioebonus:.2f}
""")