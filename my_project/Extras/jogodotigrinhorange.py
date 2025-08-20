import random
numero = random.randint(1,10)

tentativas = 3

while True:

    for i in range(tentativas):
        tentativa = int(input("digite seu numero de 1 a 10 \n"))

        if tentativa < 1 or tentativa > 10:
            print("numero invalido")
            tentativas += 1
            continue
        elif tentativa == numero:
            print("parabens, voce ganhou")
            break
        elif tentativa < numero:
            print("tente novamente com um numero mais alto")
            
        else:
            print("tente novamente com um numero mais baixo")
    
    if tentativas > 3:
        print(f"""//////////////

        VOCE PERDEU
////////////////""")




