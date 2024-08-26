#Insertion Sort

def insertion_sort(vetor):
    for j in range(1, len(vetor)):
        chave = vetor[j]
        i = j - 1
        while i >= 0 and vetor[i] > chave:
            vetor[i + 1] = vetor[i]
            i = i - 1
        vetor[i + 1] = chave
    return vetor


vetor = [5, 4, 3, 2, 1, 0]

print(f'Vetor: {vetor}')
print(f'Vetor ordenado: {insertion_sort(vetor)}')