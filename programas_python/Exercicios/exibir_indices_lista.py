#forma sem usar enumerate()
lista = ['rafa', 'mika', 'maria']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])

#usando enumerate()
for indice, dado in enumerate(lista):
    print(indice, dado)