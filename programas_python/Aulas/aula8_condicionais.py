entrada = input('você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair': #isso vermelho é um breakpoint. Usado para debugar o código (o programa para aqui).
    print('Você saiu do sistema.')
else:
    print('Comando desconhecido.')