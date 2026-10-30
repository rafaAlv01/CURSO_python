# id = Identidade
# quando uma variável está na memória, o python precisa saber onde buscar o elemento lá na memória.
# id é a identidade do elemento na memória.

v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

'''
No caso acima, há duas variáveis diferentes com valores iguais.
O python vai buscar ser o mais eficiênte possível. Assim, como os valores literais são iguais, então o python vai apontar para o mesmo valor na memória.
Entretanto, se mudar v2 pra outro valor, o id mudará.
'''

v2 = 'c'

print(id(v1))
print(id(v2))