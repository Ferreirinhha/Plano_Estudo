""" Contagem de caracteres em arquivos binários: Escreva um programa que abra um
arquivo binário (por exemplo, uma imagem) e conte quantas vezes um determinado
byte aparece no arquivo. O byte deve ser passado como argumento para a função. 
"""

arquivo = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Papel de parede Universo.jpg'

def contar_bytes(arquivo, byte):
    with open(arquivo, 'rb') as arq:
        conteudo = arq.read()
        contagem = conteudo.count(byte)
        return contagem

print(contar_bytes(arquivo, b'\x01'))






