# A herança serve para voçê acessar tudo oque ela tem
# A classe filha herda todas as funções e atributos da classe pai
# O primeiro parâmetro de um método de uma classe é sempre o self para poder acessar os atributos
class Animal:
    def som(self):
        print('O animal está fazendo um som...')

class Cachorro(Animal): # Sintáxe para herança
    def latir(self):
        print('O Cachorro está latindo.')

class Gato(Animal):
    def miar(self):
        print('O gato está miando.')
    
    def som(self): # Sobrescrevendo o método som
        print('O gato mia.')


# Usando herança
cachorro = Cachorro()
cachorro.som()
cachorro.latir()


gato = Gato()
gato.som()
gato.miar()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Usando Construtores


class Veiculo:
    def __init__(self, rodas, marca, modelo):
        self.rodas = rodas
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def info(self):
        print(f'Rodas: {self.rodas}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')


# Usando

carro = Carro(4, 'Fiat', 'Uno')
carro.info()





