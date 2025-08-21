import os
from tutorial import show_tutorial
from combat import start_combat
from data import items_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu(player, allies_data, grim_descriptions, items_data, skills_data, skill_descriptions, affinities_data, weapons_data):
    while True:
        clear_screen()
        print("Você se encontra em frente ao selo deixado por Moros. Não há mais volta.")

        choice = input("""
1 - entrar no combate
2 - adicionar membro na party
3 - remover membro da party
4 - checar party
5 - checar itens
6 - checar status dos aliados
7 - abrir tutorial

Escolha: """).strip()

        if choice == "1":
            clear_screen()
            print("Você decide entrar no combate, boa sorte!")
            start_combat(player)
            break  # Ou continuar dependendo do fluxo do jogo

        elif choice == "2":
            player.add_member(allies_data)

        elif choice == "3":
            player.remove_member()

        elif choice == "4":
            clear_screen()
            print("Membros atuais na party:")
            for id, member in player.party_members.items():
                print(f"{id} - {member}")
            input("pressione enter para continuar")

        elif choice == "5":
            clear_screen()
            print("Itens disponíveis:\n")
            for key, item in items_data.items():
                print(f"{item[0]} - Quantidade: {item[1]}")
            input("\npressione enter para continuar")

        elif choice == "6":
            player.view_status(allies_data, grim_descriptions, skills_data, affinities_data, weapons_data)

        elif choice == "7":
            show_tutorial()

        else:
            clear_screen()
            print("Opção inválida.")
            input("\npressione enter para continuar")