# Listas aninhadas 

# Listas dentro de listas 

# Matriz 3x3
lista_aninhada = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    ]

# Primeiro colchetes é a lista que quer acessar e o segundo é o elemento interno
print(lista_aninhada[1][1]) # Resultado: 5

print(lista_aninhada[2][2]) # Resultado: 9


for i in lista_aninhada:
    print(i) # Resultado [1, 2, 3] [4, 5, 6] [7, 8, 9]

for lista in lista_aninhada:
    for elemento in lista:
        print(elemento)
