import random
import animacoes
import time


player = input("Digite seu nome\n\n")

pt = {0: player}
ptmembers = {0: player, 1: "cole", 2: "mordak", 3: "miriam", 4: "leo", 5: "lia", 6: "mara"}
itens = {"pedra do renascimento(ressucita o aliado com vida cheia):": 7,
"flor dourada(recupera 450 de hp):": 4,
"nectar de litra(recupera 250 de sp:):": 6,
"calmante(remove furia de um aliado):": 3,
"antidoto(remove veneno de um aliado):": 2,
"fruta dekaja(remove buffs do tipo kaja do inimigo):": 5,
"fruta dekunda(remove debuffs de do tipo kunda dos aliados):": 5}
status = {player: [60,70,60,55,70], "cole": [57,57,57,80,40], "mordak": [81,40,90,45,75], "miriam": [30,85,45,25,50], "leo": [50,50,70,50,50], "lia": [45,60,50,50,80], "mara": [30,10,70,60,60]}
hp_sp = {player: [900,500], "cole": [900,600], "mordak": [1800,250], "miriam": [750,950], "leo": [1000,550], "lia": [850,700], "mara": [1000,700]}
atual = {player: [900,500], "cole": [900,600], "mordak": [1800,250], "miriam": [750,950], "leo": [1000,550], "lia": [850,700], "mara": [1000,700]}

grim = {player: "Truque sujo", "cole": "aposta arriscada", "mordak": "salvador", "miriam": "benção da sarcerdotisa", "lia": "maldição", "mara": "apoio divino", "leo": "Paralizar"}

descreve ={player: ["ativa uma barreira que devolve o dano ao oponente durante 3 turnos", "aumenta a barra usando magias de dano elemental"],
"cole": [f"50% de chance de ativar o estado apostador indomavel que te dá sp infinito e durante 5 turnos hits criticos são garantidos e nunca erra, ao acabar, o usuario ganha a chance de ativar de novo,\n mas se a aposta falhar o usuario fica no estado de fadiga(não se move por 3 turnos e golpes fisicos sempre dão criticos)","aumenta a barra acertando criticos"],
"mordak": [f"redireciona 25% do dano recebido por todos os aliados para si por 5 turnos","aumenta a barra recebendo dano sem defender"],
"miriam": ["cura totalmente todos os aliados e reduz o proprio hp para 1", "aumenta a barra curando aliados"],
"lia": ["ativa debuff de ataque, defesa e precisão no oponente por 3 turnos", "aumenta a barra debuffando o inimigo"],
"mara": ["ativa buffs de ataque, defesa e precisão a todos os aliados por 3 turnos", "aumenta a barra buffando aliados"],
"leo": ["congela o inimigo por 2 turnos", "aumenta barra causando aflições no inimigo"]}

armas = {player: ["espada de uma mão", 100], "cole": ["soqueiras", 77], "mordak": ["greatsword", 180], "miriam": ["cajado",50], "leo": ["rapieira", 90], "lia": ["familiar canino", 80], "mara": ["arco antigo", 50]}

aflicoes= {0: "furia", 1: "veneno", 2: "silencio", 3: "confusão"}

elementos = {0: "fisico",1: "fogo", 2: "gelo",3: "vento", 4: "raio",5: "maldição", 6:"luz"}
afinidade = {player: ["--","--", "--","--","fr","res","--"],
            "cole": ["res", "res", "--", "fr", "--", "--", "fr"],
            "mordak": ["res", "--", "--","--", "nul","fr", "nul"],
            "miriam": ["--","nul","fr","res", "--", "--", "fr"],
            "leo": ["--", "--", "res", "--", "--", "--", "--"],
            "lia": ["--", "--", "--", "--", "--", "res", "fr"],
            "mara": ["--", "--", "--", "--", "--", "--", "--"]}



def party():
    
    global pt, ptmembers
    
    while True:
        
        questao = input(f"""        
                        deseja adicionar mais um membro a sua party?
                        
                        1 - sim                                 2- não

                                            """)


        print("\033c")


        if questao == "1":
            
            if len(pt) == 4:
                print("\nsua party ja esta cheia\n")
            
            else:
                while True:
                    try:
                        aliado = int(input(f"""
                    
                    selecione um aliado para adicionar a party 
        1 - cole
        2 - mordak
        3 - miriam
        4 - leo
        5 - lia
        6 - mara

        7 - voltar
        """))
    
                        print("\033c")


                        if aliado == 7:
                            break
                        elif aliado in pt:
                            print("\033c")
                            print("\no aliado já está na party\n")
                            continue
                        elif aliado in ptmembers:
                            pt[aliado] = ptmembers[aliado]
                            break
                        else:
                            print("\033c")
                            print("\nselecione um aliado\n")
                            continue
                    except ValueError:
                        print("\nselecione um aliado\n")

        elif questao == "2":
            menu()
        
        else:
            print("\ncomando invalido\n")
            continue
        menu()



