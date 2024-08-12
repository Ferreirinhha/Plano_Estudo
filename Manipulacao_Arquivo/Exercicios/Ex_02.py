""" Copiar conteúdo de um arquivo para outro: Crie uma função que leia o 
conteúdo de um arquivo de texto e o copie para outro arquivo. O nome do arquivo 
de destino deve ser passado como argumento para a função """

def copiar(arquivo1, arquivo2):
    with open(arquivo1, 'r') as arquivo:
        conteudo = arquivo.read()
        texto = ''
    for i in conteudo.split():
        texto += ' ' + i
    with open(arquivo2, 'w') as arquivo0:
        arquivo0.write(texto)

# Gpt

def copiar1(origem, destino):
    with open(origem) as arquivo_origem:
        conteudo = arquivo_origem.read()


    with open(destino, 'w') as arquivo_destino:
        arquivo_destino.write(conteudo)


arquivo = r"C:\\Programação\\Python\\Plano_Estudo\\Manipulacao_Arquivo\\Exercicios\\Ex"        
copiar(arquivo, 'novo.txt')

