"""
with ou Context Manager

usando write, read, seek.
"""
arquivo = 'arquivo.txt' #aqui, vai criar na pasta raiz desse programa. Ou seja, dentro da pasta aulas.
caminho_arquivos_apoio = 'C:\\Users\\rafae\\OneDrive\\Desktop\\CURSO_python\\programas_python_parte_2\\arquivos_apoio\\' #aqui, pega o caminho da pasta

caminho_para_armazenar_na_pasta = caminho_arquivos_apoio + arquivo #USA O CAMINHO ABSOLUTO.

with open(caminho_para_armazenar_na_pasta, 'w') as arquivo:
    print('Escrevendo com o 1 with:')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    print('fechando com o 1 with.\n')

with open(caminho_para_armazenar_na_pasta, 'r') as arquivo:
    print('Lendo com o 2 with:\n')
    print(arquivo.read()) #extrai todo o texto do arquivo.
    #se tentar: arquivo.write('Linha 3\n') vai retornar uma mensagem dizendo que não é possível escrever, pois não está no modo escrita.
    print('fechando com o 2 with.\n')

with open(caminho_para_armazenar_na_pasta, 'r+') as arquivo:
    print('Lendo e escrevendo com o 3 with: (sem alterar a posição do cursor)\n')
    print(arquivo.read()) #extrai todo o texto do arquivo.
    arquivo.write('Linha 3\n') #escreve durante a leitura.
    print(arquivo.read()) #Essa LINHAS NÃO VAI printar nada, pois o CURSOR está depois da quebra de linha. A leitura ocorre usando como referencia a posição do cursor. Ele que controla.
    print('fechando com o 3 with.\n')

with open(caminho_para_armazenar_na_pasta, 'r+') as arquivo:
    print('Lendo e escrevendo com o 4 with: (alterando a posição do cursor)\n')
    print(arquivo.read())
    arquivo.writelines(('Linha 4\n', 'Linha 5\n', 'Linha 6\n'))
    arquivo.seek(0,0)
    print(arquivo.read())
    print('fechando com o 4 with.')

with open(caminho_para_armazenar_na_pasta, 'r') as arquivo:
    print('Lendo somente tres linhas com o 5 with:')
    print(arquivo.readline())
    print(arquivo.readline()) #A quebra de linhas a mais ocorre por causa do print. Ele também adiciona um \n no final. Dá pra resolvendo aplicando strip() no arquivo(TextIOWrapper) ou colocando o parametro end="" no print.
    print(arquivo.readline())
    print('fechando com o 5 with')

with open(caminho_para_armazenar_na_pasta, 'r') as arquivo:
    print('Lendo 3 linhas com o 6 with: (usando strip() para remover quebras de linhas criadas pelo cursor)')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print('fechando com o 5 with')

with open(caminho_para_armazenar_na_pasta, 'r') as arquivo:
    print('\nLendo o arquivo com o 7 with: lendo linha por linha usando for.')
    for linha in arquivo.readlines():
        print(linha.strip()) #usando o strip para remover a quebra de linha no final da linha e deixar somente a do print.