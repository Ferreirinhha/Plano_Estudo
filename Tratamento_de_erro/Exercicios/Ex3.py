""" Implemente um código que contenha uma função que divide dois números. Use o 
bloco try/except para capturar erros de divisão por zero. """

def dividir(a, b):
    return a / b


try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print(dividir(num1, num2))
except ZeroDivisionError:
    print('Você não pode dividir um número por zero!')
except ValueError:
    print('Digite um valor válido!')
finally:
    print('Fim do programa :D')