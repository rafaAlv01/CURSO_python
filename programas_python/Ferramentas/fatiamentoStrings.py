"""
    Fatiamento de strings

    012345678
    Olá mundo
   -987654321

   Fatiamento [i:f:p] [::]
"""

variavel = 'Olá Mundo'
print(variavel[4])
print(variavel[-4])
print()
print(variavel[4:]) #quando só tem i indice inicial, é lido do 4 até o final da string.
print(variavel[-7:7]) #note que o indice f (final) é omitido.
print(variavel[0::2]) #note que quando p é 2, ele grava de dois em dois: mostra um, omite um, mostra um, omite um, ...
print()
print(variavel[-1::-1]) #mostra a string invertida. Parte do -1 e vai até o indice que atecede o -1, que é o 0.
print(variavel[-1:3:-1]) #parte do -1 e vai até o indice 3, de trás pra frente. Quando p=-1, o passo é inverso.
print(variavel[::1])
print(variavel[::-1])