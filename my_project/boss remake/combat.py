import random
import time
import os
from data import items_data, skills_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Combat:
    def __init__(self, party_manager):
        self.party_manager = party_manager
        self.boss_hp = 10000
        self.boss_affinities = ["--", "--", "--", "--", "--", "fr", "fr"]
        self.defending = {member_id: False for member_id in party_manager.members}
        self.boss_down = False
        self.boss_down_turns = 0
        self.extra_turns = []

    def calculate_damage(self, member, skill_id=None):
        damage_multiplier = 1.0
        if self.boss_down:
            damage_multiplier *= 1.25
        if skill_id is None:
            if random.randint(1, 100) >= member.stats[4]:
                return 0, False
            damage = member.stats[0] * member.weapon[1] // 100
            if random.randint(1, 100) <= member.stats[3]:
                damage += random.randint(80, 100)
                return damage * damage_multiplier, True
            return damage * damage_multiplier, False
        else:
            skill = skills_data[skill_id]
            cost, multiplier, element = skill[1], skill[2], skill[3]
            if isinstance(element, int):
                affinity = self.boss_affinities[element]
                if affinity == "nul":
                    return 0, False
                elif affinity == "res":
                    multiplier *= 0.25
                elif affinity == "fr":
                    multiplier *= 1.25
                    return (member.stats[1] * multiplier) * damage_multiplier, True
                damage = (member.stats[1] if element > 0 else member.stats[0]) * multiplier
                return damage * damage_multiplier, False
            return 0, False

    def boss_turn(self):
        if self.boss_hp <= 0:
            return False
        for member_id, member in self.party_manager.members.items():
            if member.hp <= 0:
                continue
            damage = random.randint(50, 100)
            if self.defending[member_id]:
                damage //= 2
            member.hp -= damage
            if member_id == 1 and member.hp <= 0:
                return True
        return False

    def start_combat(self):
        while self.boss_hp > 0 and self.party_manager.members[1].hp > 0:
            if self.boss_down:
                self.boss_down_turns -= 1
                if self.boss_down_turns <= 0:
                    self.boss_down = False

            # Turnos normais
            for member_id, member in list(self.party_manager.members.items()):
                if member.hp <= 0:
                    continue
                clear_screen()
                print(f"Turno de {member.name} (HP: {member.hp}/{member.max_hp}, SP: {member.sp}/{member.max_sp}) vs Boss (HP: {self.boss_hp})")
                print("1 - atacar    2 - defender    3 - magias    4 - itens    5 - grim    6 - passar")
                choice = input("Escolha: ").strip()

                one_more = False
                if choice == "1":
                    damage, one_more = self.calculate_damage(member)
                    self.boss_hp -= damage
                elif choice == "2":
                    self.defending[member_id] = True
                elif choice == "3":
                    clear_screen()
                    print("Magias disponíveis:")
                    for skill_id in member.skills:
                        print(f"{skill_id} - {skills_data[skill_id][0]}")
                    try:
                        skill_id = int(input("Escolha uma magia: "))
                        if skill_id in member.skills and member.sp >= skills_data[skill_id][1]:
                            member.sp -= skills_data[skill_id][1]
                            damage, one_more = self.calculate_damage(member, skill_id)
                            self.boss_hp -= damage
                    except (ValueError, KeyError):
                        pass
                elif choice == "4":
                    clear_screen()
                    print("Itens disponíveis:")
                    for key, item in items_data.items():
                        print(f"{key} - {item[0]} (Quantidade: {item[1]})")
                    try:
                        item_id = int(input("Escolha um item: "))
                        if item_id in items_data and items_data[item_id][1] > 0:
                            items_data[item_id][1] -= 1
                    except (ValueError, KeyError):
                        pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    continue

                if one_more:
                    self.extra_turns.append(member_id)
                    self.boss_down = True
                    self.boss_down_turns = 2

                if 1 in self.party_manager.members and self.party_manager.members[1].hp <= 0:
                    break

            # Turnos extras
            while self.extra_turns and self.boss_hp > 0 and self.party_manager.members[1].hp > 0:
                member_id = self.extra_turns.pop(0)
                member = self.party_manager.members.get(member_id)
                if member and member.hp > 0:
                    clear_screen()
                    print(f"Turno extra de {member.name} (HP: {member.hp}/{member.max_hp}, SP: {member.sp}/{member.max_sp}) vs Boss (HP: {self.boss_hp})")
                    print("1 - atacar    2 - defender    3 - magias    4 - itens    5 - grim    6 - passar")
                    choice = input("Escolha: ").strip()
                    one_more = False
                    if choice == "1":
                        damage, one_more = self.calculate_damage(member)
                        self.boss_hp -= damage
                    elif choice == "2":
                        self.defending[member_id] = True
                    elif choice == "3":
                        clear_screen()
                        print("Magias disponíveis:")
                        for skill_id in member.skills:
                            print(f"{skill_id} - {skills_data[skill_id][0]}")
                        try:
                            skill_id = int(input("Escolha uma magia: "))
                            if skill_id in member.skills and member.sp >= skills_data[skill_id][1]:
                                member.sp -= skills_data[skill_id][1]
                                damage, one_more = self.calculate_damage(member, skill_id)
                                self.boss_hp -= damage
                        except (ValueError, KeyError):
                            pass
                    elif choice == "4":
                        clear_screen()
                        print("Itens disponíveis:")
                        for key, item in items_data.items():
                            print(f"{key} - {item[0]} (Quantidade: {item[1]})")
                        try:
                            item_id = int(input("Escolha um item: "))
                            if item_id in items_data and items_data[item_id][1] > 0:
                                items_data[item_id][1] -= 1
                        except (ValueError, KeyError):
                            pass
                    elif choice == "5":
                        pass
                    elif choice == "6":
                        continue
                    if one_more:
                        self.extra_turns.append(member_id)
                        self.boss_down = True
                        self.boss_down_turns = 2
                    if 1 in self.party_manager.members and self.party_manager.members[1].hp <= 0:
                        break

            # Turno do boss
            if self.boss_hp > 0 and self.party_manager.members[1].hp > 0:
                player_died = self.boss_turn()
                if player_died:
                    break

        clear_screen()
        if self.boss_hp <= 0:
            print("Vitória! O boss foi derrotado!")
        else:
            print("Derrota! O jogador foi derrotado.")
        input("Pressione enter para sair")

def start_combat(party_manager):
    combat = Combat(party_manager)
    combat.start_combat()