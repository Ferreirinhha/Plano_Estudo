# Marge Sort


def merge1(lista, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
    left = [0] * (n1 + 1)  # Adicionando espaço para o sentinela
    rigth = [0] * (n2 + 1)  # Adicionando espaço para o sentinela

    # Preenchendo as listas esquerda (left) e direita (right)
    for i in range(n1):
        left[i] = lista[inicio + i]
    for j in range(n2):
        rigth[j] = lista[meio + j + 1]

    left[n1] = float('inf')  # Sentinela infinito no final de e
    rigth[n2] = float('inf')  # Sentinela infinito no final de d

    i = 0
    j = 0

    # Combina as duas sub-listas em lista[inicio:fim+1]
    for k in range(inicio, fim + 1):
        if left[i] <= rigth[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = rigth[j]
            j += 1

def merge_sort1(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2  # Cálculo correto do meio
        merge_sort1(lista, inicio, meio)
        merge_sort1(lista, meio + 1, fim)
        merge1(lista, inicio, meio, fim)
    return lista

# Exemplo de uso
lista1 = [5, 4, 3, 2, 1, 0, 6, 5, 4]

print(f'lista original: {lista1}')
print(f'lista ordenado: {merge_sort1(lista1, 0, len(lista1) - 1)}')


# Criando de maneira lógica

def margesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        margesort(lista, inicio, meio)
        margesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i = 0
    j = 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j += 1
        elif j >= len(right):
            lista[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]  
            j += 1

# Exemplo de uso
lista = [5, 4, 3, 2, 1, 0, 6, 5, 4]

print(f'Lista original: {lista}')
print(f'Lista ordenada: {margesort(lista)}')


lista = [5, 4, 3 ,2, 1, 0]

print(f'lista original: {lista}')
print(f'lista ordenado: {margesort(lista)}')
