""" Escreva uma função que verifique se uma palavra é um palíndromo 
(lê-se da mesma forma de trás para frente). """


def palindromo(string):
    if string == string[::-1]:
        return 'é palindromo'
    else:
        return 'Não é palindromo'
    


print(palindromo('ovo'))
