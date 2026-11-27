"""
__dict__ e vars para atributos de instancia

    O __dict__ é um atribute especial em Python que representa o dicionário interno de namespace de um objeto, classe ou módulo. Ele armazena todos os seus atributos graváveis na forma de pares chave-valor, em que a chave é uma string contendo o nome do atributo e o valor é o conteúdo associado.

    1. O __dict__ em Instancias de Objetos
        Quando você cria uma instancia de uma classe e define atributos de instancias (ex: self.nome = 'Rafael'), por padrão o Python grava esses dados dentro do dicionário __dict__ daquele objeto individual.

        A função embutida vars(objeto) retorna exatamente o dicionário __dict__ desse objeto.

        O IDIOMA DE CRIAÇÃO DINAMICA DE ATRIBUTOS (Bunch Idiom)
            Um padrão muito utilizado em Python para instanciar registros rapidamente consiste em popular os atributos do objeto atualizando o seu __dict__ diretamente a partir de um dicionário de argumentos passados no __int__ .
                class Registro:
                    def __init__(self, **kwargs):
                        self.__dict__.update(kwargs)
                
                r = Registro(produto="Teclado", preco=150.0)
                print(r.produto) #saída: Teclado

    2. O __dict__ da Classe vs o __dict__ da Instância
        Tanto classe quanto instancia possuem seus próprios atributos __dict__, mas com responsabilidades distintas:
            -> Classe.__dic__ guarda os métodos da classe, propriedades(@property), variáveis de classe e métodos especiais.
            -> instancia.__dict__ guarda apenas os atributos de instancia especificos daquele objeto.

        Quando você tenta ler um atributo (instancia.atributo), o interpretador busca primeiro no __dict__ da própria instância. Se não encontrar, ele estende a busca para o __dict__ da classe e de suas superclasses na ordem de resolução do MRO.

        ATENÇÃO com @property e Descriptors:
            Propriedades e descriptors de sobrescrita (overriding descriptors) definidos na classe possuem precedência sobre o __dict__ da instância. Mesmo se uma chave com o mesmo nome da propriedade for inserida diretamente no instancia.__dict__, a leitura do atributo continuará executando o getter da propriedade.

    3. Name Mangling e Atributos Privados (__atributo)
        Quando um atributo de intância é nomeado com dois sublinhados no início (ex: self.__x), o Python aplica uma transformação de nome (name mangling) para evitar conflitos de nomes acidentais em subclasses. O atributo é gravado no __dict__ prefixado com _NomeDaClasse .
            Ex:
                class Conta:
                    def __init__(self, saldo):
                        self.__saldo = saldo
                
                c = Conta(100)
                print(c.__dict__) #saída: {'_Conta__saldo' : 100}

    4. Relação entre __dict__ e __slots__ (Otimização de Memória)
        Como cada dicionário Python é uma tabela hash com overhead de memória considerável, instâncias que possuem __dict__ consomem mais memória RAM.

        Quando uma aplicação manipula milhões de instâncias simples, pode-se definir a tupla __slots__ na classe. O uso de __slots__ instrui o Python a substituir o __dict__ individual por uma estrutura de array fixo e compacto em cada instância:
            -> Instancias sem __dict__ reduzem drasticamente o consumo de memória, porém PERDEM A CAPACIDADE DE ACEITAR NOVOS ATRIBUTOS CRIADOS DINAMICAMENTE.
            -> Se for necessário permitir atributos dinâmicos e ao mesmo tempo utilizar __slots__, basta incluir a string '__dict__' dentro da tupla __slots__. 

    5. Acesso ao __dict__ em Descriptors
        Ao criar descriptors (classes que controlam o acesso a atributos implementando métodos como __get__, __set__ ou __delete__), manipular diretamente o dicionário de atributos da intância via instance.__dict__[storage_name] evita loops de recursão infinita que aconteceriam se fossem utilizadas atribuição normais com ponto . .
"""

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #se não tivesse colocado Pessoa.ano_atual, a instancia buscaria o valor de ano_atual primeiro nos atributos da instancia, somente depois nos atributos da classe.


p1 = Pessoa('Rafael', 25)
print(p1.__dict__)
print(vars(p1))

#criando atributo diretamente no dicionario. Evita loops. Dá pra criar, alterar, deletar...
p1.__dict__['estado'] = 'ativo'
print(vars(p1))

p1.__dict__['nome'] = 'Mikael'
print(vars(p1))

dados_mikael = {'nome': 'Rafael', 'idade': 25}
p2 = Pessoa(**dados_mikael)
print()
print(vars(p2))