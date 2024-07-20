""" Você vai ao mercado e anota as frutas que deseja comprar, mas não quer repetir nenhum item. """


titulo = 'MERCADÃO ATACADÃO'
print(f'{titulo:=^30}')

lista_mercado = set()

for i in range(0, 10):
    itens = str(input('Qual o próximo item da lista: ')).lower()
    lista_mercado.add(itens)
print(lista_mercado)