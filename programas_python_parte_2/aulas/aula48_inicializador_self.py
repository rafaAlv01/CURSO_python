"""
    Inicializador e Construtor:
        -> O método __new__ é o verdadeiro construtor encarregado de criar a instância do objeto na memória.
        -> O método __init__ é o inicializador, chamado automaticamente após a criação do objeto para definir e atribuir os valores iniciais dos seus atributos.

    Sobre self:
    
        Nem todo método de uma classe precisa de self, apenas os métodos de instancia comuns. E mesmo neles, self é apenas uma convenção de nome, o que importa mesmo é o primeiro parâmetro posicional.

        Em Pythom, uma função definida dentro de uma class vira um descritor (objeto do tipo function que se comporta como method quando acessado pela instância). Quando você chama p1.falar(), o Python traduz isso por debaixo dos panos para:
            Pessoa.falar(p1)
        É por isso que o primeiro parametro recebe a instancia produto1 automaticamente: SEM ELE, O MÉTODO NÃO SABERIA QUAL OBJETO ESTÁ SENDO MANIPULADO (produto1, produto2, etc) nem teria como acessar self.nome ou self.preco .

        O QUE ACONTECE SE NÃO COLOCAR O PARÂMETRO NA INSTANCIA:

                class Pessoa:
                    def falar():
                        print("Olá")

                p1 = Pessoa()
                p1.falar()

            Vai retornar o "TypeError: Pessoa.falar() takes 0 positional arguments but 1 was given" isso porque o Python, automaticamente, passou p1 como primeiro argumento, mas a função não aceitava nenhum.

        Quando um método NÃO usa self?
            1. Em Métodos de classe (@classmethod): recebem a classe (cls) como primeiro argumento em vez da instância. São muito usados para construtores alternativos (ex.: criar uma Pessoa a partir de uma string JSON ou dicionário).

            2. Métodos estáticos (@staticmethod): não recebem nem self nem cls. Funcionam como funções normais agrupadas dentro do escopo da classe por organização lógica.

        IMPORTANTE: Deixar self visível na assinatura deixa claro quando você está lendo ou alterando um dado da instância (self.saldo) versus uma variável local do método (saldo).
"""

class Produto:
    
    def __init__(self, nome, preco): #todo método precisa ter como primeiro parametro o self. O python faz isso automaticamente.
        self.nome = nome
        self.preco = preco

produto1 = Produto('Hamburguer', 26.75)
print(f'Classe com __init__ e atributos: {produto1.nome}, {produto1.preco}')
