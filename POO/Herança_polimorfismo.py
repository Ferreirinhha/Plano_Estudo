# A herança serve para voçê acessar tudo oque ela tem
# A classe filha herda todas as funções e atributos da classe pai

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