def remover_party():
    while True:
        
        pergunta = input("\ndeseja remover membro?\n 1 - sim    2- não\n\n")
        print("\033c")
        if pergunta == "1":
            try:
                remove = int(input(f"""
                            
                            selecione um aliado para adicionar a party 
                1 - cole
                2 - mordak
                3 - miriam
                4 - leo
                5 - lia
                6 - mara

                7- voltar
                """))


                print("\033c")


                if remove == 7:
                    menu()
                elif remove == 0:
                    print("\nselecione um aliado\n")
                    continue
                elif remove in pt:
                    del pt[remove]
                    menu()
                else:
                    print("O aliado não se encontra na party")
                    input("\npressione enter para continuar\n")
                    continue
            except ValueError:
                print("\nselecione um aliado\n")
                continue
        elif pergunta == "2":
            menu()
        else:
            print("\ncomando invalido\n")
            input("\npressione enter para continuar\n")
            continue



def tutorial():
    print()
    print()
    print(f"""      tutorial 

este tutorial tem como inteção explicar as mecânicas apresentadas neste projeto
para facilitar a experiencia do jogador.
""")

    while True:
        print("\033c")
        tutoriais = input(f"""selecione uma opção:

1 - dano de arma e critico
2 - defesa
3 - magias de dano, elementos e afinidades
4 - magias de suporte(buffs,debuffs e curas)
5 - magias de aflição
6 - Grim
7 - itens
8 - queda
9 - one more
10 - status

11 - voltar
                          
                          """)



        if tutoriais == "1":
            print("\033c")
            print("\n armas sempre dão dano fisico comum e são calculados pela força do personagem, dano\ndo tipo fisico é o unico capaz de dar critico que é calculado pela sorte do personagem\n")
            input("pressiona enter para continuar\n")
            continue


        elif tutoriais == "2":
            print("\033c")
            print("\na defesa pode ser utilizada durante o combate para reduzir o dano recebido pela metade\n")
            input("pressiona enter para continuar\n")
        elif tutoriais == "3":
            print("\033c")

            print(f"""
                As magias de dano são utilizadas no combate a custo de sp por magias elementais e hp pelas magias de dano fisico,
                as magias podem conter elementos unicos que são essenciais para o combate já que tanto aliados quanto inimigos tem resistencias e fraquezas
                a determinados tipos de magia
    
                -- = dano normal
                res = resistencia (só toma 25% do dano)
                nul = nulifica (ignora o dano completamente)
                fr = fraqueza (toma 25% a mais dano)
                
                magias fisicas usam o status de força para calcular dano e elementais usam o status de concentração""")
        
            input("\npressiona enter para continuar\n")
    
        elif tutoriais == "4":
            print("\033c")
            print("\n magias de suporte são divididas em 3 categorias:\nmagias de cura: curam o hp do usuario ou de outro combatente\nmagias de buffs: magias que aumentam um status temporariamente\nmagias de debuff: magias que reduzem um status temporariamente")
            input("\npressione enter para continuar\n")

        elif tutoriais == "5":
            print("\033c")
            print("as magias de aflição são magias que causam um efeito negativo a um alvo. esse efeito\n dura por determinada quantidade de turnos e geralmente tem efeitos negativos")
            input("\npressione enter para continuar\n")

        elif tutoriais == "6":
            print("\033c")
            print("o grim é um encantamento unico de cada personagem que pode ser ativado ao encher uma barra que preenchida diferentemente para cada personagem")
            input("\npressione enter para continuar\n")
        
        elif tutoriais == "7":
            print("\033c")
            print("itens são consumiveis de efeitos variados porem são limitados\n")
            input("\npressione enter para continuar\n")

        elif tutoriais == "8":
            print("\033c")
            print(f"""queda é um estado que seu combatente ou um inimigo(não boss) entra ao ser atingido por uma fraqueza ou um critico,\n durante esse estado o personagem toma 25% a mais de dano""")
            input("\npressione enter para continuar\n")

        elif tutoriais == "9":
            print("\033c")
            print("ao atingir / ser atingido em uma fraqueza ou critico(em um não boss) o aliado ou inimigo ganha mais um turno\n")
            input("\npressione enter para continuar\n")

        elif tutoriais == "10":
            print("\033c")
            print(f"""os status são o que representa os atributos do seu persongem ou arma, cada personagem e arma tem status unicos que alteram
                valores durante o combate de forma unica
                
                status do personagem:
                
                
                força(fr) = valor mutiplicado pelo ataque ou magia fisica e a arma para calcular o dano
                
                concentração(ct) = valor mutiplicado para calcular o dano de magias elementais
                
                constituição(con) = valor utilizado calcular o dano recebido
                
                sorte(srt) = valor utilizado para calcular a chance de critico do ataque ou magia(fisica)
                
                precisão(prc) = chance de acerto
                
                status da arma:
                
                dano(dmg) = dano multiplicado pela força
                """)

            input("\npressione enter para continuar\n")
        
        elif tutoriais == "11":
            break
        
    menu()



