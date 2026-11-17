# Exercício - Adiando execução de funções (salvar valor no escopo da função. Explicação na aula24)
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, y):
    def salva_no_escopo(x):  
        return funcao(x, y)
    return salva_no_escopo

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(15), multiplica_por_dez(4))