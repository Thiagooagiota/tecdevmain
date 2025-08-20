import random
import time
import os
from data import items_data, skills_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Combat:
    def __init__(self, player):
        self.player = player
        self.boss_hp = 10000  # Exemplo de HP do boss
        self.boss_affinities = ["--", "--", "--", "--", "--", "--", "--"]  # Exemplo
        self.player_turn = True
        self.critical_multiplier = 1.0
        self.defending = False

    def calculate_damage(self, skill_id=None):
        if skill_id is None:  # Ataque físico normal
            if random.randint(1, 100) >= self.player.stats[4]:  # Precisão
                print(f"{self.player.name} erra o golpe!")
                return 0
            damage = self.player.stats[0] * self.player.weapon[1] // 100
            if random.randint(1, 100) <= self.player.stats[3]:  # Sorte para crítico
                print("Dano Crítico!")
                damage += random.randint(80, 100)
            return damage
        else:  # Magia
            skill = skills_data[skill_id]
            cost, multiplier, element = skill[1], skill[2], skill[3]
            if isinstance(element, int):  # Elemento numérico
                affinity = self.boss_affinities[element]
                if affinity == "nul":
                    print("Dano nulificado!")
                    return 0
                elif affinity == "res":
                    multiplier *= 0.25
                elif affinity == "fr":
                    multiplier *= 1.25
                damage = self.player.stats[1] * multiplier if element > 0 else self.player.stats[0] * multiplier
                if element == 0 and random.randint(1, 100) <= self.player.stats[3]:
                    print("Dano Crítico!")
                    damage += random.randint(80, 100)
                return damage
            return 0  # Suporte ou aflição

    def use_item(self, item_id):
        if item_id in items_data:
            item = items_data[item_id]
            if item[1] > 0:
                items_data[item_id][1] -= 1
                print(f"Usou {item[0]}!")
                # Implementar lógica de efeito do item
                time.sleep(1)
            else:
                print("Não há mais desse item!")
                time.sleep(1)
        else:
            print("Item inválido.")

    def start_combat(self):
        while self.boss_hp > 0 and self.player.hp > 0:
            clear_screen()
            print(f"Combate: {self.player.name} (HP: {self.player.hp}/{self.player.max_hp}, SP: {self.player.sp}/{self.player.max_sp}) vs Boss (HP: {self.boss_hp})")
            print("1 - atacar    2 - defender    3 - magias    4 - itens    5 - grim    6 - sair")
            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                damage = self.calculate_damage()
                self.boss_hp -= damage
                print(f"{self.player.name} ataca e causa {damage} de dano!")
                time.sleep(1)

            elif choice == "2":
                self.defending = True
                print("Você defende!")
                time.sleep(1)

            elif choice == "3":
                clear_screen()
                print("Magias disponíveis:")
                for skill_id in self.player.skills:
                    print(f"{skill_id} - {skills_data[skill_id][0]} ({skills_data[skill_id][3]})")
                try:
                    skill_id = int(input("Escolha uma magia: "))
                    if skill_id in self.player.skills and self.player.sp >= skills_data[skill_id][1]:
                        self.player.sp -= skills_data[skill_id][1]
                        damage = self.calculate_damage(skill_id)
                        self.boss_hp -= damage
                        print(f"{self.player.name} usa {skills_data[skill_id][0]} e causa {damage} de dano!")
                        time.sleep(1)
                    else:
                        print("Magia inválida ou SP insuficiente.")
                        time.sleep(1)
                except ValueError:
                    print("Entrada inválida.")
                    time.sleep(1)

            elif choice == "4":
                clear_screen()
                print("Itens disponíveis:")
                for key, item in items_data.items():
                    print(f"{key} - {item[0]} (Quantidade: {item[1]})")
                try:
                    item_id = int(input("Escolha um item: "))
                    self.use_item(item_id)
                except ValueError:
                    print("Entrada inválida.")
                    time.sleep(1)

            elif choice == "5":
                print("Grim não implementado ainda.")
                time.sleep(1)

            elif choice == "6":
                break

            else:
                print("Opção inválida.")
                time.sleep(1)

            # Turno do boss (exemplo simples)
            if self.player.hp > 0 and self.boss_hp > 0:
                damage = random.randint(50, 100)
                if self.defending:
                    damage //= 2
                self.player.hp -= damage
                print(f"Boss ataca e causa {damage} de dano a {self.player.name}!")
                self.defending = False
                time.sleep(1)

def start_combat(player):
    combat = Combat(player)
    combat.start_combat()