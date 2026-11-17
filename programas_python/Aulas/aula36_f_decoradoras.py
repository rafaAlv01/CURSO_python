"""
FUNÇÕES DECORADORAS E DECORADORES

    Decorar = Adicionar / Remover / Restringir / Alterar

    Funções decoradoras são funções que decoram outras funções. (Se quiser decorar uma função, há a necessidade de uso da Closure, portanto, deve-se implementar funções aninhadas, cuja funcao mais externa retorna a mais interna.)
    Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções, usam o elemento @ (açucar sintético)

    Um decorador em Python é um objeto chamável(callable) que aceita outra função (ou classe) como argumento e retorna uma nova função ou objeto chamável modificado. Os decoradores permitem marcar e estender o comportamento de funções ou classes diretamente no código-fonte. Lembra muito o conceito de classe abstrata no que tange "aproveitamento de código".

    Contruir decoradores personalizados exige o conhecimento de closures.

    Como funcionam os Decoradores:
        Açucar sintético -> A sintaxe com o símbolo @ posicionada imediatamente antes da definição de uma função. É um atalho sintético idêntico a realizar uma chamada explicita passando a função como parâmetro e reatribuindo seu nome ao retorno.
            @decorador         ]    [       def alvo():   
            def alvo():        | == |           ...
                ...            ]    [       alvo = decorador(alvo)
    
    PRESERVAÇÃO DE MATADADOS COM @functools.wraps
        Ao substituir uma função por uma função interna(wrapper), a função original perde metadados essenciais como __name__, __doc__, __annotations__ e a assinatura original.
        Para solucionar isso, a biblioteca padrão disponibiliza o decorador @functools.wraps, que deve ser aplicado sobre a função wrapper interna.
        Sem o @functools.wraps, o seu decorador "esconde" a função original, substituindo-a pelo envelope (wrapper), o que pode quebrar ferramentas de inspeção, documentação e depuração.
        Além de copiar os metadados, o @wraps armazena uma referência para a função original no atributo __wrapped__, permitindo inspecionar ou acessar a função sem a camada do decorador.

        Quando usar:
            -> Quando você precisa acessar o nome, o docstring ou as anotações da função (__name__, __doc__, __annotations__)
            -> Em ambientes de Testes Automatizados (como pytest ou unittest):
                Muitos frameworks de teste e bibliotecas de log usam o nome das funções (__name__) para gerar relatórios de erros ou rastreamentos (tracebacks). Se você não usar o @wraps, os erros vão apontar para o envelope em vez da função real que você escreveu, dificultando muito a depuração.
            -> Ao criar Decoradores para Frameworks Web ou APIs:
                Se você estiver escrevendo rotas personalizadas (como em Flask, Django ou FastAPI), o framework frequentemente usa o nome da função ou suas anotações de tipo (__annotations__) para registrar endpoints ou validar dados. O @wraps garante que o framework enxergue a função original por trás da camada do decorador.

        REGRA DE OURO: Sempre que escrever uma função decoradora, coloque o @functools.wraps(func) logo acima da função interna (envelope). Isso garante que o seu código continue transparente para o resto do Python.
    
    CASOS DE USO:
        1. Registro Dinâmico de Funções (Padrão Strategy):
            Permite que o seu sistema descubra e armazene funções ou classes automaticamente, sem que você precise registrá-las manualmente em uma lista ou dicionário central.

            O problema que é resolvido:
                Imagine que você está criando um sistema de pagamento ou um interpretador de comandos onde novas regras ou operações podem ser adicionadas com frequência. A forma tradicional (sem registro dinâmico) exigiria que você criasse um dicionário central e o atualizasse manualmente toda vez que criasse uma nova função. Se você esquecer de chamar o registrar, o sistema simplesmente "esquece" que a nova função existe.

                Com um decorador de registro, a própria função, ao ser decorada, se auto-insere em um dicionário global. O sistema ganha autonomia: você só precisa criar a função e colocar o @ nela.
        
        2. Otimização de Memória(functools.lru_cache):
            Decorador que implementa memorização automática, salvando em cache os resultados de chamadas prévias com os mesmos argumentos para evitar reprocessamentos computacionalmente caros (como no cálculo recursivo da sequencia de Fibonacci).

        3. Funções Genéricas e Polimorfismo (functools.singledispatch):
            Decorador que transforma uma função em uma função genérica, permitindo registrar diferentes implementações especializadas com base no tipo do primeiro argumento da função.
        
        4. Gerenciadores de Contexto Simplificados (contextlib.contextmanager):
            Decorador que permite tranformar uma função geradora contendo uma única instrução yield em um gerenciador de contexto compatível com o bloco with. O código que precedo o yiel roda na entrada (__enter__) e o código posterior executa ao sair (__exit__).
        
        5. Gerenciamento de Atributos e Comparações em Classes
            @property / @<attr>.setter: Transforma métodos em propriedades gerenciadas de leitura/escrita com validação.
            @staticmethod / @classmethod : Definem métodos estáticos (sem o recebimento automático de self) e métodos de classe (que recebem a referência da classe cls).
            @functools.total_ordering : Gera automaticamente todos os métodos de comparação rica (<=, >=, >, !=) a partir da implementação mínima dos métodos __eq__ e __lt__.

    VARIAÇÕES AVANÇADAS DE DECORADORES
        
        1. Decoradores Parametrizados (Fábrica de Decoradores):
            Quando o decorador precisa aceitar parâmetros próprios (Ex: @logged(level=logging.DEBUG)) ou @clock('{name}: {elapsed}s'), cria-se uma fábrica de decoradores: uma função externa que recebe os parâmetros e retorna o decorador real.
            ex:
                def logged(level, message=None):
                    def decorate(func):
                        @wraps(func)
                        def wrapper(*args, **kwargs):
                            print(f'[{level}] {message or func.__name__}')
                            return func(*args, **kwargs)
                        return wrapper
                    return decorate
                
                @logged(level='INFO', message='Iniciando processamento')
                def processar():
                    pass
    
        2. Decoradores Empilhados
            Ao empilhar multiplos decoradores sobre a mesma função, a aplicação ocorre de baixo pra cima.
        
        3. Decoradores Definidos como Classes
            É impossível implmentar decoradores como classes que definem o método __call__. Caso o decorador de classe seja aplicado a métodos de instâncias, a classe também deve implementar o protocolo de descritor com o o método __get__ para garantir a ligação correta do argumento self.
        
        4. Ordem ao Decorar @classmethod, @staticmethod e @abstractmethod
            Como @classmethod e @staticmethod criam objetos descritores que não são diretamente chamáveis, qualquer decorador personalizado deve ser aplicado antes (abaixo na sintaxe) desses decoradores nativos.
            Do mesmo modo, ao definir métodos abstratos em classes base abstratas, o @abstractmethod deve ser sempre o decorador mais interno (mais próximo da instrução def).
        
        5. Decoradores de Classe
            Assim como funções, classes também podem ser decoradas. Um decorador de classe recebe um objeto de classe, pode inspecionar ou alterar seu dicionário de atributos(cls.__dict__) e métodos, e retorna a classe modificada.
"""
from functools import wraps

