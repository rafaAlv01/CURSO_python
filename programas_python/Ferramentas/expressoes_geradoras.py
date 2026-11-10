"""
    Expressões geradoras são uma forma concisa de instanciar geradores em Python sem a necessidade de criar uma função explícita com a palavra-chave yield.

    SÃO FUNÇÕES QUE SABEM PAUSAR EM DETERMINADA OCASIÃO.

    É um Iterator, ou seja, retorna um objeto gerador e retorna os valores por demanda.

    Todo Generator é um Iterator, mas nem todo Iterator é um Generator.
    OCUPA MENOS ESPAÇO NA MEMÓRIA, POR SER UM ITERATOR.

    A Sintaxe padrão é
        (expressão for item in iteravel if condicao)

    Quando a expressão geradora é passada como unico argumento para uma função ou construtor, não é necessário duplicar os parênteses.

    Exemplos de utilidades:
        1. calcular o menor valor de uma coleção
        2. verificar se existe algum valor verdadeiro
        3. construções de sequencias Não-Lista(tuple, set, array, etc)
        4. Pipeline de Processamento de Dados (Arquivos e Logs)
"""
import array, sys

#Declaração simples
quadrados = (x ** 2 for x in range(10))
print(f'Sem condicional:', list(quadrados))

#Declaração com condicional
numeros_pares = (n for n in range(100) if n %2 == 0)
print(f'Com condicional:', list(numeros_pares))

#EXPRESSÕES GERADORAS OCUPA MENOS ESPAÇO NA MEMÓRIA
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(f'Omitindo o output da lista para não tomar espaço no terminal.\n{generator=}\nBytes que a lista ocupa na memória: {sys.getsizeof(lista)}\nBytes que o generator ocupa na memória: {sys.getsizeof(generator)}')


#usado com funções
soma = sum(x * x for x in range(10))
tupla_codigos = tuple(ord(char) for char in 'Python')
print(f'{soma=}', f'{tupla_codigos=}', sep='\n')

#usado com funções de mais de um argumento
meu_array = array.array('I', (ord(char) for char in 'Python'))
print(f'{meu_array=}')

#Filtrando linhas limpas de um arquivo
caminho_poema = r"programas_python\arquivos\poema.txt"
linhas_limpas = (linha.strip() for linha in open(caminho_poema, 'r', encoding='utf-8') if linha.strip())
#itera sobre as linhas. Se linha.strip, do condicional, retornar uma string vazia, isso signigica que ele tirou o unico caractere da linha, o \n, indicando ser uma linha limpa. Como uma string vazia no condicional retorna o boleano False, então ele não guardar a string vazia na lista linhas_limpas. Agora, se o if retornar True, isso significa que ainda há caracteres na linhas, mesmo após o strip inicial. Assim, a expressão de armazenamento na lista linhas_limpas é executada.

for linha in linhas_limpas:
    print(linha)
print()

#QUAL O PROBLEMA DO ALGORITMO ABAIXO?
#CAPTURANDO VARIAVEIS COM LAMBDAS --> EXPLICAÇÃO MAIS DETALHADA NA aula27_lambda.py
#As variáveis externas usadas dentro de uma expressão lambda são ligadas em tempo de execução (runtime), e não no momento de sua definição. Isso pode gerar comportamentos inesperados ao criar lambdas dentro de laços de repetição, como observado ao lado.
funcs = [lambda x: x + n for n in range(5)] 
print([f(0) for f in funcs])
funcs = [lambda x, n=n: x + n for n in range(5)]
print([f(0) for f in funcs])
print()

#RESPOSTA: Quando uma lista é criada, ela ocupa todo o espaço na memória, ela força o iterator a ser executado todo de uma vez.
#Para solucionar, para economizar menos memoria (até porque pode haver momentos em que serão trabalhados com MUITOS dados), podemos fazer assim:
funcs = (lambda x: x + n for n in range(5)) #transformou numa expressão geradora.
print([f(0) for f in funcs])
funcs = [lambda x, n=n: x + n for n in range(5)] #OBSERVE QUE O PROBLEMA DO "n" FOI RESOLVIDO, JUSTAMENTE PORQUE O VALOR DE "n" é congelado, por estar no contexto de um iterator.
print([f(0) for f in funcs])