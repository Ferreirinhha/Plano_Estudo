""" Atualização de pontuações: Implemente um programa que permita ao usuário 
atualizar a pontuação de um jogador em um nível específico. O programa deve 
verificar se o jogador e o nível existem antes de atualizar. """


jogadores = {
    "Danielo":{
        "Nível1": 100,
        "Nível2": 10233,
        "Nível3": 23,
        "Nível4": 999,
        "Nível5": 103
    },
    "Destroctor":{
        "Nível1": 1009,
        "Nível2": 33,
        "Nível3": 1023,
        "Nível4": 999,
        "Nível5": 1443
    },
    "Karine":{
        "Nível1": 1009,
        "Nível2": 7876,
        "Nível3": 16,
        "Nível4": 5559,
        "Nível5": 147873
    },
    "Emanuelo":{
        "Nível1": 10444,
        "Nível2": 33,
        "Nível3": 23453,
        "Nível4": 654,
        "Nível5": 776553
    },
    "Ash":{
        "Nível1": 15559,
        "Nível2": 33323,
        "Nível3": 165433,
        "Nível4": 565439,
        "Nível5": 765443
    }
}

nome = str(input('Jogador: '))
nivel = str(input('Nível: '))
pts = int(input('Nova pontuação: '))

jogadores[nome][f'Nível{nivel}'] = pts

print(jogadores)


