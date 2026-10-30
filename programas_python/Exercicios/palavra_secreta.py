import os #importou o módulo os
import keyboard

secret_word = 'chocolate'
repeticoes = 0
letras_acertadas = ''

while True:
    repeticoes += 1
    letra = input('Digite uma letra: ')

    if len(letra) > 1 :
        print('Digite apenas uma letra')
        continue


    if letra in secret_word:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in secret_word:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == secret_word :
        print(f'Você acertou! A palavra era {secret_word}')
        break

print(f'O número de repetições foi {repeticoes}')