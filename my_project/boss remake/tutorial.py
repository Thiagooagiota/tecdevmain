import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_tutorial():
    print("""
      Tutorial

Este tutorial tem como intenção explicar as mecânicas apresentadas neste projeto
para facilitar a experiência do jogador.
""")

    while True:
        clear_screen()
        option = input("""
Selecione uma opção:

1 - Dano de arma e crítico
2 - Defesa
3 - Magias de dano, elementos e afinidades
4 - Magias de suporte (buffs, debuffs e curas)
5 - Magias de aflição
6 - Grim
7 - Itens
8 - Queda
9 - One More
10 - Status

11 - Voltar

Escolha: """).strip()

        if option == "1":
            clear_screen()
            print("""
Armas sempre causam dano físico comum, calculado pela força do personagem.
O dano do tipo físico é o único capaz de causar crítico, que é calculado pela sorte do personagem.
""")
            input("Pressione enter para continuar\n")

        elif option == "2":
            clear_screen()
            print("""
A defesa pode ser utilizada durante o combate para reduzir o dano recebido pela metade.
""")
            input("Pressione enter para continuar\n")

        elif option == "3":
            clear_screen()
            print("""
As magias de dano são utilizadas no combate a custo de SP para magias elementais e HP para magias de dano físico.
As magias podem conter elementos únicos que são essenciais para o combate, já que tanto aliados quanto inimigos têm resistências e fraquezas a determinados tipos de magia:

-- = dano normal
res = resistência (só toma 25% do dano)
nul = nulifica (ignora o dano completamente)
fr = fraqueza (toma 25% a mais de dano)

Magias físicas usam o status de força para calcular dano, e elementais usam o status de concentração.
""")
            input("Pressione enter para continuar\n")

        elif option == "4":
            clear_screen()
            print("""
Magias de suporte são divididas em 3 categorias:
- Magias de cura: curam o HP do usuário ou de outro combatente.
- Magias de buffs: aumentam um status temporariamente.
- Magias de debuff: reduzem um status temporariamente.
""")
            input("Pressione enter para continuar\n")

        elif option == "5":
            clear_screen()
            print("""
As magias de aflição causam um efeito negativo a um alvo. Esse efeito dura por uma quantidade determinada de turnos e geralmente tem efeitos negativos.
""")
            input("Pressione enter para continuar\n")

        elif option == "6":
            clear_screen()
            print("""
O Grim é um encantamento único de cada personagem que pode ser ativado ao encher uma barra, que é preenchida diferentemente para cada personagem.
""")
            input("Pressione enter para continuar\n")

        elif option == "7":
            clear_screen()
            print("""
Itens são consumíveis de efeitos variados, porém são limitados.
""")
            input("Pressione enter para continuar\n")

        elif option == "8":
            clear_screen()
            print("""
Queda é um estado que seu combatente ou um inimigo (não boss) entra ao ser atingido por uma fraqueza ou um crítico. Durante esse estado, o personagem toma 25% a mais de dano.
""")
            input("Pressione enter para continuar\n")

        elif option == "9":
            clear_screen()
            print("""
Ao atingir ou ser atingido em uma fraqueza ou crítico (em um não boss), o aliado ou inimigo ganha mais um turno.
""")
            input("Pressione enter para continuar\n")

        elif option == "10":
            clear_screen()
            print("""
Os status representam os atributos do seu personagem ou arma. Cada personagem e arma tem status únicos que alteram valores durante o combate de forma única:

Status do personagem:
- Força: valor multiplicado pelo ataque ou magia física e a arma para calcular o dano.
- Concentração: valor multiplicado para calcular o dano de magias elementais.
- Resistência: valor utilizado para calcular o dano recebido.
- Sorte: valor utilizado para calcular a chance de crítico do ataque ou magia (física).
- Precisão: chance de acerto.

Status da arma:
- Dano (dmg): dano multiplicado pela força.
""")
            input("Pressione enter para continuar\n")

        elif option == "11":
            break

        else:
            clear_screen()
            print("Opção inválida.")
            input("Pressione enter para continuar\n")