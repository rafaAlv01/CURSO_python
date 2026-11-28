"""
@classmethod + factories(fábricas)

    O decorador @classmethod é uma ferramenta nativa do Python utilizada para definir métodos de classe.

    Diferente dos métodos de instâncias comuns(que recebem a referência ao objeto individual através do parâmetro self), um método decorado com @classmethod recebe a própria classe como seu primeiro argumento obrigatoriamente. Por convenção da comunidade Python, esse primeiro parametro é sempre nomeado de cls.

    COMO FUNCIONA E SINTAXE BASICA
        Quando um método é marcado com @classmethod, a linguagem altera a forma como a função é invocada. Seja a chamada feita através da classe (MinhaClasse.metodo()) ou a partir de uma instância (instancia.metodo()), o interpretador Python passa automaticamente o objeto da classe no parâmetro cls.

            class A:
                @classmethod
                def metodo_da_classe(cls, *args):
                    ...
    
    CASO DE USO
        O uso mais comum e idiomático do @classmethod em bibliotecas e projetos orientados a objetos é a criação de CONSTRUTORES ALTERNATIVOS.

        Enquanto o o método __init__ define a inicialização padrão de uma classe, muitas vezes é necessário instanciar objetos a partir de formatos de dados distintos (como strings formatadas, dicionários, arquivos JSON ou timestamp).
            class Data:
                def __init__(self, ano, mes, dia):
                    self.dia = dia
                    self.mes = mes
                    self.ano = ano
                @classmethod
                def hoje(cls):
                    t = time.localtime()
                    return cls(t.tm_mday, t.tm_mon, t.tm_year)
                @classmethod
                def de_string(cls, string_data):
                    dia, mes, ano = map(int, string_data.split('-'))
                    return cls(dia, mes, ano)

    VANTAGEM
        A razão crucial pela qual se utiliza cls(...) em vez de chamar explicitamente o nome(Data(...)) da classe dentro do método é o suporte correto à herança.
        Quando uma subclasse herda o método de classe e o executa, o parâmetro cls conterá a subclasse que efetuou a chamada, garantindo que a nova instância gerada seja um objeto do tipo correto da subclasse.

    COMPARAÇÃO

        1. MÉTODO DE INSTANCIA:
            - Não tem decorador, 1° argumento é o self, quem acessa/modifica é o estado do objeto individual da classe, é usado em comportamentos normais do objeto.
        2. MÉTODO DE CLASSE:
            - @classmethod, 1° argumento é o cls, quem acessa/modifica é o estado da classe e contrutores, é usado para construir CONTRUTORES ALTERNATIVOS, FÁBRICAS.
        3. MÉTODO ESTÁTICO:
            - @staticmethod, não tem argumento automatico, não recebe referencias automaticas, é usado como funções utilitárias no namespace da classe (ou rotinas de validacao).

    DETALHES DO MODELO DE DADOS
        1. Implementação via Descriptors:
            - O decorador @classmethod é implementado utilizando o protocolo de descritores do Python, armazenando a função original no atributo __func__.
        2. Ordem de Empilhamento de Decoradores:
            - Quando combinado com outros decoradores (como @abstractmethod), o @classmethod DEVE SEMPRE SER O DECORADOR MAIS EXTERNO.
                Ex:
                    from abc import ABC, abstractmethod
                    class ClasseAbstrata(ABC):
                        @classmethod
                        @abstractmethod
                        def metodo_abstrato(cls):
                            pass
"""

class Pessoa:
    ano = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls): #para não ter que passar nada no método, coloca o parametro cls, para receber a propria classe.
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome): #FÁBRICA/CONTRUTOR_ALTERNATIVO.
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade): #NÃO TEM ACESSO À INSTANCIA DESSE MÉTODO, PORQUE É CHAMADO NO MOLDE.
        return cls('desconhecido', idade)
    
p1 = Pessoa('Rafael', 25)
p2 = Pessoa.criar_com_50_anos('Maria')
p3 = Pessoa.criar_sem_nome(70)

print(Pessoa.ano)
Pessoa.metodo_de_classe()
print(vars(p1))
print(vars(p2))
print(vars(p3))