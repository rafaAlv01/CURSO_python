'''
range é um iterável e tem como expressão geral: range(start, stop, step)
O valor de stop nunca é incluido. Então, se range(10), vai gerar de 0 a 9.
range é uma sequencia imutável.

Não é possível printar a variável iteravel numero esperando receber a sequencia de números esperada. Se printar, o Python exibirá apenas a representação do objeto.
No python3, a função range() não cria uma lista pronta contendotodos os números salvos na memória. Em vez disso, ela retorna um objeto do ripo gerador/sequencia que calcula
    e fornece cada número SOB DEMANDA (conforme solicitado pelo programa).
Isso evita o consumo excessivo de memória RAM ao trabalhar com sequências de milhares ou milhões de números.

Para visualizar os valores internos de um iterável como o range, existem duas abordagens:
1. laço for: o laço for solicita um elemento por vez ao iterável e o imprime.
2. Conversão explicita para list ou tuple: A função list() força a geração de todos os valores do iterável de uma só vez e os armazena em uma lista.

É POSSÍVEL MANIPULAR O range() DIRETAMENTE CRIANDO O OBJETO ATRAVÉS DO CONSTRUTOR __int__() ---> exemplo no final da seção.
'''

#ta dizendo que quer numeros de 0 a 10
numeros = range(10)
print(numeros)

#ta dizendo que quer numeros de 5 a 10
numeros = range(5, 10)
print(numeros)

#pega numeros de 5 a 10 de 2 em 2.
numeros = range(5, 10, 2)
print(numeros)

for numero in range(5):
    print(numero)

numeros = list(range(10))
print(numeros)

#AQUI O RANGE consome do maior para o menor. BASTA USAR PASSOS NEGATIVOS.
numeros = list(range(10, 2, -1))
print(numeros)
"""
Usos para range fora do for ou list:
"""
#Desempacotamento de argumentos * : o asterisco desempacota os valores de range diretamente como argumentos de uma função
print(*range(1, 6)) # Saída: 1 2 3 4 5


#Testes de pertencimento
if 45 in range(0, 100, 5):
    print("O número 45 pertence à sequência!")
#Por que é eficiente? O Python não gera nem percorre todos os números para fazer essa checagem.
#Ele utiliza uma fórmula aritmética em tempo constante O(1), calculando se o valor está dentro dos limites de início/fim e se é múltiplo do passo (step).

#Acesso direto por índice e Fatiamento
r = range(10, 100, 2)
print(r[0]) # Retorna 10 (primeiro elemento)
print(r[-1]) # Retorna 98 (último elemento)
print(r[2:5]) # Retorna outro objeto range: range(14, 20, 2)

#Consulta de tamanho com len()
total = len(range(0, 1000000, 3))
print(total) # Retorna 333334 instantaneamente

#Métodos e funções sequenciais (.index(), min(), max())
r = range(10, 50, 5)
print(r.index(25)) # Retorna 3 (índice do número 25)
print(min(range(5, 20))) # Retorna 5

"""
    MANIPULANDO DIRETAMENTE NO INTERATOR
"""

#Percorre uma lista e multiplica cada elemento por uma sequencia decrescente começando pelo 10.

lista = [7, 2, 3, 4, 9]
resultado = []
indices = range(10, 1, -1).__iter__()
for num in lista :
    resultado.append(num*next(indices))

print(f'Resultado teste com __iter__():', resultado)