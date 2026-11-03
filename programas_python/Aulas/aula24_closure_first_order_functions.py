"""
[CLOSURE, FIRST-CLASS FUNCTIONS, HIGH ORDER FUNCTIONS]

    Uma closure é uma função interna que retém e mantém o acesso às variáveis do escopo de uma função externa que a envolveu, mesmo depois que essa função externa já concluiu sua execução e seu escopo local foi destruído.

    Condições de existencia:
        1. aninhamento de funções.
        2. a funcao interna precisa referenciar variaveis do ambiente externo.
        3. a funcao externa precisa retornar a função interna.
    
    Uma variável livre é qualquer variável usada no corpo de uma função que não foi definida no escopo local e não é um parametro.
    O Python armazena essas variáveis no próprio objeto da função retornada através de atributos especiais:
        1. __code__.co_freevars : guarda uma tupla com os nomes das variáveis livres capturadas;
        2. __closure__ : armazena uma tupla de objetos chamados células(cells), onde cada célula possui o atributo cell_contents contendo o valor atual da variável.
            Os elementos podem ser acessados diretamente por fatiamento.
    
    Quando a variável capturada é imutável e o programador tenta modificar seu valor dentro da função interna, o python assume por padrão que se trata de uma nova variável local. Isso causa UnboundLocalError. Para resolver isso, a fim de alterar a variável armazenada no escopo da closure, utiliza-se a instrução nonlocal.

    QUANDO USAR: (IMPORTANTE)
        1. Decoradores de funções (@decorator) :
            O mecanismo de decoradores em python depende fundamentalmente de closures para envolver funções e modificar seu comportamento sem alterar o código original.
        2. Substituir Classes Leves:
            Quando você precisa anexar um estado simples a uma função (como acumuladores, seletores ou callbacks), usar uma closure é muitas vezes mais limpo e rápido do que definir uma classe completa com apenas um método ou o método _call_.
        3. Injeção de configuração/aplicação parcial:
            Permite pré-configurar funções com parâmetros ou dependências pesadas e repassá-las como callbacks limpos para outras partes do sistema.
"""

def criar_saudacao(saudacao):
    def saudar(nome): #O python salva saudacao no escopo dessa função interna.
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(f'Execução da first-class function : {falar_bom_dia('Rafael')}', f'Variável do ambiente externo: {falar_bom_dia.__code__.co_freevars}', f'Conteúdo da variável externa: {falar_bom_dia.__closure__[0].cell_contents}', sep='\n')
print(falar_boa_noite('Maria'))

#MODIFICANDO VARIÁVEIS DA CLOSURE.
def criar_contador():
    contagem = 0 # Variável no escopo externo
    def incrementar():
        nonlocal contagem # Sinaliza que 'contagem' vem da closure
        contagem += 1
        return contagem
    
    return incrementar

meu_contador = criar_contador()
print(meu_contador()) # Saída: 1
print(meu_contador()) # Saída: 2