def create_function(func): #Isso aqui é uma função decoradora, pois ela recebe uma função original como argumento, cria uma nova função interna que adiciona um comportamento extra, e retorna essa nova função.

    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)

        return resultado
    return intern

@create_function
def inverter_string(string):
    print(f'imprimindo o nome da função inverter_string: {inverter_string.__name__}') #Aqui você verá que o nome mudou. __name__ aponta para o nome intern, que é a função interna da create_function.
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('"param" deve ser uma string.')

#inverter_string_checando_parametro = create_function(inverter_string)
invertida = inverter_string('123')
print(invertida)
print()

#@functools.wraps
def meu_decorador(func):
  @wraps(func)  # Copia os metadados de 'func' para o 'envelope'
  def envelope(*args, **kwargs):
    return func(*args, **kwargs)

  return envelope


@meu_decorador
def somar(a: int, b: int) -> int:
  """Soma dois números."""
  return a + b


print(somar.__name__)  # Imprime corretamente: "somar"
print(somar.__doc__)  # Imprime corretamente: "Soma dois números."
print()

#Registro dinamico de funcoes:
ESTRATEGIAS_PAGAMENTO = {} # 1. Dicionário central que vai guardar as estratégias

def registrar_estrategia(nome: str): # 2. O Decorador de Registro
    def decorador(func):
        # Aqui acontece a mágica: a função é salva no dicionário usando o 'nome' como chave
        ESTRATEGIAS_PAGAMENTO[nome] = func
        return func  # Retorna a função intacta
    return decorador

@registrar_estrategia('cartao') # 3. Criando as estratégias usando o decorador
def pagar_com_cartao(valor):
    print(f"Processando R$ {valor} no Cartão de Crédito...")

@registrar_estrategia('pix')  # Só para ilustrar o nome direto
def pagar_com_pix(valor):
    print(f"Processando R$ {valor} via Pix...")

print(ESTRATEGIAS_PAGAMENTO) # Saída: {'cartao': <function pagar_com_cartao...>, 'pix': <function pagar_com_pix...>}

# Executando a estratégia dinamicamente baseada em uma entrada (ex: vinda de um banco de dados ou API)
metodo_escolhido = "pix"
estrategia = ESTRATEGIAS_PAGAMENTO.get(metodo_escolhido)

if estrategia:
    estrategia(150.00)  # Executa: Processando R$ 150.0δοση via Pix...
print()

#FABRICA DE DECORADORES

def fabrica_de_decoradores(a=None, b=None, c=None): #em qualquer lugar do escopo dessa função tenho o acesso a esses parametros que podem ser usados para configurar o decorador.
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)