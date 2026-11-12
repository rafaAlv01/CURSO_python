"""
    __all__ é a representaçã textual para * nos imports.
    Se, dentro desse modulo, fizer 
        __all__ = [
            'variavel',
        ]
    E outro modulo que chamar esse modulo usando *
        from modulo_com__all__ import *
    Apenas o item variavel será retornado.

    Sem o __all__ especificado, ao usar o * o Python importa tudo.
"""

__all__ = [
    'variavel',
]

variavel = 'Rafael'