palavra = str(input("digite a palavra").replace(" ","").replace("   ", ""))
contagem = 0

for letra in palavra:
    contagem += 1

    print(contagem)