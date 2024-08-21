""" Implemente um sistema de veículos, onde Veiculo seja a classe mãe e Carro e 
Moto sejam classes filhas. Ambas devem ter um método info() que mostre 
informações sobre o veículo, como o nome, tipo e quantidade de rodas. 
Sobrescreva métodos quando necessário. """


class Veiculo:
    rodas = 0
    marca = ''
    modelo = ''


class Carro(Veiculo):
    def info(self):
        print(f'O carro tem {self.rodas} rodas')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')


class Moto(Veiculo):
    def info(self):
        print(f'A moto tem {self.rodas} rodas')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')



carro = Carro()
carro.rodas = 4
carro.marca = 'Fiat'
carro.modelo = 'Uno'

carro.info()


moto = Moto()
moto.rodas = 2
moto.marca = 'Yamaha'
moto.modelo = 'Não sei'

moto.info()
