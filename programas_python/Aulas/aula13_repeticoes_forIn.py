"""
    for arg1 in object -> para cada arg1 em object, faça algo.
    
    O FOR IN é usado para coisas FINITAS, determinadas.

    Da mesma forma que o while, o for também pode ser usado com else.
    for arg1 in object:
        ...
    else:
        ...
"""

texto = 'Python'

for letra in texto:
    print(letra)

#for com range. O for solicita os números ao gerador range, um por um.
numeros = range(0, 100, 50)

for numero in numeros:
    print(numero)

"""
Quando um laço 'for caractere in texto:' é executado, o Python faz exatamente esse processo automaticamente:
1. chama iter(texto) em segredo,
2. executa next() a cada iteração,
3.interrompe a repetição de forma limpa quando o iterador lança a exceção de término `StopIteration`.
"""
#simulação de como funcionaria por debaixo dos panos.

#for letra in texto
meu_iterador = texto.__iter__() # ou iter(texto)

while True:
    try:
        letra = next(meu_iterador)
        print(letra)
    except StopIteration:
        break

"""
    usando for/in em listas
"""

lista = ['Rafael', 25, True, 'CdC']

for dado in lista: #para cada item da lista, faça algo. 
    print(dado, type(dado))