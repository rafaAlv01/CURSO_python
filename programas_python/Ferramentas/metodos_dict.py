'''
    len, keys, values, items, setsefault, copy, deepcopy get, pop, popitem, update

'''

pessoa = {
            'nome' : 'Rafael',
            'sobrenome' : 'Alves de Oliveira',
            'sobrenome' : 'RA' #Essa key:value não será armazenada, pois a chave sobrenome já existe. Entretanto, esse texto vai sobrescrever o valor da existente
}

# len -> quantas chaves
print(f'Chama o método len : {pessoa.__len__()}')
print(f'Cria um objeto que chama o método len : {len(pessoa)}')
print()

#keys -> retorna um iterável com chaves
print(f'keys() retorna uma visão (iteravel set-like) : {pessoa.keys()}')
print(f'aplicando coerção em keys() : {list(pessoa.keys())}')
print()

#values -> iterável com os valores
print(f'values() retorna uma visão (iteravel set-like) : {pessoa.values()}')
print(f'aplicando coerção em values() : {list(pessoa.keys())}')
print()

#items -> iterável com chaves e valores
print(pessoa.items())
for chave, valor in pessoa.items() :
    print(chave, valor)
print()

#setdefault -> adiciona valor se a chave não existir
print(f'Consultando/inserindo com setdefault: {pessoa.setdefault('cursos', 'Ciencia da Computação')}')
print(f'total de chaves (mostrando que setdefault inseriu): {list(pessoa.keys())}')
print()

#copy -> retorna uma cópia rasa (Shallow copy) -> não copia valores mutáveis.
pessoa_mesmo_dicionario = pessoa
print('O dicionário "pessoa_copia" é uma referencia para o mesmo dicionario "pessoa" (pessoa_mesmo_dicionario = pessoa)')
pessoa['certificados'] = ['cert_1', 'cert_2']
pessoa_copia_rasa = pessoa.copy()
print('pessoa_copia_rasa é uma copia de pessoa. Copia somente os valores imutáveis. Ele não entra em subníveis.')
print(list(pessoa_copia_rasa.keys()))
print(f'Aqui, a lista {pessoa_copia_rasa.get('certificados')} é a mesma que a que contém no dicionário pessoa.')
pessoa_copia_rasa['certificados'][1] = 'modificado'
print(f'Observe que ao mudar um valor da lista de um, o o valor da lista do outro também foi modificado : \n{pessoa.get('certificados')=}    {pessoa_copia_rasa.get('certificados')=}')
pessoa_copia_rasa['certificados'] = ['modificado', 'lallala']
print(f'Após alterar o valor associado a chave: \n{pessoa_copia_rasa.get('certificados')=}      {pessoa.get('certificados')=}')  #note que a lista de pessoa não foi alterada, porque o que mudar foi que tirou a referencia para o objeto lista de 'pessoa' e inseriu outro valor. Perdeu a referencia. Nova variável.
print()

#deepcopy() -> retorna uma cópia completa, incluindo valores mutáveis.
import copy
pessoa_copia_profunda = copy.deepcopy(pessoa)
print(pessoa, pessoa_copia_profunda, sep='\n')
print()

#get -> obtém uma chave
print(f'get() retorna o valor da chave se existir, retorna None se não existir : {pessoa.get('alo alo')}')
print()

#popitem -> Retorna e apaga o ultimo item adicionado
ultima_chave = pessoa.popitem()
print(ultima_chave, list(pessoa.keys()))
print()

#update -> Atualiza um dicionário com outro
pessoa.update({

})
print(pessoa) #não acontece nada pq usou um dicionário vazio

pessoa.update({
    'nome' : 'Rafff',
    'idade' : 25,
})
print(pessoa) #aqui alterou a chave pessoa e inseriu a chave idade

pessoa.update(nome='Rafael', idade=26) #uma outra forma de usar update
print(pessoa)

tupla = ('nome', 'Maria'), ('idade', 58)
pessoa.update(tupla) #outra forma de usar update. Funciona pra lista também. Funciona pra estruturas que se comportam como key:value
print(pessoa)