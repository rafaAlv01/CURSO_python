'''
Função Lambda

    A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que contém apenas uma linha (f simplificada; inline). Ou seja, tudo deve ser contido dentro de uma única expressão, sem a necessidade de receber um nome usando a instrução def.

    Declarada usando a palavra-chave lambda e costuma ser empregada em situações onde você precisa de uma função rápida, simples e temporária para ser passada diretamente como argumento de outra função.

    FAZER:
        funcao = lambda parametro : retorno --> É UMA MÁ PRATICA DE PROGRAMAÇÃO. AULA 28 MOSTRA A FORMA CORRETA.

    SINTAXE E ESTRUTURA BASICA:

        lambda argumento : expressão
        
        -> não usa return. O resultado da expressão é avaliado e retornado automaticamente. Aceita multiplos argumentos/parametros.
    
    PRINCIPAIS CASOS DE USO:
        -> Ordenação Personalizada: usada no parametro .key() de funções de ordenação e busca, permitindo definir o critério de ordenação de forma imediata sem precisar criar uma função def externa.
        -> Uso de funções de Ordem Superior (map, filter, reduce): no paradigma funcional, as funções lambdas costumam ser usadas com map() e filter() para transformar ou filtrar coleções. NO GERAL, ESSE USO PODE SER SUBSTITUIDO POR list comprehensions PARA MAIOR CLAREZA.
        -> Leitura de dados I/O em blocos com iter() : A função iter() aceita um chamável sem argumentos e um valor sentinela. A lambda pode ser usada para criar esse chamável de zero argumentos em leituras de arquivos ou sockets.
    
    LIMITAÇÕES IMPORTANTES:
        -> expressao unica: nao aceita comandos, como atribuições, laços de repeticao, instrucoes try/except etc.
        -> dificuldade para depurar: por serem anonimas, aparecem somente como <lambda> nos relatorios de erro.
    
    Se uma função lambda ficar dificil de entender, o ideal é converte-la para uma função def.


'''

#função lambda que calcula o dobro de um número
dobro = lambda x: x * 2
print(f'Calculando o dobro usando lambda: {dobro(3)}')

#função lambda com MULTIPLOS PARAMETROS
soma = lambda x, y: x + y
print(f'Calculando a soma usando lambda: {soma(3, 2)}')
aumento = lambda x, y: (x*y/100)
print(f'Aumento percentual usando lambda: {aumento(2, 50)}') #2% de 50% é um aumento de 1% de 100%.
print()

#Ordenação Personalizada
frutas = ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
resultado = sorted(frutas, key=lambda word: word[::-1]) #passe cada elemento de frutas para a função lambda e ordene com base no valor que retornar.
print(f'Ordenado com base na ultima letra(inversao de palavras): {resultado}')

nomes = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
ordenados = sorted(nomes, key=lambda name: name.split()[-1].lower()) #divide o nome pelo espaço em branco e pega o ultimo nome.
print(f'Ordenado com base no sobrenome: {ordenados}')
print()

#Leitura de dados I/O em blocos com iter()
with open(r'programas_python\arquivos\poema.txt', 'rb') as f:
    for chuck in iter(lambda: f.read(10), b''):
        print(chuck, end=' ')
print('\n')

#CAPTURANDO VARIAVEIS

funcs = [lambda x: x + n for n in range(5)] #As variáveis externas usadas dentro de uma expressão lambda são ligadas em tempo de execução (runtime), e não no momento de sua definição. Isso pode gerar comportamentos inesperados ao criar lambdas dentro de laços de repetição, como observado ao lado.
print([f(0) for f in funcs])

'''
No caso acima quando f(0) chama a função lambda, a variável n usada armazena o valor 4, pois o laço já executou até o final. Isso ocorre porque a variável externa usado dentro da lambda mudou em tempo de execução, não guardou o contexto no closure da função. Para que o contexto seja guardado, é necessário fazer colocar um argumento padrão n=n, para que a cada ciclo do for, a variavel n da função receba um valor diferente, como ocorre no caso abaixo.

DESCRIÇÃO DO QUE OCORRE EM "funcs = [lambda x, n=n: x + n for n in range(5)]"

    -> O for é executado e guarda a função "lambda x, n=n: x+n" em todas as posições da lista gerada.
    -> Cada posição guarda um n diferente, pois ele está sendo definido/congelado a cada ciclo do for. Em n=n, o primeiro n é o parametro e o segundo é o da função.
    -> Assim, a lista ficaria:
        [lambda x, n=0: x + 0, lambda x, n=1: x + 1, lambda x, n=2: x + 2, lambda x, n=3: x + 3, lambda x, n=4: x + 4]
    -> note que o for atribui os valores padroes ao parametro.

SE FOSSE "funcs = [lambda x, n: x + n for n in range(5)]"
    -> Após o for, a lista seria [lambda x, n: x + n, lambda x, n: x + n, ...] aqui, o n seria igual a 4 em todos os casos, pois a não foram salvos os valores de n para cada ciclo do for. A closure pega o valor de padrão, que apareceu no fim da execução do for. 
    SIMULANDO:
        1 iteração: [lambda x, 0: x + 0]
        2 iteração: [lambda x, 1: x + 1, lambda x, 1: x + 1]
        3 iteração: [lambda x, 2: x + 2, lambda x, 2: x + 2, lambda x, 2: x + 2]
        4 iteração: [lambda x, 3: x + 3, lambda x, 3: x + 3, lambda x, 3: x + 3, lambda x, 3: x + 3]
        5 iteração: [lambda x, 4: x + 4, lambda x, 4: x + 4, lambda x, 4: x + 4, lambda x, 4: x + 4, lambda x, 4: x + 4] --> Lista final!

        Observe que o "n" é compartilhado em todos os momentos.
'''
funcs = [lambda x, n=n: x + n for n in range(5)]
print([f(0) for f in funcs])