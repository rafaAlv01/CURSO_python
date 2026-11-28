"""
Name Mangling

    O Name Mangling (transformação ou mutilação de nomes) é o mecanismo automático do interpretador Python que renomeia qualquer atributo ou método cujo nome comece com dois sublinhados (__) e termine com no máximo um sublinhado.

    Internamente, o Python reescreve esse nome prefixando-o com um sublinhado e o nome da classe em que foi definido — ou seja, __atributo vira _NomeDaClasse__atributo.

    FINALIDADE:
        Diferente do que muitos iniciantes imaginam, o Name Mangling não foi criado para implementar atributos estritamente privados ou impenetráveis. A sua finalidade principal é evitar colisões acidentais de nomes (accidental name clobbering) em estruturas de herança.

        Imagine o seguinte cenário:
            - A classe base Dog utiliza internamente um atributo self.__mood.
            - Um desenvolvedor cria uma subclasse Beagle (que herda de Dog) e define seu próprio atributo self.__mood sem saber que a classe pai já usava essa variável.

        Se o Python não aplicasse o mangling, o atributo da subclasse sobrescreveria o atributo da classe pai, corrompendo a lógica interna dos métodos herdados.

    REGRAS SINTÁTICAS E EXCEÇÕES IMPORTANTES:
        1. Atributos especiais / dunder methods (__nome__):
            Nomes que começam e terminam com duplo sublinhado (como __init__, __str__ e __len__) não sofrem name mangling. Eles são reservados para o modelo de dados do Python.

        2. Prefixos com sublinhado único (_nome):
            Atributos iniciados por um único sublinhado são apenas uma convenção para indicar uso interno ou protegido, mas não passam por nenhuma alteração de nome pelo interpretador.

        3. Formato obrigatório:
            O mangling só ocorre quando o nome tem pelo menos dois sublinhados no início e no máximo um no final (por exemplo, __x ou __x_).

    SEGURANÇA VS PROTEÇÃO E RECOMENDAÇÕES DE USO:
        - Proteção contra acidentes, não contra invasões:
            Como o Python prioriza transparência, qualquer código externo que conheça o nome transformado pode ler ou alterar o valor usando objeto._NomeDaClasse__atributo.

        - Devemos usar sempre dois sublinhados?
            R: Muitos desenvolvedores experientes (como Ian Bicking) recomendam evitar o uso frequente de dois sublinhados para não tornar o código desnecessariamente obscuro.
"""

#EXEMPLO:

class Pai:
    def __init__(self):
        self.__segredo = "Dados do Pai"


class Filho(Pai):
    def __init__(self):
        super().__init__()
        self.__segredo = "Dados do Filho"  # Não sobrescreve o atributo do Pai


# Instancia Filho e executa ambos os __init__ via super()
f = Filho()

# Ao inspecionar o __dict__, vemos os dois nomes transformados
print(f.__dict__)
# Saída: {'_Pai__segredo': 'Dados do Pai', '_Filho__segredo': 'Dados do Filho'}