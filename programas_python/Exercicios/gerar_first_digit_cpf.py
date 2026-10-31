"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

O DIGITO SE REFERE AO PRIMEIRO DIGITO DEPOIS DO HÍFEN.
"""

CPF = '746.824.890-70'
CPF_list = []

#copia cada digito do CPF para uma lista. ignora caracteres especiais.
for num in CPF:
    if num != '.' and num != '-':
        CPF_list.append(int(num))

#separa os 9 primeiros digitos.
*cpf_only_num, cpf_dig_1, cpf_dig_2 = CPF_list

#calculo do resultado de validação.

resultado = 0
'''
[Mexendo diretamente nos iteraveis.] -> não é recomendada, porque tem complexidade desnecessária.

indices = range(10, 1, -1).__iter__()
for num in cpf_only_num :
    resultado += num*next(indices)

'''

'''
USANDO EXPRESSAO_GERADORA, SUM E ZIP. -> é uma solução mais pythonica.

resultado = sum(num * peso for num, peso in zip(cpf_only_num, range(10, 1, -1)))

'''

#usando enumerate -> é otimizado.
for indice, num in enumerate(cpf_only_num, -10):
    resultado += num*-indice

digito = resultado if resultado <= 9 else 0

print(f'Segundo digito =', digito)