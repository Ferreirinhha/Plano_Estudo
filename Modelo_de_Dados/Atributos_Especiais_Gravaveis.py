# Função.__doc__
#Representa as docstrings da função

def soma(a: int,b: int) -> int:
    """Soma de dois números""" # Sempre na parte de cima da função
    return a + b

print(soma.__doc__)  # Saída: "Soma dois números."


# Função.__name__
# Nome da função

print(soma.__name__) # Saída: "soma"


# Função.__qualname__
# Nome completo da função, classe, modulo

print(soma.__qualname__) # Saída: "soma" (só aparece um porque ele não esta em uma classe ainda)


#Fubção.__defaults__
# O parametro da função ou None se não estiveren valores

print(soma.__defaults__) # Saída: "None"


# Função.__module__
# Nome do mmódulo onde a função foi definida

print(soma.__module__) # Saída: "__main__"


# Função.__code__
# Detalhes sobre o códio da função

print(soma.__code__) # Saída: "<code object soma at 0x0000021B7F1802D0, file "c:\Códigos\Python\Modelo_de_Dados\Atributos_Especiais_Gravaveis.py", line 4>"


# Função.__annotations__
# Um dicionario com anotações de tipo para os parâmetros da função

print(soma.__annotations__) # Saída: "{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>} "


# Função.__kwdefaults__
# Um dicionario contendo os valores padrao apenas para parâmetros nomeados

def minha_funcao(a, b=2, c=3):
    pass

print(minha_funcao.__kwdefaults__)  # Saída: {'b': 2, 'c': 3}
