"""
FUNCÕES RECURSIVAS E RECURSIVIDADE

    Funções recursivas são funções que podem se chamar de voltar.
    São úteis para dividir problemas grandes em partes menores.

    Recursão é uma técnica amplamente usada em algoritmos que envolver estruturas hierarquicas(arvores e diretórios), navegação em estruturas aninhadas e algoritmos de divisão e conquista.

    dica: se há um problema que geralmente é resolvido com estruturas de repetição, GERALMENTE, dá pra converter em função recusiva.

    TODA FUNÇÃO RECURSIVA DEVE TER:
        1. Um problema que possa ser dividido em partes menores (ex: busca binaria)
        2. Um CASO RECURSIVO que resolve o pequeno problema
        3. Um CASO BASE que para a recursão
    
    Ex básico:
        fatorial -> n! = 5*4*3*2*1 = 120
    
    Stack Overflow:
        Se a função recursiva não tiver uma condição de parada, haverá um momento em que a pilha de execução vai "estourar", porque a função estará sendo chamada infinitamente. O Python lança um erro chamado RecursionError.
        Esse problema é um exemplo básico de stackoverflow.

    Exemplo de uso:
        Percorre Listas Aninhadas de Profundidade Indefinida
            Processa estruturas com múltiplos níveis de aninhamento (como listas dentro de listas), em que não se sabe de antemão quantos níveis existem.
        
    VANTAGENS:
        1. Código elegante e visível.
        2. Divisão de problemas complexos.
    
    CUIDADOS E LIMITAÇÕES PYTHON:
        1. Limite de profundidade(Recursion Limit): O python possui um limite padrão para profundidade máxima da pilha de chamadas recursivas para previnir travamentos na aplicação por consumo excessivo de memória.
        2. Custo de desempacotamento e memória: Como o interpretador padrão não possui otimização de chamada de cauda (Tail Call Optimization), cada chamada recursiva consome um quadro de pilha (stack frame).
        3. Otimização por memorização: A sequencia de Fibonacci, onde os mesmos subproblemas são recalculados repetidamente, pode-se utilizar o decorador @functools.lru_cache() para armazenas em cache os resultados intermediários e acelerar dramaticamente a execução. Em outros casos, o problema pode ser resolvido com abordagens iterativas simples usando laços while ou for. EXPLICAÇÃO NO PACOTE funcoes.

    TEM COMO TIRAR O LIMITE DE RECURSÃO: (NÃO É RECOMENDADO)
        import sys
        sys.setrecursionlimit(1004)

        CUIDADO: toda vez que usa uma funcao recursiva, o escopo inteiro da função tem que ser salva na callstack da memória.
"""
from functools import lru_cache

#conta até dez. Coloque um print pra entender o que está acontecendo. Parece um laço.
def recursiva(inicio=0, fim=10):
    if inicio >= fim - 1:
        return str(fim)
    inicio += 1
    return f'{inicio} .. {recursiva(inicio, fim)}'

print(f'contagem até 10: {recursiva()}')

#fatorial
def fatorial(n) -> int:
    if n <= 1:
        return 1
    return n * fatorial(n-1)

print(f'fatorial por recursão: {fatorial(4)}')

#sequencia de fibonacci (cada termo é a soma dos dois anteriores [0, 1, 1, 2, 3, 5, 8, 13, ...])
#é possivel melhorar usando CACHE. EXPLICACAO EM functools_lru_cache.py
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f'fibonacci por recursão: {fibonacci(6)}')
print()

#percorrendo listas aninhadas
def imprime_elementos(lista, nivel=0):
    for elemento in lista:
        if type(elemento) == list:
            imprime_elementos(elemento, nivel + 1)
        else:
            print(' ' * nivel + str(elemento))

lista = [1, [2, 3, 4, [5, 6, [9, 10, 11, {'nome': 'Rafael'}]]]]
imprime_elementos(lista)