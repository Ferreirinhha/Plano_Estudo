""" Você está organizando uma reunião e quer saber quem confirmou presença, evitando contagem de duplicatas. """

lista_presenca = set()
lista_falta = set()

for i in range(0, 5):
    nome = str(input('Nome: ')).strip()
    presenca = str(input(f'Estará presente? ')).upper().strip()
    if presenca[0] == 'S':
        lista_presenca.add(nome)
    else:
        lista_falta.add(nome)
print(lista_presenca)
print(lista_falta)