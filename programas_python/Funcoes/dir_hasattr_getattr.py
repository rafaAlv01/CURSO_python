string = 'Rafael'
metodo = 'upper'

#Esse if permite que o metodo upper seja executado sem medo de ele nao ser um metodo da string.
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

if hasattr(string, 'upper'): #chega dinamicamente se tem esse atributo.
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe upper')
