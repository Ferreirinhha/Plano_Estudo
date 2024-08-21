""" Construtores: 
- Chamados automáticamente quando um novo objeto é instânciado
- Usado para dar valores expecíficos a objetos recém criados
- Usar o método __init__() para contrutores  """


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa = Pessoa('Gabriela', 21)

print(pessoa.idade)
print(pessoa.nome)


# Definir valores padrões a contrutores

class Carro:
    def __init__(self, marca='Desconhecida', modelo='Desconhecido', ano=2000):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def info(self):
        print(f'Modelo: {self.modelo}')
        print(f'Marca: {self.marca}')
        print(f'Ano: {self.ano}')


carro = Carro()
carro.info()

""" Super():
- É usado para chamar métodos da classe Pai """

class Veiculo:
    def __init__(self, rodas, marca, modelo):
        self.rodas = rodas
        self.marca = marca
        self.modelo = modelo


class Moto(Veiculo):
    def __init__(self, rodas, marca, modelo, ano):
        super().__init__(rodas, marca, modelo)
        self.ano = ano # Só preciso adiconar o novo, os antigos fica por parte do super()
