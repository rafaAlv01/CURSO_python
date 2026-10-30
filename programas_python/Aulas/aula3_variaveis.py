"""
Variáveis em Python são usadas para armazenar dados.
Segundo a PEP 8, o nome das variáveis deve ser descritivo e seguir a convenção snake_case: nome_variavel.

Elas podem conter diferentes tipos de valores, como números, strings, listas, dicionários, etc.
As variáveis são criadas simplesmente atribuindo um valor a um nome, sem necessidade de declaração prévia do tipo.
"""

nome = 'Rafael'  # Atribuição de uma string a uma variável
idade = 30  # Atribuição de um número inteiro a uma variável
altura = 1.75  # Atribuição de um número de ponto flutuante a uma variável
ativo = True  # Atribuição de um valor booleano a uma variável
print('Nome:', nome)  # Exibe o valor da variável nome
print('Idade:', idade)  # Exibe o valor da variável idade
print('Altura:', altura)  # Exibe o valor da variável altura
print('Ativo:', ativo)  # Exibe o valor da variável ativo

"""
Variáveis podem ser usadas em expressões e operações.
Por exemplo, podemos somar duas variáveis numéricas.
"""
soma_idade = idade + 5  # Soma a idade atual com 5
print('Soma da Idade:', soma_idade)  # Exibe o resultado da soma

"""
CONSTANTES = "Variáveis" que não mudam
"""

velocidade = 61 #velocidade do carro
local_carro = 101 #local que o carro está na estrada

RADAR_1 = 60 #velocidade maximo do radar1
LOCAL_1 = 100 #local que o radar_1 está
RADAR_RANGE = 1 #A distancia que o radar pega

#saber se o carro passou no radar e levou multa:

if velocidade > RADAR_1 :
    print('Velocidade atual do carro está maior que o RADAR_1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
     velocidade > RADAR_1:
    print('Carro Multado em RADAR_1')

# MELHORANDO O CÓDIGO:

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1 :
    print('Velocidade atual do carro está maior que o RADAR_1')

if carro_passou_radar_1 :
    print('Carro passou do radar 1')

if carro_multado_radar_1:
    print('Carro Multado em RADAR_1')