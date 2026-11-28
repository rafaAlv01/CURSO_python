"""
Properties

    O decorador @property é usado para atributos gerenciados(managed attributes). Ele permite associar métodos de leitura(getter), escrita(setter) e remoção(deleter) a um atributo de uma classe, mantendo a sintaxe simples de acesso por ponto (objeto.atributo).

    @property é uma propriedade do objeto, é um método que se comporta como um atributo! (n chama com parenteses)

    Isso implementa o Princípio do Acesso Uniforme, que estabele que todos os serviços oferecidos por um módulo devem estar disponíveis por meio de uma notação uniforme, sem expor se foram implementados por armazenadores direto em memória ou por computação.

    POR QUE USAR?
        Em linguagens como Java, é comum escrever métodos getter e setter explícitos (como get_peso() e set_peso()) desde o primeiro momento. Em Python, esse estilo é considerado desnecessariamente verboso quando não há lógica adicional a ser executada.

        A recomendação em Python é começar da maneira mais simples possível, expondo os atributos diretamente como públicos (self.peso = 10). Se mais tarde for necessário adicionar validação de dados, cálculo dinâmico ou controle de acesso, o atributo público pode ser promovido a uma @property sem alterar o código cliente que já utiliza objeto.peso.

        p/evitar quebrar código cliente (se quiser mudar o nome de uma variável, por exemplo), p/ habilitar setter, p/ executar ações ao obter um atributo.

        CÓDIGO CLIENTE: É o código que usa seu código.

    OS TRÊS COMPONENTES DE PROPERTIES:
        Uma @property completa pode ter três métodos associados com o mesmo nome:
            1. Getter (@property):
                O método principal define a propriedade e é invocado automaticamente ao ler o valor do atributo (valor = obj.atributo)

            2. Setter (@atributo.setter): # @nome_property.setter
                Método opcional invocado ao atribuir um valor ao atributo (obj.atributo = novo_valor), permitindo aplicar VALIDAÇÕES de tipo e REGRAS DE NEGÓCIO.

            3. Deletar (@atributo.deleter): @nome_property.deleter
                Método opcional invocado ao deletar o atributo (del obj.atributo).

        NOTA:
            Para evitar recursão infinita no setter e no getter, o valor real do dado é armazenado em uma variável interna ("atributo de armazenamento"), convencionamente prefixada com um sublinhado _atributo ou dois sublinhados __atributo.

            Se o getter e o setter tiverem o mesmo nome do atributo público (peso), acessar self.peso dentro de @peso.setter chama o próprio setter de novo, causando RecursionError. Guardar o valor em _peso (ou __peso) separa o nome da propriedade pública do armazenamento interno.
                EX:
                    class Pacote:
                        def __init__(self, peso):
                            self.peso = peso  # Chama o setter na inicialização

                        @property
                        def peso(self):
                            return self.peso #recursao infinita.

                        @peso.setter
                        def peso(self, valor):
                            if valor < 0:
                                raise ValueError("O peso não pode ser negativo.")
                            self._peso = valor

                Detalhes importantes da convenção:
                    _peso (um sublinhado): É a convenção padrão em Python para indicar uso interno/protegido. O valor continua acessível como obj._peso, mas sinaliza a outros desenvolvedores que a interface oficial é obj.peso.

                    __peso (dois sublinhados): Aciona o name mangling (alteração de nome), transformando o atributo internamente em _NomeDaClasse__peso. Isso ajuda a evitar colisões acidentais em subclasses, mas não impede o acesso externo nem substitui recursão se você chamar self.__peso dentro do próprio setter de __peso (em @property, o nome costuma ser peso e o interno _peso ou __peso).

    NOTA SOBRE VALIDAÇÃO:
        Alternativas modernas: Quando você só precisa validar ou normalizar um valor sem lógica complexa, bibliotecas como dataclasses com __post_init__, attrs ou pydantic costumam reduzir bastante o código repetitivo de getters e setters.

    CASOS DE USO
        1. Validação e Consistencia de Dados:
            Garante que o estado interno do objeto permaneça sempre válido. Ao definir atribuições no construtor __init__ apontando para self.atributo = valor, a validação do setter é ativada imediatamente durante a criação da instância.

        2. Atributos Calculados (Dinâmicos):
            Propriedades podem ser usadas para expor valores derivados que não precisam ser armazenados diretamente na memória, mas sim calculados sob demanda no momento da leitura.
            Ex:
                import math
                class Circulo:
                    def __init__(self, raio):
                        self.raio = raio
                    #atributo calculado dinamicamente
                    @property
                    def area(self):
                        return math.pi * (self.raio ** 2)
                c = Circulo(4.0)
                print(c.area)
        
        3. Atributos Somente Leitura (Read-Only)
            Ao definir apenas o método decorado com @property sem criar o correspondente @atributo.setter, o atributo torna-se imutável/somente leitura. Tentar alterar seu valor lançará um erro do tipo AttributeError.

    FUNCIONAMENTO DATA MODEL
        Construtor property():
            O decorador @property é uma forma simplificada e usar a classe embutida property(fget, fset, fdel, doc).

        Descritor de Sobrescrita:
            As propriedades são armazenadas como atributos da classe, mas gerenciam o acesso aos atributos em cada intância. Por ser um descritor de sobrescrita, a leitura de uma propriedade definida na classe sempre tem precedência sobre o dicionário local (__dict__) da instância.
"""
############## PARTE 1 - property - getter #############
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Entrou no property')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 'transparente'

print('[Criando objeto:]')
c = Caneta('Azul')
print('[Objeto criado.]')
print('[Solicitando a cor da caneta e da tampa:]')
print(c.cor)
print(c.cor_tampa)
print('[finalizado a parte 1.]')
#se tentar executar c.cor = 'Rosa', vai retornar um erro, pois cor é um método e não recebe atributo por atribuição.

"""
    Atributos com 1 ou 2 _ (_atributo, __atributo), NÃO devem ser usados. São protegidos ou privados.
"""
print()
########### PARTE 2 - setter - deleter ############## DÁ PRA IMPLEMENTAR O PROPERTY, SETTER, DELETER PARA OS OUTROS ATRIBUTOS DO OBJETO.
class ItemPedido:
    def __init__(self, descricao, peso):
        self.descricao = descricao 
        self.peso = peso #Executa o setter da propriedade na inicialização!
        
    # 1. GETTER: Define 'peso' como uma propriedade
    @property
    def peso(self):
        print('Entrou na property!')
        return self._peso #Atributo de armazenamento interno.
        
    #2. SETTER: Aplica validação ao tentar modificar o valor
    @peso.setter
    def peso(self, valor): # invocado automaticamente ao realizar a operação obj.peso = novo_valor
        print('Entrou no setter!')
        if valor <= 0:
            raise ValueError("O peso deve ser maior que zero")
        self._peso = valor
            
    #3. DELETER: Controla a remoção do atributo
    @peso.deleter
    def peso(self):
        raise AttributeError("Não é permitido deletar o atributo peso") #proibe del obj.atributo

print('[Criando obejeto]')
pedido1 = ItemPedido('comida', 10)
print('[objeto criado.]')

print('[Solicitando o valor de peso]')
print(f'Peso: {pedido1.peso}')
print('[finalizando solicitação.]')

print('[Trocando o peso do objeto]')
pedido1.peso = 15
print(f'Peso: {pedido1.peso}') #aqui entra em property
print('[Peso trocado.]')