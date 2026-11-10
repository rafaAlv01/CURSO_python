lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#lista.sort() #Se tentar ordenar a lista acima usando sort, o Python vai retornar TypeError, porque ele não consegue ordenar esse tipo de estrutura.
#print(lista)

def ordena(item): #ordena por nome
    return item['nome']

def ordena_2(item): #ordena por nome
    return item['sobrenome']

#Dentro de sort é possivel passar uma função para ensinar a ele a ordenar.
lista.sort(key=lambda item : item['nome']) #as funções ordena e ordena_2 podem ser substituidas pela função lambda.

for item in lista:
    print(item)
print()

"""
    ABAIXO, TUDO QUE É FEITO NUMA FUNCAO NORMAL PODE SER FEITO NUMA FUNCAO LAMBDA DESDE QUE ELA TENHA UMA LINHA.

    A IDEIA É USAR LAMBDA APENAS PARA CASOS MUITO SIMPLES, COMO ORDENAR ETC. LAMBDA DEIXA O CÓDIGO CONFUSO PARA OUTROS PROGRAMADORES ENTENDER.
"""

def executa(funcao, *args): #aqui recebe varios argumentos
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m, #note que aqui retorna outra função.
    2
)
print(duplica(2))

print( #substitui a função acima SOMA
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)