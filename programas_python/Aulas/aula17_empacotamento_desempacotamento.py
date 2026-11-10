"""
    Empacotamento e Desempacotamento.

    SUMARIO:
        -> usando lista
        -> usando dicionário
        -> em funções:
            -> args -> argumentos não nomeados.
            -> kargs -> argumentos nomeados.
"""

nomes = ['Rafa', 'Maria', 'Mika', 10]

dado1, dado2, dado3, dado4 = nomes #cria variáveis e desempacota dados da lista. Nessa sintaxe, a quantidade de variáveis precisa ser igual a de valores a ser desempacotados.

print(dado4)

print(*nomes) #desempacota todos os elmentos no print.

#trocando variaveis
a, b = 1, 2
a, b = b, a

#valores excedentes
try:
    dado1, dado2 = nomes
except ValueError:
    print('ValueError: existem menos variáveis do que valores. Não é possível desempacotar todos.')

#variaveis excedentes
try:
    dado1, dado2, dado3, dado4, dado5 = nomes
except ValueError:
    print('ValueError: existem mais variáveis do que valores. Não é possível desempacotar(unpack) nas variáveis excedentes.')

#_* ignora todos os valores à direita.
nome1, *_ = nomes
print(nome1, nomes)

#_ ignora o valor pra uma variavel. variavel descartavel.
_, nome2, *_ = nomes
print(nome2)

# * é usando pra pegar todas os valores posteriores.
nome1, *restante = nomes
print(nome1, restante)

*dados1, ultimo = nomes #nome que o * se adequa à situação. Como são duas variáveis e a ultima é comum, então ele pega do primeiro ao penultimo. O ultimo é guardado na variavel ultimo.
print(dados1, ultimo)

print()

#DICIONÁRIOS

pessoa = {
    'nome' : 'Rafael',
    'sobrenome' : 'Alves de Oliveira',
}

dados_pessoais = {
    'idade' : 25,
    'altura' : 1.75,
}

a, b = pessoa
print(a, b)
a, b = pessoa.values()
print(a, b)

(a1, a2), b = pessoa.items()
print(a1, a2, b)

pessoas_completa = {**pessoa, 'chave':1} #coloca os dados do dicionario pessoa + um dado(key:value) em pessoas_completa
print(pessoas_completa)
pessoas_completa = {**pessoa, **dados_pessoais} #junta dois dicionários usando desempacotamento.
print(pessoas_completa)
print()

#EM FUNÇÕES:

def mostra_arg_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)

    print('Nomeados:')
    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_arg_nomeados(1, 2, nome='Maria', qlq=123)
print()

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostra_arg_nomeados(configuracoes)
print()
mostra_arg_nomeados(**configuracoes)