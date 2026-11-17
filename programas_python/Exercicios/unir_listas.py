# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista_1, lista_2):
    resultado = []
    iterator_list_2 = lista_2.__iter__()
    for item in lista_1:
        try:
            prox_item_list_2 = next(iterator_list_2)
            resultado.append((item, prox_item_list_2))
        except StopIteration:
            break
    return resultado

print(zipper(cidades, siglas))

#usando zip
print(list(zip(cidades, siglas)))

#usando zip_longest --> explicação no pacote Funções.
from itertools import zip_longest
print(list(zip_longest(cidades, siglas, fillvalue='SEM CIDADE')))