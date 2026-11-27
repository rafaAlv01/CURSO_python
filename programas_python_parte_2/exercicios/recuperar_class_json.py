"""
    feito junto com o exercicio: salvar_class_json.py
"""
from salvar_class_json import SAVE_TO, Usuario, json, adiarDump

with open(SAVE_TO, 'r', encoding='utf-8') as file:
    dados = json.load(file)

    user1 = Usuario(**dados[0])
    user2 = Usuario(**dados[1])
    user3 = Usuario(**dados[2])

    print(user1.__dict__)
    print(user2.__dict__)
    print(user3.__dict__)