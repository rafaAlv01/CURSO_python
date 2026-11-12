"""
    Por padrão, modulos são singleton.
    Mas se, por algum motivo, o programador queira recarregar o módulo, pode-se usar o importlib

    Ao executar o programa abaixo ocorrerá DOIS erro.
        Quando você executou o script de dentro da pasta Ferramentas (ou alterou o sys.path), o diretório de trabalho atual (current working directory) mudou ou o Python perdeu de vista onde está o arquivo aula32_import_from_as.py.
        Como o aula33_modularizacao.py tenta importar o aula32_import_from_as usando um import absoluto simples (import aula32_import_from_as), o Python procura por ele apenas na pasta atual de execução, e não encontrou.
        
        fazer "from Aulas import aula32_import_from_as" resolveria o problema?
            NÃO.
            O arquivo aula33_modularizacao.py não sabe que você importou o aula32_import_from_as no outro arquivo. Cada arquivo em Python tem seu próprio escopo e seu próprio "espaço de nomes" (namespace). Importar um módulo no arquivo A não injeta ele automaticamente dentro do arquivo B.
        
        Como daria para resolver?
            1) Nessa pasta, colocar o caminho completo da pasta programas_python no syspath.
            2) ou no módulo aula33_modularizacao, colocar from Aulas import aula32_import_from_as, porque, assim, diz explicitamente ao Python para procurar no pacote Aulas o módulo ula32_import_from_as.
        
        OUTRO ERRO: AttributeError
            Como o nome do arquivo é importlib.py, quando você faz import importlib, o Python não importou a biblioteca padrão do sistema. Em vez disso, ele importou o seu próprio arquivo, por isso o uso do as não deu certo, pois o objeto já era o arquivo.

            Como daria pra resolver?
                Renomeando esse modulo.
"""

import importlib as lib #aqui foi criado um apelido ao importlib porque o nome do arquivo __main__ é importlib, pode sobrescrever.
import sys, os

#O sys.path.append abaixo só foi feito porque o VSCODE abriu a pasta CURSO_python, tornando-a a raiz do projeto. Se abrir como raiz programa_python, as coisas melhoram e não precisa mais modificar o path com o append.
#Não é ideal fazer sys.path.append, pois torna o programa fragil a mudanças de estrutura, aclopamento forte com o ambiente local, poluição do syspath, dificulta ferramentas de terceiros (Linters, Testes e IDEs). O ideal é: executar o programa principal na pasta raiz do projeto; executar scripts como módulos usando a flag -m a partir da raíz; alimentar o modulo __init__.py com importações para usar imports absolutos em outros locais.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #coloca no syspath o caminho da pasta programas_python

from Aulas import aula33_modularizacao #importação feita, aula33_modularização é singleton.

#Se quiser recarregar o módulo:
lib.reload(aula33_modularizacao)