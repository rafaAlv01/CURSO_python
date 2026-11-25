"""

    CUIDADO AO DEFINIR LISTAS EM PYTHON!

    Quando você não passa argumentos pra lista (ex pra funcao adiciona_clientes_v0, na linha 12), o python não vai executar o parametro da lista de novo.
    
    A função é definida junto com o Python. Assim, todas as vezes que chamar a função adiciona_clientes_v0, sem passar argumentos para o parametro lista, a lista que foi definida na primeira execução da função será usada.

    Qual o problema?
        R: Agora, TODAS as vezes teria que passar uma lista pra função. Imagina que você queira criar duas listas usando a função adiciona_clientes_v0. Depois de criar a primeira lista (linha 19), você deseja criar outra lista (linha 21). Ao adicionar pessoas nessa suposta outra lista, quando você vai printar, vai aparecer tanto os nomes da primeira lista quanto os nomes da segunda! Isso occore porque o Python usa a primeira lista em todas as chamadas da função quando o argumento lista não recebe nenhum valor.

    Como resolver:
        1. Sempre passar uma lista para a função.
        2. Não usar parametros mutáveis nas funções. lista=None.
"""

def adiciona_clientes_v0(nome, lista=[]):
    lista.append(nome)
    return lista

cliente4 = adiciona_clientes_v0('Rafael')
adiciona_clientes_v0('Maria', cliente4)
adiciona_clientes_v0('José', cliente4)

cliente5 = adiciona_clientes_v0('Mikael') #como não foi passado o segundo argumento, a função pegou a lista definida no momento de criação.
adiciona_clientes_v0('Raimunda', cliente5)
print(f'Note que, aqui, o que era pra ser uma lista isolada acabou sendo a mesma lista anterior: {cliente5}')

#PARA RESOLVER:

def adiciona_clientes(nome, lista=None):
    if lista is None: #toda vez que o usuário não passar uma lista, uma nova lista é criada!
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)