"""
try(tentar executar o código)/except(ocorreu algum erro ao tentar executar)

"""

numero= '1.1'

if numero.isdigit() : #o método isdigit() retorna True se todos os digitos forem numericos. Se entrar com 1, dá True. Se entrar com 1.1, dá false.
    numero_f = float(numero)
    print(f'O dobro de {numero} é {numero_f * 2:.2f}')
else:
    print('Isso não é um número.')

print()
print('Usando Try/Except')
print()

try: #o try/except funciona pra diversas situações, diversos erros. Por exemplo, se aqui digitarmos 1.1, não passa pelo if mas passa pelo try.
    numero = input('Vou dobrar o número que vc digitar: ')
    print('STR: ', numero)
    numero_f = float(numero) #se digitar uma letra, trava aqui. A execução é interrompida e o compilador pula direto pro except.
    print('FLOAT: ', numero_f)
    print(f'O dobro de {numero} é {numero_f * 2:.2f}')
except: #Esse except pega qualquer erro que surgir entre as linhas 19 e 23. Se o usuário apertar Ctrl + C, o programa não será encerrado, pois o erro KeyboardInterrupt seria capturado.
        #Para evitar isso, é importante especificar o tipo de erro. Ex: except ValueError:
    print('Isso não é um número.')