""" Exercício 3: Crie um conjunto com os elementos {'maçã', 'banana', 'laranja'} e tente adicionar 
{'banana', 'uva'}. Imprima o conjunto após a adição. """

frutas = set(['maça', 'banana', 'laranja'])

frutas.add('banana')
frutas.add('uva')

# ou 

frutas.add({'banana', 'uva'})

print(frutas)