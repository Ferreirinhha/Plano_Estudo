""" Comparação de arquivos binários: Escreva uma função que receba dois arquivos 
binários e compare seu conteúdo byte a byte. A função deve retornar True se os 
arquivos forem idênticos e False caso contrário """


arquivo1 = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Papel de parede Universo copy.jpg'
arquivo2 = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Papel de parede Universo.jpg'

with open(arquivo1, 'rb') as arq1, open(arquivo2,'rb') as arq2:
    while True:
        bity1 = arq1.read(1)
        bity2 = arq2.read(1)

        if bity1 != bity2:
            print('Arquivo diferente')
            break
        if bity1 == b'':
            print('Arquivo igual')
            break