"""
TIPAGEM: dinâmica e forte, ou seja, não é necessário declarar o tipo de uma variável, pois a váriavel pode
ser alterada durante a execução do programa.
A tipagem é forte, pois não é possível realizar operações entre tipos diferentes, como
somar uma string com um número.

"""

# Na ocasião abaixo, as aspas simples ou duplas são equivalentes.
nome = 'Rafael'
nome2 = "Maria"
print('O nome é', nome)
print("O nome é", nome2)

# Tipos int e float.
num1 = 10
num2 = 3.14
print('O número é', num2)
num2 = 2 # Provando  que a tipagem é dinâmica.
print('O número é', num2)

# Tipos str e bool.
texto = "Olá, mundo!"
verdadeiro = True
print('O texto é', texto)
print('O valor booleano é', verdadeiro)

print(1 == 1) # Saída: True
print(1 == 2) # Saída: False

# Tipo None (representa a ausência de valor).
variavel_nula = None
print('O valor da variável nula é', variavel_nula)

# O boolean pode ser usado de diferentes formas.
print('O valor booleano é', verdadeiro)
print('O valor booleano é', not verdadeiro)
print('O valor booleano é', verdadeiro and False)
print('O valor booleano é', verdadeiro or False)