""" Crie uma lista aninhada que represente uma matriz 3x3 e calcule a soma de todos os elementos da matriz """

matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]
soma = 0 
for linha in matriz:
    for coluna in linha:
        soma += coluna
print(soma)

#GPT com List Comprehension

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
soma1 = [sum(linha) for linha in matriz]
print(soma1) #Resultado: [6, 15, 24]

soma2 = sum(sum(linha) for linha in matriz)
print(soma1) #Resultado: 45
