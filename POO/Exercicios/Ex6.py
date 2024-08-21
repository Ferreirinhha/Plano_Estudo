""" Crie uma classe base Funcionario com um método calcular_pagamento(), e crie 
subclasses Gerente e Vendedor que implementem diferentes formas de calcular o 
pagamento. """


class Funcionario:
    def __init__(self, salario):
        self.salario = salario


    def calcular_pagamento(self):
        return self.salario


class Gerente(Funcionario):
    def __init__(self, salario):
        super().__init__(salario)
    

    def calcular_pagamento(self):
        self.salario += (self.salario * 0.2)
        return self.salario


class Vendedor(Funcionario):
    def __init__(self, salario):
        super().__init__(salario)
    

    def calcular_pagamento(self):
        self.salario += (self.salario * 0.1)
        return self.salario        



funcionario = Funcionario(1200)
print(funcionario.calcular_pagamento())

gerente = Gerente(1200)
print(gerente.calcular_pagamento())

vendedor = Vendedor(1200)
print(vendedor.calcular_pagamento())