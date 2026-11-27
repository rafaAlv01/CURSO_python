# Exercício - Salve sua classe em JSON

# Salve os dados da sua instancia em JSON e depois crie novamente as instâncias da classe com os dados salvos.

# Faça em arquivos separados. (nesse arquivo e em recuperar_class_json.py)
import os
from pathlib import Path
import json

BASE_DIR = Path.cwd()
SAVE_TO = BASE_DIR / "arquivos_apoio" / "salvar_classe.json"

class Usuario:

    def __init__(self, id, servico, estado=False):
        self.id = id
        self.servico = servico
        self.estado = estado

    def ativar_usuario(self, estado):
        if self.estado :
            return f'Esse usuário já está ativo.'
        self.estado = True
        return f'Usuário ativado.'

user1 = Usuario(1, 'administrador')
user2 = Usuario(2, 'funcionario')
user3 = Usuario(3, 'usuario')

banco_dados = [vars(user1), vars(user2), vars(user3)]


#SE TENTAR PASSAR O OBJETO PARA O json.dump, vai dar TypeError, porque uma instancia de uma classe E a propria classe NÃO SÃO serializaveis.
def adiarDump():
    with open(SAVE_TO, 'w', encoding='utf-8') as file:
        json.dump(banco_dados, file, indent=2, ensure_ascii=False)

"""
    Abaixo o código foi escrito pra evitar que a função adiarDump seja executada por outro módulo. A ideia é realizar o dump NESSE arquivo, e, feito nesse arquivo, o outro poderá recuperar os dados DESSE DUMP considerando a primeira execução desse programa.

    Por que fazer isso?
        Se dados forem apagados do Json após a execução DESSE programa, o outro programa retornará um erro, pois ele espera TRES instancias (user1, user2, user3) entre as linhas 9-11.
    Se não fizesse isso:
        Toda vez que o outro programa fosse executado, a função adiarDump() seria executada.

    POR QUE o nome da função é adiarDump ?
        Pra justamente resolver esse problema. O dump só é executado se a função adiarDump for chamada. Enquanto ela não for chamada, os arquivos não serão armazenados no Json.
"""
if __name__ == '__main__':
    print('Execução do adiarDump será feita.')
    adiarDump()
else:
    print(f'O dump desse programa(__name__={__name__}) não foi feito a partir de outro programa.')