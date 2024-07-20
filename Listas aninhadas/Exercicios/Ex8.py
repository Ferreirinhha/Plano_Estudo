""" Dada uma lista aninhada que representa uma matriz 5x5, escreva um código 
que encontre a posição (linha e coluna) de um número específico dentro da matriz """

num = int(input('Qual número quer encontrar na lista: '))

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 16],
    [17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26]
]

for i in range(len(matriz)):
   for j in range(len(matriz[i])): # len(matriz[i]) serve para contar quantos elementos tem em cada linha
      if matriz[i][j] == num:
         print(f'Linha {i}')
         print(f'Coluna {j}')

