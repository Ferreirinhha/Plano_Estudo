# Criando classes


class Carro:
    marca = 'Desconhecida'
    modelo = 'Desconhecido'

    def detalhes(carro):
        print(f'Carro: {carro.marca} {carro.modelo}')



# Usando as classes ( Criando objetos )

carro1 = Carro() # Instânciando um novo objeto (novo carro)
carro1.marca = 'Honda' # Atribuindo um valor a variável desse novo carro
carro1.modelo = 'Civic'

carro1.detalhes()