""" Jogadores aprovados e reprovados: Considere que a pontuação mínima para 
aprovação em um nível é 60. Crie um programa que liste os jogadores aprovados e 
reprovados em cada nível """


jogadores = {
    "Danielo":{
        "Nível1": 100,
        "Nível2": 10233,
        "Nível3": 23,
        "Nível4": 999,
        "Nível5": 103
    },
    "Emanuelo":{
        "Nível1": 1009,
        "Nível2": 33,
        "Nível3": 1023,
        "Nível4": 999,
        "Nível5": 1443
    }
}


for name, levels in jogadores.items():
    for nivel, pontos in levels.items():
        if pontos < 60:
            print(f'O jogador {name} terá que repetir o nível: {nivel}')