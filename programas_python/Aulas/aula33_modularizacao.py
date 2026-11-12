"""
MODULARIZAÇÃO

    BOA PRÁTICA: O ideal é executar o módulo __main__ a partir da pasta principal. Se esse curso fosse um programa, o ideal é que dentro da pasta principal CURSO_python estivesse o programa inicial que chamasse todos os outro. NO MESMO LOCAL DO __main__ que as pastas serão criadas para modularizar.
    Nunca dê aos seus arquivos o mesmo nome de módulos nativos do Python.

    É uma técnica de engenharia de software que consiste em dividir um programa de computador grande ou complexo em partes menores, independentes e bem definidas, chamadas de módulos. Em vez de manter todo o código em um único arquiv extenso, o sistema é fracionado em componentes reutilizáveis e especializados, nos quais cada módulo resolve um problema ou tarefa específica.

    O primeiro módulo executado pelo Python chama-se __main__. [IMPORTANTE]
    O Python conhece a pasta onde o __main__ está e as pastas abaixo dele. Ele não conhece as pastas que estão acima por padrão.
    O Python conhece todos os pacotes e módulos presentes nos caminhos de sys.path

    Módulos(.py):
        -> Qualquer arquivo contendo código Python com a extensão .py (contendo funções, classes ou variáveis) é um módulo.
        -> O módulo é um singleton (isso significa que só pode existir uma única instancia desse módulo. Se já importou, não vai importar ele de novo por questão de eficiência.)
        -> ex: aula33_modularizacao.py

    Pacotes(diretórios com __init__.py):
        -> Um pacote é uma pasta no sistema de arquivos que agrupa múltiplos módulos de forma hierárquica. A presença do arquivo __init__.py (que pode estar vazio) sinaliza ao interpretador Python que aquele diretório deve ser tratado como um pacote. A partir do Python 3.3 não precisa mais do arquivo __init__.py
        -> ex: from Aulas import aula33_modularizacao -> Aulas é um pacote.

    Pacotes de Namespace:
        -> Permitem unificar múltiplos diretórios de código separados sob um mesmo nome de pacote sem a necessidade de conter arquivos __init__.py.
        -> Permite dividir um único pacote em vários diretórios diferentes no disco (ou até em locais diferentes do sistema de arquivos).
        -> É útil em grandes projetos corporativos ou bibliotecas de terceiros (como plugins ou pacotes iniciados com google.* ou azure.*), onde diferentes partes do mesmo pacote vêm de fontes distintas.

    FORMAS DE IMPORTAÇÃO:
        -> import modulo, from modulo import funcao, from modulo import *.

    IMPORTS RELATIVOS vs ABSOLUTOS:
        -> Em pacotes complexos, é possível utilizar a sintaxe de pontos para realizar importações relativas à posição do arquivo atual.
        -> ex: from . import aula32_import_from_as -> para a mesma pasta.
        -> ex2: from ..Exercicios import calculadora -> para pastas superiores.

    VANTAGENS: reutilização de código, isolamento de escopo e manutenção, organização arquitetural e legibilidade, abstração e encapsulamento(permite tratar módulos e funções como "caixas pretas", nas quais se conhecem as entradas e saídas esperadas sem a necessidade de se preocupar com os detalhes internos de implementação.)
"""
#note que o retorno é o __main__. O __main__ é definido A PARTIR da execução.
print('Este módulo se chama', __name__)

import sys, os
import aula32_import_from_as
#AS DUAS LINHAS ABAIXO CONTÉM A SOLUÇÃO DO PROBLEMA APRESENTADO no módulo importlib.py, que está na pasta Ferramentas. Para funcionar, precisa deletar a linha 41, pois só dá pra importar um módulo uma única vez (singleton).
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from Aulas import aula32_import_from_as #Se passar o mouse em cima do modulo importado, teremos a descrição contida no DOCSTRING.

try:
    sys.path.append(r'\programas_python') #append insere um diretorio no sys.path(Lista de locais de busca).
    from ..Exercicios import calculadora
except ModuleNotFoundError:
    ...
except ImportError as error:
    print('Importar a calculadora deu erro porque .. só funciona dentro de pacoters hierarquicos(um dentro do outro).\nComo Aulas e Exercicios estão no mesmo nível, .. falha.')

print('\nAdicionando a pasta pai programas_python no sys.path...')

#O sys.path.append abaixo só foi feito porque o VSCODE abriu a pasta CURSO_python, tornando-a a raiz do projeto. Se abrir como raiz programa_python, as coisas melhoram e não precisa mais modificar o path com o append.
#Não é ideal fazer sys.path.append, pois torna o programa fragil a mudanças de estrutura, aclopamento forte com o ambiente local, poluição do syspath, dificulta ferramentas de terceiros (Linters, Testes e IDEs). O ideal é: executar o programa principal na pasta raiz do projeto; executar scripts como módulos usando a flag -m a partir da raíz; alimentar o modulo __init__.py com importações para usar imports absolutos em outros locais.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #dirname pela o endereço contido em __file__ e remove o nome do arquivo; join junta o endereço modificado com .., para procurar na pasta superior; abspath transforma o caminho "limpo e absoluto", resolvendo os .. para garantir que o Python exergue o caminho limpinho e completo.
#Resultado: c:\Users\...\programas_python
print('Importando calculadora...\n')
from Exercicios import calculadora 

print('\nsys.path :')
print(*sys.path, sep='\n')