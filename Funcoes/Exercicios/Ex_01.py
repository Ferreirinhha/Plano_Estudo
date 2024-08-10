""" Crie uma função que receba uma lista de números e retorne uma nova lista com
cada número ao quadrado. """


def multiplicar(lista):
    nova_lista = list()
    for i in range(len(lista)):
        nova_lista.append(lista[i]**2)
    return nova_lista



lista = [4, 5, 6, 7, 8, 9, 10]

print(multiplicar(lista))