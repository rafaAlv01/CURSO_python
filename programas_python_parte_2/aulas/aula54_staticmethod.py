"""
Métodos Estáticos

    Diferente dos métodos de instancias comuns(=self) e dos métodos de classe(=cls), um método marcado com o decorador @staticmethod não recebe nenhum argumento automático inicial.
    Na prática, um método estático funciona como uma função simples e independente que habita o namespace da classe. Ao ser invocado - seja diretamente via classe ou a partir de uma instancia, ele apenas repassa os argumentos fornecidos pela chamador.

    CASO DE USO
        Indicado para funções utilitárias ou rotinas de validação/computação que possuem forte ligação conceitual com o domínio da classe, mas que não precisam acessar nem modificar os atributos do objeto nem os da classe.

    DISCUSSÃO NA COMUNIDADE
        1. Algumas pessoas consideram o método estático inutil, pois ela não interage com a classe nem com instâncias. Pra elas, defini-la como uma função no módulo costuma ser uma solução mais direta e idiomática.
        2. Por outro lado, outras pessoas destacam que o uso de @staticmethod ajuda a manter o programa coeso e organizado, evitando funções soltas no módulo e garantindo que o utilitário permaneça associado ao contexto da classe a qual pertence.

    SOBRE MODELO DE DADOS
        1. Protocolo de Descritores:
            Ele cria um descritor não-sobrescrito que armazena a função original no atributo __func__ sem aplicar a ligação automática de argumentos ao ser acessado.
        2. Empilhamento em Classes Abstratas:
            O decorador @staticmethod deve obrigatoriamente ser colocado na camada mais externa.
                class InterfaceAbstrata(ABC):
                    @staticmethod
                    @abstractmethod
                    def validar(dados): 
                        pass
"""

class DemoMetodos: 
    def __init__(self, valor): 
        self.valor = valor 
    # 1. Método de Instância
    def metodo_instancia(self):
        return f"Instância acessada: {self.valor}"
    # 2. Método de Classe
    @classmethod
    def metodo_classe(cls, *args):
        return (cls, args)
    # 3. Método Estático
    @staticmethod 
    def metodo_estatico(*args):
        return args
    
# Chamadas via classe
print(DemoMetodos.metodo_classe("a"))