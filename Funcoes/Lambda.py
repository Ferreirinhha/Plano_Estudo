# Lambda

""" São Funções anônimas, sem nome, sem 'definir' Elas são usadas principalmente
quando você precisa de uma função curta e simples por um breve momento, sem a 
necessidade de definir uma função completa com def. """


# Extrutura 

# lambda argumento: expressao


#Sem lambda
def somar1(a, b):
    return a * b


#Com lambda 
somar = lambda a, b: a * b