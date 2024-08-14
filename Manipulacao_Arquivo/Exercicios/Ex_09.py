""" Uso de with para múltiplos arquivos: Escreva uma função que abra dois 
arquivos de texto ao mesmo tempo (usando with), leia o conteúdo de ambos e crie
um novo arquivo que combine o conteúdo dos dois """


arquivo1 = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\novo.txt'
arquivo2 = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Ex.txt'

def copiar(arquivo1, arquivo2):
    with open(arquivo1, 'r') as arq, open(arquivo2, 'r') as arq2:
        conteudo = arq.read()
        conteudo2 = arq2.read()

        with open('Arquivonovo.txt', 'w') as novo:
            novo.write(conteudo)
            novo.write(conteudo2)