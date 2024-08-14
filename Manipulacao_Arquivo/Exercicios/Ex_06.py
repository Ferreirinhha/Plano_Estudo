""" Leitura e escrita de listas: Escreva uma função que receba uma lista de 
números, salve-a em um arquivo de texto (cada número em uma linha) e, em seguida, 
leia o arquivo e retorne a lista de números. """


arquivo = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\novo.txt'

lista = ['4', '3', '2', '1']

with open(arquivo, 'w') as arq:
    for i in lista:
        arq.write(f"{i}\n") 
    # arq.seek(0) muda o ponteiro do arquivo na hora de ler

# se eu usar o readline ao inves do readlines, o for vai pegar cada caracter da linha
with open(arquivo) as arq:
    nova_lista = list()
    for i in arq.readlines():
        nova_lista.append(int(i))
    print(nova_lista)