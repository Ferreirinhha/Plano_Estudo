#Bubble Sort


def bubble_sort(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor) - 1, i, - 1):
            if vetor[j] < vetor[j - 1]:
                trocar(vetor, j, j - 1)
    return vetor


def trocar(vetor, a, b):
    troca = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = troca


vetor = [5, 4, 3, 2, 1, 0]

print(f'Vetor: {vetor}')
print(f'Vetor organizado: {bubble_sort(vetor)}')


