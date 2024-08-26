#Verificar se a pilha está cheia
def is_full(vetor, topo):
    if topo == len(vetor):
        return True
    else:
        return False
    
#Adicionar elementos na pilha
def push(vetor, topo, elemento):
    if not is_full(vetor, topo):
        vetor[topo] = elemento
        topo += topo
        return topo
    else:
        print('Pilha cheia:')

#Verificar se a pilha está vazia
def is_empty(topo):
    if topo == 0:
        return True
    else: 
        return False

#Remover o últiimo elemento da lista
def pop(vetor, topo):
    if not is_empty(topo):
        vetor[topo] = None
        topo -= 1
        return topo