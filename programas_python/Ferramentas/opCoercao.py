"""
A coercão de tipos em Python é feita automaticamente quando necessário,
permitindo operações entre tipos diferentes.
Por exemplo, ao somar um inteiro e um float, o Python converte o inteiro para float.

A coercão explícita é feita usando o esquema: tipo_de_dado(dado_a_coerção).
"""

# Coerção implícita
num_int = 5
num_float = 3.2
resultado = num_int + num_float # Aqui ocorre uma coerção implicita de int para float.
print('O resultado da soma é', resultado)

# Coerção explícita
num_str = "10"
num_int2 = 5
resultado2 = int(num_str) + num_int2 # Aqui ocorre uma coerção explícita de str para int.
print('O resultado da soma é', resultado2)

# A função input retorna uma string, então é necessário fazer a coerção explícita.
num_input = int(input("Digite um número: "))

# A coercão usando bool
print(bool(0))   # Saída: False
print(bool(1))  # Saída: True
print(bool(""))   # Saída: False
print(bool("Hello"))  # Saída: True # Strings não vazias são True
print(bool([]))   # Saída: False
print(bool([1, 2, 3]))  # Saída: True # Estruturas de dados não vazias são True