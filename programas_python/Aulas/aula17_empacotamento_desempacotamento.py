"""
    Empacotamento e Desempacotamento.
"""

nomes = ['Rafa', 'Maria', 'Mika', 10]

dado1, dado2, dado3, dado4 = nomes #cria variáveis e desempacota dados da lista. Nessa sintaxe, a quantidade de variáveis precisa ser igual a de valores a ser desempacotados.

print(dado4)

print(*nomes) #desempacota todos os elmentos no print.

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

