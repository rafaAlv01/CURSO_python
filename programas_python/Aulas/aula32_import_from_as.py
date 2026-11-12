"""
MÓDULOS PADRÕES DO PYTHON (import, from, as e *)
reference: https://docs.python.org/3/py-modindex.html

    AS IMPORTAÇÕES DEPENDE DO PONTO DE VISTA DO PYTHON. DEPENDE DE ONDE VOCÊ EXECUTA SEU PROGRAMA. DEPENDE DO PONTO DE VISTA A PARTIR DO __main__
    inteiro: import nome_modulo
        -> Vantagens: você tem o namespace do módulo, protegendo o que você tem no módulo.
        -> Desvantagens: nomes grandes

    partes: from nome_modulo import objeto1, objeto2
        -> Vantagens: nomes pequenos
        -> Desvantagens: sem o namespace do módulo, não tem a proteção do módulo. Tem que tomar cuidado pra não sobrescrever o objeto.
    
    alias 1: import nome_modulo as apelido
    alias 2: from nome_modulo import objeto as apelido
        -> Vantagens: você pode reservar nomes para seu código. Esses nomes são objetos do tipo módulo.
        -> Desvantagens: pode ficar fora do padrão da linguagem
    
    MÁ PRÁTICA : from nome_modulo import *
        -> Vantagens: importa tudo de um módulo
        -> Desvantagens: importa tudo de um módulo

        NOTA: usar o __all__ especifica ao python o que ele deve pegar usando o *. Explicação no modulo  modulo_com__all__.py.

        https://stackoverflow.com/questions/2386714/why-is-import-bad
"""
# import inteiro
import sys #sys é chamado de namespace
import os

#O sys.path.append abaixo só foi feito porque o VSCODE abriu a pasta CURSO_python, tornando-a a raiz do projeto. Se abrir como raiz programa_python, as coisas melhoram e não precisa mais modificar o path com o append.
#Não é ideal fazer sys.path.append, pois torna o programa fragil a mudanças de estrutura, aclopamento forte com o ambiente local, poluição do syspath, dificulta ferramentas de terceiros (Linters, Testes e IDEs). O ideal é: executar o programa principal na pasta raiz do projeto; executar scripts como módulos usando a flag -m a partir da raíz; alimentar o modulo __init__.py com importações para usar imports absolutos em outros locais.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #colocando no syspath o endereço da pasta raiz programas_python, para importar o modulo de outro pacote.

from Ferramentas import modulo_com__all__

platform = 'Rafael' #mesmo nome do objeto do sys. Criar uma mesma variável com o mesmo nome do objeto, quando o import é inteiro, não quebra a referencia.
print(sys.platform) #plataform é um objeto do modulo sys que verifica o nome do sistema.
print(platform)

#import em partes
from sys import exit
exit = 'Alo'
print(type(exit)) #note que não é possível fazer exit(), pois exit passou a ser uma string.

#as
import time as tempo #as aqui cria um apelido para o objeto.

time = 'Tempo' #aqui, mesmo sobrescrevendo time, o apelido "tempo" ainda pode ser usado como módulo. Lembrando que quando é feito "import sys", um objeto do tipo módulo é criado, chamado de sys.
print(type(time), type(tempo)) 

try:
    ...
except ZeroDivisionError as erro:
    #dentro desse bloco, "erro" é uma instancia(um objeto) da classe ZeroDivisionError.
    #as aqui CRIA UM OBJETO.
    ...