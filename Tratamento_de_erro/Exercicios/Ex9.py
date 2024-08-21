""" Desenvolva um código que contenha múltiplos blocos except para capturar 
diferentes tipos de exceções (por exemplo, ValueError e ZeroDivisionError). """

try:
    num = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    print(num / num2)
    if num < 0:
        raise ValueError('Número menor que zero.')
except ValueError as erro:
    print(erro)
except ZeroDivisionError:
    print('O divisor não pode ser zero: ')