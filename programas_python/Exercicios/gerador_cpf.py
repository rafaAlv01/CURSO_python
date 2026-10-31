import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

#daria pra ficar numa funcao
resultado = 0
for indice, num in enumerate(nove_digitos , -10):
    resultado += int(num)*-indice
resultado = (resultado*10)%11
digito_1 = resultado if resultado <= 9 else 0

nove_digitos += str(digito_1)
resultado = 0
for indice, num in enumerate(nove_digitos, -11):
    resultado += int(num)*-indice
resultado = (resultado*10)%11
digito_2 = resultado if resultado <= 9 else 0

cpf_gerado = nove_digitos + str(digito_2)

print('O CPF gerado é ', cpf_gerado)