# A função len retorna a quantidade de caracteres

string = 'abracadabra'

print(f'A string tem {len(string)} caracteres.')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreve "Seu nome é curto"; se tiver 5 e 6 letras, escreva "Seu nome é normal";
se tiver mais de 6, escreva "Seu nome é muito grande"
'''

nome = input('Digite seu primeiro nome: ')

if len(nome) > 1 and nome.isalpha():
    if len(nome) <= 4 :
        print('Seu nome é curto')
    elif len(nome) <= 6 :
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite um nome válido.')