"""
vars(instancia) é usada para retornar um dicionario com todos os atributos da instancia.
"""
class Oi:
    atrib_class = 10
    def __init__(self, saudacao):
        self.saudacao = saudacao

ra = Oi('Bom dia!')
print(vars(ra))