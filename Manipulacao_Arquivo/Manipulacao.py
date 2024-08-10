# Manipulação de Arquivo


# With: usar o with garante que após o arquivo ser aberto, ele será fechado corretamente

""" Usar o with é como se estivessemos usando isso

arquivo = open('arquivo.txt', 'r')
try:
    conteudo = arquivo.read()
finally:
    arquivo.close()
    
"""

def abrir_arquivo():
    open('Nome do Arquivo.txt', 'w') # dois parâmetros (nome_arquivo, tipo de abertura)

# r: leitura
# w: escrita, se o arquivo não existir, criara um
# a: adicionar no final
# r+: leitura e escrita
# b: escrever em formato binário

def ler_arquivo_todo_de_uma_vez():
    with open('Nome do Arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read() # para ler o arquivo no terminal
        print(conteudo)

def ler_arquivo_linha_por_linha():
    with open('Nome do Arquivo.txt', 'r') as arquivo:
        linha = arquivo.readline()
        print(linha)
        # Da para meter um while para ler todas as linhas
        while linha:
            print(linha, end='')
            linha = arquivo.readline()

def ler_arquivo_todo_adicionando_numa_lista():
    with open('Nome do Arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.readlines() # Le o arquivo todo adicionando-o numa lista
        print(conteudo)


# Escrever no arquivo
def escrever():
    with open('Nome do Arquivo.txt', 'w') as arquivo:
        escrever = arquivo.write('Escrevendo no arquivo.\n')

def escrever_linhas_com_listas():
    with open('Nome do Arquivo.txt', 'w') as arquivo:
        escrever = arquivo.writelines(['Linha1\n', 'linha2\n']) # Escreve linhas no arquivo atraves de uma lista



# Leitura de arquvios binarios
# Exemplo, quando você vai ler uma imagem
def ler_imagem():
    with open('imagem.png', 'rb') as arquivo:
        dados = arquivo.read()
        print(dados)
# Na hora de abrir aquivos binarios, usar os modos binarios

#wb: escrever binario
#rb: ler binario
