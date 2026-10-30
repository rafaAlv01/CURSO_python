"""
    Listas em PYHTON
    Type = Mutável -> isso significa que pode ser alterado, adicionado e removido após sua criação.
    Suporte a vário valores de qualquer tipo. É heterogeneo: uma única lista pode armazenar elementos de tipos de dados variados, até mesmo outras listas.
    Conhecimentos reutilizáveis - indice de fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend, +

    Ordenada: mantém a posição exata em que foram inseridos e são acessados a partir do seu indice.
        índice positivo: acessa o primeiro elemento, o segundo e assim por diante.
        índice negativo: acessam de trás pra frente, lista[-1] pega o ultimo, lista[-2] o penultimo e assim por diante.

    Fatiamento: permite extrair uma sublista com a sintaxe
            lista[inicio:fim] (o limite final não é incluído)
    
    Modificação direta: para alterar um elemento, atribui-se um NOVO valor diretamente ao seu índice.

    ATENÇÃO: AO ATRIBUIR UMA LISTA A OUTRA LISTA (v2 = v1), O PYTHON NÃO CRIA UMA NOVA CÓPIA, MAS SIM UMA REFERÊNCIA APONTANDO PARA O MESMO OBJETO NA MEMÓRIA.
             ALTERAR UMA VARIÁVEL AFETARÁ A OUTRA.

    Na List podemos Criar, Ler, Alterar, Apagar. Na programação isso é chamado de CRUD(create, read, update, delete).

"""
#Para criar um pacote com várias coisas, pode-se usar uma lista.

"""
    FORMAS DE DECLARAR UMA LISTA
"""

lista_vazia = []
lista_com_elementos = ['gato', 'cachorro', 'tartaruga']
dados_diferentes_tipos = ['amor', 10, True, None, 42]
listas_aninhadas = [['cat', 'bat'], ...] #lista de listas ou as famosas MATRIZES.

#declarando usando o Construtor list() (Construtor é um método/função que cria o objeto)
#A função embutida list() é utilizada principalmente para converter outros objetos iteráveis em uma nova lista.

lista_metodo = list('hello') #cria a partir de uma string
lista_metodo1 = list(('gato', 'cachorro', 5)) #a partir de uma tupla
lista_metodo_rage = list(range(5)) #a partir de um iterável

#Contruindo lista aplicando transformações e filtros sobre outros iteráveis

#TRANSFORMAÇÃO DE ELEMENTOS
simbolos_1 = ['A', 'B', 'C']
codigos = [ord(simbolo) for simbolo in simbolos_1] #percorre simbolo em simbolos, aplica a função ord() para obter o código ASCII de cada valor. Armazena tudo na nova lista códigos.
print(codigos)
# Saída: [65, 66, 67]

#FILTRAGEM CONDICIONAL
simbolos_2 = ['A', '€', 'B', '~']
ascii_altos = [ord(s) for s in simbolos_2 if ord(s) > 127] #apenas caracteres cujo código ASCII sejam superiores a 127 são incluídas na nova lista.
print(ascii_altos)
# Saída: [8364, 126]  (códigos do '€' e do '~')

"""
    CONTRUÇÃO DE MATRIZES (LISTAS ANINHADAS)
"""
tabuleiro = [['_'] * 3 for i in range(3)] #cria uma linha com 3 elementos '_', Repete esse processo 3 vezes.
print(tabuleiro)
# Saída: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

#Construindo usando operadores de CONCATENAÇÃO(+) e REPLICAÇÃO(*)
nova_lista_concatenacao = simbolos_1 + simbolos_2
print(nova_lista_concatenacao)

nova_lista_replicacao = tabuleiro * 2
print(nova_lista_replicacao)

salas = [['Maria', 'Helena',], ['Roberta',], ['Rafa', 'Mika', 'Bia', (0, 10, 20, 30, 40)]]
print(salas[0][1], salas[0], salas[2][3][2])

"""
    DESEMPACOTAMENTO COM O OPERADOR ESTRELA (*)

    Permite capturar múltiplos elementos de uma sequência (como uma lista ou tupla) de forma flexível, armazenando as sobras ou itens intermediários diretamente em uma lista.

    Não permite mais de um operador * na expressão.    
"""

#CAPTURANDO O RESTANTE NO FINAL
notas = [8.5, 9.0, 7.5, 6.0, 10.0]
primeira, segunda, *restantes = notas
print(primeira)    # Saída: 8.5
print(segunda)     # Saída: 9.0
print(restantes)   # Saída: [7.5, 6.0, 10.0] -> note que restantes é uma lista.

#CAPTURANDO O RESTANTE NO INICIO OU NO MEIO
# no início
*cabecalho, penultimo, ultimo = [1, 2, 3, 4, 5, 6]
print(cabecalho)  # Saída: [1, 2, 3, 4]
print(penultimo)  # Saída: 5
print(ultimo)     # Saída: 6

# Capturando elementos do meio
primeiro, *meio, ultimo = "Python"
print(primeiro)   # Saída: P
print(meio)       # Saída: ['y', 't', 'h', 'o']
print(ultimo)     # Saída: n

#IGNORANDO VALORES COM O SUBLINHADO (_) -> indica variavel descartável
#usar apenas um _, captura um unico elemento.
#usar *_, captura multiplos elementos.
#*_ é a mesma coisa que *__

dados_usuario = ("Ana", 25, "Engenheira", "Brasil", "SP")
nome, idade, *__ = dados_usuario #O sublinhado indica que os outros valores serão capturados apenas pra descartá-los ou indicar que não serão utilizados.
print(nome)   # Saída: Ana
print(idade)  # Saída: 25

"""
    Principais Operações e Métodos
"""
numeros = [6, 14, 15]

numeros.append(40) # Adiciona o elemento ao final da lista [6, 14, 15, 40]
numeros.insert(1, 15) # Insere um novo elemento em uma posição específica [6, 15, 15, 40]
numeros.remove(15) # Procura e remove a primeira ocorrência do valor especificado. Se não existir na lista, retorna ValueError.
del numeros[:1] # Apaga os elementos da posição 0 a posição 1.

print(40 in numeros) # Saída: True

"""
    ITERAÇÃO E SINTAXES AVANÇADAS

    for é a maneira mais simples e direta de percorrer os elementos da lista.

    enumerate() permite iterar pela lista recebendo, simultaneamente, o indice e o valor de cada posição.    
"""

frutas = ['banana', 'maça', 'uva']
for indice, fruta in enumerate(frutas):
    print(f'Posição {indice}: {fruta}')

#COMPREENSÃO DE LISTA
pares = [n for n in range(10) if n%2 == 0] #a lista só recebera valores (n) quando o número for par.
print(pares)