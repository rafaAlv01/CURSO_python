"""
VARIÁVEIS LIVRES + NONLOCAL

    Uma variável livre é um termo técnico para qualquer variável que seja referenciada no corpo de uma função interna, mas que não foi definida nem atribuída no escopo local dessa função.
    Quando uma função interna acessa uma variável livre definida na função que a envolve, o Python cria uma closure. A closure é uma estrutura que estende o escopo da função interna para reter e "lembrar" dos bindings(ligações) das variáveis livres existentes no momento em que a função foi definida, mesmo depois que a função externa já concluiu sua execução e seu escopo local foi destruído.

    ERRO: UnboundLocalError
        Quando a variável livre é de um tipo imutável, a única maneira de atualizar seu valor é realizando uma REATRIBUIÇÃO (ex: count += count).
        É aí que surge um comportamento fundamental do compilador de bytecode do Python:
            -> Quando o Python analisa e compila o corpo de uma função, qualquer variável que receba uma atribuição em qualquer ponto da função é automaticamente classificada como uma variável local.
            -> Quando o programa roda a instruição count += count dentro da função interna, o interpretador tenta ler o valor de count à direita da atribuição antes de atribuir o novo valor à esquerda. Mas como count foi marcada como local na compilação e ainda não recebeu um valor dentro dessa execução local, o Python lança a exceção UnboundLocalError: local variable referenced before assignment.

    Para resolver a limitação acima, o Python3 introduziu a palavra-chave nonlocal.

    A declaração nonlocal informa explicitamente ao compilador que determinados nomes referenciam variáveis livres pertencentes ao escopo envolvente externo mais próximo (enclosing scope), permitindo que elas sejam reatribuídas diretamente sem que o Python cria uma nova variável local.
    Ao atribuir um novo valor a uma variável declarada como nonlocal, a ligação(binding) armazenada no objeto da closure é atualizada dinamicamente para os chamados futuros.

    global x nonlocal
        global -> aponta para o escopo global do modulo; afeta variáveis no nível raíz do arquivo .py; se a variável global não existir no momento da atribuição, o Python a cria no escopo global.
        nonlocal -> aponta para o escopo envolvente intermediário; não pode referenciar nem alterar variáveis no escopo global; se a variável não existir em nenhum escopo envolvente interno, o Python lança um erro de sintaxe (SyntaxError)
"""

def externa(string):
    string_final = string
    def interna(string_a_concatenar): #essa funcao interna por si só já é uma variável livre dentro dela mesma, pois ela é definida dentro da função externa.
        #print(f'variáveis livres dentro da funcao dentro(): {dentro.__code__.co_freevars}')
        #se tentar "concatenar string_final += string_a_concatenar" será retornado um erro, pois string_final será considerada uma variável local no momento da compilação.
        nonlocal string_final
        string_final += string_a_concatenar
        return string_final # string_final é uma variável livre porque ela está definida fora da função local.
    return interna

#palavra contém a função interna() que retornam o valor de uma variável livre.
palavra = externa('R')
palavra('a')
palavra('f')
palavra('a')
palavra('e')

print(palavra('l'))