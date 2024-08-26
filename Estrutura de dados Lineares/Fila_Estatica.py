
# Verifica se o vetor está cheio, o tail aponta para o final do vetor.
def is_full(vetor, tail):
    if tail == len(vetor):
        return True
    else:
        return False

# Adicionar elemento na fila
def enqueue(vetor, tail, elemento):
    if not is_full(vetor, tail):
        vetor[tail] = elemento # Tail vai apontar para uma posição depois de um elemento, caso não tenha, apontará para a primeira posição
        tail += 1
    else:
        print('A fila está cheia.')
    return tail

#Verifica se a fila está vazia
def is_empty(head, tail):
    if head == tail:
        return True
    else:
        return False

#Remove elementos da lista
def dequeue(vetor, head, tail):
    if not is_empty(head, tail):
        vetor[head] = None
        head += 1
        return head

tamanho = 5
vetor = [None] * tamanho
tail = 0
head = 0

try:
    tail = enqueue(vetor, tail, 1) # sempre atualizando o valor de tail com o tail =
    tail = enqueue(vetor, tail, 1)
    tail = enqueue(vetor, tail, 1)
    tail = enqueue(vetor, tail, 1)

except:
    print('Fila cheia')


head = dequeue(vetor, head, tail)
head = dequeue(vetor, head, tail)
print(is_empty(head, tail))
print(vetor)


