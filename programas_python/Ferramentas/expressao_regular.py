r"""
    EXPRESSÃO REGULAR (regex ou regexp)

    É uma sequência de caracteres que descreve um padrão de texto a ser localizado, validado ou manipulado em uma string.
    Enquanto a busca tradicional por texto se limita a palavras exatas, as expressões regulares permitem procurar estruturas complexas, como números e telefones, endereços de e-mail, datas ou formatos específicos de código, reduzindo significamente a quantidade de linhas necessárias para processar textos.

    UTILIDADES:
        1. Encontrar padrões de caracteres específicos em texto;
        2. Validar formato de texto (como endereço de email)
        3. Extrair informações de texto
        4. Substituir texto

    No Python, todas as funcionalidades de expressões regulares estão contidas no módulo re.

    A declaração segue o padrão:

        var = re.<metodo>(<parametros>,...)

        Os parametros seguem a formula:
            <metodo>(padrão, texto)

            -> Esse "padrão" é o molde da string que será capturada pelo método. Esse molde é criado através de simbolos e metacaracteres.
            -> Os métodos aceitam Flags e Modificadores de compilação.

    Principais simbolos e metacaracteres:

        Classes de Caracteres Abreviadas (Shorthand Classes)
        1. \d: Qualquer dígito numérico de 0 a 9
        2. \D: Qualquer caractere que não seja um dígito numérico.
        3. \w: Qualquer caractere de palavra (letras, dígitos ou o caractere sublinhado _).
        4. \W: Qualquer caractere que não seja de palavra.
        5. \s: Qualquer caractere de espaço em branco (espaço, tabulação \t ou quebra de linha \n).
        6. \S: Qualquer caractere que não seja espaço em branco.

        Quantificadores (Repetição)
        1. ?: Torna o grupo anterior opcional (corresponde a 0 ou 1 ocorrência). Por exemplo:
            \d+\.?\d*
                \d -> um ou mais digitos
                \.? -> pega o ponto SE tiver.
                \d* -> zero ou mais digitos após o ponto decimal.
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
    
    Para manipular simpolos e metacaracteres numa string, é importante utilizar o r'' para evitar que o compilador considere a barra invertida como caractere de escape.

    Como utilizar o regex:
        1. Importa o módulo
        2. Compila o padrão: diz qual padrão o objeto deve considerar
        3. Opera o objeto: busca o padrão
        4. Extrai o resultado

    SOBRE CORRESPONDENCIA GULOSA NO CONTEXTO DE EXPRESSÃO REGULAR:

        Por padrão, os quantificadores (?, *, +, {n}, {n,m}, entre outros) utilizam o modo guloso. Isso significa que tentam corresponder ao maior trecho de texto possível.

        Adicionar uma interrogação '?' após um quantificador, tranforma-o em NÃO GULOSO, fazendo com que ele busque a menor correspondencia possivel.

    SOBRE INTELIGENCIA ARTIFICIAL:
        Funções de regex ainda são altamente utilizados na limpeza inicial dos dados (remover tags HTML, URLs, caracteres estranhos e padronizar espaços) antes de passá-los para a IA.
"""
#EXEMPLO_1:

import re

cpf = '746.824.890-70'

cpf = re.sub(r'[^0-9]', '', cpf) #pega qualquer coisa que não for um número([^0-9]) e substitui por ''.
print(cpf, type(cpf))

#EXEMPLO_2:
re.sub()
telefone_regex = re.compile(r'\((\d{2})\) \d{5}-\d{4}')

obj_match = telefone_regex.search('Meu telefone é (89) 98109-4738') #procura com o molde e devolve um objeto Match

if obj_match:
    print('Telefone encontrado:', obj_match.group()) #mostra o elemento.

#EXEMPLO_3 (modo GULOSO -> não GULOSO):
texto = 'O participante se chama <Mikael> Costa>.'

guloso = re.compile(r'<.*>')
print(f'GULOSO: {guloso.search(texto).group()}')

nao_guloso = re.compile(r'<.*?>')
print(f'NÃO GULOSO: {nao_guloso.search(texto).group()}')

#EXEMPLO_4 (FLAGS)

texto = 'Meu nome é Rafael.'
padrao = r'rafael'
resultado = re.search(padrao, texto, re.IGNORECASE) #busca sem diferenciar maiusculas e minusculas.
if resultado:
    print('Encontrou!')
else:
    print('Não Encontrou')