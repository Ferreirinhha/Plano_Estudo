""" Desenvolva uma classe ContaBancaria com atributos saldo e titular. Crie 
métodos para depositar() e sacar() dinheiro, garantindo que o saldo nunca fique 
negativo. """

class ContaBancaria:
    saldo = 0
    titular = None

    def saldo_negativo(self):
        if self.saldo < 0:
            raise Exception('O saldo não pode ser menor que zero.')
        else:
            return self.saldo


    def depositar(self, deposito):
        self.saldo += deposito # Atualizando o saldo
        self.saldo_negativo()
        return self.saldo
    

    def sacar(self, saque):
        if saque > self.saldo:
            raise Exception('O saque não pode ser maior que o saldo')
        else:
            self.saldo -= saque # Atualizando o saldo
            self.saldo_negativo()
            return self.saldo
            
    


conta1 = ContaBancaria()
conta1.saldo = 10
conta1.titular = '87638292826262'

print(conta1.depositar(10))

try:
    print(conta1.sacar(20))
except Exception as erro:
    print(erro)



    

