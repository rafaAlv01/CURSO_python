"""
map, partial, GeneratorType e esgotamento de Iterators

    TRES FUNCOES QUE ANDAM JUNTAS: maps, filter, reduce. são parecidas.

    Na aula de list comprehension foi aprendido o mapeamento.

    MÓDULO functools são FERRAMENTAS para funções.

        -> partil é uma função que vai receber uma função, um dos argumentos (ou varios argumentos), e vai retornar uma função simplificada. Ela é usada para simplificar funções em que alguns de seus argumentos podem se repetir para diferentes casos.
            ex: considere uma função
                    valor_camiseta(camiseta, cor, tamanho, tecido)
                que retorna o valor de uma camiseta de acordo com a camiseta, sua cor e seu tamanho.

                observe que uma camiseta y, da cor x, pode, ainda, ter vários tamanho e pode ser feita de vários tecidos. Nesse sentido, usando partial, é possível simplificar essa função criando outra função que fixe o valor de y e x.
                    valor_camiseta_x_cor_y = partial(valor_camiseta, camiseta=y, cor=x)
                Assim, a função valor_camiseta_x_cor_y() só vai receber dois argumentos: tamanho e cor, nessa ordem.
    
    MAP -> precisa de outra função, essa outra função que realizará a tarefa que o programador quiser.

        É uma função embutida projetada para aplicar uma função a cada elemento de um ou mais iteráveis.

        SINTAXE:
            map(funcao, iteravel_1, ..., iteravel_n)

        Retorna um iterável, que NÃO É um gerador. Para não ter problemas com esgotamento de iterator e reaproveitar os valores, basta transformar o map em uma lista.

        Processamento em Paralelo com Múltiplos Iteráveis
            Os elementos de cada iteravel são consumidos em paralelo. A iteração é encerrada de forma automática assim que o iterável mais curto for esgotado.

        map() vs List Comprehensions e Generator Expressions
            -> List Comprehensions e Generator Expressions são ainda mais usadas que o map.
            -> map() traz menos legibilidade que as outras.
            -> map() pode exigir o uso de funções lambdas encadeadas, enquanto listcomp ou genexp resolvem a mesmo operação de forma mais legível.
            -> Se precisa de um iterator, uma expressão geradora, ex (fact(n) for n in range(6)), realiza o mesmo papel que o map, ex map(fact(n), range(6))

"""
from operator import mul
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem(valor, porcentagem): #aumenta porcentagem
    return round(valor * porcentagem, 2)

#usando partial para simplificar.
aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

def aumentar_preco_de_produto(produto): #aumenta preco em 10%
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#USANDO LIST COMPREHENSION
novos_produtos = [ #usando list comprehension
    {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos
]

print('Usando list comprehension:')
print_iter(novos_produtos)

novos_produtos = [ #usando list comprehension
    aumentar_preco_de_produto(p) for p in produtos
]
print('Usando a funcao aumentar_precos_produtos com aplicacao da partial:')
print_iter(novos_produtos)

#USANDO MAP
novos_produtos = map( #map passará a função em cada um dos produtos.
    aumentar_preco_de_produto,
    produtos
)
print('Usando map:')
print(novos_produtos)
print_iter(novos_produtos)
print('Tentando imprimir novos_produtos de novo:')
print_iter(novos_produtos)
#Para solucionar esse problema, basta jogar o map, iterator, em uma lista. Aí é possível reutilizar.

#GeneratorTypes
print(f'Mostrando que map é um iterator mas não é um generator: {isinstance(novos_produtos, GeneratorType)}')
print()

multiplicados = map(mul, range(11), [10, 15, 16])
print('Exemplificando map com vários iteráveis:', list(multiplicados)) #0 * 10, 1 * 15, 2 * 16