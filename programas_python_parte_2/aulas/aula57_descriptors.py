"""
DESCRITORES

    Um descriptor (descritor de atributos) em Python é uma classe que implementa o protocolo de descritores, composto por um ou mais métodos especiais:
        __get__()
        __set__()
        __delete__()

    Em vez de definir métodos getter e setter individuais para cada atributo (como se faz com @property), uma intância de um descritor é declarada como um atributo de classe em outra classe (a classe gerenciada). O descritor passa a interceptar e controlar o acesso, a atribuição e a remoção daquele atributo em todas as instâncias da classe gerenciada.

    TERMINOLOGIA FUNDAMENTAL
        - Descriptor Class: A classe que implementa o protocolo de descritores.
        - Managed Classe: A classe que declara instâncias do descritor como atributos de classe.
        - Descriptor Instance: O objeto individual instanciado a partir da classe gerenciada.
        - Managed Instance: O objeto individual instanciado a partir da classe gerenciada.
        - Storage Attribute (atributo de armazenamento): O atributo na instância gerenciada que guarda o valor real do dado (geralmente no __dict__)
        - Managed Attribute (atributo gerenciado): O atributo público exposto na classe gerenciada que é interceptado e controlado pelo descritor.

    DUAS CATEGORIAS DE DESCRITORES
        A presença ou ausência do método __set__ divide os descritores em duas categorias com comportamentos de busca distintos no interpretador:
        1. DESCRITORES DE SOBREPOSIÇÃO/OVERRIDING DESCRIPTORS (Data Descriptors):
            - Implementam obrigatoriamente o método __set__ (e geralmente __get__).
            - Precedencia sobre o __dict__.
        2. DESCRITORES DE NÃO-SOBREPOSIÇÃO/ NON-OVERRIDING DESCRIPTORS (Non-data Descriptors):
            - Implementam apenas o método __get__.
            - Pode ser sombreado (shadowable, ou descritor sem dados):
                Se um valor for atribuído diretamente na instância gerenciada, um atributo com o mesmo nome será criado no __dict__ da instância, sombreado o descritor nas leituras futuras para aquela instância específica.
        3. FUNÇÕES E MÉTODOS:
            Todas as funções em Python são descritores de não-sobreposição. Ao acessar um método a partir de uma instância (obj.metodo), o __get__ da função é invocado para retornar um bound method (um objeto invocável que vincula a instância ao primeiro parametro self).

    CASOS DE USO
        - Infraestrutura Interna do Python: Recursos como @property, @classmethod, @staticmethod e a ligação de métodos a intâncias são todos implementados sob o capô utlizando descritores.
        - Validação Reutilizável de Atributos: Permitem extrair e reutilizar lógicas de validação complexas (como garantir que um preço seja um número positivo ou que um campo de texto não esteja vazio) em múltiplos atributos de diferentes classes SEM DUPLICAR CÓDIGO.
        - Mapeamento Objeto-Relacional(ORMs): Os campos de tabelas em frameworks como Django ORM e SQLAlchemy são descritores que gerenciam validação, conversão e fluxo de dados entre banco de dados e objeots Python.
        - Cache de Atributos Calculados (Lazy Properties): Um descritor de não-sobreposição pode executar um calculo pesado na primeira leitura (__get__), gravar o resultado direto no __dict__ da instância e fazer com que os acessos seguintes leiam o valor em memóra sem reexecutar o descritor.

"""

#EXEMPLO PRÁTICO: A classe Positivo atua como um descritor de sobreposição para validar que determinados campos numéricos da classe ItemPedido sejam maiores que zero.

# 1. Descriptor Class (Classe Descritora)
class Positivo:
    def __init__(self, storage_name):
        self.storage_name = storage_name  # Nome do atributo de armazenamento interno

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Acesso direto via classe (ItemPedido.quantidade) retorna o próprio descritor
        # Lê do dicionário da instância gerenciada
        return instance.__dict__.get(self.storage_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"O valor para '{self.storage_name}' deve ser maior que zero.")
        # Grava diretamente no __dict__ da instância para evitar recursão infinita
        instance.__dict__[self.storage_name] = value


# 2. Managed Class (Classe Gerenciada)
class ItemPedido:
    # Instâncias do descritor declaradas como atributos de classe
    quantidade = Positivo("quantidade")
    preco = Positivo("preco")

    def __init__(self, quantidade, preco):
        self.quantidade = quantidade  # Aciona o __set__ do descritor
        self.preco = preco  # Aciona o __set__ do descritor

    def total(self):
        return self.quantidade * self.preco


# Testando a validação:
item = ItemPedido(2, 10.0)
print(item.total())  # Saída: 50.0

# Tentativa inválida aciona a validação do descritor:
# item.quantidade = -2  # Lança ValueError: O valor para 'quantidade' deve ser maior que zero.