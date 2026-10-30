"""
    O tipo tupla é uma lista imutável.

    O MÉTODO tuple() converte outro iteravel em tuplas.

    A tupla promove:
        1. Proteção de Dados: após a criação, seus elementos não podem ser alterados, adicionados ou removidos. Garante a INTEGRIDADE.
        2. Desempenho: por ser imutáveis, o interpretador Python consegue aplicar otimizações internas.
        3. Imutabilidade relativa: A imutabilidade se aplica às referências DIRETAS mantidas pela tupla. Se uma tupla mantiver uma referencia para um objeto mutável,
            como a list, o conteúdo dessa lista interna poderá ser modificado.
        4. Uso em dicionários: diferentes de listas, tuplas podem ser utilizadas como chaves de dicionários e elementos conjuntos(set), desde que todos os objetos
            contidos na tupla também sejam imutáveis e associáveis a um hash.

    Quando uma função retorna multiplos valores separados por virgula, na realidade ela esta construindo e retornando uma unica tupla.

"""

#DECLARAÇÕES

tupla_vazia = tuple()
tupla_vazia2 = ()
ponto = (10, 20)
dado = ('Rafael', 25, 10000)
tupla_unica = (10,) #aqui é uma tupla de um elemento
nao_tupla = (1) #aqui é um inteiro

#EMPACOTAMENTO -> cria uma tupla separando os valores por virgula.
coordenadas = 1, 2, 3 #gera uma tupla com 3 valores: (1, 2, 3)

#DESEMPACOTAMENTO
dado1, *restante = dado
print(dado1, restante) #restante é uma lista!

#TROCA DE VARIÁVEIS sem variavel temporaria.
dado, coordenadas = coordenadas, dado
print(dado, coordenadas)

#OPERAÇÕES SUPORTADAS: Indexação por fatiamento, verificação e métodos de consulta, concatenação e replicação.
eggs = ('hi', 25, 0.2)
print(eggs[0], eggs[1:5], len(eggs), 25 in eggs, 0.2 not in eggs, eggs.count('hi'))

''' 
    TUPLAS NOMEADAS usa a fábrica collection.namedtuple que cria subclasses de tuplas cujos
        campos podem ser acessados tanto por nome de atributo quanto por indice numerico.
    Mantém baixo consumo de memória e trazem mais clareza ao código.
'''

#tuple()
lista = [1, 2, 'olá']
print(type(lista), lista)
convertida = tuple(lista)
print(type(convertida), convertida)

"""
    TUPLAS VAZIAS servem para:

    1. Manter a INTEGRIDADE DOS VALORES. Não é interessante usar uma lista vazia [] como valor padrão de um argumento em funções, pois o objeto da lista é
        compartilhado entre chamadas consecutivas (causando bugs dificeis de rastrar). Se uma função precisa retornar ou receber algo imutável, a tupla vazia é o padrão ideal.
    
    2. Desempacotamento seguro ou funções que retornam múltiplos valores vazios. Se você tem uma função que busca dados dinamicamente, e ela não encontra nenhum resultado,
        retornar uma tupla vazia () indica formalmente que nenhum dado foi encontrado, mantendo o mesmo tipo de retorno esperado de quando a busca é bem-sucedida.

    3. Usada em código avançado, algoritmos recursivos ou estruturas de dados baseadas em árvores/grafos: os nós folhas ou ramos vazios são frequentemente representados
        por tuplas vazias para economizar espaço e evitar que dados acidentalmente corrompam a estrutura.

"""