"""
PACOTES(PACKAGES)

    Pacote em Python é uma estrutura de diretórios que permite organizar múltiplos módulos relacionados sob um único espaço de nomes (namespace). Enquanto um módulo é um único arquivo contendo código Python (.py), um pacote é uma pasta que agrupa módulos e/ou outros subpacotes, evitando conflitos de nomes de funções/classes e facilitando a manutenção de projetos de médio e grande porte. Ex: pasta Aulas.

    Pacotes Regulares:
        -> São diretórios tradicionais que possuem um arquivo __init__.py. Quando importados, o Python executa o __init__.py e atribui ao atributo __file__ do módulo o caminho desse arquivo.
    
    SOBRE __init__ :
        -> modulo usado para dizer ao python que uma pasta é um pacote.
        -> o que pode ficar dentro desse modulo:
            -> pode ser vazio.
            -> pode importar todos os modulos que estão no mesmo pacote que ele. Por exemplo, dentro do __init__ do pacote Aulas, todas as aulas poderiam ser importadas ali dentro.
            QUAL A FINALIDADE DISSO?
                -> Se um programa que está fora do pacote Aulas tentar usar algum modulo de Aulas, o __ini__ vai "repassar" para o programa os modulos presentes em Aulas.
        DETALHE IMPORTANTE: isso evitaria ter que colocar o caminho do diretório PAI (programas_python) no syspath!
            Se a pasta programas_python (a raiz) estiver aberta no seu VS Code, o interpretador do Python já reconhece essa raiz automaticamente como o diretório de trabalho.
            Portanto, se dentro de Aulas/__init__.py você expuser os módulos, a partir do script testar.py você pode importar direto assim:
                from Aulas import aula33_modularizacao #(sem precisar de sys.path.append!)

    Pacotes de Namespace (PEP 420):
        -> permite criar pacotes sem o arquivo __init__.py
        -> permite fundir diferentes diretórios físicos localizados em locais totalmente distintos do sistema de arquivos (ou dentro do sys.path) sob um único namespace compartilhado.
        -> muito utilizado em grandes bibliotecas e frameworks para permitir que plugins ou extensões de terceiros façam parte da mesma estrutura conceitual de pacotes.
        -> um pacote de namespace não possui o atributo __file__, mas possui um atributo __path__ que armazena a lista somente de leitura de todas as pastas unificadas sob ele.

    IMPORTAÇÕES RELATIVAS:
        Utilizam a sintaxe de pontos (.) para navegar dentro do próprio pacote, evitando codificar o nome do pacote principal (hardcoding) e facilitando refatorações futuras.
            . -> referencia o pacote atual
            .. -> referencia o pacote pai, imediatamente superior.
        Nota: Importações relativas só funcionam dentro de módulos que pertencem a um pacote importado. Para executar um módulo individual de um pacote via terminal mantendo o suporte a imports relativos, deve-se usar a flag -m :
            python3 -m Aulas.pacotes
        O que o . exige:
            O ponto (.) em importações relativas (from . import ...) não depende do sys.path. Ele depende de uma propriedade interna do módulo chamada __package__. Por isso que mesmo se colocar no syspath o caminho do programa atual ainda não daria pra usar importações relativas.
            Quando você executa um arquivo diretamente, o Python define o __package__ dele como None.
            Como o Python não sabe qual é o "pacote pai", ele bloqueia qualquer ponto (.) imediatamente com o erro ImportError.
"""
import sys
import os

#O sys.path.append abaixo só foi feito porque o VSCODE abriu a pasta CURSO_python, tornando-a a raiz do projeto. Se abrir como raiz programa_python, as coisas melhoram e não precisa mais modificar o path com o append.
#Não é ideal fazer sys.path.append, pois torna o programa fragil a mudanças de estrutura, aclopamento forte com o ambiente local, poluição do syspath, dificulta ferramentas de terceiros (Linters, Testes e IDEs). O ideal é: executar o programa principal na pasta raiz do projeto; executar scripts como módulos usando a flag -m a partir da raíz; alimentar o modulo __init__.py com importações para usar imports absolutos em outros locais.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #colocando no syspath o endereço da pasta raiz programas_python, para importar o modulo de outro pacote.
from Ferramentas import modulo_com__all__ #mostrando pra que serve a variavel __all__

#SINTAXE:
import aula32_import_from_as

#o código da linha abaixo dá errado porque o Python vai procurar dentro da pasta Aulas OUTRA pasta Aulas.
#from Aulas import aula32_import_from_as

#aqui dá certo porque o pacote exercicios ta no mesmo diretorio que esse programa.
from exercicios_apoio import importando_sem_poluir_path

#sintaxe importações relativas: AQUI retorna erro, pois só dá pra fazer isso abrindo o terminar dentro da pasta principal programas_python usando a flag -m.
from . import aula32_import_from_as
from ..Exercicios import calculadora