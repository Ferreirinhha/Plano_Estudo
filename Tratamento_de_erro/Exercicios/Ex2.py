""" Faça um programa que tente abrir um arquivo inexistente e trate a exceção de 
arquivo não encontrado. Adicione um bloco finally que exiba uma mensagem 
indicando o encerramento do processo. """

def abrir_aquivo(arquivo):
    with open(arquivo) as arq:
        print(arq)


try:
    abrir_aquivo('Amigos.txt')
except FileNotFoundError as erro:
    print('Arquivo não encontrado!!!')
finally:
    print('Fim do programa!!!')