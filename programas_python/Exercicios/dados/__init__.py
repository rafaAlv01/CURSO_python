"""
    COMO esse produtos pretendem ser utilizados FORA do pacote dados, então deve-se usar o operador referencial . , pois a partir da referencia de fora, ao olhar aqui pra dentro, o que está de fora saberá que deverá ir em dados/produtos_modulo para importar produtos.

    Se fizer apenas
        from produtos_modulo import produtos
    Ocorrerá o erro: 
        ModuleNotFoundError: No module named 'produtos_modulo', pois, olhando de fora, o Python não reconhece o módulo produtos_modulo.

        Isso ocorre porque olhando de fora, é como se dentro de Exercicios houvesse um modulo chamado produtos_modulos, o que não é verdade.
        É como se no módulo chamador estivesse escrito da mesma forma (from produtos_modulo import produtos).
    
    Para resolver isso, deve-se especificar ONDE está esse módulo, usando o operador .
    Aqui, olhando de fora, o Python entra no pacote dados e no modulo produtos_modulo, e importa produtos.
"""

from dados.produtos_modulo import produtos