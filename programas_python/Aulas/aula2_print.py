"""
print é uma função de saída de dados. Ela imprime
na tela/terminal um conjunto de dados.

Por padrão, ela possui os parametros:
print(*objects, sep=' ', end='\n', file=None, flush=False)

1. objetcts: são os dados que serão impressos.
2. sep: é o separador entre os objetos, por padrão é um espaço.
3. end: é o que será impresso no final, por padrão é uma quebra de linha.
4. file: é onde a saída será direcionada, por padrão é a tela/terminal.
5. flush: se True, força a saída imediata dos dados. ---> Serve para esvaziar a saída de dados em momentos que exigem que a gravação e a exibição seja instantanea. Com o Flush=False, isso é feito de forma automática, o dado fica em um Buffer, e aparece na tela ou é gravado somente em momentos especificos (quando o buffer enche, quando o programa é encerrado, quando encontra uma quebra de linha...)
Isso acontece porque o Python adota uma postura de espera e eficiência. -> melhoras do desempenho e otimização.
Sempre que o Python precisar lidar com memória intermediária (buffer) para otimizar desempenho ao gravar em telas, arquivos ou conexões, o conceito de flush vai aparecer.

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

#Testando Flush Flase e True

import time

for i in range(5, 0, -1):
    print(i, end="...", flush=True)
    time.sleep(1)
print("Fogo!")
