"""
    Para o código abaixo, foi usada uma tatica que recebe em que o programa recebe um comando, e esse comando é buscando dentro de um dicionário que armazenam funções lambdas que retornam as funções desejadas para cada comando.

    Logo em baixo há vários condicionais que poderiam poluir o código.
"""

import os
import subprocess

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

def funct_add(lista, tarefa):
    lista.append(tarefa)

def funct_clear():
    comando_limpeza = ["cmd", "/c", "cls"] if os.name == 'nt' else ['clear']
    subprocess.run(comando_limpeza, check=False)

todo = []
desfazer = []
tarefa = ''
while tarefa != 'sair' :
    print('Opções:\n')
    print('[LISTAR] - [DESFAZER] - [REFAZER] - [SAIR]\n')
    tarefa = input('Digite uma tarefa ou uma opção desejada:').strip().lower()

    comandos = {
        'listar' : lambda: funct_listar(todo),
        'desfazer' : lambda: funct_desfazer(todo),
        'refazer' : lambda: funct_refazer(todo),
        'clear' : lambda: funct_clear(),
        'adicionar' : lambda: funct_add(todo, tarefa),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

    # if resp == "SAIR":
    #     break
    # elif resp == "LISTAR":
    #     funct_listar(todo)
    # elif resp == "DESFAZER":
    #     funct_desfazer(todo)
    # elif resp == "REFAZER":
    #     funct_refazer(todo)
    # elif resp == "CLEAR":
    #     funct_clear()
    # todo.append(resp)