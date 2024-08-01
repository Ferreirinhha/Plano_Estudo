""" Cadastro de jogadores e suas pontuações em diferentes níveis: Crie um 
programa que permita ao usuário cadastrar jogadores e suas pontuações em 
diferentes níveis de um jogo. Permita adicionar novos jogadores e novos níveis, 
e exiba o cadastro completo no final """

cadastro = dict()


while True:
    jogador = str(input('Nome de usuário: ')).capitalize()
    cadastro[jogador] = {}
    for i in range(1, 6):
        while True:
            try:
                pts = int(input(f'Pontuação no Nível{i}: '))
            except:
                print('\033[1;31mPontuação inválida!\033[m')
                continue
            else:
                print('\033[1;32mPontuação cadastrada!\033[m')
                cadastro[jogador][f'Nível{i}'] = f'{pts}pts'
                break
    print(cadastro)
    continuar = str(input('Continuar [S/N]: ')).upper()[0]
    if continuar == 'N':
        break


for name, level in cadastro.items():
    print('='*30)
    print(f'\033[1;36m{name.center(30)}\033[m')
    print('='*30)
    for nivel, pontos in level.items():
        print(f'\033[1;31m{nivel}: \033[1;33m{pontos}\033[m')
    