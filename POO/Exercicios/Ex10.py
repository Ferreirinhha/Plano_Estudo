""" Implemente uma classe Pessoa com atributos privados __nome e __idade, e 
métodos para modificar e acessar esses atributos. """


class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    

    def cartorio(self, novo_nome):
        self.__nome = novo_nome
        return novo_nome


