""" Crie uma classe Pessoa com os atributos nome, idade e endereco que são 
inicializados no construtor. Em seguida, crie uma classe Funcionario que herda 
de Pessoa, adicionando o atributo cargo. Escreva um método info() em Funcionario 
que exiba todas as informações """


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco



class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, cargo):
        super().__init__(nome, idade, endereco)
        self.cargo = cargo

    
    def info(self):
        print(f'Nome : {self.nome}')
        print(f'Idade : {self.idade}')
        print(f'Endereço : {self.endereco}')
        print(f'Cargo : {self.cargo}')



funcionario = Funcionario('Daniel', 10, 'Rua Dr Souza Soares', 'Desenvolvedor')
funcionario.info()