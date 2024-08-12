""" Leitura e contagem de palavras: Escreva uma função que abra um arquivo de 
texto, leia seu conteúdo e retorne a quantidade de palavras no arquivo """


def contar_palavras(arquivo):
    with open(arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        for i, v in enumerate(conteudo.split()):
            None
        print(f'Palavras no arquivo: {i}')


# GPT

def contar_palavrass(arquivo):
    with open(arquivo) as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return len(palavras)


arquivo = 'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Ex'
contar_palavras(arquivo)
print(contar_palavrass(arquivo))