def status_geral():
    while True:
        try:
            selec = int(input(f"""

                        selecione o aliado do qual você deseja ver os status
            0 - {player}
            1 - cole
            2 - mordak
            3 - miriam
            4 - leo
            5 - lia
            6 - mara

            7- voltar
            """))


            print("\033c")


            if selec == 7:
                menu()

            elif selec in ptmembers:
                nome = ptmembers[selec]
                hp_atual, sp_atual = atual[nome]
                hp_total, sp_total = hp_sp[nome]
                fr, ct, con, srt, prc = status[nome]
                poder = grim[nome]
                desc1, desc2 = descreve[nome]
                arma, dano = armas[nome]

                
                print(f"""Status de {nome}:

HP: {hp_atual}/{hp_total}
SP: {sp_atual}/{sp_total}

Afinidades:

fisico: ({afinidade[nome][0]})          fogo: ({afinidade[nome][1]})
gelo: ({afinidade[nome][2]})              vento: ({afinidade[nome][3]})
raio: ({afinidade[nome][4]})             maldição: ({afinidade[nome][5]})
                        
                luz: ({afinidade[nome][6]})



Arma:

{arma}, {dano} dmg



Atributos:

Força (fr): {fr}
Concentração (ct): {ct}
Constituição (con): {con}
Sorte (srt): {srt}
Precisão (prc): {prc}

grim: {poder}

descrição: {desc1}

ganho de grim: {desc2}
""")
                input("\npressione enter para continuar\n")
                menu()


            else:
                print("numero invalido")
                input("\npressione enter para continuar\n")
                continue
        
        except ValueError:
            
            print("\nselecione um aliado\n")
            continue





class Personagem:

