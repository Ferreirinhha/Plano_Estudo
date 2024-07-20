""" Dada uma lista aninhada que representa uma matriz 3x3, crie uma nova 
lista aninhada que seja a transposta da matriz original """

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(0, 3):
    for linha in matriz:
        print(f'[{linha[i]}]', end=" ")
    print()

# GPT
transposta = []

for j in range(len(matriz[0])):
    transposta.append([]) # Criou uma lista vazia com outras 3 listas [[], [], []]
print(transposta)

for j in range(len(matriz[0])):  # percorre cada coluna da matriz original
    for i in range(len(matriz)):  # percorre cada linha da matriz original
        transposta[i].append(matriz[j][i])
print(transposta)
  
# Tentando transformar em List comprehension

trasnposta2 = [[matriz[linha][coluna] for linha in range(len(matriz))] for coluna in range(len(matriz[0]))]
print(trasnposta2)
       
