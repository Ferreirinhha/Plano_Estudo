#Pesquisa Sequencial

def pesquisar(vetor, elemento):
    for i in range(len(vetor)):
        if elemento == vetor[i]:
            return True
    return False
        

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(pesquisar(vetor, 10))