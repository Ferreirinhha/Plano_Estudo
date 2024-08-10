""" Escreva uma função que receba uma string e retorne um dicionário com a 
contagem de cada caractere """


def contar(string):
    letras = dict()
    for i in string:
        letras[f'{i}'] = string.count(i)
    return letras



print(contar('Joao fez banana na feira de são josé'))
