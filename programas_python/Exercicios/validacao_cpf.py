import re #regular expression
import sys

cpf = input('CPF: ')
cpf_enviado = re.sub(r'[^0-9]', '', cpf) #pega qualquer coisa que não for um número([^0-9]) e substitui por ''.

validacao_cpf = cpf == cpf[0] * len(cpf)
if validacao_cpf:
    print('Você enviou dados sequenciais.')
    sys.exit()
 
*cpf_only_num, cpf_dig_1, cpf_dig_2 = cpf_enviado

#daria pra ficar numa funcao
resultado = 0
for indice, num in enumerate(cpf_only_num , -10):
    resultado += int(num)*-indice
resultado = (resultado*10)%11
digito_1 = str(resultado) if resultado <= 9 else 0

cpf_only_num.append(cpf_dig_1)
resultado = 0
for indice, num in enumerate(cpf_only_num, -11):
    resultado += int(num)*-indice
resultado = (resultado*10)%11
digito_2 = str(resultado) if resultado <= 9 else 0


if digito_1 == cpf_dig_1 and digito_2 == cpf_dig_2 :
    print('CPF válido!')
else:
    print('CPF inválido.')