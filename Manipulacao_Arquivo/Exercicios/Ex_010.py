""" Criação de logs em arquivos: Escreva uma função que receba uma string e a 
escreva em um arquivo de log com a data e a hora atuais. Toda vez que a função 
for chamada, uma nova linha deve ser adicionada ao arquivo com a mensagem e o 
timestamp. """

import datetime


def mensagens(mensagem):
    arquivo = r'C:\Programação\Python\Plano_Estudo\Manipulacao_Arquivo\Exercicios\Arquivo_log.txt'
    today = datetime.date.today()
    hours = datetime.datetime.now().time()
    with open(arquivo, 'a') as arq:
        arq.write(mensagem)
        arq.write(f' Data: {today}  Hora: {hours} \n')


mensagens('Joaninho me ama!!!')