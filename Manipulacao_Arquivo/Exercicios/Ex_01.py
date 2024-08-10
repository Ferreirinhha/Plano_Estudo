""" Leitura e contagem de palavras: Escreva uma função que abra um arquivo de 
texto, leia seu conteúdo e retorne a quantidade de palavras no arquivo """


with open('C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Ex', 'r') as arquivo:
    conteudo = arquivo.read()
    for i, v in enumerate(conteudo.split()):
        None
    print(f'Palavras no arquivo: {i}')
