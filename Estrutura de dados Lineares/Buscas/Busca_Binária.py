# Busca Binária


def busca_binaria(vetor, elemento, inicio=0, fim=None):
    if fim == None:
        fim = len(vetor) - 1
    if inicio > fim:
        return - 1
    else:
        meio = (inicio + fim) // 2
        if vetor[meio] == elemento:
            return meio
        else:
            if vetor[meio] < elemento:
                return busca_binaria(vetor, elemento, meio + 1, fim)
            else:
                return busca_binaria(vetor, elemento, inicio, meio - 1)
                

vetor = [1, 5, 7, 8, 9 , 32, 56, 8]

print(busca_binaria(vetor, 99))
