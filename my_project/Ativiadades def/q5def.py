def palindromo(palavra):
    palavra = palavra.lower()

    inversao = palavra[::-1]
    return palavra == inversao

while True:
    palavra = input("escreva o palindromo \n")
    if palindromo(palavra):
        print("é palindromo")
    else:
        print("nao é palindromo")