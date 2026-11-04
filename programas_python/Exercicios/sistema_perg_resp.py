# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0

for item in perguntas:
    pergunta = item['Pergunta']
    print(f'Pergunta: {pergunta}', end='\n\n')

    opcoes = item['Opções']
    print('Opções:')
    for indice, opcao in enumerate(opcoes):
        print(f'{indice}) {opcao}')

    resp = item['Resposta']   
    entrada_usuario = input('Escolha uma opção: ')
    if entrada_usuario not in '0123':
        print('Errou!', end='\n\n')
        continue

    if opcoes[int(entrada_usuario)] == resp :
        acertos += 1
        print('Acertou!')
    else :
        print('Errou!')
    print()

print(f'Você acertou {acertos}\nde {len(perguntas)} perguntas.')