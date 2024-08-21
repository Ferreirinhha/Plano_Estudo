""" Implemente uma classe base Instrumento com um método tocar(), e crie classes 
filhas Violao e Piano que sobrescrevem o método de maneira polimórfica. """

class Instrumento:
    def tocar(self):
        print('Nenhum instrumento é tocado.')


class Violao(Instrumento):
    def tocar(self):
        print('O violão toca acordes incríveis que inlouquecem qualquer um.')


class Piano(Instrumento):
    def tocar(self):
        print('O Piano toca notas suaves que deixam a plateia calma.')


instrumento = Instrumento()
instrumento.tocar()

violao = Violao()
violao.tocar()

piano = Piano()
piano.tocar()