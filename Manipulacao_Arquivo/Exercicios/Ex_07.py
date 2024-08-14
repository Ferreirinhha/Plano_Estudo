""" Manipulação de um arquivo CSV: Crie uma função que leia um arquivo CSV, some
os valores de uma coluna específica e retorne o total. O nome da coluna deve 
ser passado como argumento para a função. """

""" Ex de arquivo CSV: 
nome/email/idade
daniel,daniel@gmail.com,20
daniel,danielferreirinha@gmail.com,23
daniel,danielmacedo@gmail.com,24
daniel,danielsilva@gmail.com,27
"""

arquivo = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Pokemons.csv'

def csv_somar(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        lista = list()
        for i in conteudo:
            texto += i
            if i == ',' or i == '\n':
                lista.append(texto)
                texto = ''
        lista_num = list()
        for i in range(5, len(lista) - 1, 3):
            lista_num.append(int(i))
            soma = sum(lista_num)
    return soma


# Gpt
import csv

"""Importante: o csv.reader transforma todo o csv numa lista cada linha em uma lista diferente
ex: csv
daniel,ferreirinha,10

csv.reader = ['daniel', 'ferreirinha', '10']
"""

def csv_cont_numeros(arquivo, coluna):
    somar = 0
    with open(arquivo, 'r', encoding='utf-8') as arq:
        leitor = csv.DictReader(arq) 
        for linha in leitor:
            valor = linha.get(coluna)
            if valor is not None:
                somar += int(valor)
        return somar
            
    



