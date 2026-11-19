"""
Filter é um filtro funcional.

    SINTAXE:
        filter(function, iterator_1, ..., iterator_n)

    RETORNO:
        retorna um iteravel.

    No Python moderno a forma mais comum e recomendade de filtrar dados é usando List Comprehension ou Generator Expressions.
            positivos = list(filter(lambda x: x &gt; 0, numeros))
                                 é igual a
        positivos = [x for x in numeros if x &gt; 0] ou positivos = (x for x in numeros if x &gt; 0), este é um gerador.

    QUANDO VALE A PENA USAR

        Funções de Validação Existentes ou Complexas:
            Quando o critério de filtragem envolve exceções (try/except) ou uma lógica extensa, é melhor isolar o código em uma função def dedicada e passá-la diretamente para o filter().

        Remover valores falsos (Falsy):
            Passar None no primeiro argumento do filter() faz com que a função remova automaticamente todos os elementos equivalentes a False (como None, 0, '' ou listas vazias) de forma concisa.

        Pipelines de Processamento Funcional:
            Em fluxos onde você já está conectando múltiplos geradores e funções da biblioteca padrão (como o módulo itertools).
            Ex:

                def e_linha_de_erro(linha):
                        #Função predicado: retorna True se a linha contiver status 404 ou 500.
                        #Exemplo simples de checagem no texto da linha
                    return 'HTTP/1.1" 404' in linha or 'HTTP/1.1" 500' in linha
                
                def analisar_logs_com_filter(caminho_arquivo):
                    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                            #filter() recebe a função predicado e o objeto do arquivo (que é um iterável)
                            #Nenhuma linha é lida para a memória neste momento!
                        erros_stream = filter(e_linha_de_erro, arquivo)
                            #O laço for solicita uma linha por vez ao iterador
                        for linha in erros_stream:
                            print(f"[ERRO ENCONTRADO]: {linha.strip()}")
                            
"""
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#Usando list comprehension
novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]


print('filtro feito com condicional(if):')
print_iter(novos_produtos)

#USANDO filter
novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)

print('filtro feito com a funcao filter:')
print_iter(novos_produtos)

#usando filter para FILTRAGENS COMPLEXAS
print('usando filter para filtragens complexas:')
def e_inteiro_valido(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

valores = ['1', '2', '-3', '-', '4', 'N/A', '5'] # Passar a função criada diretamente ao filter fica limpo e legível
inteiros = list(filter(e_inteiro_valido, valores))
print(inteiros)
print()

#usando filter para REMOVER VALORES FALSOS
dados = ['Alice', '', None, 'Bob', 0, 'Carla']
limpos = list(filter(None, dados))
print('usando filter para REMOVER valores falsos:')
print(limpos)
print()