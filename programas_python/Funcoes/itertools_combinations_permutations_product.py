"""
Combinação - ordem não importa, iterator, tamanho do grupo, um grupo não pode se repetir. ((x, y) e (y, x) não são possiveis na combinação)

Permutação - Ordem importa, iterator, tamanho do grupo, um grupo não pode se repetir. ((x, y) e (y, x) são possiveis na permutação)

Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product, combinations_with_replacement

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Mikael', 'Joana', 'Rafael', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliester'],
]

#Quantas combinações dá pra fazer em pessoas
print_iter(combinations(pessoas, 2))

#combinações que permite repetição: ex: (x, x) é possível.
print_iter(combinations_with_replacement(pessoas, 2))

#Quantas permutações dá pra fazer em pessoas
print_iter(permutations(pessoas, 2))

#produto cartesiano
print_iter(product(*camisetas))
print_iter(product(camisetas))