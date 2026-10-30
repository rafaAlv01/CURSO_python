"""
    Listas em Python

    DADOS MUTÁVEIS exigem cuidado.
    
    OBS: MOVER ITENS NA LISTA EXIGE MUITO PROCESSAMENTO SE FOR UMA LISTA GRANDE.

    del, append, pop, insert, extend, copy,
"""

lista = []
print(lista, type(lista))

lista = [123, True, 'Rafa', 1.2, []]
print(lista)

#acesso por indice
print(lista[2].upper(), type(lista[2]))

#mostra que é possível alterar um dado. MUTABILIDADE.
lista[-3] = 'Rafael'
print(lista)

"""
List suporta o CRUD
"""

del lista[-1] #quando isso acontece, os itens da lista são movidos à esquerda.
print(lista)

lista.append('Amor') #insere dado no final da lista.
print(lista)

dado_removido = lista.pop() #Remove o ultimo valor da lista, retornando o item removido.
print(lista)
print(dado_removido)

dado_removido = lista.pop(0) #Remove o valor do indice 0. Os elementos são deslocados à esquerda.
print(lista)
print(dado_removido)

lista.insert(2, 25) #insere no indice 2 o numero 25. Todos os elementos posteriores serão deslocados à direita.
print(lista)        #se o indice for maior que o indice do ultimo elemento da lista, o valor será inserido depois da ultima posição.

#Metodo extend para concatenação.
lista_a = ['1', '2', '3']
print(lista_a)
lista_a.extend(lista) #extend altera a variável antes do ponto.
print(lista_a)

#metodo copy
lista_b = ['Rafa']
lista_b = lista_a.copy() #o método copy() retorna uma nova lista com os mesmos valores da lista_a.
print(lista_b)