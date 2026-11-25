"""

https://otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

Em Python 3, existe uma distinção entre texto estruturado para leitura humana(str) e sequências de bytes brutos(bytes).

    Encoding(Codificação):
        No padrão Unicode, cada caractere é identificado de forma abstrata por um número único chamado code point (por exemplo, a letra A possui o code point U+0041).

            Encoding: É o algoritmo que converte esses code points abstratos de texto(str) em uma sequência de bytes armazenáveis em disco ou trasmissíveis via rede. O método responsável por essa conversão em Python é o .encode() .

            Decoding (Decodificação): É o processo inverso, no qual uma sequência de bytes brutos é convertida de volta para caracteres de texto humano através do método .decode() .

    O Princípio do "Unicode Sandwich"
        A boa prática recomendada para o tratamento de dados textuais na arquitetura de softwares é o Unicode Sandwich.
            1. Entrada: Decodifica-se os bytes de entrada para str o mais rapido possível.
            2. Processamento: Toda a lógica de negócios e manipulação de texto do programa deve ser feita 100% utilizando objetos do tipo str.
            3. Saída: Codifica-se o texto de str de volta para bytes o mais tarde possível, no momento de salvar o arquivo ou enviar a resposta.

    Principais Encodings (Codecs)
        1. ASCII (contem letras do alfabeto inglês, números e pontuações básicas(sem suporte a acentos)).
        2. Latin-1 (ISO-8859-1) e CP1252 :
            Mapeiam os primeiros 256 valores de bytes diretamente para caracteres latinos; o CP1252 é uma extensão comum da Microsoft para o Windows que adiciona símbolos como o sinal do Euro e aspas curvadas.
        3. UTF-8 :
            Codificação de tamanho variável mais utilizada na Web e padrão em sistemas Linux e macOS. É capaz de representar qualquer code point do Unicode e é totalmente compatível com arquivos ASCII.
        4. UTF-16 :
            Codificação de 16 bits que utiliza pares de escape para caracteres estendidos. Pode incluir um indicador da ordem dos bytes no inicio do arquivo chamado BOM(Byte Order Mark, como b'\\xff\\xfe').

    O PARAMETRO encoding NA FUNÇÃO open()
        
        Ao abrir arquivos de texto utilizando a função open(), se o parâmetro encoding for omitido, o Python assumirá por padrão a codificação de preferência da localidade do sistema operacional(locale.getpreferredencoding()).
        
        Isso é uma causa comum de erros de portabilidade: um arquivo gravado em UTF-8 no Linux ou macOS pode ser lido como CP1252 no Windows, gerando caracteres corrompidos.

        BOA PRÁTICA: Nunca dependa da configuração padrão do sistema e passe sempre o parâmetro encoding='utf-8' explicitamente ao manipular arquivos de texto.

"""
texto = 'café'
bytes_utf8 = texto.encode('utf-8')

texto_recuperado = bytes_utf8.decode('utf-8')

print(f'Texto em bytes: {bytes_utf8}\nTexto humano: {texto_recuperado}\n')

arquivo = 'arquivo.txt'
caminho_arquivos_apoio = 'C:\\Users\\rafae\\OneDrive\\Desktop\\CURSO_python\\programas_python_parte_2\\arquivos_apoio\\'
caminho_para_armazenar_na_pasta = caminho_arquivos_apoio + arquivo

with open(caminho_para_armazenar_na_pasta, 'w') as arquivo:
    arquivo.write('Atenção: linha com acentuação.\n')
    arquivo.writelines(('Linha 1\n', 'Linha 2\n', 'Linha 3\n'))

#Se olhar no arquivo txt os caracteres especiais não aparecerão como deveriam aparecer. Isso acontece porque o Windows usa uma codificação diferente da do Linux/macOS. Como o Python utiliza codificação do SISTEMA (Select Encoding -> Reopen with Encoding -> digite Windows e verifique qual a codificação usada para a américa).

with open(caminho_para_armazenar_na_pasta, 'w', encoding='utf-8') as arquivo: #explicitando encoding para normalizar! Olhe o arquivo novamente.
    arquivo.write('Atenção: linha com acentuação.\n')
    arquivo.writelines(('Linha 1\n', 'Linha 2\n', 'Linha 3\n'))