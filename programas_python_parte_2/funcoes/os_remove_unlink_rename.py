"""
    os.unlink(path) / os.remove(path) : Deleta um arquivo permanentemente.
    os.rename()

    rename retorna uma exceção se já tiver um arquivo com o mesmo nome que será usado para renomear. FileExistsError

    EXECUTE NO DEBUGGER, PARA VER O QUE ESTA ACONTECENDO.
"""
from os import unlink, remove, rename

arquivo = 'arquivo_para_remover.txt'
caminho_arquivos_apoio = 'C:\\Users\\rafae\\OneDrive\\Desktop\\CURSO_python\\programas_python_parte_2\\arquivos_apoio\\'
caminho_para_armazenar_na_pasta = caminho_arquivos_apoio + arquivo

with open(caminho_para_armazenar_na_pasta, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção: linha com acentuação.\n')
    arquivo.writelines(('Linha 1\n', 'Linha 2\n', 'Linha 3\n'))

rename(caminho_para_armazenar_na_pasta, f'{caminho_arquivos_apoio + 'novo_nome.txt'}')

unlink(f'{caminho_arquivos_apoio + 'novo_nome.txt'}')