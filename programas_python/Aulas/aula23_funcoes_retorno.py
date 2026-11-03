'''
[RETORNO DE FUNÇÕES]

    Funções retornam valores em suas chamadas. Se o retorno não for especificado usando o 'return', a função retorna, por padrão, None.
    O tipo da variável None é NoneType, indicando um não-valor.
    Se tentar imprimir uma função, o retorno será um objeto do tipo function indicando seu endereço na memória em hexadecimal.

    SOMENTE FUNÇÕES E MÉTODOS tem a palavra-chave return.

    args -> Argumentos não nomeados.
    * - *args (empacotamento e desempacotamento)
        1. *args é uma convenção de escrita utilizada para representar argumentos não nomeados. Lembre-se: A expressão *args pega uma sequencia de argumentos e empacota em args.
        2. Funções empacotam tudos os argumentos em uma tupla. Não é possível alterar os valores de uma tupla, mas é possível transformar essa tupla em lista ter mais liberdade de modificação.


    O que funções podem retornar (o que return aceita) :
        1. Tipos básicos e primitivos (int, float, str, booleanos)
        2. Coleções e Estruturas de dados (lista, tuplas, dicionários, conjuntos)
        3. Multiplos valores : ao separar multiplos valores por virgulas, o python empacota em uma tupla.
        4. Expressões e operações : qualquer operação lógica ou matemática. O python calcula e depois retorna o valor.
        5. Se return estiver sozinho, ele devolverá o valor None.
        6. Outras funções e chamáveis (First-Class Functions):
            - funções são objetos e podem ser armazenas em variáveise e passadas como argumento.
            - Uma função pode retornar a referencia de uma função.
        7. Instâncias de Classes Personalizadas: pode retornar qualquer objeto ou instancia de classe criada pelo programador.

    Padrões comportamentais do return:
        1. Uma função pode ter vários return
        2. expressões ternárias são validas
    
    EM FUNÇÕES GERADORAS, o yield é utilizado em vez de return para produzir uma sequência de valores sob demanda ao longo do tempo.
'''
#desempacotamente em x e y. empacotamento em resto.
x, y, *resto = 1, 2, 3, 4, 5

def soma(x, y):
    result = x + y

def soma_com_return(x, y):
    result = x + y
    return result

def soma_varios_args(*args): #Essa função pode ser substituida pela função sum();
    print(f'Empacotamento em tupla feita pela função: {args}')
    total = 0
    for num in args:
        total += num

    return total

def firs_class_functions(n): #funcao first-class function
    def multiplicar(*args):
        total = 1
        for num in args:
            total *= num

        return total * n
        
    return multiplicar

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):

    return funcao(*args)

resultado = soma(1, 2)
resultado_2 = soma_com_return(1, 2)

print(f'Imprimindo a função soma: {soma}', f'O que a função soma retorna: {resultado}', sep='\n')
print(f'Soma com retorno especificado: {resultado_2}')

resultado_3 = soma_varios_args(2, 2, 2, 2, 2)
print(f'Retorno da função soma_varios_args : {resultado_3}')

tupla = (3, 4, 5, 6, 7)
resultado_4 = soma_varios_args(*tupla)
print(f'Retorno da função soma_varios_args desempacotando uma tupla nos argumentos de chamada : {resultado_4}')

print(f'Retorno usando a função build-in sum : {sum((5, 5, 5, 5, 5))}') #SUM recebe um iteravel.

#EXEMPLOS COM FUNCOES QUE RETORNAM OUTRAS FUNCOES E CHAMAVEIS
"""
    Aqui acontece algo interessante.

    Quando uma função interna usa uma variável do escopo externo(no caso, multiplicacao usa 'n' da firs_class_function(n)), o Python cria uma Closure. Assim, a função interna mantém uma referência ao ambiente léxico necessário para acessar variáveis externas. Assim, o ambiente interno não precisa que o frame externo continue existindo para que ele acesse variáveis externas.

    O ambiente necessário para a closure é preservado enquanto houver referências que precisem dele!

"""
resultado_5 = firs_class_functions(2) #Aqui a função retorna a funcao multiplicacao e é encerrada. Entretanto, as variaveis externas que multiplicacao precisa continuam preservadas na closure.
print(f'Retorno da funcao interna da função first_class_function: {resultado_5}',
      f'Valor que a função interna (multiplicacao) retorna: {resultado_5(*tupla)}', sep='\n') #O resultado é 3520 * 2, pois o 2 passado inicialmente foi preservado na closure da função multiplicacao.

v = executa(saudacao, 'Bom dia', 'Rafael')
print(v)
