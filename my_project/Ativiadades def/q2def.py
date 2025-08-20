def numeros():
    numli = []

    for i in range(4):
        num = int(input("seu numero \n"))
        numli.append(num)

        total = sum(numli)

    media = total / 4

    return media
    
print(numeros())

