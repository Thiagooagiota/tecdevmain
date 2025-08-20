while True:
    nm = int(input("digita teu numero \n"))

    if nm <= 0:
        print("digite um numero maior que zero")
        continue
    else:
        break
while nm > 0:
    nm -= 1
    print(nm)