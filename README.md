DEBUGGER

Para Debugar um código, basta usar os BreakPoints.
A breakpoint pausa a execução no exato ponto onde foi inserida e abre um console interativo chamado PDB(Python Debugger).
Nesse console, as variáveis que até ele foram executadas serão exibidas, mostrando seus conteúdos.

DOCUMENTAÇÃO PYTHON:
https://docs.python.org/pt-br/3.16/builtins/stdtypes.html

AMBIENTE VIRTUAL (venv)
É como se fosse uma bolha para cada projeto.
python -m venv nome_ambiente_virtual -> comando básico para criar um ambiente virtual. Vai executar o modulo venv como script.

SOBRE O INTERPRETADOR DO PYTHON

python mod.py (executa o modulo)
python -u (unbuffered -> o codrunning diz para jogar tudo na tela, sem salvar no buffer)
python -m mod (lib mod como script -> executa uma biblioteca do python como script)
python -c 'cmd' (executa um comando no terminal)
python -i mod.py (interativo com mod -> traz toda a saída do módulo e logo em seguida é possível interagir com o código.)