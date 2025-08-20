# Dados do jogador (populado dinamicamente)
player_data = {}

# Dados dos aliados
allies_data = {
    "cole": {
        "hp": 900, "max_hp": 900, "sp": 600, "max_sp": 600,
        "stats": [57, 57, 57, 80, 40],
        "skills": [18, 3, 8, 25, 1, 15, 31, 2],
        "grim": "jackpot"
    },
    "mordak": {
        "hp": 1800, "max_hp": 1800, "sp": 250, "max_sp": 250,
        "stats": [81, 40, 90, 45, 75],
        "skills": [16, 19, 25, 1, 20, 32, 2, 4],
        "grim": "salvador"
    },
    "miriam": {
        "hp": 750, "max_hp": 750, "sp": 950, "max_sp": 950,
        "stats": [30, 85, 45, 25, 50],
        "skills": [22, 27, 11, 10, 15, 33, 24, 13],
        "grim": "benção da sarcerdotisa"
    },
    "leo": {
        "hp": 1000, "max_hp": 1000, "sp": 550, "max_sp": 550,
        "stats": [50, 50, 70, 50, 50],
        "skills": [17, 23, 13, 14, 15, 7, 4],
        "grim": "Paralizar"
    },
    "lia": {
        "hp": 850, "max_hp": 850, "sp": 700, "max_sp": 700,
        "stats": [45, 60, 50, 50, 80],
        "skills": [26, 9, 11, 28, 4, 5, 21, 25],
        "grim": "maldição"
    },
    "mara": {
        "hp": 1000, "max_hp": 1000, "sp": 700, "max_sp": 700,
        "stats": [30, 40, 70, 60, 60],
        "skills": [27, 21, 6, 7, 8, 11, 10, 12],
        "grim": "apoio divino"
    }
}

# Descrições de grim
grim_descriptions = {
    "Truque sujo": ["ativa uma barreira que devolve o dano ao oponente durante 3 turnos", "aumenta a barra usando magias de dano elemental"],
    "jackpot": ["50% de chance de ativar o estado apostador indomável que te dá sp infinito e durante 5 turnos hits críticos são garantidos e nunca erra, ao acabar, o usuário ganha a chance de ativar de novo,\n mas se a aposta falhar o usuário fica no estado de fadiga(não se move por 3 turnos e golpes físicos sempre dão críticos)", "aumenta a barra acertando críticos"],
    "salvador": ["redireciona 25% do dano recebido por todos os aliados para si por 5 turnos", "aumenta a barra recebendo dano sem defender"],
    "benção da sarcerdotisa": ["cura totalmente todos os aliados e reduz o próprio hp para 1", "aumenta a barra curando aliados"],
    "Paralizar": ["congela o inimigo por 2 turnos", "aumenta barra causando aflições no inimigo"],
    "maldição": ["ativa debuff de ataque, defesa e precisão no oponente por 3 turnos", "aumenta a barra debuffando o inimigo"],
    "apoio divino": ["ativa buffs de ataque, defesa e precisão a todos os aliados por 3 turnos", "aumenta a barra buffando aliados"]
}

# Dados das armas
weapons_data = {
    "cole": ["soqueiras", 77],
    "mordak": ["greatsword", 180],
    "miriam": ["cajado", 50],
    "leo": ["rapieira", 90],
    "lia": ["familiar canino", 80],
    "mara": ["arco antigo", 50]
}

# Dados das afinidades
affinities_data = {
    "cole": ["res", "res", "--", "fr", "--", "--", "fr"],
    "mordak": ["res", "--", "--", "--", "nul", "fr", "nul"],
    "miriam": ["--", "nul", "fr", "res", "--", "--", "fr"],
    "leo": ["--", "--", "res", "--", "--", "--", "--"],
    "lia": ["--", "--", "--", "--", "--", "res", "fr"],
    "mara": ["--", "--", "--", "--", "--", "--", "--"]
}

# Dados dos itens
items_data = {
    1: ["pedra do renascimento (ressuscita o aliado com vida cheia)", 7],
    2: ["flor dourada (recupera 450 de hp)", 4],
    3: ["nectar de litra (recupera 250 de sp)", 6],
    4: ["calmante (remove furia de um aliado)", 3],
    5: ["antidoto (remove veneno de um aliado)", 2],
    6: ["fruta dekaja (remove buffs de ataque e defesa dos inimigos exceto concentrar/carregar)", 5],
    7: ["fruta dekunda (remove debuffs de ataque e defesa dos aliados exceto concentrar/carregar)", 5]
}

