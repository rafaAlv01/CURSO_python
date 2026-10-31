"""
    Existem diversos métodos built-in para str. Aqui, listei alguns que podem ser usados com mais frequencia no curso.
    https://docs.python.org/pt-br/3.16/builtins/stdtypes.html#string-methods -> documentação com todos os métodos built-in do tipo str.
"""

texto1 = "Python"
texto2 = "Python3"
texto3 = "Olá Mundo"  # O espaço em branco faz retornar False
texto4 = "      "
texto5 = "12345"
texto6 = "12341.."

print(texto1.isalpha())  
print(texto2.isalpha())  
print(texto3.isalpha())

#.isalnum() verifica se todos são alfanuméricos
print(texto1.isalnum())  
print(texto5.isalnum())  
print(texto3.isalnum())

#.isdigit() ou .isnumeric() verifica se todos os caracteres são digitos numericos. isnumeric() é mais abrangente que isdigit().
print(texto1.isdigit())  
print(texto2.isdigit())  
print(texto5.isdigit())
print(texto6.isdigit())

# .isspace() vericia se a string contém apenas espaços em branco
print(texto1.isspace())  
print(texto5.isspace())  
print(texto4.isspace())

# .count() verifica quantas vezes algo apareceu na string.
frase = 'Olá mundo! Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'
print(frase.count('Python'))

# .lower() converte todas as maiusculas para minusculas. .replace(arg1, arg2) em todas as insidencias de arg1, o valor é trocado para arg2.
frase = 'Olá mundo! Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'.lower().replace(" ", "") #tira todos os espaços da frase.
print(frase)
"""
frase.index(elemento, inicio, fim)
elemento: O valor que você deseja encontrar na lista.
inicio (opcional): O índice a partir do qual a busca deve começar. O padrão é 0.
fim (opcional): O índice onde a busca deve parar. O padrão é o final da lista.
"""
print(frase.index('o', 2))

# .replace() -> troca um caractere por outro.
print(frase.replace('!', '.').replace('á', 'a'))