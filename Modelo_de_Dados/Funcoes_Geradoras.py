# Yield --> Retorna os valores da função sob demanda, conforme for sendo incializado ele vai dando um valor por vez


def contar_ate_3():
    yield 1 # Pausa e "devolve" 1
    yield 2 # Pausa e "devolve" 2
    yield 3 # Pausa e "devolve" 3




# Exemplo pratico

def ler_arquivo_grande(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            yield linha.strip()


# Usando a função geradora

for linha in ler_arquivo_grande('grande_arquivo.log'):
    if "ERRO" in linha: #Proucura por linhas que contenham "ERRO"
        print(linha)


#Outro exemplo

def gerar_fibonacci():
    a, b = 0, 1
    while True:  # Sequência infinita
        yield a  # Retorna o próximo número da sequência
        a, b = b, a + b

# Usando a função geradora
contador = 0
for numero in gerar_fibonacci():
    print(numero)
    contador += 1
    if contador == 10:  # Interrompe após 10 números
        break
