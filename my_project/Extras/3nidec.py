while True:
    nm1 = int(input("digite seus numero 1 \n"))
    nm2 = int(input("digite seu numero 2 \n"))
    nm3 = int(input("digite seu numero 3 \n"))

    if nm1 > nm2 and nm1 > nm3 and nm2 > nm3:
        print (f"""a ordem decresente é {nm1},{nm2} e {nm3}""")

    elif nm1 > nm2 and nm1 > nm3 and nm3 > nm2:
        print (f"""a ordem decresente é {nm1},{nm3} e {nm2}""")

    elif nm2 > nm1 and nm2 > nm3 and nm1 > nm3:
        print (f"""a ordem decresente é {nm2},{nm1} e {nm3}""")

    elif nm2 > nm1 and nm2 > nm3 and nm3 > nm1:
        print (f"""a ordem decresente é {nm2},{nm3} e {nm1}""")

    elif nm3 > nm2 and nm3 > nm1 and nm1 > nm2:
        print (f"""a ordem decresente é {nm3},{nm1} e {nm2}""")

    elif nm3 > nm2 and nm3 > nm1 and nm2 > nm1:
        print (f"""a ordem decresente é {nm3},{nm2} e {nm1}""")

    else:
        print (f"""digite tres numeros diferentes por favor""")
