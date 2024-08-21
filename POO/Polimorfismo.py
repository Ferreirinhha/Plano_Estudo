""" Polimorfismo (Muitas formas):
- Permite que várias classes em uma hierarquia de herança implemente o mesmo 
método de maneiras diferente (sobrescrita) 
-O objetivo é permitir que o mesmo método se comporte de maneiras distintas 
dependendo do objeto que o chama."""


class Animal:
    def fazer_som(self):
        # O pass é usado para dizer ao python não fazer nada, um bloco de codigo que roda mas não faz nada
        pass # Método genérico, será sobrescrito por subclasses


class Cachorro(Animal):
    def fazer_som(self):
        return 'Cachorro faz auau'
    

class Gato(Animal):
    def fazer_som(self):
        return 'Gato faz miau'


class Vaca(Animal):
    def fazer_som(self):
        return 'Vaca faz mumu'


def emitir_som(animal):
    print(animal.fazer_som())


cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

emitir_som(cachorro)
emitir_som(gato)
emitir_som(vaca)


# Polimorfismo em funções e métodos
# A mesma função operando sobre diferentes tipos de dados
def somar(a, b):
    return a + b


print(somar(1, 2))
print(somar('Daniel', ' Ferreirinha'))
print(somar([1,2,3], [4,5,6]))