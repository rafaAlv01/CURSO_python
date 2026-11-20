"""
PIP -> PyPI -> pypi.org

    O pip é um instalador de pacotes padrão do Python, utilizado para baixar, instalar, atualizar e gerenciar bibliotecas e módulos de terceiros.
    Ele faz o download seguro dos pacotes diretamente do PyPI(Python Package Index), o repositório público mantido pela Python Software Foundation.

    Comando executado no terminal: pip

    Instalar pacotes:
        pip install nome_do_pacote
    
    Desinstalar pacotes:
        pip uninstall nomu_do_pacote

    Atualizar um pacote para a versão mais recente:
        pip install -U nome_do_pacote 
                    ou
        python -m pip install --upgrade <nome_do_pacote>
        
        (-m pip: executa o pip associado a esse interpretador.)
        (-U: Upgrade)

    Listar os pacotes instalados:
        pip freeze

    Instalar uma lista de dependencias (requeirements.txt):
        pip install -r requirements.txt

    Instalar apenas para o usuário atual(sem acesso de administrador):
        pip intall --user nome_do_pacote

        (grava o pacote no diretório site-packages do usuário local em vez de alterar o diretório do sistema)
    
    Instalar um pacote local em modo editável:
        pip install -e

        (instala o projeto local atual contendo um setup.py em modo de desenvolvimento)

    Ao ativar um ambiente virtual, o pip direciona as instalações automaticamante para a pasta site-packages isolada daquele ambiente, sem afetar o Python Global do S.O.

    SOBRE ambiente virtual
        Verificar qual python esta sendo executado:
            python -c "import sys; print(sys.executable)"
        Verificar onde o pip está instalando os pacotes
            python -m pip --version
        Listar as dependencias:
            python -m pip list
    
    BOA PRATICA:
        Antes de instalar uma dependencia, é interessante verificar ONDE ela será armazenada. Use os comando (python -c "import sys; print(sys.executable)" e python -m pip --version) para verificar.
"""
import pymysql
print('Oi')