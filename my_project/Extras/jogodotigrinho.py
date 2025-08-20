import random

while True:
    numero = random.randint(1,10)

    tentativa = int(input("digite seu numero de 1 a 10 \n"))

    if tentativa < 1 or tentativa > 10:
        print("numero invalido") 
        continue
    elif tentativa == numero:
        print("voce ganhou \n")
    elif tentativa > numero:
        tentativa2 = int(input("tente novamente um pouca mais para baixo \n"))
        
    else:
        tentativa2 = int(input("tente novamente um pouca mais para cima \n"))
    
    
    if tentativa2 < 1 or tentativa > 10:
        print("numero invalido") 
        continue
    elif tentativa2 == numero:
        print("voce ganhou \n")
    elif tentativa2 > numero:
        tentativa3 = int(input("tente novamente mais para baixo \n"))
        
    else:
        tentativa3 = int(input("tente novamente mais para cima \n"))
        

    if tentativa < 1 or tentativa > 10:
        print("numero invalido") 
        continue
    elif tentativa3 == numero:
        print("voce ganhou")
    else:
        print(f"voce perdeu, o numero era {numero}")