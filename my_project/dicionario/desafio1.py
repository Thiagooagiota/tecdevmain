while True:
    traduzir = {"ola": "привет", "obrigado": "Спасибо", "porfavor": "пожалуйста"}

    palavra = input("digite sua palavra em pt-br\n").strip().lower()


    if palavra in traduzir:
        print(traduzir[palavra])
    else:
        print("invalida")
        continue