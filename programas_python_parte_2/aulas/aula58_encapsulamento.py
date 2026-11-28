"""
ENCAPSULAMENTO (modificadores de acesso: public, protected, private)

    O encapsulamento é um dos pilares da Programação Orientada a Objetos (POO). Ele consiste em agrupar dados e comportamentos dentro de uma classe e ocultar ou restringir os detalhes de funcionamento interno de um objeto em relação ao mundo externo.
    
    Essa abordagem permite criar abstrações claras, proteger a consistência dos dados e isolar a implementação interna de uma classe, garantindo que ela possa ser alterada no futuro sem quebrar o código que a utiliza.

    O ENCAPSULAMENTO EM PYTHON: CONVENÇÕES EM VEZ DE BLOQUEIOS

        Diferentes de linguagens como Java ou C++, que utilizam modificadores rígidos impostos pelo compilador (private, protected), o Python adota a filosofia de "segurança contra acidentes, não contra invasões intencionais". Em vez de proibir o acesso, a linguagem se apoia em convenções e mecanismos de segurança:
            
            1. sintaxe: _atributos  (Atributos Internos/protegidos)
                A convenção padrão da comunidade é prefixar nomes de atributos ou métodos com um único sublinhado. O interpretador não bloqueia o acesso direto a obj._atributo, mas esse prefixo indica claramente a outros desenvolvedores que se trata de uma implementação interna e que acessá-lo de fora é má prática.
                SE DEVE SER ACESSO DENTRO DA CLASSE E DE SUAS SUBCLASSES.

            2. sintaxe: __atributo   (Atributos Privados e Name Mangling)
                Quando um atributo é nomeado com dois sublinhados no início (ex: self.__saldo), o Python aplica uma transformação automática de nome chamada Name Mangling. O atributo é armazenado internamento no dicionário do objeto como _NomeDaClasse__atributo. Esse recurso visa prevenir a sobrescrita acidental de atributos internos por subclasses em estruturas de herança, e não criar uma tranca inviolável.

    ENCAPSULAMENTO PYTHONICO COM PROPRIEDADES (@property)

        A orientação idiomática em Python é começar com atributos públicos simples. Caso surja a necessidade de aplicar validações de dados ou regras de negócio, promove-se o atributo público a uma @property (com getter e setter).

        Essa evolução respeita o Princípio do Acesso Uniforme e preserva a interface do código cliente, garantindo que o estado interno do objeto não seja corrompido com valores inválidos.

    ENCAPSULAMENTO EM NÍVEL DE ARQUITETURA (Agregados)

        Em projetos com arquitetura orientada ao domínio (Domain-Driven Design / DDD), o encapsulamento é estendido além das classes individuais através do conceito de Agregados. Um Agregado agrupa um conjunto de entidades e objetos de valor em torno de uma raiz, que atua como o único ponto de entrada para modificar o grupo e garantir a consistência do conjunto.

    "Como o Python não cria itens private ou protected, ele se torna mais passível a ataques?"

        R:  NÃO. A ausência de modificadores rígidos como private ou protected em Python não torna o código mais vulnerável a ataques em comparação a linguagens como Java. Na verdade, ocorre o oposto em um ponto crucial de segurança: encapsulamento orientado a objetos não é o mesmo que controle de acesso de segurança. Quando você precisa impedir alterações inválidas ou proteger dados sensíveis, a defesa vem de validação explícita (em propriedades, descritores ou modelos de validação), isolamento de processos/serviços, boas práticas de autenticação/autorização e armazenamento seguro de segredos — independentemente da linguagem.
"""
################# EXEMPLO 1 #################
class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido' #isso normalmente é usado para lógica interna da classe.
        self.__exemplo = 'isso é privado'

    def metodo_publico(self):
        return 'metodo publico'

    def metodo_acessar_itens_protegidos(self):
        return f'"{self._metodo_protected()}" e "{self._protected}" acessados DENTRO da classe. ISSO PODE.'

    def _metodo_protected(self):
        return '_metodo_protegido'

    def metodo_acessar_item_privado(self):
        return f'"{self.__exemplo}" pode ser acessado somente dentro da classe.'

f = Foo()
print(f.public)
print(f'"{f._protected}" e "{f._metodo_protected()}" podem ser acessados fora da classe, mas isso NÃO DEVE ACONTECER.')
print(f.metodo_acessar_itens_protegidos())
print(f.metodo_acessar_item_privado())
try:
    print(f.__exemplo)
except AttributeError as e:
    print(f'{e.__class__.__name__} : Não é possível acessar o item privado (__) FORA da classe. O Python dá a sugestão certa de usar, no caso, "_Foo__exemplo".')

################# EXEMPLO 2 #####################
print()
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        # Atributo com name mangling para evitar colisões em subclasses
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    # Propriedade de leitura (Getter público) - impede a operação conta.saldo = valor, pois não define o setter. Gera AttributeError.
    @property
    def saldo(self):
        return self.__saldo

    # Métodos públicos para alterar o estado interno com validação
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False


# Uso da classe:
conta = ContaBancaria("Ana", 100.0)

# Leitura controlada via @property
print(conta.saldo)  # Saída: 100.0

# Tentativa de alteração direta sem setter lança erro:
# conta.saldo = 200.0  # AttributeError: property 'saldo' of 'ContaBancaria' object has no setter

# Alteração de estado realizada pelos métodos com validação
conta.depositar(50.0)
print(conta.saldo)  # Saída: 150.0

conta.sacar(30.0)
print(conta.saldo)  # Saída: 120.0