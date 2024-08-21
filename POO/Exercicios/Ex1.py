""" Crie uma classe Pessoa que possua os atributos nome e idade, e um método 
cumprimentar() que imprime uma mensagem com o nome da pessoa. Crie dois objetos 
diferentes da classe e teste o método. """



class Pessoa:
    nome = None
    idade = None

    def cumprimentar(nomes):
        print(f'É um prazer te conhecer {nomes.nome}')

pessoa1 = Pessoa()
pessoa1.nome = 'Daniel'
pessoa1.idade = 20

pessoa1.cumprimentar()


pessoa2 = Pessoa()
pessoa2.nome = 'Jubilaine'
pessoa2.idade = 30

pessoa2.cumprimentar()