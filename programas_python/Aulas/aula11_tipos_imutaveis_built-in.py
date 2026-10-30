"""
Tipos imutaveis são aqueles que não podem ser alterados durante a execução do código.
Imutáveis: str, int, float, bool

built-in são tipos e metodos que já vem EMBUTIDOS no python.
"""

string = 'Rafael Oliveira'

#se eu quiser mudar uma letra da string, terei que criar outra, pois o python considera expressão string[3] = 'i' como errada, pois str é imutável. 
outra_variavel = f'{string[:3]}i{string[4:]}'

print(outra_variavel)
print(string.capitalize()) #retorna uma copia da string com o primeiro caractere maiusculo e o resto minusculo
