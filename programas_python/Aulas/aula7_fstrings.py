# fstrings são uma forma moderna e eficiente de formatar strings em Python, introduzidas na versão 3.6. Elas permitem incorporar expressões dentro de strings, facilitando a criação de mensagens dinâmicas e legíveis.
nome = 'Rafael'
altura = 1.75
peso = 59.5
imc = peso / (altura ** 2)
print(f'{nome} tem {altura} de altura e pesa {peso} kg.')
print(f'IMC: {imc}')

#STRINGS SÃO OBJETOS, OU SEJA, POSSUEM MÉTODOS E ATRIBUTOS
formato = 'abc = {}'.format(123) #observe que a string possui métodos.

# As fstrings são definidas prefixando a string com a letra 'f' ou 'F' e usando chaves {} para incluir expressões que serão avaliadas no momento da execução.
# Elas suportam várias funcionalidades, como formatação de números, alinhamento de texto e chamadas de funções diretamente dentro das chaves.
# Exemplo de formatação de números com fstrings:
pi = 3.141592653589793
print(f'Valor de pi com 2 casas decimais: {pi:.2f}')
print(f'Valor de pi com 4 casas decimais: {pi:.4f}')
#os dois pontos (:) dentro das chaves indicam o início da especificação de formatação,
# e .2f ou .4f indicam que o número deve ser formatado como um float com 2 ou 4 casas decimais, respectivamente.

# Exemplo de alinhamento de texto com fstrings:
print(f'{"Nome":<10} {"Idade":<5} {"Cidade":<15}')
print(f'{nome:<10} {30:<5} {"São Paulo":<15}')

# Exemplo de chamada de função dentro de fstrings:
def saudacao(nome):
    return f'Olá, {nome}!'
print(f'{saudacao(nome)} Bem-vindo ao curso de Python.')
# As fstrings são geralmente mais rápidas e mais fáceis de ler do que os métodos tradicionais de formatação de strings, como o operador % ou o método str.format().
# Elas são amplamente utilizadas em código Python moderno para melhorar a clareza e a eficiência na manipulação de strings.

# Exemplo comparativo com métodos tradicionais:
# Usando o operador %
print('%s tem %.2f de altura e pesa %.2f kg.' % (nome, altura, peso)) #mesmo estilo do C

# Usando o método str.format()
print('{} tem {:.2f} de altura e pesa {:.2f} kg.'.format(nome, altura, peso))