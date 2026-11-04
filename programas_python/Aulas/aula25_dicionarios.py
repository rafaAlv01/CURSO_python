"""
DICIONÁRIO (tipo dict) 

    NOTA: ALGUNS MÉTODOS AQUI LISTADOS SERÃO APRESENTADOS NO MÓDULO metodos_dict.py, na pasta FERRAMENTAS.

    Os dicionários são uma das estruturas de dados mais versáteis e fundamentais da linguagem. Trata-se de uma coleção de mapeamento flexível que armazena pares de chave valor.
    Dicionários são estruturas de dados do tipo par de "chave" e "valor":
        Chaves podem ser consideradas "índices" que vimos na lista e podem ser de tipos imutáveis(str, int, float, bool, tuple, etc).
        Valor pode ser qualquer tipo, incluindo outro dicionário.

    LISTA X DICIONÁRIO
        1. Ao contrário das listas que utilizam indices numéricos inteiros sequenciais, os dicionários utilizam chaves de diversos tipos de dados imutáveis para mapear e localizar valores associados.
        2. Duas listas só são iguais se contiverem os mesmos elementos na mesma ordem. Já nos dicionários, a ordem de inserção dos pares chave-valor não altera o resultado da comparação de igualdade.

    Usamos as chaves {} ou o construtor dict() para criar dicionários.

    NOTA:
        tipos imutáveis: str, int, float, bool, tuple
        tipos mutáveis: dict, lista, etc.
    
    sintaxe:
        dicionario['chave'] => valor (retorna o valor)

    OPERAÇÕES FUNDAMENTAIS E MÉTODOS NATIVOS
        1. Acesso Seguro e Tratamento de Erros (KeyError vc .get): Tentar acessar uma chave que não existe via colchetes gera a exceção KeyError. O método .get(chave, valor) evita o erro retornando um valor alternativo, ZERO, caso a chave não seja encontrada.
        2. Adição e Alternancia de Elementos: A atribuição dict[chave] = valor atualiza o valor se a chave já existir ou cria um novo par chave-valor caso não exista.
        3. Remoção de Itens: A instrução del dict[chave] apaga o par chave-valor especificado. O método .pop(chave) remove o par chave-valor e retorna apenas o valor associado.
        4. Verificação de Pertencimento (in / not in): Os operadores in e not in podem ser usados para verificar se uma chave está contida no dicionário.
        5. Método de Visão (Dictionary Views) :
            .keys() : retorna uma visão contendo todas as chaves.
            .values() : retorna uma visão contendo todos os valores.
            .items() : retorna uma visão contendo tuplas no formato (chave, valor), ideal para laços FOR.

            VISÃO:

                Uma visão em Python é um objeto que oferece uma janela dinâmica e em tempo real para os dados de um dicionário (seja para suas chaves, seus valores ou ambos).
                Diferente de uma simples cópia estática, uma visão está conectada diretamente ao dicionário.

                CARACTERÍSTICAS:
                    1. Dinamismo (atualização em tempo real): Se o dicionário original for modificado, a visão é atualizada automaticamente na mesma hora, sem precisar ser recriada.
                    2. EFICIENCIA DA MEMÓRIA: por ser apenas uma referencia para a estrutura interna do dicionário, ela consome menos memória e opera com alta eficiencia.
                    3. COMPORTAMENTO DE CONJUNTO:
                        As visões .keys() e .items() comportam-se como conjuntos, pois seu conteúdo não pode se repetir. Isso significa que é possível realizar operações matemáticas de conjuntos, como:
                        3.1. INTERSEÇÃO: descobrir chaves que existem em dois dicionários diferentes.
                        3.2. DIFERENÇA: Saber quais chaves estão em um dicionário e não em outro.
    
    RECURSOS AVANÇADOS:
        -> Método .setdefault() : busca o valor de uma chave. Se a chave não existir, insere-a com o valor informado e o retorna em uma unica operação.
        -> Compreensão de Dicionários (Dict Comprehensions): Sintaxe concisa para criar novos dicionários aplicando transformações e filtros sobre iteráveis.
        -> Mapeamentos Especiais do Módulo collections :
            1. defaultdict : gera automaticamente valores padrão ao acessar chaves ausentes usando uma função fábrica (default_factory). Evita o erro KeyError ao tentar acessar uma chave que não existe. Ele inicializa automaticamente a chave com um valor padrão gerado por uma função fábrica(int, list, set, etc)
            2. OrderedDict : Mantém rigorosamente a ordem de inserção das chaves e possui métodos otimizados para reordenação (como mover itens para o início ou para o final). O metodo OrderedDict é ideal se o seu código faz operações frequentes de reordenação.
            3. Counter : dicionários especializado para contar cocorrências de itens. Ele mapeia os elementos como chaves e suas frequências como valores, além de trazer métodos úteis como o most_common().
            4. ChainMap : unifica multiplos dicionários em uma única visão de busca sem criar novos objetos. As buscas são feitas na ordem em que os dicionários foram passados (o primeiro dicionário tem prioridade sobre o segundo). (IMPORTANTE).

    TABELA HASH:
        Por baixo dos panos, os dicionários utilizam uma tabela hash. Uma tabela hash funciona fazendo um cálculo matemático (a função hash) na sua chave para descobrir diretamente em qual posição da memória o valor está guardado. Isso garante uma velocidade fantástica de busca O(1).
        No entanto, se a tabela estiver muito cheia, diferentes chaves podem gerar o mesmo resultado na função hash (uma colisão). Para manter as colisões em um nível aceitável e garantir que a busca continue ultra-rápida, o Python impõe um limite chamado fator de carga (load factor).
    
    TABELA HASH E DICIONÁRIO:
        Ao buscar uma chave, o Python calcula o valor hash(chave) e acessa diretamente a posição (bucket) da memória, garantindo alto desempenho mesmo com milhões de registros. Apenas objetos imutáveis/encapsuláveis (hashable) podem ser usados como chaves.
        Quando um dicionário em atinge cerca de 2/3 de ocupação, ele automaticamente aloca uma nova tabela maior (e mais vazia/esparsa) e copa os elementos para lá. Ou seja, espaços vazios são propositais e obrigatórios para que a tabele hash funcione sem travar em colisoes.
        O uso da tabela hash exige que a estrutura seja mantida de forma esparsa na memória, tornando os dicionários mais custosos (espaços vazios obrigatórios, overhead de matadados(hash, ponteiros), ponteiros extras) em uso de RAM do que sequências simples como listas ou tuplas.
        

    NOTA:
        Uma forma esparsa ocorre quando lidamos com uma estrutura de dados onde a enorme maioria dos elementos possui um valor "vazio"(None), zero ou padrão, e apenas uma fração muito pequena contém dados úteis.
        Em vez de disperdiçar espaços guardando todos os zeros ou None's, a estrutura esparsa armazena apenas os dados que realmente importam (junto com a posição ou índice deles).

        EX: Imagine uma matriz gigante de 1000 x 1000.
            -> Se ela for densa (modo tradicional), o computador reserva 1 milhão de espaços na memória. Se 900 mil forem zeros, o computador gasta memória armazenando-os.
            -> Se ele for ESPARSA, o sistema guarda apenas algo como: "Na posição [12, 45] o valor é 7; na posição [700, 750] o valor é 3" (E IGNORA O RESTO, assumindo que tudo que não está listado ali é ZERO)

    RELAÇÃO DICIONÁRIO X ESPARSIDADE :
        -> Dicionário só aloca memória para as chaves que existem, comportando-se naturalmente de forma esparsa. As chaves não podem ser iguais, portanto, não haverá chaves repetidas.
"""

