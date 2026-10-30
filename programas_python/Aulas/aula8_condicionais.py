"""
    Quanto mais condições no mesmo if, menos limpo ele é. Evitar muitas condições no mesmo if usando operadores logicos.
    O código precisa ser fácil de ser lido.
"""

entrada = input('você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair': #isso vermelho é um breakpoint. Usado para debugar o código (o programa para aqui).
    print('Você saiu do sistema.')
else:
    print('Comando desconhecido.')