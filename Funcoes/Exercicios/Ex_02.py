""" Escreva uma função que receba um dicionário e retorne uma lista com todas as 
chaves cujo valor é um número par. """


def par(dicionario):
    nova_lista = list()
    for i, v in dicionario.items():
        if v % 2 == 0:
            nova_lista.append(v)
    return nova_lista




dicionario = {"Chave1":2418, "Chave2":1517, "Chave3":9865, "Chave4":8765 }

print(par(dicionario))