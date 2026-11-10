"""
try/except
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

    try:
        ...
    except:
        ...

        -> Tenta executar algo. Se retornar um erro, é capturado pelo except.
        -> except sozinho captura QUALQUER erro. Não é uma boa prática de programação porque pode mascarar erros.

        except Exception as error:
            -> Exception é a classe pai, a primordial. error é uma instancia da subclasse que retornou o erro.
            -> 'as' é usado para colocar o erro capturado na instancia error.

            -> error.__class__.__name__ -> pega a classe que gerou o erro e retorna o nome dela. ISSO SERVE PARA RETORNAR O ERRO PARA O PROGRAMADOR VER. O USUÁRIO NÃO ENTENDERIA SE APARECESSE O ERRO: TypeError. A propria instancia traduz para uma forma mais entendível ao usuário.
    
    try:
        ...
    finally: -> aqui, depois de executar o try, o finally SEMPRE é executado. Se ocorrer um erro em try, o finally é executado e só depois o erro é propagado.
        ...

    Quando finally é usado:
        -> Indicado principalmente para operações em que a não execução da limpeza comprometeria o sistema ou vazaria recursos de memória/SO.
        
        -> Fechamento de Conexões e Arquivos:
            Garantir que arquivos em disco, conexões de banco de dados ou conexões de rede (sockets) sejam explicitamente fechados e liberados, evitando que fiquem travados ou consumam recursos do sistema.
        -> Liberação de Travas em Concorrência(Locks):
            Em programas multithreaded ou assíncronos, ao adquirir uma trava (Lock, Semaphore), o finally garante que o bloqueio seja desfeito (lock.release()), mesmo que o bloco protegido levante um erro.
        -> Restauração de Estado Global ou Temporário:
            Quando um programa precisa alterar temporariamente uma configuração (como redirecionar sys.stdout), alterar diretórios ou modificar sinalizadores de sistema) e precisa restaurar o estado original com segurança.
        ->Limpeza em Geradores e Corrotinas:
            Ao trabalhar com funções geradoras ou corrotinas, o bloco try/finally assegura que tarefas de cancelamento e finalização de tarefas sejam processadas adequadamente quando a execução for interrompida.
    
    RELAÇÃO COM A INSTRUÇÃO with (Gerenciador de contexto)
        -> A instrução with foi criada especificamente para simplificar e padronizar o padrão try/finally.

        -> Quando você utiliza `with open(...) as f:`, o método interno `__exit__` do arquivo funciona exatamente desempenhando o papel do bloco `finally`
        ->Ao criar seus próprios gerenciadores de contexto com o decorador `@contextmanager`, o ponto onde o código é restaurado após o `yield` é colocado dentro de um `finally`. ISSO ESTÁ DEMONSTRADO NO FINAL DESSE ARQUIVO.
"""
from contextlib import contextmanager
import time

numero= '1.1'

if numero.isdigit() : #o método isdigit() retorna True se todos os digitos forem numericos. Se entrar com 1, dá True. Se entrar com 1.1, dá false.
    numero_f = float(numero)
    print(f'O dobro de {numero} é {numero_f * 2:.2f}')
else:
    print('Isso não é um número.')

print()
print('Usando Try/Except')
print()

try: #o try/except funciona pra diversas situações, diversos erros. Por exemplo, se aqui digitarmos 1.1, não passa pelo if mas passa pelo try.
    numero = input('Vou dobrar o número que vc digitar: ')
    print('STR: ', numero)
    numero_f = float(numero) #se digitar uma letra, trava aqui. A execução é interrompida e o compilador pula direto pro except.
    print('FLOAT: ', numero_f)
    print(f'O dobro de {numero} é {numero_f * 2:.2f}')
except: #Esse except pega qualquer erro que surgir entre as linhas 19 e 23. Se o usuário apertar Ctrl + C, o programa não será encerrado, pois o erro KeyboardInterrupt seria capturado.
        #Para evitar isso, é importante especificar o tipo de erro. Ex: except ValueError:
    print('Isso não é um número.')


#BOA PRÁTICA DE PROGRAMAÇÃO: ESPECIFICAR O ERRO PARA RETORNAR O QUE CAUSOU O ERRO.
print('\n', 'Especificando o erro', sep='')
dicionario_vazio = dict()
try:
    print(dicionario_vazio['curso'])
except Exception as error:
    print(f'O erro dado foi porque a seguinte chave não existe no dicionário: {error}')
    print('MSG:', error.__class__.__name__)
print()

#ZeroDivisionError, NameError
try:
    a, b = 10, 0
    c = a/b
    print(f'{b[0]}')
except ZeroDivisionError as e: #isso é uma classe. PascalCase. Cada palavra começa com letra maiuscula.
    print('MSG: ', e)
except NameError:
    print('Nome b não está definido') #esse erro ocorreria se a variavel b não fosse definida.
except (TypeError, IndexError) as error:
    print('MSG:', error) #se tentasse verificar a posição 0 de b, mesmo ele n tenho index por não ser uma lista.
    print('MSG:', error.__class__.__name__)
except Exception:
    print('Erro DESCONHECIDO')
print()

'''
Ao criar seus próprios gerenciadores de contexto com o decorador @contextmanager, o ponto onde o código é restaurado após o yield é colocado dentro de um finally.

    @contextomanager : É um decorador do módulo contextlib que transforma uma função geradora comum (uma função que usa yield) em um gerenciador de contexto. Isso permite que a função seja usada com a palavra-chave with.

    O yield pausa a execução da função temporizador e "entrega" o controle para o bloco de código que está dentro do with. O try garante que, aconteça o que acontecer, a parte seguinte será executada.

    finally: fim = time.time(): O bloco finally é sempre executado, mesmo se o código de dentro do with terminar normalmente ou se lançar algum erro (exceção). Ele captura o horário de término.
'''

@contextmanager
def temporizador(rotulo):
    inicio = time.time()
    try:
        yield
    finally: #Esse finally só é executado depois que o comando dentro do with é executado.
        fim = time.time()
        print(f'{rotulo} : {fim - inicio:.4f} segundos')

# Simulando uma tarefa demorada
with temporizador("Processamento de dados"):
    # Tudo dentro deste bloco é medido pelo temporizador
    time.sleep(1.5)  # Simula uma pausa de 1.5 segundos