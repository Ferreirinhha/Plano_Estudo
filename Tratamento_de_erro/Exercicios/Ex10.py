""" Faça um programa que trate erros de índice fora do intervalo de uma lista, 
mostrando uma mensagem clara ao usuário sobre o erro ocorrido. """


lista = [1,2,3,4,5]

try:
    for i in range(10):
        lista[i]
except IndexError:
    print('Contador fora do index da lista.')

