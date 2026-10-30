#Calculadora usando While

start_calc = input('Deseja realizar um cálculo? Digite \'sim\' para continuar.')
start_calc = start_calc.lower()
condicao = True if start_calc == 'sim' else False

while condicao:

    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador: (+-/*)')
    num_1_float = 0
    num_2_float = 0
    resultado = 0.0

    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except Exception as error:
        print(error)
        numeros_validos = None

    if numeros_validos is None:
        resposta = input('Um ou ambos os números são inválidos. Digite \'sim\' se deseja continuar:').lower()
        if resposta != 'sim':
            break
        else:
            continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '/' and num_2_float == 0:
        resposta = input('Não é possível realizar essa divisão. Digite \'sim\' se deseja continuar:').lower()
        if resposta != 'sim':
            break
        else:
            continue

    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '/':
        resultado = num_1_float / num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float

    print(f'O resultado é: {resultado}')

    break
    