import random

while True:
    
    
    numeros = []

    input("pressione enter para lançar o dado 100 vezes \n")

    for i in range(100):
        nums = random.randint(1,6)
        numeros.append(nums)

    n1 = numeros.count(1)
    n2 = numeros.count(2)
    n3 = numeros.count(3)
    n4 = numeros.count(4)
    n5 = numeros.count(5)
    n6 = numeros.count(6)

    print(f"""o numero 1 apareceu {n1} vezes
o numero 2 apareceu {n2} vezes
o numero 3 apareceu {n3} vezes
o numero 4 apareceu {n4} vezes
o numero 5 apareceu {n5} vezes
o numero 6 apareceu {n6} vezes""")
