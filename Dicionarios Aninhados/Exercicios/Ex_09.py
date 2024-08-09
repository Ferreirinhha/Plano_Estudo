""" Relatório de pontuações em formato de tabela: Crie um programa que gere um 
relatório em formato de tabela, exibindo as pontuações de todos os jogadores em 
todos os níveis, com as médias de cada jogador e as médias de cada nível. """


print('='*80)
print(f'{'Resumo dos jogadores'.center(80)}')
print('='*80)
print(f'\033[1;35m| {'Name'.center(10):<10} ', end='')
print(f'| {'Nível1'.center(10):<10} ', end='')
print(f'| {'Nível2'.center(10):<10} ', end='')
print(f'| {'Nível3'.center(10):<10} ', end='')
print(f'| {'Nível4'.center(10):<10} ', end='')
print(f'| {'Nível5'.center(10):<10} | \033[m', end='')
print()
print('\033[1;35m-\033[m'*80, end='')




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

for name, levels in jogadores.items():
    print(f'\n\033[1;35m|\033[m \033[1;33m{name:<10}\033[m ', end='')
    for level in levels:
        print(f'\033[1;35m|\033[m \033[1;32m{f'{jogadores[name][level]}'.center(10):<10}\033[m ', end='')
    print()
    print('\033[1;35m-\033[m'*80, end='')


