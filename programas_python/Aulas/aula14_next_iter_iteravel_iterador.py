"""
Iterável -> str, rangem etc (__iter__)
Iterador -> quem sabe entregar um valor por vez. É o método que tem o iter.
next -> me entregue o próximo valor
iter -> me entre seu iterador
"""

texto = 'Rafael' #texto é o iterável. Em Python,strings são coleções iteráveis.
numeros = range(0, 100, 25)

print(texto.__iter__()) #__iter__() gera o Iterador. O Python intancia uma "máquina de estado" específica para percorrer aquela string.
#esse iter retorna um outro objeto:
#<str_ascii_iterator object at 0x00000226B9E87A00>
#str_ascii_iterator é o iterador responsável de percorrer strings contendo caracteres ASCII.
#object at 0x00000226B9E87A00 -> representa o endereço de memória onde esse objeto iterador recém-criado foi alocado.

print(texto.__repr__()) #esse método devolve de forma mais detalhada do objeto.

for numero in numeros:
    print(numero)

"""
Quando um laço 'for caractere in texto:' é executado, o Python faz exatamente esse processo automaticamente:
1. chama iter(texto) em segredo,
2. executa next() a cada iteração,
3.interrompe a repetição de forma limpa quando o iterador lança a exceção de término `StopIteration`.
"""
#simulação de como funcionaria.
meu_iterador = texto.__iter__() # ou iter(texto)
print(next(meu_iterador)) # Saída: 'R'
print(next(meu_iterador)) # Saída: 'a'
print(next(meu_iterador)) # Saída: 'f'

#OUTRA SIMULAÇÃO: percorre uma lista e multiplica cada elemento por uma sequencia decrescente começando pelo 10.

lista = [7, 2, 3, 4, 9]
resultado = []
indices = range(10, 1, -1).__iter__()
for num in lista :
    resultado.append(num*next(indices))

print(f'Resultado teste com __iter__():', resultado)
