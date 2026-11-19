"""
Decorador lru_cache()

    É uma ferramenta para aplicar memoização. A memoização é uma técnica de otimização que armazena em memórias os resultados de chamadas anteriores de uma função custosa, evitando que o mesmo cálculo seja reprocessado para os mesmo argumentos.

    A sigla LRU significa Least Recently Used, indicando que, quando o cache atinge seu limite de capacidade, os resultados menos acessados há mais tempo são automaticamente descartados para dar lugar a novos resultados.

    SINTAXE:
        @functools.lru_cache(maxsize=128, typed=False)

        -> maxsize define a quantidade máxima de resultados armazenado no cache. O valor padrão é 128. Se for definido como None, o limite é desativado e o cache cresce infinitamente. Para melhor desempenho, recomenda-se que maxsize seja uma potencia de 2, pois os valores são convertidos e armazenados no formato binário.
        -> typed: quando definido como True, trata argumentos de tipos diferentes de forma separada. Por exemplo, f(1) e f(1.0) serão guardados como duas entradas distintas no cache.

        REQUISITO:
            Como lru_cache usa um dicionário interno para mapear os argumentos para o resultado correspondente, todos os argumentos passados para a função decorada devem ser hashtable(imutaveis). Passar argumentos mutaveis causará um erro TypeError.
    
    IMPACTO NA RECURSÃO
        O impacto mais impressionante do @lru_cache ocorre em algoritmos recursivos com subproblemas sobrepostos, como o cálculo da sequência de Fibonacci.

        Fibonacci sem cache:
            Na implementação recursiva tradicional sem cache, a função recalcula os mesmo valores várias vezes exponencialmente. Para calcular fibonacci(6), por exemplo, a função fibonacci(1) é chamada 8 vezes e fibonacci(2) é chamada 5 vezes. Para um valor modesto como fibonacci(30), a função sem cache realiza 2.692.537 chamadas recursivas, levando segundos para ser concluída.

        Fibonacci com cache:
            Ao adicionar o decorador @functools.lre_cache(), a complexidade de tempo cai de EXPONENCIAL O(2^n) para linear O(n). Com cache ativado, cada valor de n é calculado uma única vez. Nas chamadas seguintes para o mesmo subproblema, o resultado é retornado instantaneamente da memória.
    
    ALGUNS MÉTODOS:
        Retorna estatísticas: hits (acertos), misses (erros), maxsize e currsize
            print(fibonacci.cache_info()) # Exemplo de saída: CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
        Limpa/reseta totalmente o cache armazenado
            fibonacci.cache_clear()

    QUANDO USAR:
        -> Algoritmos recursivos com subproblemas repetidos(Fibonacci, arvore de decisão, programação dinamica)
        -> Funções puras computacionalmente pesadas que recebem os mesmo argumentos repetidas vezes.
        -> Chamadas frequentes de leitura de APIs ou consultas a banco de dados na rede que retornam dados estatisticos.

    QUANDO EVITAR:
        -> Funções com efeitos colaterais(que alteram o estado global ou gravam dados em arquivos/discos), pois a execução interna do corpo da função é ignorada se o resultado já estiver no cache.
        -> Funções cujos argumentos mudam constantemente sem repetição, o que apenas consumirá memória RAM sem gerar acertos (hits) no cache.
"""
from functools import lru_cache
import time

#RECURSÃO SEM CACHE.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

inicio = time.perf_counter()
resultado = fibonacci(40)
tempo_sem = time.perf_counter() - inicio
print(f'Com tempo de execuçaõ {tempo_sem}, o resultado é {resultado}')

#RECURSÃO COM CACHE
@lru_cache(maxsize=128)
def fibonacci_2(n):
    if n <= 1:
        return n
    return fibonacci_2(n-1) + fibonacci_2(n-2)

fibonacci_2.cache_clear()
inicio = time.perf_counter()
resultado = fibonacci_2(40)
tempo_sem = time.perf_counter() - inicio
print(f'Com tempo de execuçaõ {tempo_sem}, o resultado é {resultado}')
fibonacci_2.cache_clear()