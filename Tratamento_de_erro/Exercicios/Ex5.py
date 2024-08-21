""" Desenvolva um código que use o bloco finally para garantir que um arquivo 
seja fechado, independentemente de erros no código. """

arquivo = open('Arquivo.txt', 'r+')

try:
    ler = arquivo.read()
    print(ler)
finally:
    arquivo.close()
    