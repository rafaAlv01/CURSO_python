# Operadores Lógicos
# and(e), or(ou), not(não), None(não valor, valor que não existe), in, not in

entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if not senha_digitada:
    print('Voce não digitou nada.')

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(bool(''))
print(0 or False or 0 or bool('abc') or 0.0)
print(not 1) #O not inverte a expressão.

# in e not in
#string são iteraveis
# 0 1 2 3
# r a f a
#-4-3-2-1

print()
print("Operadores in e in not")
print()
nome = 'rafa'

print('fa' in nome)
print('fael' in nome)
print('fa' not in nome)
print(f'f esta em {nome[-2]}')