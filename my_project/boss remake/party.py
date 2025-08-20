import os
from data import allies_data, grim_descriptions, skills_data, affinities_data, weapons_data,player_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Party:
    def __init__(self, name, hp, max_hp, sp, max_sp, stats, skills, grim, affliction, affinities, weapon):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.sp = sp
        self.max_sp = max_sp
        self.stats = stats  # [força, concentração, resistência, sorte, precisão]
        self.skills = skills
        self.grim = grim
        self.affliction = affliction
        self.affinities = affinities
        self.weapon = weapon
        self.party_members = {1: self.name}  # Jogador sempre na party

    def add_member(self, allies_data):
        options = {
            "1": "cole",
            "2": "mordak",
            "3": "miriam",
            "4": "leo",
            "5": "lia",
            "6": "mara"
        }

        while True:
            clear_screen()
            print("""
Escolha o membro que deseja adicionar:

1 - cole
2 - mordak
3 - miriam
4 - leo
5 - lia
6 - mara

7 - voltar
""")
            add_member = input("Escolha: ").strip()

            if add_member == "7":
                break

            if add_member in options:
                member_name = options[add_member]
                if member_name in self.party_members.values():
                    clear_screen()
                    print("Esse membro já está na party!")
                    input("pressione enter para continuar")
                    continue

                if len(self.party_members) < 4:
                    clear_screen()
                    self.party_members[len(self.party_members) + 1] = member_name
                    print(f"{member_name} adicionado com sucesso!")
                    input("pressione enter para continuar")
                else:
                    clear_screen()
                    print("A party já está cheia (máximo 4 membros).")
                    input("pressione enter para continuar")
            else:
                clear_screen()
                print("Opção inválida. Tente novamente.")
                input("pressione enter para continuar")

    def remove_member(self):
        while True:
            clear_screen()
            print("Membros atuais na party:")
            for id, member in self.party_members.items():
                print(f"{id} - {member}")
            print("\n7 - voltar")

            if len(self.party_members) == 1:
                print("A party só tem o jogador, que não pode ser removido.")
                input("pressione enter para continuar")
                return

            try:
                remove = int(input("Digite o ID do membro que deseja remover: "))
                if remove == 7:
                    break
                if remove == 1:
                    clear_screen()
                    print("O jogador não pode ser removido da party!")
                    input("pressione enter para continuar")
                    continue
                if remove in self.party_members:
                    member_name = self.party_members[remove]
                    clear_screen()
                    print(f"{member_name} removido com sucesso!")
                    del self.party_members[remove]
                    input("pressione enter para continuar")
                else:
                    clear_screen()
                    print("Membro inválido. Tente novamente.")
                    input("pressione enter para continuar")
            except ValueError:
                clear_screen()
                print("Entrada inválida. Por favor, digite um número válido.")
                input("pressione enter para continuar")

    def view_status(self, allies_data, grim_descriptions, skills_data, affinities_data, weapons_data):
            
        while True:
            clear_screen()
            print("Aliados disponíveis:")
            for name in allies_data:
                print(f"- {name}")
            print("\nDigite o nome do aliado para ver status ou 'voltar' para sair.")

        
            choice = input("Escolha: ").strip().lower()
            if choice == 'voltar':
                break
            if choice in allies_data or choice == self.name:
                info = allies_data.get(choice, {
                    'hp': self.hp, 'max_hp': self.max_hp, 'sp': self.sp, 'max_sp': self.max_sp,
                    'stats': self.stats, 'skills': self.skills, 'grim': self.grim
                })
                grim_desc = grim_descriptions[info['grim']]
                skill_names = [skills_data[skill_id][0] for skill_id in info['skills']]
                skill_descs = [skills_data[skill_id][3] for skill_id in info['skills']]
                affinities = affinities_data.get(choice, self.affinities)
                weapon = weapons_data.get(choice, self.weapon)

                print(f"""
{choice.capitalize()}:

HP: {info['hp']}/{info['max_hp']}       SP: {info['sp']}/{info['max_sp']}

Arma: {weapon[0]} - Dano: {weapon[1]}

Afinidades:
Fisico: {affinities[0]}
Fogo: {affinities[1]}
Gelo: {affinities[2]}
Vento: {affinities[3]}
Raio: {affinities[4]}
Maldição: {affinities[5]}
Luz: {affinities[6]}

Status:
Força: {info['stats'][0]}
Concentração: {info['stats'][1]}
Resistência: {info['stats'][2]}
Sorte: {info['stats'][3]}
Precisão: {info['stats'][4]}

Magias:
""")
                for i in range(len(skill_names)):
                    print(f"{skill_names[i]} ({skill_descs[i]})\n")

                print(f"\nGrim: {info['grim']}\n\nEfeito: {grim_desc[0]}\n\nGanho de barra: {grim_desc[1]}")
                input("\npressione enter para continuar")
            else:
                clear_screen()
                print("Aliado inválido.")
                input("pressione enter para continuar")
                continue