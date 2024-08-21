""" Crie um programa que solicite ao usuário um número inteiro entre 1 e 100. Se 
o número estiver fora desse intervalo, levante uma exceção personalizada. """

try:
    num = int(input('Digite um número entre 0 e 100: '))
    if num > 100 or num < 0:
        raise ValueError('Número maior que 100 ou menor que 0')
except ValueError as erro:
    print(f'{erro}.')
finally:
    print('Fim do programa.')