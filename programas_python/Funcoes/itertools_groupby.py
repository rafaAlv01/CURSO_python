"""
groupby - AGRUPANDO VALORES

Complexo de usar porque é necessário tratar os dados antes de começar a agrupar.

OS DADOS PRECISAM ESTAR ORDENADOS PARA QUE O groupby POSSA ORDENAR CORRETAMENTE.

LEMBRE-SE SEMPRE DE ORDENAR OS DADOS COM BASE NO CRITÉRIO DE AGRUPAMENTO.

alunos = [
    'a','a','a','a','a','a','b','c'
]

nessa lista há 3 grupos: a, b, c. O grupo 'a' tem o valor ['a','a','a','a','a','a'], pois são identicos.
Por isso a necessidade de tratar os dados. 'b' e 'c' tem um grupo cada.

ALÉM DISSO, para estruturas de dados mais complexas, como lista de dicionários, normalmente se usa groupby para mostrar grupos de dicionários considerando um valor em especifico.
EX: TODOS OS ALUNOS QUE TIRARAM NOTA 'A'.

"""
from itertools import groupby

alunos = [
    'a','a','a','a','a','a','b','c'
]
grupos = groupby(alunos)
#print(list(grupos)) -> se usar isso, o iterator vai sumir, pois vai acabar os elemetos a serem processados.s

#grupos contém uma lista de tuplas, com chave e valor. A chave é o item da lista, o valor é o objeto.
print('Grupo com valores ordenados:')
for chave, valor in grupos:
    print(chave,'->',list(valor))
print()

alunos = [
    'a','a','a','a','a','b','c','a'
]
grupos = groupby(alunos)
print('Grupo com valores NÃO ordenados: (note que o \'a\' que não está ordenado é contado como um grupo distinto.)')
for chave, valor in grupos:
    print(chave,'->',list(valor))
print()

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
grupos = groupby(alunos)

#usando uma funcao lambda para não repetir codigo:
def ordena(aluno): #isso é a mesma coisa que lambda x:x['nota']
    return aluno['nota']

#A ideia aqui é ordenar a lista primeiramente, preparar os dados.
alunos_agrupados = sorted(alunos, key=ordena)

print('Dados ordenados para usar o groupby com uma lista de dicionários:')
print(*alunos_agrupados, sep='\n')
print()

#informando a chave para groupby para que ele saiba qual valor usar para ordenar.
grupos = groupby(alunos_agrupados, key=ordena)
print('Dados agrupados a partir da chave \'nota\' do dicionário:')
for chave, valor in grupos:
    print(chave,'->',list(valor))
print()