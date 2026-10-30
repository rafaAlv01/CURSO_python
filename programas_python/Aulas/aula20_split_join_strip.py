"""
    split, join, strip

    São métodos importantíssimos da str.
"""

frase = 'Preciso de, um emprego'

# [SPLIT] divide ums string em determinado caractere. Quando o split não recebe argumento, ele usa qualquer caractere de espaço em branco (espaços, \n, \t) como separador.
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras2_cruas = frase.split(',') #divide quando encontrar , (virgula)
print(lista_palavras2_cruas)

lista_palavras2_modified = [] #criar uma variavel para modificação é uma boa prática de programação. Segurança.

# [STRIP] remove caracteres das extremidades sem alterar os caracteres presentes no meio do texto.
# se o argumento estiver vazio, strip remove qualquer caractere de espaço em branco.
for i, frase in enumerate(lista_palavras2_cruas):
    lista_palavras2_modified.append(lista_palavras2_cruas[i].strip())

print(lista_palavras2_modified)

#lstrip() -> remove apenas da extremidade esquerda.
#rstrip() -> remove apenas da extremidade direita.

# [JOIN] realiza a operação inversa do split(): ele pega uma lista de strings e junta todos os elementos em um única string,
#       utilizando a string a qual o método foi chamado como separador.
#SINTAXE: separador.join(lista_de_strings)

lista_palavras2_modified.append('1')

frases_unidas = ', '.join(lista_palavras2_modified) #join só aceita listas que sejam exclusivamente de strings.
print(frases_unidas)