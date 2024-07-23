""" Crie uma função que gere uma matriz identidade de tamanho n, onde n é 
um número inteiro positivo passado como argumento  """   

def matriz_identidade(tam: int):
    matriz = list()

    # Criar matriz
    for i in range(tam):
        matriz.append([])

    # Gerar Numeros na matriz
    for i in range(len(matriz)):
        for j in range(tam):
            matriz[i].append(0)
    
    # Criar a linha diagonal
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = 1
    return matriz



def matrizidentidade(tam: int):
    return [[1 if i == j else 0 for j in range(tam)] for i in range(tam)]


matriz = matriz_identidade(3)

for i in range(len(matriz)):
    print(matriz[i])