"""
    Salvar tarefas em um json no final de uma execução e depois, em outra execução, listar as tarefas salvas no json.
"""
import os
import subprocess
import json
from pathlib import Path
from functools import wraps

BASE_DIR = Path.cwd() #diretório de trabalho atual
SAVE_TO = BASE_DIR / "arquivos_apoio" / "grava_le_apaga.json"

def lista_vazia(func):

    @wraps(func)
    def wrapper(lista, *args, **kwargs):
        if not lista :
            print('Não há tarefas na lista.\n')
            return
        return func(lista, *args, **kwargs)
    
    return wrapper

@lista_vazia
def funct_listar(lista):
    for item in lista:
        print(item)
    print()

@lista_vazia
def funct_desfazer(lista):
    desfazer.append(lista.pop())
    funct_listar(lista)


def funct_refazer(lista):
    try:
        lista.append(desfazer.pop())
        funct_listar(lista)
    except IndexError:
        funct_listar(lista)


#A função add foi feita desse jeito para impedir que listas vazias, comando do python automaticos, como o cls,
def funct_add(lista, tarefa):
  tarefa_limpa = tarefa.strip() #remove espaços e strings vazias da tarefa
  if not tarefa_limpa:
    return
  if "cls ;" in tarefa_limpa.lower() or "python -u" in tarefa_limpa.lower(): #igonora comandos parecidos com de terminal.
    return
  lista.append(tarefa_limpa)

def funct_clear():
    comando_limpeza = ["cmd", "/c", "cls"] if os.name == 'nt' else ['clear']
    subprocess.run(comando_limpeza, check=False)

@lista_vazia
def funct_gravar(lista):
    if SAVE_TO.exists() and SAVE_TO.stat().st_size > 0:
        with open(SAVE_TO, 'r', encoding='utf-8') as file:
            historico = json.load(file)
    else:
        historico = []

    historico.append(lista)

    with open(SAVE_TO, 'w', encoding='utf-8') as file:
        json.dump(historico, file, indent=2, ensure_ascii=False)

    lista.clear()


def funct_ler():
    if not SAVE_TO.exists() or SAVE_TO.stat().st_size == 0:
        print('Nenhum lista de tarefas foi salva.')
        return

    with open(SAVE_TO, 'r', encoding='utf-8') as file:
        historico = json.load(file)

    for indice, tarefa in enumerate(historico, 1):
        print(f'Lista de tarefas {indice}:\n{tarefa}')

def funct_apagar_json():
    if SAVE_TO.exists():
        SAVE_TO.unlink()

todo = []
desfazer = []

tarefa = ''
while tarefa != 'sair' :
    print('Opções:\n')
    print('[LISTAR] - [DESFAZER] - [REFAZER] - [SAIR] - [GRAVAR NO JSON] - [LER DO JSON] - [APAGAR JSON]\n')
    tarefa = input('Digite uma tarefa ou uma opção desejada:').strip()
    
    comandos = {
        'listar' : lambda: funct_listar(todo),
        'desfazer' : lambda: funct_desfazer(todo),
        'refazer' : lambda: funct_refazer(todo),
        'clear' : lambda: funct_clear(),
        'adicionar' : lambda: funct_add(todo, tarefa),
        'gravar no json' : lambda: funct_gravar(todo),
        'ler do json' : lambda:funct_ler(),
        'apagar json' : lambda:funct_apagar_json(),
    }

    comando = comandos.get(tarefa.lower()) if comandos.get(tarefa.lower()) is not None else comandos['adicionar']
    comando()
    