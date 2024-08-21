""" Crie uma função que solicite ao usuário um número e levante uma exceção 
personalizada se o número for negativo. """


def numero():
    try:
        num = int(input('Digite um número: '))
        if num < 0:
            raise ValueError('Número menor que zero!!!')
    except ValueError as erro:
        print(erro)



numero()