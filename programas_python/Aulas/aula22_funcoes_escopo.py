'''
ESCOPO DE FUNCOES EM PYTHON
    Escopo significa o local onde aquele código pode atingir. Existe escopo global e local.
        global: local onde todo o código é alcançavel
        local: apenas nomes do mesmo local podem ser alcançados.
    No geral, as variáveis de um bloco ficam visiveis a todo o espaço do bloco. Fora deles, elas não existem.

    Definir variáveis globais é uma má prática na programação. Elas são definidas para todo o MÓDULO. O Módulo é basicamente todas as linhas de um arquivo.
    Uma variável global não pode ser alterada dentro de funções implicitamente. As funções podem ler a variável global, mas NÃO PODEM ALTERAR.

    NOTA: SÓ é possível alterar o valor de uma variável global usando a palavra-chave global.
        1. A variável global faz uma variável do escopo externo ser a mesma no escopo interno.
        2. usar global é uma má prática de programação. O mais correto seria passar a variável global por parametro.
'''

y = 10 #normalmente as variáveis globais são definidas antes das declarações das funções.

def escopo_1():
    x=1
    y=12 #esse y é diferente do que está globalmente! outra variável, pois foi delimitada dentro desse escopo.
    print(f'variavel {x=} dentro do escopo_1')
    def dobrar():
        global y
        print(f'variável {y=} global')
        dobrada = x*2
        print(f'variável {dobrada=} dentro do escopo dobrar')
        def global_teste():
            y #se passar o mouse em cima desse print, veremos que ele referencia a variável global.

    def mostrar_y():
        #y *= 2 -> se essa linha não estivesse comentada, o y que seria impresso acima seria o dessa função, e não a imediatamente fora dela. O que geraria erro, pois a operação y = y * 2 não pode ser completada, pois y nessa funcao ainda não existe.
        print(f'variável {y=} do escopo_1')
        #y = 1829371 -> se essa linha não estivesse comentada, o y que seria printado mais acima retornaria um erro, pois ele não seria mais uma variável do escopo_1, e sim dessa função. Como a declaração vem depois do print, então o erro UnboundLocalError é retornado.
    
    #print(dobrada) -> note que aqui a variável dobrada não existe.
    dobrar()
    mostrar_y()
    print(f'variável {y=} do escopo_1')

def escopo_2():
    #print(x) -> se tentar executar o x do escopo_1, ocorrerá um erro, pois o x foi definido no local do escopo_1.
    print(f'variável {y=} global') #aqui é possível, pois y foi definida globalmente.
    ...

#USANDO "global variavel"
def escopo_3():
    global y
    y=12 #esse y aponta para o mesmo espaço de memória da variável global!!!

    def mostrar_y():
        print(f'variável {y=} do escopo_3')
        #y *= 2 #-> se essa linha não estivesse comentada, o y que seria impresso acima seria o dessa função, e não a imediatamente fora dela. O que geraria erro, pois a operação y = y * 2 não pode ser completada, pois y nessa funcao ainda não existe.
        #y = 1829371 -> se essa linha não estivesse comentada, o y que seria printado mais acima retornaria um erro, pois ele não seria mais uma variável , e sim dessa função. Como a declaração vem depois do print, então o erro UnboundLocalError é retornado.
    
    mostrar_y()
    y *= 2
    print(f'variável {y=} do escopo_3 após a operação y *= 2 .')

#Se a var x, do escopo_1, fosse definida nesse ponto, ainda funcionaria, pois x seria uma variável global, e, no momento da chamda da função, a var x já teria sido declarada.
print('Escopo_1_resultado: ')
escopo_1()
print('\nEscopo_2_resultado: ')
escopo_2()
print('\nEscopo_3_resultado: ')
escopo_3()
print('\nVariável_global_final: ')
escopo_2()

#Se a var x, do escopo_1, fosse definida nesse ponto, o programa seria interrompido, pois o x usado na chamada ainda não existe.