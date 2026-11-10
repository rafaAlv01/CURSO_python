"""
List Comprehension

    É uma forma rápida para criar listas a partir de iteráveis.

    Sumário:
        -> forma de usar;
        -> mapeamento de dados (map) : permite pegar cada elemento de uma coleção e transforá-lo em um novo valor. Ele substitui a função nativa map(), oferecendo uma sintaxe mais legivel e direta. O elemento inicial é do mesmo tamanho que o final(a lista inicial tem o mesmo tamanho que a lista final(apos o map)).
        -> filtro de dados em list comprehension (filter) : serve para selecionar apenas os elementos que atendem a um critério especifico, descartando os demais. Essa operação substitui a função filter().
        -> Lista comprehension com mais de um for.
    
    Mapeamento é o if que vem antes do for.
    Filtro é o if que vem depois do for. Nesse caso, só tem o if. Não tem o else.
"""

lista = [num for num in range(5)]
lista_1 = [1 for num in range(5)]
lista_2 = [num*2 for num in range(5)]
print(lista)
print(lista_1)
print(lista_2)
print()

#Mapeamento de dados (map)
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [ #**produto -> novo dicionário. desempacotamento. 'preco': produto['preco'] * 1.05 --> lembre-se que o valor do dicionário é mutável. Como a chave é única, então ao fazer 'preco': produto['preco'] * 1.05 o Python vai alterar o valor da chave existente 'preco'.
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} ##esse if ternario irá executar a cada iteração do for.
    for produto in produtos
]

print(*novos_produtos, sep='\n')
print()

#Filtro de dados (filter)
lista = list(n for n in range(10))
print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10 #só vai colocar no novo dicionário quando o preço for maior que 10.
]

print(*novos_produtos, sep='\n')
print()

#Com mais de um for

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y)) #usando tupla para inserir dois valores em um indice da lista.
print(f'Sem list comprehension: {lista}')

lista = [
    x
    for x in range(3)
    for y in range(3)
]
print(f'Com list comprehension sem tupla: {lista}')
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(f'Com list comprehension com tupla: {lista}')

lista = [
    [letra for letra in 'Rafa']
    for x in range(3)
]
print(f'List comprehension dentro de list comprehension: {lista}')
lista = [
    [(x, letra) for letra in 'Rafa']
    for x in range(3)
]
print(f'List comprehension dentro de list comprehension com tupla: {lista}')