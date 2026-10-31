r"""
    EXPRESSÃO REGULAR (regex ou regexp)

    É uma sequência de caracteres que descreve um padrão de texto a ser localizado, validado ou manipulado em uma string.
    Enquanto a busca tradicional por texto se limita a palavras exatas, as expressões regulares permitem procurar estruturas complexas, como números e telefones, endereços de e-mail, datas ou formatos específicos de código, reduzindo significamente a quantidade de linhas necessárias para processar textos.

    No Python, todas as funcionalidades de expressões regulares estão contidas no módulo re.

    A declaração segue o padrão:
        var = re.<metodo>(<parametros>,...)

    Principais simbolos e metacaracteres:

        Classes de Caracteres Abreviadas (Shorthand Classes)
        1. \d: Qualquer dígito numérico de 0 a 9
        2. \D: Qualquer caractere que não seja um dígito numérico.
        3. \w: Qualquer caractere de palavra (letras, dígitos ou o caractere sublinhado _).
        4. \W: Qualquer caractere que não seja de palavra.
        5. \s: Qualquer caractere de espaço em branco (espaço, tabulação \t ou quebra de linha \n).
        6. \S: Qualquer caractere que não seja espaço em branco.

        Quantificadores (Repetição)
        1. ?: Torna o grupo anterior opcional (corresponde a 0 ou 1 ocorrência).
        2. *: Corresponde a zero ou mais ocorrências do grupo anterior.
        3. +: Corresponde a uma ou mais ocorrências (o elemento precisa aparecer ao menos uma vez).
        4. {n}: Corresponde a exatamente n repetições.
        5. {n,m}: Corresponde a uma faixa de repetições, no mínimo n e no máximo m. Omita o segundo número ({n,}) para especificar n ou mais

        Âncoras de Posição
        1. ^: Exige que a correspondência ocorra no início do texto.
        2. $: Exige que a correspondência ocorra no fim do texto.
        3. ^\d+$: Exige que a string inteira seja composta exclusivamente por dígitos do início ao fim.

        Curingas e Agrupamentos
        1. .(Ponto): Funciona como um curinga, correspondendo a qualquer caractere individual, exceto quebras de linha (\n)[23].
        2. .* : Combina com qualquer sequência de caracteres.
        3. | (Pipe): Funciona como um operador OU, permitindo casar um entre vários padrões.
        4. () (Parênteses): Cria grupos na expressão regular. É possível extrair partes específicas da correspondência chamando group(1), group(2), etc.
        5. [...] (Classe personalizada): Define um conjunto de caracteres permitidos. Por exemplo, [aeiouAEIOU] corresponde a qualquer vogal. Adicionar um acento circunflexo no início ([^aeiou]) nega a classe, correspondendo a tudo que não for vogal.
"""

import re #regular expression

cpf = '746.824.890-70'
cpf = re.sub(r'[^0-9]', '', cpf) #pega qualquer coisa que não for um número([^0-9]) e substitui por ''.
print(cpf, type(cpf))