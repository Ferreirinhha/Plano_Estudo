class cachorro:
    nome = ''
    raca = ''
    tamanho = ''
    idade = 0 # isso é um atributo da classe animal


    def morder(self, pessoa): # Isso é um método, funções dentro de classes
        print(f'O {self.nome} mordeu o {pessoa}')