"""
Flag -> serve para marcar um local
None -> Não valor
is e is not -> é ou não é (tipo, valor, identidade)
"""

condicao = False
passou_no_if = None #essa seria uma Flag.

if condicao :
    passou_no_if = True
    print('Faça algo')
    ...
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if.')
else:
    print('Passou no if: ', passou_no_if, passou_no_if is not None)

inteiro = 5

print(5 is inteiro)