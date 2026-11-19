"""
    A função sorted() é um dos recursos mais poderosos e flexíveis da linguagem Python para ordenação de dados. Ela aceita qualquer coleção ou objeto iterável e produz uma nova lista com os elementos devidamente ordenados.

    sorted() ou list.sort()
        -> list.sort(): método exclusivo da tipo list. Ele ordena a lista no próprio local(in-place), modificando o objeto original e retornando None. Não pode ser aplicadao diretamente a iteráveis imutáveis(como tuplas ou strings) ou geradores.
        -> sorted(): função global que aceita qualquer objeto iterável e sempre retorna uma nova lista, mantendo a coleção original intacta.

    SINTAXE:
        sorted(iterable, key=None, reverse=False)

        1. iterable: recebe um iteravel contendo as entradas.
        2. key (opcional): uma função(lambda) de um único argumento aplicada a cada elemento antes da comparação para gerar a sua chave/critéerio de ordenação. O padrão para comparar os próprio elementos(None). Usado para ordenar iteráveis cujos elementos contém mais de uma informação normada (ex: dicionarios).
        3. reverse(opcional): True em ordem decrescente e False crescente.

        NOTA: o sorted recebe a função lambda(key), chama ela para cada produto e obtém apenas os números(valores associados). É com esses números que o Python faz a ordenação de verdade.

        O parâmetro key é extremamente eficiente porque a função especificada é chamada exatamente uma única vez para cada item da coleção (para calcular a chave), e a comparação subsequente é realizada diretamente em código C otimizado no interpretador.

    Algoritmo Timsort:
        -> O Python utiliza internamente o Timsort. Trata-se de um algoritmo híbrido adaptativo que alterna entre as estratégias de insertion sort e merge sort, aproveitando subsequencias pré-ordenadas que frequentemente existem em dados do mundo real.
        -> É um algoritmo estável, o que significa que ele preserva rigorosamente a ordem relativa original de elementos que possuem chaves de comparação iguais.

    Recursos Avançados e casos de uso:
        Ordenando Dicionários e Estruturas Complexas com operator.itemgetter:
            -> Embora expressões lambda possam ser usadas como chave(key), a função operator.itemgetter() costuma ser mais rápida e legível ao ordenar listas de dicionários ou tuplas por um ou mais campos.

        Ordenando Objetos Customizados com operator.attrgetter e methodcaller
            -> Para ordenar listas de instâncias de classes personalizadas por atributos, utiliza-se operator.attrgetter().
            -> Para ordenar com base no resultado de um método do objeto, utiliza-se operator.methodcaller().
                ex:
                    from operator import attrgetter, methodcaller

                    # Ordena objetos pela propriedade user_id
                    sorted(lista_usuarios, key=attrgetter('user_id'))

                    # Ordena objetos de pontos pela distância da origem chamando o método distance(0,0)
                    sorted(pontos, key=methodcaller('distance', 0, 0))
        
        Ordenando Dicionários por Valores com zip()
            -> Para realizar cálculos ou ordenar um dicionário com base nos seus valores(e não nas chaves), é comum inverter os pares utilizando a função zip(dict.values(), dict.keys()).

        Injeção de Parâmetros Extras com functools.partial
            -> Se o critério de ordenação exigir uma função que receba mais de um parâmetro (por exemplo, calcular a distancia de cada ponto em relação a uma coordenada fixa pt), utiliza-se functools.partial para pré-fixar o argumento e atender à exigencia do key (que aceita apenas funcoes de um argumento).

    TRATAMENTO DE TIPOS MISTOS E EXCEÇÕES:
        No Python 3, tentar ordenar uma coleção que contenha tipos heterogeneos não comparáveis (como números e strings mesclados) resulta na exceção TypeError: unorderable types.
        Para contornar essa restrição quando necessário, pode-se padronizar a compração convertendo todos os elementos via key.
    
    Ordenação de Texto Unicode e Localização:
        A ordenação padrão de strings compara os códigos Unicode (code points) de cada caractere, o que faz com que letras maiúsculas venham antes de minúsculas e caracteres acentuados fiquem fora da ordem alfabética convencional.
            -> Ordenação sensível à localização(locale.strxfrm): Converte strings de acordo com as regras alfabéticas do idioma/sistema operacional configurado.
            -> Algoritmo UCA(pyUCA): Para ordenação Unicode independente do sistema operacional, utiliza-se a biblioteca pyuca, passando key=coll.sortkey. PRECISA INSTALAR A BIBLIOTECA pyuca.
                ex:
                    import pyuca
                    coll = pyuca.Collator()
                    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']

                    sorted_fruits = sorted(fruits, key=coll.sort_key)
                    print(sorted_fruits) #Resultado: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
    
    Suporte a Ordenação em Classes Personalizadas:
        Para que instancias de uma classe própria possam ser ordenadas nativamente(usando operadores de comparação), pode-se implementar os métodos de comparação rica (__lt__, __eq__) ou utilizar o decorador @functools.total_ordering, que preenche automaticamente os demais métodos de comparação a partir das definições mínimas.
                    
"""
from operator import itemgetter
from functools import partial
import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1) #calcula a diferença euclidiana.

#Ordenação:
frutas = ['grape', 'raspberry', 'apple', 'banana'] 
resultado = sorted(frutas)
print(f'Ordem crescente: {resultado}')

resultado = sorted(frutas, reverse=True)
print(f'Ordem decrescente: {resultado}')

# Ordenação pelo comprimento da string
resultado = sorted(frutas, key=len)
print(f'Ordenando da menor palavra pra maior: {resultado}')
print()

#USANDO COM DICIONARIOS
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_ordenados_por_preco = sorted(produtos, key=lambda x: x['preco']) #pega o dicionario x, e ordena de acordo com o valor da chave (x['preco'])
print(f'Dicionario ordenado considerando uma chave em especifica:\n{produtos_ordenados_por_preco}')
print()

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# Ordena por sobrenome e depois por primeiro nome
rows_ordenados = sorted(rows, key=itemgetter('lname', 'fname'))
print(f'Duas chaves sendo usadas para ordenação: primeiro lname e depois fname.\n{rows}')
print()

precos = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20}
precos_ordenados = sorted(zip(precos.values(), precos.keys()))
print(f'Usando zip para n usar o parametro key:\n{precos_ordenados}')
print()

#Usando partial de functools
pontos = [(1, 2), (3, 4), (5, 6)]
ponto_referencia = (4, 3)

#fixa o primeiro argumento da função de distancia
pontos_2 = sorted(pontos, key=partial(distance, ponto_referencia)) #pegou o ponto (1,2) e calculou a distancia até (4,3) e a assim por diante.
print(f'Usando partial para ordenar: {pontos}')
print()

#TRATAMENTO DE TIPOS MISTOS E EXCEÇÕES
lista_mista = [28, 14, '28', 5, '9', '1']
lista_mista_ordenada = sorted(lista_mista, key=int) #converte tudo para int durante a comparação.
print(f'Convertendo tipos mistos para inteiros, a fim de realizar a ordenação: {lista_mista_ordenada}')
print()
