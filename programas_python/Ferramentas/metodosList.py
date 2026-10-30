"""
    MÉTODOS ÚTEIS:
        append, insert, pop, del, clear, extend, copy,
"""
lista = [123, True, 'Rafa', 1.2, []]

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
#SE NÃO TIVESSE USADO O MÉTODO copy(), lista_b RECEBERIA A REFERENCIA DA lista_a. OU SEJA, ALTERAÇÕES FEITAS EM QUALQUER UMA, PREJUDICARIA A OUTRA, pois são a mesma lista.