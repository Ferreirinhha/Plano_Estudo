""" Crie uma função que receba um dicionário e retorne um novo dicionário com as
chaves e valores invertidos. """


def inverter(dicionario):
    novo_dicionario = dict()
    for i, v in dicionario.items():
        novo_dicionario[v] = i
    return novo_dicionario


dicionario = {"Chave1":2418, "Chave2":1517, "Chave3":9865, "Chave4":8765 }

print(inverter(dicionario))