""" Implemente uma classe Retângulo com atributos largura e altura. Crie um 
método calcular_area() que retorne a área do retângulo. Instancie três objetos 
diferentes e calcule as áreas. """


class Retangulo:
    largura = None
    altura = None 

    def calcular_area(self):
        print(f'Largura: {self.largura}')
        print(f'Altura: {self.altura}')
        return f'A área é: {self.altura * self.largura}'
    


retangulo1 = Retangulo()
retangulo1.altura = 10
retangulo1.largura = 20

print(retangulo1.calcular_area())


ret2 = Retangulo()
ret2.altura = 29
ret2.largura = 90

print(ret2.calcular_area())



ret3 = Retangulo()
ret3.largura = 20
ret3.altura = 87

print(ret3.calcular_area())