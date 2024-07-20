""" Dada uma lista aninhada que representa uma matriz 3x3, escreva um código que 
verifique se a matriz é um quadrado mágico (soma das linhas, colunas e diagonais são iguais).  """

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

constande_magica = 0

# Adicionar na posição...
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero na posição [{linha}, {coluna}]: '))

constande_magica = matriz[0][0] + matriz[0][1] + matriz[0][2]
cont = 0
print(constande_magica)

# Desenhar matriz
for linha in range(0, 3):
    soma_coluna = 0
    for coluna in range(0, 3):
        soma_coluna += matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]}]', end=" ")
        if coluna == 2:
            print(f'-> {soma_coluna}', end="")
    if constande_magica == soma_coluna:
        cont += 1

    print()
# Contar Linha
for i in range(0, 3):
    soma_linha = 0
    for linha in matriz:
        if i == 0:
            soma_linha += linha[i]
        elif i == 1:
            soma_linha += linha[i]
        else:
            soma_linha += linha[i]
    print(f'A soma da linha[{i}]: {soma_linha}')
    if constande_magica == soma_linha:
        cont += 1

# Contar diagonais
soma_diagonais1 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        if linha == 0 and coluna == 0:
            soma_diagonais1 += matriz[linha][coluna]
        elif linha == 1 and coluna == 1:
            soma_diagonais1 += matriz[linha][coluna]
        elif linha == 2 and coluna == 2:
            soma_diagonais1 += matriz[linha][coluna]

if constande_magica == soma_diagonais1:
        cont += 1        

soma_diagonais2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if linha == 0 and coluna == 2:
            soma_diagonais2 += matriz[linha][coluna]
        elif linha == 1 and coluna == 1:
            soma_diagonais2 += matriz[linha][coluna]
        elif linha == 2 and coluna == 0:
            soma_diagonais2 += matriz[linha][coluna]  
if constande_magica == soma_diagonais2:
        cont += 1           

if cont == 8:
    print('A matriz é um quadrado mágico')
else:
    print('Não é um quadrado mágico')

referencia = sum(matriz[0])

print(referencia)






