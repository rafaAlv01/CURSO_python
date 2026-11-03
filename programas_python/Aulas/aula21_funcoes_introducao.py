"""
    INTRODUÇÃO A FUNÇÕES

    Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código.
    Podem receber valores para parametros e retornar um valor especifico.

    Por padrão, funções Python retornam None.
    As variáveis dentro da função são resetadas assim que elas terminam de ser executadas, ou seja, quando elas retornam um valor.

    Os valores colocados (opcionalmente) nos parametros da função são usados para preencher os parametros se na chamada da função não for passado nenhum valor.

    DECLARAÇÃO GERAL:

        def <nome_função>(parametro_1, parametro_2, ...) :
            #corpo da função
    
    Argumentos posicionais: depende da ordem inserida na chamada para executar com sucesso.
    Argumento nomeados: não depende da ordem inserida. É especificado na chamada qual variavel vai receber o valor.
        NOTA: se tivermos
            print(conta_especifica(1, b=2, 5)) --> ERRO
        Se nomear uma varável no meio dos argumentos da chamada de uma função, todos os posteriores a ele devem ser nomeados.

    Valo None para argumentos: o valor None é usado para representar um não valor. Ajuda a refatorar códigos.
        NOTA: def conta_especifica(a, b, c, x=None, y): --> ERRO, todos os posteriores ao nomeado precisa também ser nomeados.

    TERMOS ESPECIFICOS:
        High Order Functions -> funções que podem receber e/ou retornar outras funções.
            ex:
                def somar(a, b):
                    return a + b

                def multiplicar(a, b):
                    return a * b

                def executar(funcao, a, b): # aqui é uma high order function
                    return funcao(a, b)

        First-Class Functions -> funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc)
            ex:
                variavel = executar(somar, 10, 20) #note que aqui a funcao é colocada numa variável.
                print(variavel)

            ex2:
                operacoes = [somar, multiplicar]
                print(operacoes[0](2, 3)) #note que a funcao foi tratada como uma lista.

"""

def imprimir():
    print('Declarando função')
    ...

def conta_especifica(a, b, c, x=None): #USANDO valor None para argumentos.
    result = 0
    if x is not None:
        result = a + b*c*x
        print(f'{a=} {b=} {c=} {x=}')
    else:
        result = a + b*c
        print(f'{a=} {b=} {c=}')
    return result

def saudacao(nome='Desconhecido'): #valor padrão colocado no parametro
    print(f'Olá, {nome}!')

imprimir()
print(conta_especifica(2, 2, 2), conta_especifica(7, 7, 7)) #note que função print só imprime depois que todas as funcoes forem chamadas.
saudacao('Rafael') #passando valor
saudacao() #não passando valor

#Argumentos posicionados
print(conta_especifica(2, 2, 2))

#Argumentos nomeados
print(conta_especifica(b=2,a=1, c=0, x=1000)) #a ordem aqui não importa SE FOR NOMEADO.