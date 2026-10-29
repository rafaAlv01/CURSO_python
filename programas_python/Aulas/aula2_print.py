"""
print é uma função de saída de dados. Ela imprime
na tela/terminal um conjunto de dados.

Por padrão, ela possui os parametros:
print(*objects, sep=' ', end='\n', file=None, flush=False)

1. objetcts: são os dados que serão impressos.
2. sep: é o separador entre os objetos, por padrão é um espaço.
3. end: é o que será impresso no final, por padrão é uma quebra de linha.
4. file: é onde a saída será direcionada, por padrão é a tela/terminal.
5. flush: se True, força a saída imediata dos dados.

"""

# a virgula é o separador de objetos. Ela adiciona um espaço.
print(12,34)

print(12, 34, sep='-') 
print(12, 34, sep='-', end='!') #note que o end \n foi substituído por !
#print(12, 34, sep='-', end='!', file=open('output.txt', 'w')) 
print(12, 34, sep='-', end='!', flush=True)

"""
Dentro do print, podemos usar operações matemáticas, concatenação de strings, etc.
"""
print(12 + 34)
print("O resultado é:", 10 + 10)
print("Olá, " + "mundo!")