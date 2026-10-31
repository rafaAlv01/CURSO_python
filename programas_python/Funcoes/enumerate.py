'''
    enumerate -> enumera iteráveis (indices)
    enumerate é um iterator. ISTO É, ele contém um protocolo de iteração e seu consumo é único. Ele produz os elementos por demanda.

    Como ele mantém um estado interno do seu progresso, após ser totalmente percorrido (dentro de um loop, ao ser convertido pra uma lista, ou usando next), ele é 'esgotado'.
        Se tentar percorrer de novo, ele retornará vazio.

    Normalmente não se usa numa variável, se usa direto num for por exemplo.

    Quando o enumerate é usado no for, a variavel de iteração será uma tupla: (indice, valor).

'''

lista = ['oi', 'tudo', 'bem']

lista_enumerada = enumerate(lista) #enumera, coloca indices atrelados aos valores.
#estado 1 = ['oi', 'tudo', 'bem']
print(next(lista_enumerada)) #aqui, um elemento foi produzido por demanda. #estado 2 = ['tudo', 'bem']
for item in lista_enumerada: #aqui, o restante dos elementos foi produzido por demanda.#estado 3 = ['bem']
    print(item)
#estado 4 : lista_enumerada = []

#Aqui, o for não é executado porque lista_enumerada está vazia.
for item in lista_enumerada:
    print(item)

print(end='\n'*3)

lista = ['oi', 'tudo', 'bem']

for item in enumerate(lista):
    print('FOR da tupla:')
    for valor in item:
        print(f'\t{valor}')

'''
    EXERCÍCIO:
        multiplique cada um dos valores por uma contagem regressiva começando de 10. Cria uma lista com os resultados.
        lista = [7, 2, 3, 4, 9]
'''
lista_exerc = [7, 2, 3, 4, 9]
other_list_exerc = []
for indice, num in enumerate(lista_exerc, -10):
    other_list_exerc.append(num*-indice) #7*-(-10) , 2*-(-9), ...

print('Resultado do exercicio:', other_list_exerc)