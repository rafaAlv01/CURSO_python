'''
OPERAÇÃO TERNÁRIA SEGUE O PADRÃO:

<valor final se a condição for true> if <condição> else <valor final se a condição for false>
'''
start_calc = input('Deseja realizar um cálculo? Digite \'sim\' para continuar.')
start_calc = start_calc.lower()

condicao = True if start_calc == 'sim' else False

print(condicao)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)