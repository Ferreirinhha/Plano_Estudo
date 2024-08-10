""" Escreva uma função que receba uma lista de dicionários e retorne o 
dicionário com o maior valor associado à chave "idade". """


def maior_idade(lista):
    for i, v in enumerate(lista):
        if i == 0:
            maior_idade = v['idade']
            dicionario = v
        elif maior_idade < v['idade']:
            maior_idade = v['idade']
            dicionario = v
    return dicionario


#gpt
def maior(lista):
    return max(lista, key=lambda b: b['idade'])
        
        
pessoa = [{'Nome':'Daniel', 'idade':30}, {'Nome':'Gabriela', 'idade':59}, {'Nome':'Fernando', 'idade':20}]

print(maior_idade(pessoa))
print(maior(pessoa))