#Declarando dicionário
pessoa = {
            'nome' : 'Rafael',
            'sobrenome' : 'Alves de Oliveira',
            'idade' : 18,
            'altura' : 1.76,
            'enderecos' : [
                {'rua' : 'tal tal', 'numero' : 123},
                {'rua' : 'teu teu', 'numero' : 321},
            ]
}
dicionario_vazio = dict()

#Manipulação chaves e valores (CRUD completo)

print(pessoa, type(pessoa),'\n',dicionario_vazio, type(dicionario_vazio))
print()
print(f'Exibindo o valor da chave nome: {pessoa['nome']}') #retorna o valor.
print(f'Exibindo exatamente uma chave:key de enderecos: {list(pessoa['enderecos'])[0]}') #retorna o valor.

print()

chave = 'curso' #chave dinamica. Se alterar ela, não vai mudar no dicionario.
pessoa[chave] = 'Ciencia da Computação' #cria uma nova chave com o valor especificado.
print(pessoa[chave])

pessoa['idade'] = 25 #alterando valor correspondente a chave
print(f'Valor alterado para chave idade: {pessoa['idade']}')

apagada = pessoa.pop('curso') #remove e retorna o valor correspondente a chave.
print(f'chave:key apagadas. Valor da chave removida: {apagada}')

