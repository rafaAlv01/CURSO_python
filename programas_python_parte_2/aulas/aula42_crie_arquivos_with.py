# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

arquivo = 'arquivo.txt' #aqui, vai criar na pasta raiz desse programa. Ou seja, dentro da pasta aulas.
caminho_arquivos_apoio = 'C:\\Users\\rafae\\OneDrive\\Desktop\\CURSO_python\\programas_python_parte_2\\arquivos_apoio\\' #aqui, pega o caminho da pasta

caminho_para_armazenar_na_pasta = caminho_arquivos_apoio + arquivo #USA O CAMINHO ABSOLUTO.

print(f'Caminho obtido: {caminho_para_armazenar_na_pasta}')

try:
    arquivo = open(caminho_para_armazenar_na_pasta, 'r') #FileNotFoundError -> vai dar esse erro porque o arquivo AINDA não existe na pasta, portanto, não é possível ler 'r'.
except FileNotFoundError as e:
    print(f'O arquivo não existe na pasta: {e.__class__}') #SEM O with (Context Manager), é MUITO IMPORTANTE que o arquivo seja fechado sempre que aberto.

#Para criar um arquivo pode-se usar os modos 'a', 'w' e '+'.
arquivo = open(caminho_para_armazenar_na_pasta, 'w')

arquivo.close()

#Context Manager: with
#Ele é tipo um protocolo para abrir arquivos. Ele abre com open, cria um alias(apelido) para a variavel TextIOWrapper, e, ao final da execução, fecha o arquivo. (O close fica escondido.)
with open(caminho_para_armazenar_na_pasta, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')