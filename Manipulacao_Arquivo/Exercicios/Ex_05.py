""" Adicionar conteúdo a um arquivo: Escreva uma função que receba uma lista de
strings e as adicione ao final de um arquivo de texto existente, sem apagar o 
conteúdo anterior """


def adicionar_conteudo(arquivo, lista):
    with open(arquivo, 'a') as arq:
        for i in lista:
            arq.write(f'\n{i} ')


arquivo = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\novo.txt'
textos = ['banana', 'abacate', 'caju', 'caqui']

adicionar_conteudo(arquivo, textos)
