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