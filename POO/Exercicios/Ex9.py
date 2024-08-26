""" Desenvolva uma classe ContaCorrente com métodos para depositar(), sacar(), e
um atributo privado __saldo que só pode ser alterado por métodos específicos. """

class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0
        self.titular = titular
    

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor não pode ser negativo.')
    

    def sacar(self, valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            print(f'Saque no valor de {valor}')
            print(f'Saldo: {self.__saldo}')
        else: 
            print('Não foi possivel sacar')


conta = ContaCorrente('Daniel')
conta.depositar(1000)
conta.sacar(100)