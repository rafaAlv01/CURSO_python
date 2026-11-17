import copy
from collections.abc import Iterable

def aumentar_preco(produtos: Iterable[list], aumento) -> dict:
    novos_produtos = [
        {**p, 'preco': round(p['preco']*1.1, 2)}
        for p in copy.deepcopy(produtos)
    ]
    return novos_produtos

def ordem_decrescente(produtos: Iterable[list]) -> dict:
    produtos_ordenados_por_nome = copy.deepcopy(produtos) 
    
    return sorted(produtos_ordenados_por_nome, key=lambda x: x['nome'],reverse=True)

def ordem_preco_crescente(produtos: Iterable[list]) -> dict:
    produtos_ordenados_preco = copy.deepcopy(produtos)

    return sorted(produtos_ordenados_preco, key=lambda x: x['preco'])