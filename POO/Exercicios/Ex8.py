""" Crie uma classe Carro com atributos privados __velocidade e métodos públicos 
para acelerar() e frear(). Implemente um método para mostrar a velocidade atual 
sem permitir acesso direto ao atributo. """

class Carro:
    def __init__(self):
        self.__velocidade = 0
    

    def acelerar(self, valor):
        if valor > 0:
            self.__velocidade += valor
            if self.__velocidade < 0:
                self.__velocidade = 0
                print('O carro está parado')
            else:
                print(f'O carro está a {self.__velocidade}')
        else:
            print('A velocidade tem que ser maior que zero.')


    def frear(self, valor):
        if valor > 0:
            self.__velocidade -= valor
            print(f'O carro está a {self.__velocidade} e desacelerando.')



carro = Carro()
carro.acelerar(120)
carro.acelerar(80)
carro.frear(100)
carro.frear(100)
