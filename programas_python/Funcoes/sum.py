"""
    A função sum() é utilizada para somar todos os elementos numéricos de um iterável(listas, tuplas, conjuntos ou geradores) e retornar o valor total acumulado.

    Assinatura: sum(iterable, start=0) -> start é o valor inicial da soma.
"""
indices = [1, 2, 3]
lista = list(range(3))


print(sum(lista))

print(dict(zip(indices, lista)))

#quando é usado em um dicionário, soma apenas os valores das chaves.
print(sum(dict(zip(indices, lista))))

#range
print(sum(range(5)))

#usando START
vendas = [150.0, 200.0, 50.0]
saldo_inicial = 500.0
total_caixa = sum(vendas, start=saldo_inicial)
print(f'Usando o parametro start:', total_caixa)

#USANDO COM EXPRESSÕES GERADORAS
num = list(range(1, 3))
soma_quadrados = sum(x*x for x in num)
print(soma_quadrados)

cpf_numeros=list(range(10))
soma_nove_digitos = sum(int(num) for indice, num in enumerate(cpf_numeros) if indice < 9)