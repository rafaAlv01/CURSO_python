"""
    namedtuple é um objeto que cria subclasses de tuplas cujos campos podem ser acessados tanto por nome de atributo quanto por índice numérico.

    está no módulo collections. Precisa ser importado.
"""
from collections import namedtuple

tupla_modificada = namedtuple('tupla_modificada', ['x', 'y'])

t = tupla_modificada(10, 20)
print(t.x, t.y)