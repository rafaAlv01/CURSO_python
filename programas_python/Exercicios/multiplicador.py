'''
Exercicio:
    -> crie um programa que duplique, triplique e quadruplique um valor.

conhecimentos usados na solução: funcoes, closure, otimização.
'''

def multiplicador_geral(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = multiplicador_geral(2)
triplicar = multiplicador_geral(3)
quadruplicar = multiplicador_geral(4)

print(duplicar(4), triplicar(5), quadruplicar(25))