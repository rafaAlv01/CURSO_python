'''
Na aula 14 tem mais sobre isso. Além disso, lá na aula que fala do forin fala sobre isso.

iteratores são usados para economizar memória.
'''
import sys

iteravel = ['Eu', 'tenho', '__iter__'] #tem os valores
iterador = iteravel.__iter__() #entrega os valores por vez. Só sabe te entregar o proximo valor (next()).
#daria pra fazer: iterador = iter(iteravel)

print(next(iterador))
print(next(iterador))
print(next(iterador))
#Se tentar chamar next dnv, vai dar erro, pois o iterador está vazio.

#VENDO O QUANTO DE MEMÓRIA OCUPA.
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(f'Omitindo o output da lista para não tomar espaço no terminal.\n{generator=}\nBytes que a lista ocupa na memória: {sys.getsizeof(lista)}\nBytes que o generator ocupa na memória: {sys.getsizeof(generator)}')