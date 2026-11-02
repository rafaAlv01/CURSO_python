r"""
IMPORTANTE: Em expressões refulares, os grupos são criados para delimitar trechos de um padrão usando os parênteses. Servem para isolar, extrair e manipular subpartes do texto.

Como os grupos funcionam:
    1. Numeração: O grupo 0 (.group() sem args) representa a correspondencia completa do padrao. Cada par de parenteses subsequentes, da esquerda pra direita, define os grupos 1, 2, 3 e assim por diante.
    2. Acesso aos valores: Em um objeto Match, usa-se o método .group() para obter partes especificas, ou .groups() para recuperar uma tupla contendo todos os grupos capturados.
    3. No método .sub(), os grupos capturados podem ser referenciados diretamente na string de substituição usando a sintaxe \1, \2, \3, etc.

Alguns dos principais métodos do módulo re.

    1. search(padrao, texto) : Varre a string e retorna UM objeto Match para a PRIMEIRA ocorrência encontrada. Se houver mais de um grupo no padrão, o objeto Match pode usar o método groups() para retornar todos os grupos de captura definidos na expressão regular(no padrão).

    2. match(padrão, texto) : Verifica se há correspondência especifica no início da string.

    3. findall(padrão, texto) : Localiza TODAS as ocorrências no texto.
        Se o padrão não tiver grupos, retorna uma lista de strings.
        Se o padrão possuir, retorna uma lista de tuplas contendo o texto de cada grupo.
    
    4. finditer(padrão, texto) : retorna um iterador de objetos Match. Poupa memória ao processar grandes arquivos ou volumes de dados.

    5. sub(padrão, texto) : substitui as ocorrencias encontradas por um novo texto. É possível usar para "ocultar" a informação.

    6.split(padrão, texto) : Divide a string utilizando a expressão regular como delimitador flexível. ESSA É UMA FERRAMENTA DE PRE-PROCESSAMENTO DE TEXTO, fundamental para preparar dados para treinar modelos de I.A. O split pode ser usado para preparar os dados na fase incial, MAS, hoje, existem ferramentas melhores para isso, como o Byte-Pair Encoding, que divide o texto em pedaços inteligentes (subpalavras).
"""

import re
texto_0 = "O evento aconteceu na data de 25/12/2026."
texto_1 = "Meu nome é Rafael, tenho 25 anos. Quero uma vaga de emprego. Meus contatos são (86) 98115-1603, (89) 98114-1409"
texto_2 = "O macarrão foi R$25 reais, a lasanha foi R$50,21 reais ,256 reais, a calabresa foi R$3.000,00 reais. A empada custou R$ 5.0,12 reais, a manteiga R$.12,00 reais e o molho R$  6,000.167,0 reais, a agua foi R$ 900000,00, o tempero foi R$3.000,00,0.0"


#SEARCH
padrao = r'\((\d{2})\) \d{5}-\d{4}'
resultado = re.search(padrao, texto_1)
print(f'SEARCH, encontrado: {resultado.group()}' if resultado else 'SEARCH, não encontrado')

#SEARCH retorna tupla com todos os grupos definidos na expressao regular.
padrao_groups = r"(\d{2})/(\d{2})/(\d{4})"
resultado = re.search(padrao_groups, texto_0)
print(f'SEARCH grupos, encontrado: {resultado.groups()}' if resultado else 'SEARCH grupos, não encontrado')

#MATCH
resultado = re.match(r'Meu', texto_1)
print(f'MATCH, encontrado: {resultado.group()}' if resultado else 'MATCH, não encontrado')

resultado = re.match(r'Rafael', texto_1)
print(f'MATCH, encontrado: {resultado.group()}' if resultado else 'MATCH, não encontrado')

#FINDALL
r'''
FINDALL

Ex1:
padrao_findall_no_group = r'\$\s*\d+([.,]\d+)*'
---> a expressão acima contém um grupo. Quando se usa o método findall e usa na expressão padrão somente um grupo explicitado, apenas a ocorrencia do grupo será capturada. O resto será ignorado. Teste a saída.

padrao_findall_no_group = r'\$\s*\d+(?:[.,]\d+)*'
--> Aqui, tudo é capturado. A expressão (?:...) é um grupo que não é capturado, ele apenas agrupa os elementos.
Entretanto, valores como R$3.00,00,0.0 são aceitas.

padrao_findall_no_group = r'R\$\s*(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d{2})?'
-->Aqui o padrão é mais elaborado. Entretanto, numeros como R$ 5.0,12 reais são coletados errados. Teste.

padrao_findall_no_group = r'R\$\s*(?:\d+|\d{1,3}(?:\.\d{3})+)(?:,\d{2})?(?![\d.,])'
--> Esse padrão está ótimo para valores padronizados com ponto e vírgula. A expressão (?![\d.,]) impede que a correspondencia termine antes de outro dígito, ponto ou vírgula. Entretanto, não recolhe valores como R$900000,00 , que, apesar da falta de uma ponto, para separar a casa do milhar, continua sendo uma expressão válida, pois o ponto pode ser omitido.
'''
padrao_findall_no_group = r'R\$\s*(?:\d+|\d{1,3}(?:\.\d{3})+)(?:,\d{2})?(?![\d.,])'
resultado = re.findall(padrao_findall_no_group, texto_2)
print(f'FINDALL NO GROUP, encontrado: {resultado}' if resultado else 'FINDALL NO GROUP, não encontrado')

#para capturar os parenteses: r'(\(\d{2}\)) (\d{5}-\d{4})'
padrao_findall_group = r'\((\d{2})\) (\d{5}-\d{4})'
resultado = re.findall(padrao_findall_group, texto_1)
print(f'FINDALL GROUP, encontrado: {resultado}' if resultado else 'FINDALL GROUP, não encontrado')

#FINDITER

texto_3 = 'IDs dos produtos: A12, B45, C78'
padrao_finditer = r"[A-Z]\d{2}"

for match in re.finditer(padrao_finditer, texto_3):
  print(
      f'ID: {match.group()} (Encontrado na posição {match.start()}-{match.end()})'
  ) #note que aqui que é possível retornar a posição dos elementos encontrados. Vantagem de iteradores: mais dados gerados, mas por demanda.

#SUB

texto_sub = re.sub(padrao, '**** **********', texto_1)
print(texto_sub)

#SUB substituindo apenas grupos especificos
padrao_sub = r'\((\d{2})\) (\d{5})-(\d{4})'
texto_sub = re.sub(padrao_sub, r'(\1) *****-****', texto_1) #Aqui, o grupo 1 n é modificado.
print('SUB substituindo apenas partes do padrão: ', texto_sub)
#SPLIT

padrao_split = r'[,;.\s]+'
texto_split = re.split(padrao_split, texto_1)
print('Texto dividido: ', texto_split)