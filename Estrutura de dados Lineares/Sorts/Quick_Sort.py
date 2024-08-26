# Quick Sort


def quick_sort(vetor, p, r): # p = Primeira posição do vetor, r: Última posição do vetor
    if p < r:
        q = partition(vetor, p, r)
        quick_sort(vetor, p, q - 1)
        quick_sort(vetor, q + 1, r)
    return vetor


def partition(vetor, p, r):
    x = vetor[r]
    i = p - 1
    for j in range(p, r):
        if vetor[j] <= x:
            i += 1
            trocar(vetor, i, j)
    trocar(vetor, i+1, r)
    return i + 1


def trocar(vetor, a, b):
    troca = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = troca


vetor = [99, 5, 1, 6, 3, 5, 7, 8, 9, 2 ,5 ,8]

print(f'Vetor: {vetor}')
print(f'Vetor Organizado: {quick_sort(vetor, 0, len(vetor) - 1)}')
        