"""
    Imprecisão de ponto flutuante.

    Internamente, os computadores armazenam números e realizam cálculos usando o sistema binário e o padrão de hardware IEEE 754.
    No sistema decimal, números como 0.1 e 0.7 são frações exatas e finitas(1/10 e 7/10). No entanto, no sistema binário,
        esses mesmos números não possuem representação exata e se tornam dízimas periódicas infinitas.
    Como a memória reservada para um número de ponto flutuante é finita, a máquina precisa truncar/arredondar essa dízima binária
        para o valor representável mais próximo.
    Quando o Python executa a soma de dois flutuantes, ele está somando duas aproximações binárias guardadas na memória. O resultado
        dessa adição binária converte-se para um valor aproximado ao invés do valor exato.
"""
import decimal
from fractions import Fraction

num_1 = 0.1
num_2 = 0.7

result = num_1 + num_2

print(f'{result=}') #note que o resultado é 0.799999999999999999 -> aproximado.

"""
    RESOLVENDO
"""

#delimitando o número de casas decimais
print(f'{result:.2f}')

#usando a função round, que arredonda o valor.
print(round(result, 2))

#usando o modulo decimal (Precisão Decimal Exata) -> usar quando imprecisões são inaceitáveis. Usado para sistemas financeiros e de contabilidade.
num_3 = decimal.Decimal('0.1')
num_4 = decimal.Decimal('0.7')
result2 = num_3 + num_4
print(result2)

#usando o MODULO fractions (Fracao exata) -> para trabalhar com valores racionais.
result3 = Fraction('0.1') + Fraction('0.7')
print(result3)
