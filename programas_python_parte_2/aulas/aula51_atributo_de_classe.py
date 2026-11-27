"""
Atributo de Classe

    É um atributo DA CLASSE. Ele é único para todas as instancias da classe.
    Se alterar o atributo da classe, todos as instancias sofrerão com isso.
"""

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #se não tivesse colocado Pessoa.ano_atual, a instancia buscaria o valor de ano_atual primeiro nos atributos da instancia, somente depois nos atributos da classe.


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())