"""
Classe, Atributo de Instancia

    Em Programação Orientada a Objetos (POO), classe é a estrutura fundamental que define um NOVO TIPO DE DADO, agrupando dados (atributos) e comportamentos (métodos) em uma única unidade.

    Funcionam como um modelo/planta para que, a partir delas, sejam construídos objetos, também chamados de instâncias.

    Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

    Namespace da classe: tudo que ta dentro da classe. atributos de classes, metodos...

    PascalCase -> Método de escrita usada para nomear, por convensão, classes.

    ESTRUTURA E COMPONENTES PRINCIPAIS:
        Declaração:
            classe NomeClasse :
                ...
        
        Inicializador e Construtor:
            -> O método __new__ é o verdadeiro construtor encarregado de criar a instância do objeto na memória.
            -> O método __init__ é o inicializador, chamado automaticamente após a criação do objeto para definir e atribuir os valores iniciais dos seus atributos.

        Parametro self :
            -> Representa a própria instância do objeto sobre a qual o método está operando. Ele deve ser obrigatoriamente o primeiro parametro de qualquer método de instância para permitir o acesso aos seus atributos e outros métodos.

        Atributos:
            -> Variáveis associadas ao objeto(self.atributte) que armazenam seu estado ou característica.

        Métodos:
            -> Funções definidas dentro do bloco da classe que especificam as ações e comportamentos que o objeto pode executar.

    CONCEITOS FUNDAMENTAIS:
        1. Instanciação :
            Processo de invocar a classe para gerar um objeto real na memória. Cada objeto instanciado possui cópias independentes dos seus atributos de instâncias.
        2. Encapsulamento :
            Oculta os detalhes internos de implementação da classe em relação ao código externo. O mundo externo interage apenas com a interface PÚBLICA dos métodos, sem precisar saber como os dados são processados internamente.
        3. Métodos Mágicos (Dunder Methods) :
            Métodos especiais delimitados por duplo sublinhado (como __str__, __len__, __eq__) que permitem integrar instâncias da classe com operações nativas do Python, tais como impressões, comparações e verificação de tamanho.
        4. Herança:
            Permite criar subclasses que herdam atributos e métodos de uma superclasse, reaproveitando código e permitindo especializar comportamentos existentes.
"""

string = 'Rafael' #é uma instancia de str
string_upper = string.upper() #método da classe str
print(isinstance(string, str)) #str é uma classe para strings. 

#DECLARAÇÃO
class Pessoa:

    ...

p1 = Pessoa() #p1 é uma instancia da classe Pessoa. 

"""
    Em: <__main__.Pessoa object at 0x00000216F6EE6A50>

    __main__  ->  indica que a classe Pessoa foi criada no módulo de execução (nesse arquivo).
    .Pessoa  ->  o nome da classe usada para instanciar o objeto (p1 = Pessoa())
    object at 0x00000216F6EE6A50  ->  o endereço de memória, em hex, onde essa instancia específica está armazenada durante a execução do programa.
"""
print(p1) 

p1.nome = 'Rafael'
p1.sobrenome = 'Alves de Oliveira'

"""
    Esses atributos acima são ATRIBUTOS DE INSTANCIA:
        Atributos criados somente na instancia criada (nesse caso, somente em p1).
"""
print(p1.nome, p1.sobrenome)