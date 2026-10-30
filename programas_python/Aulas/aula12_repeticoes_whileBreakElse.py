"""
while (enquanto)
Executa um pedaço de código enquanto a condição for verdadeira.

Se houver um break, a execução é interrompida e o interpretador sai da caixa while.

Se houver um continue, a execução volta imediatamente para o inicio do loop

WHILE é usado quando não se sabe quantas repetições serão feitas. INDETERMINADO.
"""

condicao = True
i = 0
while condicao:
    i += 1
    if i > 10:
        break
    if i == 4:
        continue #se i==4, pula pro inicio do while. Não executa a linha 18.
    print(i)

print(end='\n\n\n')

#laços internos

qtd_linhas = 5
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print(end='\n\n\n')

#while com else

string = 'valor qualquer'
i=0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
    #se houver um break aqui, o else não seria executado.
else:
    print('como a condição do while foi falsa, o else foi executado.')
