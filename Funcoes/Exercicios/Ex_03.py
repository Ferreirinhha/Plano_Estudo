""" Crie uma função que receba duas listas e retorne um dicionário onde as 
chaves são os elementos da primeira lista e os valores são os elementos 
correspondentes da segunda lista. """



def juntar(lista1, lista2):
    cont = 0
    dicionario = dict()
    for i in lista1:
        dicionario[f'{i}'] = None
    for i, v in dicionario.items():
        dicionario[f'{i}'] = lista2[cont]
        cont += 1
    return dicionario


# Com gpt

def juntar2(lista1, lista2):
    return dict(zip(lista1, lista2))

lista1 = ['banana', 'pera', 'uva', 'abacaxi']
lista2 = [2.99, 5.89, 4.56, 9.99]

print(juntar(lista1, lista2))
print(juntar2(lista1, lista2))