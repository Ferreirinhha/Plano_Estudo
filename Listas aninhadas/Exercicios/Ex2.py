""" Dada uma lista aninhada que representa uma matriz 4x4, calcule a média de todos os elementos. """

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
soma = 0
for linha in matriz:
    for coluna in linha:
        soma += coluna
media = soma / 16

print(f'A mádia da matriz: {media} ')

#GPT com List Comprehension

matriz1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

total_elementos = sum(len(linha) for linha in matriz1)
print(total_elementos) #Resultado: 16

soma_elementos = sum(sum(linha) for linha in matriz1)
print(soma_elementos) #Resultado: 136

media = soma_elementos / total_elementos
print(f'A média da matriz: {media}')


