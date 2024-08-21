""" Faça um programa que receba o nome de um arquivo do usuário e o abra. Se o 
arquivo não existir, crie-o, e, em seguida, adicione um bloco finally que feche 
o arquivo corretamente. """


arquivo_nome = str(input('Digite o nome do Arquivo: '))

try: 
    arquivo = open(f'{arquivo_nome}.txt', 'r')
    print(arquivo.read())
except FileNotFoundError:
    print('Arquivo não encontrado')
    print('Criando Arquivo....')
    open(f'{arquivo_nome}.txt', 'w')
finally:
    arquivo.close()
