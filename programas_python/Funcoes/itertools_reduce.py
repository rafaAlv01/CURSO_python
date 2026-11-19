"""
FUNÇÃO reduce

    Usada para reduzir um iterável em um único valor.

    A função reduce precisa de um acumulador.

    SINTAXE:
        reduce(function, iterator->iter, acumulador->int)
"""
from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0 #acumulador do for
for p in produtos:
    total += p['preco']

print(f'Mostra o valor total dos produtos usando um for: {round(total, 2)}')

print(f'Usando a funcao sum: {round(sum([p['preco'] for p in produtos]), 2)}')

def funcao_soma(acumulador, produto): #pode ser substituida por: lambda ac, p: ac + p['preco']
    return acumulador + produto['preco'] 

total = round(
    reduce(
        funcao_soma,
        produtos,
        0
    ),
    2
)

print(f'Usando a funcao reduce: {total}')