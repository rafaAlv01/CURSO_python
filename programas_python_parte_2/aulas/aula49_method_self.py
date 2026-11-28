"""
    Em Programação Orientada a Objetos (POO), um método é uma função definida no corpo de uma classe e associada a essa classe ou aos seus objetos. Enquanto os atributos guardam o estado (dados), os métodos definem os comportamentos e as ações que um objeto pode realizar.

    Em Python, existem diferentes tipos de métodos, cada um cumprindo um papel específico na arquitetura da classe:
        1. Métodos de Instância :
            O seu primeiro parametro é, obrigatoriamente, a palavra self, que representa a propria instancia do objeto sobre a qual o método está atuando.
                1. Quando invoca objeto.metodo(), o interpretador passa a referencia desse objeto automaticamente no parametro self.
                2. permitem ler e modificar livremente o estado interno (atributos) daquele objeto específico.

        2. Métodos especiais (Dunder Methods):
            formato: __init__, __str__, etc

            Foram projetados para serem invocados implicitamente pelo interpretação Python em resposta a operações da sintaxe nativa.

            Ex:
                Exemplos: 
                    Chamar
                        len(meu_objeto)
                    executa o método
                        meu_objeto.__len__()
                    Usar o operador == executa o método 
                        __eq__
                    Criar um objeto ativa o construtor/inicializador
                        __init__

        3. Métodos de Classe:
            Definidos com o decorador @classmethod, eles alteram a forma de chamada para receber a própria classe (cls) como primeiro argumento, em vez de uma instancia.

            Caso de uso mais frequente:
                1. Criação de construtores alternativos para instanciar objetos a partir de formatos de dados diferentes (como strings ou arquivos).

        4. Métodos Estáticos:
            Definidos com o decorador @staticmethod, funcionam como funções comuns agrupadas dentro do namespace da classe.
                1. Não recebem nem self nem cls atuomaticamente.
                2. São uteis par organizar funções utilitárias que pertencem ao contexto da classe, mas que não precisam acessar ou alterar nem o estado da instância nem o da classe.
        
        5. Métodos de propriedade:
            Definidos com o decorador @property, transformam métodos de leitura (getter) e escrita (setter) em acessos sintáticos parecidos com atributos diretos.
                1. Permitem incluir validações de dados e regras de negócio sem quebrar o código do usuário.
"""

class Carro:
    #toda vez que for criar atributos pra instancia, vai usar o __init__.
    def __init__(self, nome):
        self.nome = nome #Em Python, os atributos de instancias são criados dinamicamente durante a execução, sem precisar de um molde pre-definido, como em JAVA.

    def acelerar(self):
        return f'{self.nome} está acelerando...'

fusca = Carro('fusca')
print(fusca.nome)

celta = Carro('celta')
print(celta.nome)

print(fusca.acelerar())