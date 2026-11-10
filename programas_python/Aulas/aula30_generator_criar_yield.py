"""
COMO CRIAR UMA Generator functions em Python.
É uma função que pausa a execução para depois voltar.
ECONOMIZA MEMÓRIA.

    yield (PAUSA A EXECUÇÃO)
        -> É usada no corpo de uma função para transformá-la em uma função geradora.
        -> Ao contrário de uma função convencional que utiliza return para devolver um resultado e encerrar sua execução dentruindo o escopo local, yield produz/emite um valor e suspende temporariamente a execução da função, preservando todo o seu estado e variáveis locais para quando ela for chamada novamente.
        -> next() para que a função geradora continue a execução até o proximo yild.
    
    Yield from (retorna dados de outro generator)
        -> pode ser usado para construir GENERATORS complexos.
"""

def generator(n=0):
    yield 1 #pausou aqui
    print('Continuando...')
    yield 2
    return 'ACABOU' #Esse "acabou" aparece na exceção StopIteration, que sinaliza o término limpo da iteração.

gen = generator(n=0)
print(next(gen))
print(next(gen))

print()

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=3)

#O for usa o next() implicitamente.
for n in gen:
    print(n)
print()

#Yield from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()