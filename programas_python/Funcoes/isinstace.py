'''
isinstace()

    Utilizado para verificar se determinada coisa é de determinado tipo.

    USO:
        -> checagem antes de efetuar determinada operação.
        -> Usar Try/Except ou isinstance() ?
            R: DEPENDE. O PYTHON PREFERE A FILOSOFIA EAFP de boas praticas de programação (documentado no README), mas pode haver momentos em que a verificação antes de realizar a ação seja necessária (filosofia LBYL). NO GERAL, isinstance é usado para REJEITAR entradas inválidas logo no início.
    
    Quando usar isinstance()?
        -> Quando o comportamento da função precisa mudar radicalmente dependendo do tipo (ex: se for string faz A, se for int faz B).
        -> Em fronteiras de sistemas (ex: validando dados que vieram de uma API externa ou JSON antes de processar).
        -> Para evitar efeitos colaterais perigosos (ex: checar se um arquivo existe antes de tentar abrir e apagar algo).
'''

print('É str!') if isinstance('ola', str) else print('Não é str!')

print('É str ou int!') if isinstance(1, (str, int)) else print('Não é str nem int!') #verifica se é str ou int

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista: #OBSERVE QUE UMA LISTA DE VÁRIOS TIPOS PRECISA DE CHECAGEM PARA EFETUAR DETERMINADAS OPERAÇÕES, SEM QUEBRAR O CÓDIGO.
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2) #essa operação só é possível com numeros.
    else:
        print('OUTRO')
        print(item)