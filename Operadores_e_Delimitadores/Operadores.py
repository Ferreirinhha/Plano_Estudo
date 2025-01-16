# @ --> Mutiplicacção de matrizes



# << --> Desloca bits a esquerda, adicionado zeros a direita

x = 5 # bits = 101

print(x << 1) # resultado: 10


# >> --> Desloca bits a direita, descartando bits a direita

y = 20 # Binário = 10100
print(y >> 2) # Resultado: 5 (Binario: 101)


#:= --> Cria uma variavel já atribuindo um valor

# Ao invés disso

n = 10
if n > 5:
    print(n)

# Faça isso

if(n := 10) > 5:
    print(n)