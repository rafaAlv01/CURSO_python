"""
ARQUIVOS

    A manipulação de arquivos em Python é importante para persistência de dados, automação de tarefas e integração de sistemas.

    CICLO DE VIDA:
        Para manipular um arquivo em disco, é necessário realizar um ciclo básico.

            Abertura, Leitura/Escrita e Fechamento.

        A abertura é feita pela função nativa open(), que conecta o programa ao arquivo gerenciado pelo sistema operacional e retorna um file object.
        O fechamento explícito com .close() é fundamental para liberar os recursos do sistema operacional e garantir que os dados em memória buffer sejam gravados no disco. A forma moderna e recomendada de gerenciar esse ciclo Python é utilizando o Gerenciador de Contexto With, que garante o fechamento automático do arquivo mesmo que ocorram excessões.

        Context Manager - with (abre e fecha).

    MODOS DE LEITURA:
        O comportamento da função open() é determinado pelo parâmetro de modo:
            1. 'r' (read) : modo de leitura padrão. Retorna erro se o arquivo não existir.
            2. 'w' (write) : modo de escrita. Cria um novo arquivo ou sobrescreve/apaga todo o conteúdo de um arquivo existente.
            3. 'a' (append) : modo anexo. Adiciona novos dados ao final do arquivo preservando o conteúdo existente.
            4. 'x' (Exclusive Creation) : Cria o arquivo para escrita, mas lança uma exceção FileExistsError se o arquivo já existir, prevenindo sobrescritas acidentais.
            5. 'b' (Binary) : Abre o arquivo em modo binário (ex: 'rb', 'wb'), lidando com dados brutos em bytes em vez de strings.
            6. '+' (Update) : Permite leitura e escrita simultâneas (ex: 'r+', 'w+').
            7. 't' (text) : modo texto.
        
        Diferença entre 'w' e 'a'.
            O modo 'w' APAGA TUDO do arquivo e sobrescreve ele.
            O modo 'a' INSERE coisas do arquivo a partir da ULTIMA linha do arquivo. Bom pra gerar logs.

    Texto vs Binário e o Unicode Sandwich
        Em arquivos de texto, os caracteres são codificados/decodificados automaticamente. Para garantir a portabilidade entre sistemas operacionais, é essencial definir o parâmetro encoding='utf-8' explicitamente ao abrir arquivos de texto. A boa prática conhecida como "Unicode Sandwich" dita que dados recebidos devem ser codificados para str na entrada (leitura), processados como str na lógica interna e codificados para bytes na saída (escrita).

    LEITURA E ESCRITA DE DADOS:
        Métodos de Leitura
            1. .read(tamanho) : Lê o arquivo inteiro de uma só vez (ou até o tamanho bytes/caracteres) e retorna uma string ou objeto bytes.
            2. .readLine() : Lê uma única linha do arquivo por vez.
            3. .readlines() : Lê o arquivo inteiro e retorna uma lista de strings, onde cada elemento corresponde a uma linha do arquivo.
            4. Interação direta (RECOMENDADO PARA ARQUIVOS GRANDES): O próprio objeto de arquivo é um iterável; iterar linha por linha em um laço for consome pouca memória RAM.
                with open('dados.txt', 'r', encoding='utf-8') as f:
                    for linha in f:
                        print(linha.strip())
        
        Métodos de escrita:
            1. .write(string) : Escreve uma string no arquivo. Não adiciona quebras de linhas automaticamente.
            2. writelines(iterável) : Escreve várias linhas.
            2. Redirecionamento com print() : Pode-se redirecionar a saída do print() diretamente para um arquivo aberto em modo texto utilizando o argumento file.
                with open('relatorio.txt', 'w', encoding='utf-8') as f:
                    print("Cabeçalho do Relatório", file=f)
            
        Outros métodos:
            1. seek() : move o cursor.
    
    MANIPULAÇÃO DE CAMINHOS E DIRETÓRIOS (os, os.path e pathlib)
        O Python disponibiliza ferramentas para navegar e inspecionar o sistema de arquivos.

        Navegação e Inspeção com o Módulo os e os.path

            1. Diretório Atual e Mudança : os.getcwd() obtém o diretório de trabalho atual e os.chdir(caminho) altera o diretório ativo.
                myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
                for filename in myFiles:
                    print(os.path.join('C://Users//asweigart', filename))

                (vai retornar os diretorios dos arquivos presentes na lista. A partir de algo assim, é possível alternar entre arquivos.)
            
            2. Construção de Caminhos : os.path.join('pasta', 'arquivo.txt') combina nomes de pastas usando o separador correto de cada sistema operacional (\ no Windows e / no Linux/macOS).

            3. Decomposição de Caminhos :
                -> os.path.basename(path) : Retorna o nome do arquivo.
                -> os.path.dirname(path) : Retorna o caminho da pasta pai.
                -> os.path.split(path) : Retorna uma tupla (dirname, basename).
                -> os.path.abspath(path) : Converte um caminho relativo em um caminho absoluto.
            
            4. Validação e Metadados :
                -> os.path.exists(path) : Verifica se o caminho existe. True se sim, False se não.
                -> os.path.isfile(path) e os.path.isdir(path) : Verificam se é um arquivo ou pasta.
                -> os.path.getsize(path) : Retorna o tamanho do arquivo em bytes.
        
        pathlib.Path.parts
            pathlib lida nativamente com as regras de cada sistema operacional e devolve uma tupla com as partes do caminho.

                from pathlib import Path

                p_posix = Path("/home/user/docs/relatorio.pdf")
                print(p_posix.parts)
                # ('/', 'home', 'user', 'docs', 'relatorio.pdf')

                p_windows = Path(r"C:\Users\nome\docs\relatorio.pdf")
                print(p_windows.parts)
                # ('C:\\', 'Users', 'nome', 'docs', 'relatorio.pdf')
            
            se precisar especificamente de uma list, basta converter: list(Path(caminho).parts)
            se quiser ignorar a raiz ("C:\\" ou "/") ou barras finais, Path.parts já evita barras finais vazias e separa claramente a raiz do restante do caminho.

            PORQUE pathlib.Path.parts para retornar o caminho ao invés de split(os.path.sep)?
                split(os.path.sep) pode falhar em:
                    Barras no início ou no fim geram strings vazias (""):
                        "/home/user/docs".split("/") retorna ["", "home", "user", "docs"].
                        "/home/user/docs/".split("/") retorna ["", "home", "user", "docs", ""].

                    Separadores misturados no Windows:
                        No Windows, os.path.sep é "\\", mas caminhos frequentemente misturam "/" e "\\". split(os.path.sep) não divide as barras "/".

                    Unidades e caminhos UNC no Windows:
                        Em "C:\\Users\\nome", split("\\") gera ["C:", "Users", "nome"], tratando "C:" como uma pasta comum em vez de raiz/unidade.

                    Caminhos relativos ou redundantes:
                        "./pasta//arquivo.txt".split("/") mantém "." e "" no meio da lista.
            
        VARREDURA RECURSIVA COM os.walk()
            A função os.walk(top) percorre uma árvore de diretórios inteira, gerando para cada pasta uma tupla contendo:
                (caminho_da_pasta_atual, lista_de_subpastas, lista_de_arquivos)
                EX:
                    import os
                    
                    for raiz, diretorios, arquivos in os.walk('.'):
                        for nome_arquivo in arquivos:
                            caminho_completo = os.path.join(raiz, nome_arquivo)
                            print(caminho_completo)

    
    ORGANIZAÇÃO, CÓPIA, MOVIMENTAÇÃO E REMOÇÃO (shutil e send2trash)
        Para operações estruturais de arquivos e pastas no disco, utiliza-se o módulo shutil.
            1. Copiar Arquivos e Pastas:
                shutil.copy(origem, destino) : Copia um único arquivo.
                shutil.copytree(origem, destino) : Copia uma pasta inteira de forma recursiva com todos os seus arquivos e subpastas.
            2. Mover e Renomear:
                shutil.move(origem, destino): Move ou renomeia arquivos e diretórios.
            3. Remoção de Arquivos e Diretórios:
                os.unlink(path) / os.remove(path) : Deleta um arquivo permanentemente.
                os. rmdir(path) : Deleta uma pasta vazia.
                shutil.rmtree(path) : Deleta permanentemente uma pasta e todo o seu conteúdo.
            4. Lixeira Segura (send2trash) :
                A biblioteca de terceiros send2trash envia arquivos para a lixeira do sistema operacional em vez de apagá-los permanentemente, precenindo perdas acidentais de dados durante a automação.
    
    FORMATOS ESPECÍFICOS, DADOS ESTRUTURADOS E BUFFERS
        1. Serialização e Armazenamento de Variáveis:
            a) shelve e pickle : O módulo shelve permite armazenar objetos e dados Python(listas, dicionarios) em arquivos binários que funcionam como dicionários chave-valor em disco. O módulo pickle serializa/reconstrói objetos complexos diretamente.
            b) csv : Permite ler e escrever arquivos delimitados utilizando leitores e escritores (csv.reader, csv.writer, csv.DictReader, csv.DictWriter)
                Para ler dados de um arquivo CSV com o módulo 'csv', você precisa criar um objeto 'Reader'. Um objeto 'Reader' permite que você percorra as linhas do arquivo CSV. Digite o seguinte código, com example.csv no diretório de trabalho atual:

                    import csv
                    
                    exampleFile = open('example.csv')
                    exampleReader = csv.reader(exampleFile)
                    exampleData = list(exampleReader)
                    print(exampleData)
                    
                    # Retorno: [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
                
        2. Arquivos Comprimidos(gzip, bz2, zipfile)
            a) O módulo zipfile permite criar(zipfile.ZipFile('arquivo.zip', 'w')), ler('r') e extrair arquivos .zip.
            b) Os módulos gzip e bz2 oferecem versão alternativas da função open() para ler arquivos compactos .gz e .bz2 como se fossem arquivos regulares.

        3. Operações em Memória e Arquivos Temporários
            a) io.StringIO e io.BytesIO : Criam objetos que se comportam como arquivos abertos, mas que operam inteiramente em buffers da memória RAM.
            b) tempfile: Fornece funções como tempfile.TemporaryFile() ou tempfile.TemporaryDirectory() para criar arquivos e diretórios temporários que são excluídos automaticamante após o término do uso.
                Ex: pode ser usado para criar um diretório que faça o download automático de arquivos. Essa pasta normalmente fica no diretório que será armazenado o arquivo, e pode ser excluída utilizando a referida ferramenta após o download.
"""