print()

#PERTENCIMENTO
print('Existe!') if 'nome' in pessoa else print('Não existe!')
print()

#ALTERANDO O DICIONARIO PARA ALTERAR A VISÃO
visao_chaves = pessoa.keys()
print(visao_chaves)
pessoa['nova_chave'] = 'novo valor'
print(visao_chaves) #note que a visão foi alterada.
print()

#COMO FUNCIONA EM UM FOR
#nessa forma, não é possivel fazer "for chave, valor in pessoa" -> dá erro, pois o for só consegue iterar sobre as chaves quando aplicado diretamente a um dicionário.
for chave in pessoa: 
    print(f'{chave=} -> {pessoa[chave]}')
print()

#Ao tentar acessar uma chave que não tem no dicionário vai dar erro.
try:
    print(pessoa['curso'])
except Exception as e:
    print(f'O erro dado foi porque a seguinte chave não existe no dicionário: {e}')

print('Usando get() : A chave existe!', f'valor retornado: {pessoa.get('curso')}', sep='\n') if pessoa.get('curso') else print('Usando get() : A chave não existe', f'valor retornado: {pessoa.get('curso')}', sep='\n')
print()

#DICT COMPREHENSIONS

codigos = [(86, 'China'), (55, 'Brasil'), (1, 'EUA')]
paises = {pais: code for code, pais in codigos} #note que essa expressao geradora cria o dicionário paises.
print(paises)
print()

#Mapeamentos Especiais do Módulo collections
from collections import defaultdict, OrderedDict, Counter, ChainMap

#defaultdict
agrupado = defaultdict(list) #usando 'list' como fábrica: se a chave não existir, cria uma lista vazia automaticamente
dados = [('fruta', 'maçã'), ('vegetal', 'cenoura'), ('fruta', 'banana')]

for categoria, item in dados:
    agrupado[categoria].append(item) #Note que a expressão agrupado[categoria] é do tipo list, pois representa a fabrica. 'fruta' não existia, mas foi criada como [] na hora. categoria seria o indice e item o valor.
print(agrupado)
print()

#OrderedDict()

d = OrderedDict()
d['primeiro'] = 1
d['segundo'] = 2
d['terceiro'] = 3
print(d)

d.move_to_end('primeiro') #move uma chave especifica para o final
print(d)
print()

#Counter

votos = ['azul', 'vermelho', 'azul', 'verde', 'amarelo', 'azul', 'vermelho', 'amarelo']
resultado = Counter(votos)
print(resultado)
print(resultado.most_common(1)) #descobre o item com mais quantidade
print()

#ChainMap
config_padrao = {'tema': 'claro', 'resolucao': '1080p', 'notificacoes': True}
config_usuario = {'tema': 'escuro'}

configuracoes = ChainMap(config_usuario, config_padrao) #unificando

print(configuracoes['tema']) #Olha que interessante: se o usuário decidir que quer o tema escuro, então vai retornar o tema escuro, pois ele tem prioridade.
print(configuracoes['resolucao'])
print(configuracoes['notificacoes'])