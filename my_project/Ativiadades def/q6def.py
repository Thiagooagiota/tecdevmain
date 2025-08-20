def contar(numero):
    return len(str(abs(int(numero))))

n = input("seu numero \n")
total = contar(n)
print(f"seu numero tem {total} digitos")