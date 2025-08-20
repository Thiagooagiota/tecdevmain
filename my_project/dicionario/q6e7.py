inf = {"jao": "19", "marquin": "32", "thiago": "69", "rodrigo": "17", "danilo": "41"}

if __name__ == "__main__":

    for nome in inf:
        print(nome,inf[nome])

    name = input("digita o nome \n").strip().lower()

    if name in inf:
        print("ta na lista")
    else:
        print("nao esta na lista")