#gaste de: hp,sp, multiplicador, aflicao, buff/debuff, um/varios/todos

    skillsA = {1: ["tarukaja",0,10,1.5,0,1,0], 
                     2: ["rakukaja",0,10,1.5,0,1,0], 
                     3: ["sukukaja",0,10,1.5,0,1,0],
                     4: ["tarunda",0,10,1.5,0,2,0], 
                     5: ["rakunda",0,10,1.5,0,2,0],
                     6: ["sukunda",0,10,1.5,0,2,0],
                     7: ["matarukaja",0,25,1.5,0,1,1],
                     8: ["marakukaja",0,25,1.5,0,1,1],
                     9: ["masukukaja",0,25,1.5,0,1,1],
                     10: ["salvação",0,80,0.45,0,0,1],
                     11: ["ressucitar",0,90,0.30,0,0,0],
                     12: ["surto de raiva",0,70,0,1,0,0],
                     13: ["cegueira",0,120,0,1,0,0],
                     14: ["nuvem de veneno",0,80,0,1,0,0],
                     15: ["concentrar",0,60,2,0,1,0],
                     16: ["carregar",0,75,2,0,1,0],
                     17: ["chuva de cortes",120,0,1.5,0,0,0],
                     18: ["golpe baixo",77,0,1.2,0,0,0],
                     19: ["mil cortes", 85,0,1.5,0,0,0],
                     20: ["perfuração",40,0,1.2,0,0,0],
                     21: ["petalas flamejantes",0,150,1.7,0,0,0],
                     22: ["clima de apostas",0,70,1.5,0,1,2],
                     23: ["geleira",0,80,1.5,0,0,0],
                     24: ["tornado",0,70,1.5,0,0,0],
                     25: ["trovão",0,60,1.5,0,0,0],
                     26: ["Umbra",0,50,1.5,0,0,0],
                     27: ["graça angelical",0,50,1.5,0,0,0],
                     28: ["oratorio",0,70,0.70,0,0,0],
                     29: ["confundir",0,50,0,1,0,0],
                     30: ["cura simples",0,45,0.45,0,0,0]}


    descricao_skills = {1: "aumenta o dano de 1 em 1.5x por 3 turnos",
                        2: "aumenta a defesa de 1 em 1.5x por 3 turnos",
                        3: "aumenta sorte de 1 em 1.5x por 3 turnos",
                        4: "reduz o dano de 1 em 1.5x por 3 turnos",
                        5: "reduz a defesa de 1 em 1.5x por 3 turnos",
                        6: "reduz a sorte de 1 em 1.5x por 3 turnos",
                        7: "aumenta o dano de todos os aliados em 1.5x por 3 turnos",
                        8: "aumenta a defesa de todos os aliados em 1.5x por 3 turnos",
                        9: "aumenta a sorte de todos os aliados em 1.5x por 3 turnos",
                        10: f"cura 45% de hp de todos os aliados",
                        11: f"ressucita um aliado caido com 30% de hp",
                        12: "deixa o inimigo com raiva(atacando apenas com ataques fisicos inimigos aleatorios)\n durante 3 turnos",
                        13: "deixa um inimigo com cegueira(diminui a chance de acertar ataques em 20%) por 3 turnos",
                        14: "deixa um inimigo envenenado(dano continuo a cada turno) por 3 turnos",
                        15: "dobra o proprio dano magico do proximo ataque magico",
                        16: "dobra o proprio dano do proximo ataque fisico",
                        17: "dano fisico moderado a um inimigo",
                        18: "dano fisico leve a um inimigo",
                        19: "dano fisico moderado a um inimigo",
                        20: "dano fisico leve a um inimigo",
                        21: "dano massivo de fogo a um inimigo",
                        22: "dobra a chance de critico de todos em campo",
                        23: "dano moderado de gelo a um inimigo",
                        24: "dano de vento moderado a um inimigo",
                        25: "dano de raio moderado a um inimigo",
                        26: "dano de sombra moderado a um inimigo",
                        27: "dano de luz moderado a um inimigo",
                        28: f"cura 70% de hp de todos um aliado",
                        29: "deixa um inimigo confuso(usando ataques aleatorios) por 3 turnos",
                        30: f"cura 45% de hp de um aliado"}
    
    userskill = {player: [skillsA[], skillsA[], skillsA[], skillsA[], skillsA[], skillsA[], skillsA[], skillsA[],}
    
    def __init__(self, nome):
        self.nome = nome
        self.hp = hp_sp[nome][0]
        self.sp = hp_sp[nome][1]
        self.aflito = []
        self.boost = []

    def critico(self,dano):
        chance = random.randint(1,100)
        critico = dano + random.randint(80,100)
        if chance <= status[self.nome][3]:
            print("\033c")
            print("Dano Critico!")
            time.sleep(0.5)
            return critico
        else:
            return dano


    def ataqueN(self, jogador):
        
        erro = random.randint(1,100)
        if erro >= status[self.nome][4]:
            print(f"{self.nome} erra o golpe")
            return 0
        
        dano_arma = armas[self.nome][1]
        
        dano_total = dano_arma + status[self.nome][0]
        dano_final = self.critico(dano_total)
        print(f"{self.nome} ataca e tira {dano_final} de dano ")
        return dano_final

    def bossstats():
        pass


    def buff_debuff(cls):
        pass
    
    def magias(self, usada):
        pass
    
    def aflingido(self):
        pass








def menu():
    while True:
        print("\033c")
        print(f"""      \nvocê se encontra em frente a barreira força no topo do céu, você vê Moros do lado de dentro te esperando. Agora já não há como voltar atrás\n\n """)

        principal = input("\n 1 - entrar no combate    2 - adicionar membro na party   3 - remover membro da party    4 - checar party  5 - checar itens  6 - checar status dos aliados   \n 7 - abrir tutorial \n")

        if principal == "1":
            pass


        elif principal == "2":
            print("\033c")
            party()


        elif principal == "3":
            print("\033c")
            remover_party()


        elif principal == "4":
            print("\033c")
            print("\nparty atual:")
            for membro in pt:
                print(pt[membro])
            input("\npressione enter para continuar\n")


        elif principal == "5":
            print("\033c")
            print("seus itens:")
            for item, valor in itens.items():
                print(item, valor,"\n")
            input("\npressione enter para continuar\n")


        elif principal == "6":
            status_geral()


        elif principal == "7":
            print("\033c")
            tutorial()
        else:
            print("\033c")
            print("invalido")
            input("\npressione enter para continuar\n")
            continue


menu()