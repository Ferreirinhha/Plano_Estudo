""" Adição de novos níveis para todos os jogadores: Faça um programa que 
adicione um novo nível com uma pontuação padrão (por exemplo, 0) para todos os 
jogadores no dicionário aninhado. """



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

for nome, levels in jogadores.items():
    levels['Nivel6'] = 0
print(jogadores)