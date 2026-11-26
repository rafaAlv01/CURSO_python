# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# tarefas = [] -> lista de tarefas
# tarefas = ['fazer café'] -> Adicionar fazer café
# tarefas = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = tarefas ['fazer café']
# refazer = tarefas ['fazer café', 'caminhar']
#se o usuário digitar um comando, vai fazer uma ação. ações: listar, desfazer, refazer.
import os
import subprocess
import json
from pathlib import Path

BASE_DIR = Path.cwd() #retorna para o diretório de trabalho atual.
SAVE_TO = BASE_DIR / "arquivos_apoio" / "desfazer_refazer_save.json"

def funct_listar(lista):
    for item in lista:
        print(item)
    print()

def funct_desfazer(lista):
    try:
        desfazer.append(lista.pop())
        funct_listar(lista)
    except IndexError:
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

def funct_clear():
    comando_limpeza = ["cmd", "/c", "cls"] if os.name == 'nt' else ['clear']
    subprocess.run(comando_limpeza, check=False)

def funct_gravar(tarefas):
    dados = tarefas
    with open(SAVE_TO, 'w', encoding='utf-8') as file:
        dados = json.dump(tarefas, file, indent=2, ensure_ascii=False) #ensure_ascii=False é usado pra visualizar os acentos.

    return dados


def funct_ler():
    dados = []
    if not SAVE_TO.exists():
        print('O arquivo não existe.')
        return dados

    with open(SAVE_TO, 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

tarefas = funct_ler()
desfazer = []

while True :
    print('Opções:\n')
    print('[LISTAR] - [DESFAZER] - [REFAZER] - [SAIR]\n')
    tarefa = input('Digite uma tarefa ou uma opção desejada:').strip().lower()

    if tarefa == 'sair':
        break

    comandos = {
        'listar' : lambda: funct_listar(tarefas),
        'desfazer' : lambda: funct_desfazer(tarefas),
        'refazer' : lambda: funct_refazer(tarefas),
        'clear' : lambda: funct_clear(),
        'adicionar' : lambda: funct_add(tarefas, tarefa),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    funct_gravar(tarefas)