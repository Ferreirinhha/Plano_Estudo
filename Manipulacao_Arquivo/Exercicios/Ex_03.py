""" Filtragem de linhas em um arquivo: Escreva uma função que leia um arquivo de
texto e crie um novo arquivo contendo apenas as linhas que começam com uma letra
específica. A letra deve ser passada como argumento para a função """


def filtar(arquivo, letra: str):
    with open(arquivo) as arq, open('Filtragem.txt', 'a') as arquivo0:
        linha = arq.readline()
        while linha:
            for i, v in enumerate(linha):
                if i == 0 and v in letra: # verifica se a primeira letra da linha começa com alguma letra
                    arquivo0.write(linha)
            linha = arq.readline() # avança para próxima linha


# gpt
def filtrar(arquivo, letra, destino):
    with open(arquivo) as arquivo:
        linhas = arquivo.readlines()
    
    with open(destino, 'w') as arquivo_destino:
        for linha in linhas:
            if linha.startswith(letra):
                arquivo_destino.write(linha)


arquivo = 'C:\\Programação\\Python\\Plano_Estudo\\Manipulacao_Arquivo\\Exercicios\\novo.txt'

filtrar(arquivo, 'p', 'Filtragem.txt')

