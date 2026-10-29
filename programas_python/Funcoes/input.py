#A função input() em Python é usada para obter entrada do usuário. Quando chamada, ela exibe uma mensagem opcional (prompt) e espera que o usuário digite algo no console. O valor digitado é retornado como uma string.
#Se for necessário um tipo diferente, como int ou float, é preciso converter a string usando a função apropriada, como int() ou float(). -> coersão.

nome = input('Digite seu nome: ')
print('Olá,', nome)

idade = int(input('Digite sua idade: '))  # Converte a entrada para inteiro
print('Você tem', idade, 'anos.')

#note que a função input sempre retorna uma string, por isso a necessidade de converter para int no caso da idade.
