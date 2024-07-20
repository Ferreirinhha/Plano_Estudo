# Conjuntos.

#Criar conjuntos

meu_conjunto = {1, 2, 3, 4} # sempre com chaveis
outro_conjunto = set([1, 2, 3, 4]) #Podemos criar usando o set tbm

print(meu_conjunto, outro_conjunto)

# Adicionar elementos
meu_conjunto.add(5)
print(meu_conjunto)

#Remover elementos
meu_conjunto.remove(3) #Remove o 3 porém se o 3 não existir, gera um erro
meu_conjunto.discard(6) #Remove o 6 mas não gera erro se o 6 não existir.

print(meu_conjunto)
