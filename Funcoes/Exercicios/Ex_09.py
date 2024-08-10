""" Crie uma função que receba uma lista de strings e retorne a mais longa """


def mais_longa(lista):
    dicionario = dict()
    for i, value in enumerate(lista):
        maior_palavra = 0
        for index, v in enumerate(value):
            maior_palavra += 1
        dicionario[value] = maior_palavra
    return max(dicionario, key=dicionario.get) # key=dicionario.get pega a chave de cada valor e retorna o valor


#gpt
def maior(lista):
    return max(lista, key=len)


lista = ['banana', 'uva', 'pera', 'abaxaqui']

print(mais_longa(lista))
print(maior(lista))


