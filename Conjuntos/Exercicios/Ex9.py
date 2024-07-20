""" Exercício 9: Dado o conjunto conjunto_a = {1, 2, 3} e conjunto_b = {2, 3, 4}, verifique se 
todos os elementos de conjunto_a estão em conjunto_b. Imprima o resultado. """

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 1}

todos_presentes = conjunto_a.issubset(conjunto_b) # verifica se A e subconjunto de B ou se todos de A estão presentes em B

# ou 

presente = conjunto_a <= conjunto_b

print(todos_presentes)
print(presente)