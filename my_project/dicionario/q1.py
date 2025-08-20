infos = {"nome:": "Thiago", "idade:": 19, "sexo:": "desconheço", "altura:": "1,70", "endereço:": "aquela rua la"}

if __name__ == "__main__":


    print(infos)
    print(infos.keys())
    print(infos.items())
    print(infos.values())

    for chave in infos:
        print(chave, infos[chave])
    for chave, valor in infos.items():
        print(chave, valor)