# Dados das magias
skills_data = {
    1: ["fortalecer", 30, 1.5, "aumenta o dano de 1 combatente por 3 turnos"],
    2: ["aumento de defesa", 30, 1.5, "diminui o dano recebido de 1 combatente por 3 turnos"],
    3: ["aumentar a aposta", 55, 1.5, "aumenta a chance de crítico de 1 combatente por 3 turnos"],
    4: ["enfraquecer", 60, 1.5, "diminui o dano causado de 1 combatente por 3 turnos"],
    5: ["reduzir defesa", 60, 1.5, "aumenta o dano recebido de 1 combatente por 3 turnos"],
    6: ["levantar moral", 95, 1.5, "aumenta o dano de um grupo por 3 turnos"],
    7: ["erguer guarda", 95, 1.5, "diminui o dano recebido de um grupo por 3 turnos"],
    8: ["aposta arriscada", 120, 1.5, "aumenta a chance de crítico de todos os combatentes por 3 turnos"],
    9: ["cura simples", 45, 1.3, "cura 30% do hp de um combatente"],
    10: ["salvação", 110, 1.7, "cura 70% do hp de um combatente"],
    11: ["graça angelical", 95, 1.3, "cura 30% do hp de um grupo"],
    12: ["oratorio", 150, 1.7, "cura 70% do hp de um grupo"],
    13: ["nuvem de veneno", 75, 0, "envenena um combatente e dá dano passivo nele por 3 turnos"],
    14: ["provocar", 100, 0, "enfurece um combatente deixando-o incapaz de usar qualquer coisa além de ataques físicos e dobra o dano causado e recebido por 3 turnos"],
    15: ["confundir", 120, 0, "deixa um combatente confuso, fazendo-o usar ataques aleatoriamente e garante o crítico no próximo ataque físico"],
    16: ["corte profundo", 110, 1.7, "dano físico poderoso a um combatente"],
    17: ["perfuração", 60, 1.2, "dano físico leve moderado a um combatente"],
    18: ["golpe baixo", 60, 1.2, "dano físico leve moderado a um combatente"],
    19: ["chuva de cortes", 85, 1.5, "dano físico moderado a um combatente"],
    20: ["carregar", 70, 2, "dobra o próprio dano do próximo ataque físico"],
    21: ["concentrar", 70, 2, "dobra o próprio dano do próximo ataque elemental"],
    22: ["petalas flamejantes", 125, 1.7, "dano poderoso de fogo a um combatente"],
    23: ["geleira", 65, 1.4, "dano moderado de gelo a um combatente"],
    24: ["tornado", 65, 1.5, "dano moderado de vento a um combatente"],
    25: ["tempestade de raios", 65, 1.5, "dano moderado de raio a um combatente"],
    26: ["umbra", 70, 1.6, "dano moderado de maldição a um combatente"],
    27: ["luz sagrada", 70, 1.5, "dano moderado de luz a um combatente"],
    28: ["ressucitar", 180, 100, "ressuscita um aliado caído"],
    29: ["barreira amarela", 50, 4, "resistencia a raios para um combatente por 3 turnos"],
    30: ["barreira branca", 50, 6, "resistencia a luz para um combatente por 3 turnos"],
    31: ["barreira vermelha", 50, 1, "resistencia a fogo para um combatente por 3 turnos"],
    32: ["barreira fisica", 50, 0, "resistencia a dano físico para um combatente por 3 turnos"],
    33: ["barreira verde", 50, 3, "resistencia a vento para um combatente por 3 turnos"]
}

# Descrições das magias
skill_descriptions = {
    1: "aumenta o dano de 1 em 1.5x por 3 turnos",
    2: "aumenta a defesa de 1 em 1.5x por 3 turnos",
    3: "aumenta sorte de 1 em 1.5x por 3 turnos",
    4: "reduz o dano de 1 em 1.5x por 3 turnos",
    5: "reduz a defesa de 1 em 1.5x por 3 turnos",
    6: "reduz a sorte de 1 em 1.5x por 3 turnos",
    7: "aumenta o dano de todos os aliados em 1.5x por 3 turnos",
    8: "aumenta a defesa de todos os aliados em 1.5x por 3 turnos",
    9: "aumenta a sorte de todos os aliados em 1.5x por 3 turnos",
    10: "cura 45% de hp de todos os aliados",
    11: "ressuscita um aliado caído com 30% de hp",
    12: "deixa o inimigo com raiva (atacando apenas com ataques físicos inimigos aleatórios) durante 3 turnos",
    13: "deixa um inimigo com cegueira (diminui a chance de acertar ataques em 20%) por 3 turnos",
    14: "deixa um inimigo envenenado (dano contínuo a cada turno) por 3 turnos",
    15: "dobra o próprio dano mágico do próximo ataque mágico",
    16: "dobra o próprio dano do próximo ataque físico",
    17: "dano físico moderado a um inimigo",
    18: "dano físico leve a um inimigo",
    19: "dano físico moderado a um inimigo",
    20: "dano físico leve a um inimigo",
    21: "dano massivo de fogo a um inimigo",
    22: "dobra a chance de crítico de todos em campo",
    23: "dano moderado de gelo a um inimigo",
    24: "dano de vento moderado a um inimigo",
    25: "dano de raio moderado a um inimigo",
    26: "dano de sombra moderado a um inimigo",
    27: "dano de luz moderado a um inimigo",
    28: "cura 70% de hp de todos um aliado",
    29: "deixa um inimigo confuso (usando ataques aleatórios) por 3 turnos",
    30: "cura 45% de hp de um aliado",
    31: "resistencia a fogo para um combatente por 3 turnos",
    32: "resistencia a dano físico para um combatente por 3 turnos",
    33: "resistencia a vento para um combatente por 3 turnos"
}