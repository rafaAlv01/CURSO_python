"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re #regular expression
import sys

cpf = input('CPF: ')
cpf_enviado = re.sub(r'[^0-9]', '', cpf) #pega qualquer coisa que não for um número([^0-9]) e substitui por ''.

validacao_cpf = cpf == cpf[0] * len(cpf)
if validacao_cpf:
    print('Você enviou dados sequenciais.')
    sys.exit()

*cpf_numeros, cpf_dig_2 = cpf_enviado
 
resultado = 0
for indice, num in enumerate(cpf_numeros, -11):
    resultado += int(num)*-indice

resultado = (resultado*10)%11

digito = resultado if resultado <= 9 else 0

print(f'Segundo digito =', digito)