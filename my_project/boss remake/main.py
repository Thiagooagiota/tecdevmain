import os
from party import Party
from menu import main_menu
from data import player_data, allies_data, grim_descriptions, weapons_data, affinities_data, items_data, skills_data, skill_descriptions

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Obtém o nome do jogador
player_name = input("Digite seu nome\n\n").strip()

# Inicializa o jogador como instância de Party
player_data[player_name] = {
    'hp': 900, 'max_hp': 900, 'sp': 500, 'max_sp': 500,
    'stats': [60, 70, 60, 55, 70],
    'skills': [19, 25, 24, 9, 1, 15, 29, 30],
    'grim': "Truque sujo"
}

player = Party(
    name=player_name,
    hp=player_data[player_name]['hp'],
    max_hp=player_data[player_name]['max_hp'],
    sp=player_data[player_name]['sp'],
    max_sp=player_data[player_name]['max_sp'],
    stats=player_data[player_name]['stats'],
    skills=player_data[player_name]['skills'],
    grim=player_data[player_name]['grim'],
    affliction=None,
    affinities=affinities_data.get(player_name, ["--", "--", "--", "--", "fr", "res", "--"]),
    weapon=weapons_data.get(player_name, ["espada de uma mão", 100])
)

# Inicia o menu principal
main_menu(player, allies_data, grim_descriptions, items_data, skills_data, skill_descriptions, affinities_data, weapons_data)