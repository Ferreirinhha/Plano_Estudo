""" Dadas duas listas aninhadas que representam duas matrizes 2x2, escreva um código que realize a multiplicação 
das matrizes e retorne o resultado """

matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]

resultado = [
    [
        matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],
        matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]
    ],
    [
        matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],
        matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]
    ]
]

print(resultado)