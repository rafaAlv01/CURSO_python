'''
    https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

    raise - lançando exceção
    -> força o Python a lançar um erro.
    ->Quando o interpretador executa um raise, a execução normal da função é imediatamente interrompida e o programa transfere o fluxo para a cláusula except correspondente na cadeia de chamadas. Se não houver nenhum bloco `try/except` tratando essa exceção, o programa é encerrado exibindo a mensagem de erro e o traceback.

    Por que o raise é usado?

        1. Sinalizar condições inválidas ou inconsistências: Permite interromper o código assim que uma regra de negócio ou requisito de dados for violado, evitando que o programa continue rodando com dados incorretos ou em estado inválido.
        2. Delegar o tratamento de erros para quem chamou a função: A função que identifica um problema nem sempre sabe como resolvê-lo; utilizar o raise permite que a função chamadora capture o erro com try/except e decida a melhor forma de tratá-lo.
        3. Tratar erros recuperáveis e de usuários: Ao contrário das checagens com assert (que servem apenas para testes de sanidade do desenvolvedor durante o desenvolvimento), o raise é o recurso indicado para erros dos quais o sistema pode se recuperar, como entradas de usuários inválidas ou falhas de arquivos.
        4. Relançar e encadear exceções:
            ->Relançar a mesma exceção: Permite capturar uma exceção em um bloco except, realizar algum procedimento (como registrar um log ou limpar recursos) e usar a instrução raise sozinha para repassar a mesma exceção adiante.
            ->Encadear exceções (raise ... from): Permite capturar um erro de baixo nível e lançar uma exceção mais significativa para a aplicação, preservando a causa original no traceback com a sintaxe raise NovaExcecao from erro_original
    
    Exemplo de uso:
        -> Verificação de Respostas em Requisições HTTP: Métodos de bibliotecas (como `raise_for_status()` em `requests`) utilizam o `raise` interno para disparar exceções quando o servidor retorna códigos de erro (ex.: 404 ou 500).
'''
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') #cria seu proprio erro.
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))