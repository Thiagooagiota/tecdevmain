import time
import random

hpboss = 4000
hpplayer = 900
spplayer = 250

edenM = 2
Potion = 4

barreira = 0
defesa = 1

fase = 0
dmgm = 1

charge = 0

while True:
    critico = random.choice(range(1, 11))  # Número aleatório entre 1 e 10
    
    # Pergunta ao jogador o que ele quer fazer
    boss = (f"""""")
    player = int(input(f"""     
            Jüncdīrgardishizid hp:{hpboss}
    
    HP: {hpplayer}/900               SP: {spplayer}/250
    1. ataque  2. defender  3. magia  4. itens
                       """))

    time.sleep(0.5)
    
    if player == 1 and critico == 4:  # Se for um crítico, quando o número sorteado for 4
        hpboss -= 80
        print("ACERTO CRÍTICO! O boss perde 80 de vida. \n")
        time.sleep(0.5)
    elif player == 1:
        missc = random.choice(range(1, 11))  # Sorteio para ver se o ataque falha (10% de chance)
        if missc == 4:
            print("O ataque falhou \n")
        else:
            hpboss -= 50  # Ataque normal
            print("Ataque normal! O boss perde 50 de vida. \n")
            
    if player == 2 and defesa == 1:
        defesa = 2


    if player == 3:
        
        selecmag = int(input(f"""1. ice fang(dano de gelo) por 10sp
    2.recovery(recupera 20% do hp) por 5sp
    3.salvation (chance de 50% de devolver dano) por 70hp
    4.fair trade (troca 50% de hp total por 50% de sp total) por 50%hp total
    5. hell fire (dano de fogo) por 10sp
    6. cross slash (dano fisico com chance de critico) por 30hp
    7. retornar ao menu
          """))
            
        missif = random.choice(range(1,11))
        misssa = random.choice(range(1,11))
        misshf = random.choice(range(1,11))
        misscs = random.choice(range(1,11))
        cscri = random.choice(range(1,6))

        if selecmag == 1 and missif == 5 and spplayer >= 10:
            print ("voce errou")
            spplayer -= 10

        elif selecmag == 1 and missif != 5 and spplayer >= 10:
            hpboss -= 150
            spplayer -= 10

            print("150 de dano")

        elif selecmag == 1 and spplayer < 10:
            print("voce nao tem mana o suficiente")
            time.sleep(0.5)
            continue


        if selecmag == 2 and hpplayer == 900:
            print("seu hp ja esta cheio")
            time.sleep(0.5)
            continue
        
        elif selecmag == 2 and spplayer >= 5:
            hpplayer += round(hpplayer * 0.20)
            spplayer -= 5
            if hpplayer > 900:
                hpplayer = 900
        
        elif selecmag == 2 and spplayer < 5:
            print("voce nao tem mana o suficiente")
            continue

        if selecmag == 3 and hpplayer > 70 and barreira == 0:
            salvtest = random.randint(1,2)
            hpplayer -= 70
            print ("voce perde 70hp em uma aposta perigosa")
            time.sleep(0.5)

            if salvtest == 2:
                print("voce ergue uma barreira")
                barreira += 1

            elif salvtest == 1:
                print("o feitiço falha e a barreira nao funciona")

        elif selecmag == 3 and hpplayer > 70 and barreira == 1:
            print("a barreira ja esta ativada")
            continue


        elif selecmag == 3 and hpplayer <= 70:
            print("voce nao tem hp o suficiente")


        if selecmag == 4 and spplayer == 250:
            print("seu sp esta cheio")
            continue

        elif selecmag == 4 and hpplayer > 450 :
            spplayer += round(250 * 0.50)
            hpplayer -= 200
            if spplayer > 250:
                spplayer = 250

        elif selecmag == 4 and hpplayer <= 450:
            print("voce nao tem hp o suficiente")
            continue

        if selecmag == 5 and spplayer >= 10 and misshf == 5:
            print("voce errou")
            spplayer -= 10
            time.sleep(0.5)

        elif selecmag == 5 and spplayer >= 10 and misshf != 5:
            spplayer -= 10
            hpboss -= 150
            print("150 de dano")
            time.sleep(0.5)

        elif selecmag == 5 and spplayer < 10:
            print("voce nao tem sp o suficiente")
            time.sleep(0.5)
            continue

        if selecmag == 6 and hpplayer > 50 and misscs == 5:
            print("voce errou")
            hpplayer -= 30
            time.sleep(0.5)

        elif selecmag == 6 and hpplayer > 50 and misscs != 5 and cscri != 5:
            print("100 de dano")
            hpplayer -= 30
            hpboss -= 100
            time.sleep(0.5)

        elif selecmag == 6 and hpplayer > 50 and misscs != 5 and cscri == 5:
            print("dano critico")
            print("220 de dano")
            hpplayer -= 30
            hpboss -= 220
            time.sleep(0.5)

        elif selecmag == 6 and hpplayer <= 50:
            print("voce nao tem hp o suficiente")
            time.sleep(0.5)
            continue
            

        if selecmag == 7:
            time.sleep(0.5)
            continue

    if player == 4:
        selecitem = int(input(f"""#1 maça do eden (recupera 100 de sp): {edenM}
#2 poçao de cura(recupera 290 de hp): {Potion}

#3 retornar ao menu 
"""))

        if selecitem == 1 and spplayer < 250 and edenM > 0:
            edenM -= 1
            spplayer += 100
            
            if spplayer > 250:
                spplayer = 250
        
        elif selecitem == 1 and edenM < 1:
            print(" voce nao tem mais maças do eden")
            continue
             
             
        elif selecitem == 1 and spplayer == 250:
            print("seu sp esta cheio")
            continue
             
             
             
        if selecitem == 2 and hpplayer < 900 and Potion > 0:
            Potion -= 1
            hpplayer += 290
            if hpplayer > 900:
                hpplayer = 900
        
        elif selecitem == 2 and hpplayer == 900:
            print("seu hp esta cheio")
            time.sleep(0.5)
            continue
            
        elif selecitem == 2 and Potion < 1:
            print("suas poçoes acabaram")
            time.sleep(0.5)
            continue


        if selecitem == 3:
            continue



        #boss


    #fase 1: ataques fracos com vida acima de 3500
    
    if fase == 0 and hpboss >= 3500:
        bsc = random.randint(1,2)


        if bsc == 1:
            print("Jüncdīrgardishizid te assiste enquanto zomba de você")
            time.sleep(0.5)

        if bsc == 2:
            print("Jüncdīrgardishizid ergue seu braço e usa um soco poderoso no chão")
            time.sleep(0.5)
            if barreira == 1:
                hpboss -= 20 / defesa
                barreira = 0

                if defesa == 1:
                    print("o ataque é refletido de volta")
                    time.sleep(0.5)
                    print("20 de dano")
                    time.sleep(0.5)

                elif defesa == 2:
                    print("o ataque é refletido de volta")
                    time.sleep(0.5)
                    print("20 de dano")
                    time.sleep(0.5)

            
            elif barreira == 0:
                hpplayer -= 20 / defesa
                if defesa == 1:
                    print("você toma 20 de dano")
                    time.sleep(0.5)
                elif defesa == 2:
                    print("você toma 10 de dano")
                    time.sleep(0.5)
    
    elif hpboss < 3500 and fase == 0:
        print("vamos acabar com essa brincadeira")
        time.sleep(0.5)
        print("Jüncdīrgardishizid recupera seu hp")
        hpboss = 4000
        fase = 1
    
    
    if fase == 1 and charge == 0:
        attchoice = random.randint(1,6)
        missboss = random.randint(1,10)

        
        
        if attchoice == 1 and dmgm == 1:
            print(f"""Jüncdīrgardishizid concentra poder para o proximo ataque""")
            time.sleep(0.5)
            print(f"""Dano dobrado no proximo turno""")
            dmgm += 1
        elif attchoice ==1 and dmgm != 1:
            attchoice = random.randint(3,6)




        if attchoice == 2 and hpboss < 3000 and dmgm == 1 and hpplayer <= 500:
            bop = random.randint(1,2)
            print('Jüncdīrgardishizid usa a magia "desejo"')
            time.sleep(0.5)
            desej = int(input(f"""voce se recorda das palavras de seu mestre *"a magia desejo não pode ser utilizada por quem a conjura
você deve fazer um pedido e ele será concedido aleatoriamente a você ou ao conjurador, é um movimento que só é usado para momentos de
desespero ou caçoar do oponente"*

                                qual o seu pedido?
1- Recupere minhas forças(cura sua vida completamente ou 500 de hp do boss) 2 - recupere minha magia (recupera seu sp completamente ou dobra o dano do boss)
                                                                
                                                                3- negar desejo
"""))
            if desej == 1 and bop == 1:
                hpplayer = 900
                print("você é escolhido e seu HP é restaurado")
                time.sleep(0.5)
            elif desej == 1 and bop == 2:
                hpboss += 500
                print("Jüncdīrgardishizid é escolhido e recupera 500 de HP")
                time.sleep(0.5)
            elif desej == 2 and bop == 1:
                spplayer = 250
                print("você é escolhido e seu SP é restaurado")
                time.sleep(0.5)
            elif desej == 2 and bop == 2:
                dmgm += 1
                print("Jüncdīrgardishizid é escolhido e recupera 500 de HP")
                time.sleep(0.5)
            elif desej == 3:
                attchoice = random.randint(3,6)


        elif attchoice == 2 and hpboss > 3000 or attchoice == 2 and dmgm == 2 or attchoice == 2 and hpplayer > 500:
            attchoice = random.randint(3,6)




        if attchoice == 3 and missboss != 5 and barreira == 0:
            print(f"""Jüncdīrgardishizid invoca uma chuva de meteoros""")
            hpplayer -= (120 / defesa) * dmgm
            time.sleep(0.5)

            if defesa == 1 and dmgm == 1:
                print(f"""120 de dano""")
                time.sleep(0.5)
            elif defesa == 2 and dmgm == 1:
                print(f"""60 de dano""")
                time.sleep(0.5)
            elif defesa == 1 and dmgm == 2:
                print(f"""240 de dano""")
                time.sleep(0.5)
                dmgm -= 1
            elif defesa == 2 and dmgm == 2:
                print(f"""120 de dano""")
                time.sleep(0.5)
                dmgm -= 1

            
        elif attchoice == 3 and missboss != 5 and barreira == 1:
            print(f"""Jüncdīrgardishizid invoca uma chuva de meteoros""")
            hpboss -= (120 / defesa) * dmgm
            time.sleep(0.5)
            print("Mas sua barreira devolve todos para ele com força total")
            time.sleep(0.5)
            barreira -= 1

            if defesa == 1 and dmgm == 1:
                print(f"""120 de dano""")
                time.sleep(0.5)
                barreira -= 1
            elif defesa == 2 and dmgm == 1:
                print(f"""60 de dano""")
                time.sleep(0.5)
                barreira -= 1
            elif defesa == 1 and dmgm == 2:
                print(f"""240 de dano""")
                time.sleep(0.5)
                dmgm -= 1
                barreira -= 1
            elif defesa == 2 and dmgm == 2:
                print(f"""120 de dano""")
                time.sleep(0.5)
                dmgm -= 1
                barreira -= 1
            

        if attchoice == 3 and missboss == 5:
            print(f"""Jüncdīrgardishizid invoca uma chuva de meteoros""")
            time.sleep(0.5)
            print ("Mas voce desvia com excelencia")
            time.sleep(0.5)
            print("Jüncdīrgardishizid: Rato imundo")


        if attchoice == 4 and missboss != 5:
            bcr = random.randint(1,20)
            print("Jüncdīrgardishizid: ergue sua mao direita carregada com uma energia poderosa")
            time.sleep(0.5)
            print("ele acerta você com toda a força")
            time.sleep(0.5)

            if bcr != 5 and barreira == 0:

                hpplayer -= (50 / defesa) * dmgm

                if defesa == 1 and dmgm == 1:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                elif defesa == 2 and dmgm == 1:
                    print(f"""25 de dano""")
                    time.sleep(0.5)
                elif defesa == 1 and dmgm == 2:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                elif defesa == 2 and dmgm == 2:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
            
            elif bcr != 5 and barreira == 1:

                hpboss -= (50 / defesa) * dmgm
                print("a barreira devolve o golpe")

                if defesa == 1 and dmgm == 1:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                    barreira = 0
                elif defesa == 2 and dmgm == 1:
                    print(f"""25 de dano""")
                    time.sleep(0.5)
                    barreira = 0
                elif defesa == 1 and dmgm == 2:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira = 0
                elif defesa == 2 and dmgm == 2:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira = 0


            elif bcr == 5 and barreira == 0:

                hpplayer -= (100 / defesa) * dmgm
                print("dano critico")
                time.sleep(0.5)
                if defesa == 1 and dmgm == 1:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                elif defesa == 2 and dmgm == 1:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                elif defesa == 1 and dmgm == 2:
                    print(f"""200 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                elif defesa == 2 and dmgm == 2:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                print("Jüncdīrgardishizid: esse é o poder de um deus")

            elif bcr == 5 and barreira == 1:
                print("a barreira defende e o dano e devolvido")
                print("dano critico")
                time.sleep(0.5)
                hpboss -= 100 * dmgm

                if defesa == 1 and dmgm == 1:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                    barreira -= 1
                elif defesa == 2 and dmgm == 1:
                    print(f"""50 de dano""")
                    time.sleep(0.5)
                    barreira -= 1
                elif defesa == 1 and dmgm == 2:
                    print(f"""200 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira -= 1
                elif defesa == 2 and dmgm == 2:
                    print(f"""100 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira -= 1


                print("Jüncdīrgardishizid: esse é o poder de um deus")
    
        if attchoice == 4 and missboss == 5:
            print("Jüncdīrgardishizid: ergue sua mao direita carregada com uma energia poderosa")
            time.sleep(0.5)
            print("você se esquiva do soco dele por pouco")
            time.sleep(0.5)
            print("Jüncdīrgardishizid: Morra de uma vez, inseto")


        
        if attchoice == 5:
            print(f"""Jüncdīrgardishizid: PATETICO""")
            time.sleep(0.5)
            print(f"""Jüncdīrgardishizid joga uma de suas esferas de energia""")

            if missboss == 5:
                print(f"""Mas erra""")
                time.sleep(0.5)
            elif missboss != 5 and barreira == 0:
                print(f"""A esfera explode e você sente uma dor excruciante""")
                time.sleep(0.5)
                hpplayer -= (90 / defesa) * dmgm
                
                if defesa == 1 and dmgm == 1:
                    print(f"""90 de dano""")
                    time.sleep(0.5)
                elif defesa == 2 and dmgm == 1:
                    print(f"""45 de dano""")
                    time.sleep(0.5)
                elif defesa == 1 and dmgm == 2:
                    print(f"""180 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                elif defesa == 2 and dmgm == 2:
                    print(f"""90 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                
                
            elif missboss != 5 and barreira == 1:
                print(f"""A esfera atinge fortemente a barreira erguida quase a atravessando mas falha e é refletida""")
                time.sleep(0.5)
                hpboss -= (90 / defesa) * dmgm

                if defesa == 1 and dmgm == 1:
                    print(f"""90 de dano""")
                    time.sleep(0.5)
                    barreira -= 1
                elif defesa == 2 and dmgm == 1:
                    print(f"""45 de dano""")
                    time.sleep(0.5)
                    barreira -= 1
                elif defesa == 1 and dmgm == 2:
                    print(f"""180 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira -= 1
                elif defesa == 2 and dmgm == 2:
                    print(f"""90 de dano""")
                    time.sleep(0.5)
                    dmgm -= 1
                    barreira -= 1



        if attchoice == 6:
            charge += 3
            print("Jüncdīrgardishizid levanta ambas as mãos e começa a carregar um ataque massivo")




    elif fase == 1 and charge > 1:
        print("a esfera fica maior")
        charge -= 1

    elif fase == 1 and charge == 1:
        print("Jüncdīrgardishizid joga a esfera em voce com toda força")
        charge-= 1

        if defesa == 1 and barreira == 0:
            print("você é acertado por um ataque devastador")
            time.sleep(0.5)
            print("você não aguenta o ataque de peito aberto")
            hpplayer = 0
        if defesa == 2 and barreira == 0:
            print("você é acertado por um ataque devastador")
            time.sleep(0.5)
            print("você defende diminuindo o impacto")
            hpplayer -= 200
        if defesa == 1 and barreira == 1:
            print("você é acertado por um ataque devastador")
            time.sleep(0.5)
            barreira -= 1
            print("o ataque volta para Jüncdīrgardishizid mas ele simplesmente o absorve")
        if defesa == 2 and barreira == 1:
            print("você é acertado por um ataque devastador")
            time.sleep(0.5)
            barreira -= 1
            print("o ataque volta para Jüncdīrgardishizid mas ele simplesmente o absorve")








    if defesa == 2:
        defesa = 1
    
    if hpplayer <= 0:
        print("você morreu")
        break
    
    # Verifica se o boss foi derrotado
    if hpboss <= 0:
        print("Você derrotou o boss!")
        break
    
    time.sleep(1)  # Pausa para a próxima ação

