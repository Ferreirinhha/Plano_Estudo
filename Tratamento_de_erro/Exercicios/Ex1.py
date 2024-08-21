""" Crie um código que leia um número do usuário e trate a exceção no caso de o 
usuário inserir um valor não numérico. """

while True:
    num = str(input('Digite um número: '))
    try:
        int(num)
    except ValueError as erro:
        print(f'O valor "{num}" é inválido válido!!!')
        continue # Impede que o código de baixo seja execultado caso ocorra um erro.
    print('Valor válido :)')
    break
print('Fim.')
