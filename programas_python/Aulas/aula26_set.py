"""
CONJUNTOS [set]

    Set em Python representam os conjuntos na metemática. (Resumo sobre Conjuntos na pasta arquivos)
    Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
    Não aceita se dentro de uma tupla tiver um tipo mutavel.
    MOTIVO: por usar tabela hash, os dados inseridos no conjunto não podem mudar (precisam ser hashable). Logo, não é possível criar um conjunto de conjuntos.

    Sets são eficientes para remover valores duplicados de iteráveis.

    Busca em tempo 0(1) -> usa Hash Table

    CARACTERISTICAS:
        -> não tem index
        -> não garantem a ordem
        -> são iteráveis (for, in, not in)

    Métodos úteis:
        -> add: adiciona um item ao conjunto
        -> update: adiciona de forma iterada
        -> clear: remove todos os elementos do conjunto
        -> discard: remove o item se ele estiver presente (não lança um erro)
        -> pop: remove e retorna um elemento arbitrário do conjunto (lança KeyError se estiver vazio)
        -> remove: remove o item, mas lança a exceção KeyError caso o elemento não exista no conjunto.

    UNIAO -> | -> a.union(b)
    INTERSEÇÃO -> & -> a.intersection(b)
    DIFERENÇA -> - -> a.difference(b)
    DIFERENÇA SIMÉTRICA -> ^ -> a.symmetric_difference(b)

    Onde pode ser usado:
        -> remoção instatanea de duplicatas.
        -> testes de pertencimento de alta performance (se itens pertencem a um catalogo)
        -> comparações de chaves em dicionários :
            O método keys() dos dicionários se comportam de maneira similar a conjuntos, permitindo aplicar operadores como & e - diretamente sobre chaves de dicionários.
                chaves_comuns = dict_a.keys() & dict_b.keys()
        -> Controle de permissões e Tags:
            Útil para comparar permissões de usuários. Ex: verificar se as permissões exigidas por uma rota são um subconjuntos das permissões do usuário logado usando <= .
"""

#DECLARAÇÃO -> set(iterável) ou {1, 2, 3}
conjunto_1 = set()
conjunto_2 = set('Rafael') #se coloca um iteravel dentro, ele vai forçar a fragmentação dele.
print(f'Str dentro de um Set: {conjunto_2, type(conjunto_2)}') #note que a ordem fica aleatoria. Aqui, só dá pra colocar um argumento.

conjunto_3 = {'Luiz', 2, 1, 1, (1,2)}
print(f'Set com vários argumentos: {conjunto_3}') #Note que o 1 não entrou no conjunto, pois ele é repetido.

dicionario = {}
print('Ao tentar criar um conjunto (set) vazio, não use { }, pois estará criando um dicionario.')
print()

#for, in, not in
print(f'Usando in: {'f' in conjunto_2}')

for date in conjunto_3:
    print(date, end=' ')

print('\n')

#UNIAO, INTERSEÇÃO, DIFERENÇA, DIFERENÇA SIMÉTRICA.
dados_1 = {'Rafael', 'Maria', 'Jose'}
dados_2 = {'Rafael', 'Lucia', 'Bianca'}
uniao = dados_1 | dados_2 #retorna a junção dos conjuntos
intersecao = dados_1 & dados_2 #retorna apenas os elementos em comum
diferenca = dados_1 - dados_2 #retorna os elementos que estao em dados_1, mas nao estao em dados_2
diferenca_simetrica = dados_1 ^ dados_2 #retorna os elementos que estão em um dos conjuntos, mas não em ambos.

print(f'{uniao=}\n{intersecao=}\n{diferenca=}\n{diferenca_simetrica=}')
print()

#add()
conjunto_2.add('Maria')
conjunto_2.add(2)
print(f'Inserindo com add() : {conjunto_2}')

#update
conjunto_2.update(('BraSil', 1, 2, 3, 4)) #note que é uma tupla. Se fosse somente o nome, iria colocar letra por letra.
print(f'Inserindo com update : {conjunto_2}')

#discard
conjunto_2.discard(4)
print(f'Removendo com discard : {conjunto_2}')

#pop
dado_arbitrario = conjunto_2.pop()
print(f'Removendo aleatoriamente com pop : {dado_arbitrario}\n{conjunto_2=}')

#clear
conjunto_2.clear()
print(f'Removendo tudo com clear : {conjunto_2}')