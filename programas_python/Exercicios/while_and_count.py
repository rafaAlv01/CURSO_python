#Qual letra apareceu mais vezes na frase?

frase = 'Olá mundo! Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'.lower().replace(" ", "")
print(frase.count('python'))

i=0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if quantas_vezes_letra_apareceu > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra \'{letra_apareceu_mais_vezes}\' foi a que apareceu mais vezes, totalizando, {qtd_apareceu_mais_vezes} aparições.')
    