""" Escreva uma função que receba uma lista de números e retorne a soma de todos
os números pares. """

def somar_par(lista):
    somar = 0
    for i in lista:
        if i % 2 == 0:
            somar += i 
    return somar
            


lista = [2, 4, 6, 8, 3]

print(somar_par(lista))