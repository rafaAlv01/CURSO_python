"""
    A função zip() é uma função nativa do Python projetada para permitir a iteração simultânea e em paralelo sobre duas ou mais sequências iteraveis. Ela junta duas sequências elemento a elemento de forma segura.

    Ela pega o primeiro elemento de cada iterável e os junta em uma tupla, depois o segundo elemento de cada um formando outra tupla, e assim sucessivamente.

    A função zip() cria um objeto iterador/gerador que produz as tuplas por demanda.

    Por padrão, o zip() interrompe a geração de tuplas assim que a menor das sequências de entrada se esgota. Os elementos excedentes são ignorados.

    Não é interessante ignorar elementos excedentes em Ciência de Dados. Para que o zip() não descarte esses elementos, usa-se a função zip_longest() do módulo itertools. A função fillvalue= usada dentro do argumento é usada para tratar valores None.

    Facilita a criação de dicionários. Ao usar a função de conversão dict(), as tuplas geradas pela função zip são usadas para criar um dicionário contendo os pares key:value, sendo o key de um iteravel e o value de outro.
"""

from itertools import zip_longest

nomes = ['Rafael', 'Maria', 'Mikael', 'Raimunda']
indices = list(range(4))
zipper = zip(nomes, indices) #cria o objeto iterador

print(f'Produz um objeto iterador:', zipper) #retorno preguiçoso
print(f'Visualizando em uma lista:', list(zipper))

#forma de usar em um for.
for nome, indice in zip(nomes, indices):
    print(f'{nome} tem indice {indice}')

#lidando com sequencias de tamanho diferentes
curto = ['1', '2']
longo = ['a', 'b', 'c', 'd']
print(f'Sequencias de tamanhos diferentes:', list(zip(curto, longo)))

#lidando com tamanhos diferentes sem descartar o excedente.
print(list(zip_longest(curto, longo, fillvalue='-')))

#Criando dicionários a partir do zip.
key = ['nome', 'cargo', 'salario']
value = ['Rafael', 'Dev', 5000]

dados = dict(zip(key, value))
print(f'Dicionário criado:', dados)