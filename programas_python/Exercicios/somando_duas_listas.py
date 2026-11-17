"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [
    dado1 + dado2
    for dado1, dado2 in zip_longest(lista_a, lista_b, fillvalue=0) #se quisesse que em lista_soma tivesse apenas os resultados que ocorreram a soma, use zip, pois vai delimitar o tamanho de lista_soma.
]
print(lista_soma)