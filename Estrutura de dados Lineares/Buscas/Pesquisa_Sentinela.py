#Pesquisa sentinela


def sentinela(vetor, elemento):
    i = 0
    vetor[len(vetor) - 1] = elemento
    while elemento != vetor[i]:
        i += 1
    if i == len(vetor) - 1:
        return False
    else:
        return True


vetor = [1, 5, 7, 8, 9 , 32, 56, 8]
print(sentinela(vetor, 0))