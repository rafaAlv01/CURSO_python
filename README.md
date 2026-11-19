DEBUGGER

    Para Debugar um código, basta usar os BreakPoints.
    A breakpoint pausa a execução no exato ponto onde foi inserida e abre um console interativo chamado PDB(Python Debugger).
    Nesse console, as variáveis que até ele foram executadas serão exibidas, mostrando seus conteúdos.

    Call Stack (pilha de chamadas): 
        É a estrutura de dados dinamica organizada em LIFO(Last in, First out) que o interpretador do python utiliza para rastrar a execução do programa e saber para onde deve retornar quando uma função termina.
        Sob a optica do debugger, a call stack deixa de ser uma abstração invvisível do sistema e se torna uma ferramenta de navegação no tempo e no espaço do código, permitindo entender extamente como o programa chegou a determinado ponto.

        Como a call stack é estruturada no debugger:
            [frame_last_in]    [endereço do arquivo]  [linha:coluna]
            [frame_penultimo]  [endereço do arquivo]  [linha:coluna]
            ...                     ...                 ...
            [frame_first_in]   [endereço do arquivo]  [linha:coluna]
        
        Frame -> é o registro de uma chamada de função que está atualmente na memória da execução.
        linha -> é a linha do frame capturada.
        coluna -> é a posição na linha capturada. Se houver um erro, a coluna indicará a posição precisa do erro.

        NOTA: O TRACEBACK não exibe conforme o padrão LIFO da call stack. Ele imprime seguindo a sequencia inversa.
            [frame_first_in] ....
              ...
            [frama_penultimo] ....
            [frame_last_in] ....

    BOTÕES DO DEBUGGUER:
        [Continue]  -> Executa o programa em velocidade normal até encontrar o p´roximo breakpoint ou o fim do script.
        [Step Over] -> Executa a linha atual. Se houver uma chamada de função, o debugger a executa em velocidade normal e pausa na linha seguinte da função atual, sem detalhar o que aconteceu nos quadros internos.
        [Step Into] -> Avança para a próxima linha de intrução. Se a linha for uma chamda de função, o debugger "entra" na função e empilha um novo frame no topo da call stack.
        [Step Out]  -> Continua a execução do código em velocidade normal até que a função atual termine, desempilhando o frame atual e pausando imediatamente após o retorno na função chamadora.
        [Restart]   -> Reinicia a depuração.
        [Stop]      -> Interrompe a depuração.

    CURIOSIDADE: Ferramentas de depuração via linha de comando, como o módulo nativo pdb, permitem iniciar o debugger no modo pós-morte (pdb.pm()) logo após um travamento. Com o comando w (where), o pdb exibe o traceback da pilha e permite navegar por cada frame para inspecionar as variáveis que causaram o erro.

    MÉTODOS QUE PODEM SER USADOS NO MODO INTERATIVO DO DEBUGGER:
        -> digite a variável que deseja ver.
        -> digite: dir(string) -> isso vai mostrar todos os atributos definidos dentro da string. Há outros métodos, como hasattr, getattr e etc.


DOCUMENTAÇÃO PYTHON
    https://docs.python.org/pt-br/3.16/builtins/stdtypes.html

ATALHOS VISUAL STUDIO CODE
    https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf

AMBIENTE VIRTUAL (venv)

    É como se fosse uma bolha para cada projeto.
    python -m venv nome_ambiente_virtual -> comando básico para criar um ambiente virtual. Vai executar o modulo venv como script.
    Há uma aula explicando isso.

    Configurar a Extensão da Microsoft (ESCOLHENDO O INTERPRETADOR DO AMBIENTE VIRTUAL):
        Atalho: Ctrl + Shift + P (Python Select Interpret)

        >select interpreter -> clica em select intepreter -> (Depois, selecione o caminho do python do ambiente virtual)

        Se não aparecer o ambiente virtual, clique em Enter interpreter path para selecionar o python dentro da pasta Scripts do ambiente virtual.

    É RECOMENDÁVEL abrir o VS CODE na pasta que existe o ambiente virtual, para evitar incoveniencias.

        PROBLEMA: Ao clicar Ctrl C, ou clicar varias vezes no botão run, o caminho de execucao do programa volta para a pasta CURSO_python, e sai, consequentemente, do ambiente virtual.
            Explicação:

                Considere o caminho
                    C:\Users\rafae\Desktop\CURSO_python\programas_python_parte_2
                CURSO_python foi a pasta aberta no VSCODE.
                programas_python_parte_2 é a pasta que contém o ambiente virtual.

                O comportamento de voltar para a pasta CURSO_python e sair do ambiente virtual acontece porque o VS Code está reutilizando uma sessão/processo do terminal que iniciou na pasta CURSO_python ou a extensão Python/gerenciador de ambientes está resetando/reabrindo o shell na raiz do workspace (CURSO_python), além de "python-envs.defaultEnvManager": "ms-python.python:system" priorizar o Python do sistema quando a extensão recarrega o ambiente.
        
        SOLUCAO DO PROBLEMA:
            1. Corrigir o diretório e manter o ambiente virtual ativo ao rodar ou interromper

                a. Abrir a pasta específica do projeto no VS Code (em vez da pasta CURSO_python):
                    No menu superior do VS Code, clique em File > Open Folder... (Arquivo > Abrir Pasta...) e abra diretamente projeto_experimental (ou a subpasta do seu projeto), em vez de abrir a pasta raiz CURSO_python.
                    Verification: A barra de título e o explorador lateral do VS Code passam a mostrar apenas a pasta do projeto atual, e o terminal inicia direto nela.
                
                b. Selecionar o Python do ambiente virtual como padrão do projeto:
                    Pressione Ctrl + Shift + P, digite Python: Select Interpreter e escolha o python.exe de dentro da pasta .venv do seu projeto (ou use Enter interpreter path... apontando para ...\.venv\Scripts\python.exe).
                    Verification: O VS Code exibe o interpretador do .venv selecionado na barra inferior e cria/atualiza a configuração local do projeto sem depender apenas do Python do sistema.
                
                c. Evitar múltiplos cliques rápidos no Run e fechar terminais antigos:
                    Clique na aba do terminal que está em CURSO_python e feche-a no ícone de lixeira; ao executar seu código, use python arquivo.py direto no terminal já ativado com .\.venv\Scripts\Activate.ps1.
                    Verification: Ao pressionar Ctrl + C durante uma execução, o comando é interrompido no mesmo prompt (.venv) da pasta do projeto, sem voltar para CURSO_python nem perder a ativação do ambiente.
            
            2. Ajustar configurações se o VS Code continuar resetando o ambiente ou o diretório
                Se o VS Code abrir o terminal sempre na pasta CURSO_python: 
                    Abra as configurações (Ctrl + ,), pesquise por terminal.integrated.cwd e deixe vazio (ou aponte para ${fileDirname} caso queira que o terminal use a pasta do arquivo aberto).Verificação: Novos terminais abrem na pasta esperada e não forçam o retorno para CURSO_python.
                Se o VS Code estiver usando a nova interface de ambientes (python-envs) e perdendo o .venv:
                    Abra a paleta de comandos (Ctrl + Shift + P), digite Python: Clear Cache and Reload Window para limpar o cache de ambientes antigo e redefinir o interpretador do .venv em seguida.Verificação: A janela recarrega e o interpretador do .venv permanece selecionado após rodar ou apertar Ctrl + C.

    Problemas com segurança:

        1. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

            Esse comando ajusta a política de execução de scripts do PowerShell para permitir que seus scripts locais rodem normalmente, mantendo uma camada de segurança contra scripts baixados da internet sem assinatura digital confiável.

            No Windows, o PowerShell vem configurado por padrão de forma restritiva (Restricted ou AllSigned em alguns cenários) para evitar que um script malicioso seja executado acidentalmente. É exatamente esse bloqueio que impediu o Activate.ps1 de rodar no seu terminal.

            Partes:
                Set-ExecutionPolicy: É o cmdlet (comando) do PowerShell usado para alterar a regra de execução de scripts (.ps1) e arquivos de configuração.
                -ExecutionPolicy RemoteSigned: Define a regra em si:
                    Scripts criados ou salvos localmente na sua máquina (como o Activate.ps1 dentro do seu .venv) podem ser executados sem precisar de assinatura digital.
                    Scripts baixados da internet (que o Windows marca com o fluxo Zone.Identifier) só são executados se tiverem uma assinatura digital confiável (ou se você desbloquear o arquivo manualmente).
                -Scope CurrentUser: Aplica essa mudança apenas para o seu usuário atual no Windows, sem exigir privilégios de Administrador e sem alterar a configuração de outros usuários ou do sistema inteiro.
        
        2. Get-ExecutionPolicy -List

            Ver qual política está ativa no momento.

        3. Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser

            Reseta a política de execução.Remove a sobrescrita feita no escopo CurrentUser e faz o PowerShell voltar a seguir o nível superior.

    Comandos:
        gcm python -> verifica o caminho do python.
        (macOS or Linux)which python -> mostra qual o caminho do python que esta sendo usado. (funciona no powersheel)

PROBLEMA AO RENOMEEAR DIRETORIOS QUE CONTÉM AMBIENTE VIRTUAL

    Quando você renomeia uma pasta que contém um ambiente virtual (ou uma pasta ancestral dele), o comando deactivate pode parar de funcionar porque a função deactivate é carregada em memória pelo script de ativação do ambiente — e, se o terminal foi reiniciado ou o ambiente não foi carregado de forma limpa/apontando para o caminho antigo, o comando não existe na sessão atual. Além disso, ambientes virtuais Python gravam caminhos absolutos internos nos scripts e executáveis, então renomear pastas costuma quebrar o ambiente.

    Como resolver:
        1. Sair da sessão atual ou limpar a variável manualmente
            a. Fechar e abrir um novo terminal
            b. Restaurar o prompt e o PATH na sessão atual (se preferir não fechar o terminal)
                No PowerShell, se o prompt ainda exibir o nome antigo entre parênteses, você pode limpar a alteração do prompt com

                    function prompt { "PS $($executionContext.SessionState.Path.CurrentLocation)$('>' * ($nestedPromptLevel + 1)) " }

                Verification: A linha de comando volta a mostrar apenas PS seguido do caminho da pasta atual.
            
        2. Recriar o ambiente virtual após renomear a pasta
            Como renomear a pasta invalída os caminhos absolutos internos de um venv, a forma mais limpa e segura de evitar erros com pip, python e atalhos é recriar o ambiente na pasta já renomeada:

            a. Remover a pasta antiga do ambiente virtual
                Apague a pasta antiga do ambiente virtual (por exemplo, .venv ou .env) dentro da pasta renomeada.
            b. Criar um novo ambiente virtual limpo
                No terminal dentro da pasta renomeada, execute python -m venv .venv.
            c. Ativar o novo ambiente e reinstalar dependências
                Ative com .\.venv\Scripts\Activate.ps1 (no PowerShell) e instale os pacotes necessários novamente (por exemplo, pip install -r requirements.txt).
                Verification: O terminal exibe (.venv) antes do caminho e Get-Command python aponta para ...\.venv\Scripts\python.exe.
            
            (Nota: se você tiver um arquivo requirements.txt ou pyproject.toml, reinstalar as bibliotecas no novo .venv leva poucos segundos e evita bugs ocultos de caminhos antigos.)

    Limpando vestígios do caminho do antigo caminho.
        Quando você aperta Ctrl + C no terminal e o caminho volta ou muda para um diretório antigo/excluído do ambiente quebrado — e você não consegue executar nenhum programa — o problema geralmente está em um atalho de teclado do VS Code, em uma configuração/tarefa de execução (Run Python File / tasks.json / settings.json) que ainda guarda o caminho antigo, ou na sessão do PowerShell presa em um diretório inexistente.

        1. Corrigir a sessão presa e limpar o caminho antigo no VS Code
            a. Sair do diretório inexistente no PowerShell:
                Digite 
                    Set-Location $HOME (ou cd ~)
                e depois
                    cd "C:\Users\rafae\OneDrive\Desktop"
                para tirar o PowerShell de um caminho que foi renomeado ou apagado.
            Verification: O prompt passa a exibir um caminho válido existente no seu computador sem erro de diretório não encontrado.

            b. Verificar o que o Ctrl + C está fazendo no VS Code (se ao fizer isso, voltar para o caminho apagado.)
                Pressione
                    Ctrl + K Ctrl + S
                para abrir Keyboard Shortcuts (Atalhos de Teclado), digite ctrl+c na barra de busca e veja se algum comando (como uma tarefa ou extensão) está associado a Ctrl + C além do padrão de copiar/interromper.
                Verification: A lista mostra apenas os atalhos padrão esperados (como copiar texto ou interromper comando no terminal), sem nenhum comando customizado apontando para o caminho antigo.
            
            c. Checar se há configurações ou tarefas antigas na pasta do projeto
                Na pasta do projeto (ex.: projeto_experimental), abra a pasta oculta .vscode (se existir) e verifique arquivos como settings.json ou tasks.json para ver se algum caminho do ambiente virtual antigo ficou gravado lá.
                Verification: Nenhum caminho antigo ou excluído aparece em settings.json ou tasks.json (se houver, apague ou atualize para o caminho atual).

        2. Restaurar a execução de programas
            a. Abrir um terminal PowerShell limpo:
                Feche todas as abas abertas do terminal no VS Code e abra uma nova com Ctrl + Shift + '.
                Verification: Abre uma sessão nova do PowerShell sem resquícios do ambiente quebrado.

            b. Selecionar um interpretador Python válido:Pressione Ctrl + Shift + P, digite Python: Select Interpreter e escolha um Python existente (ou o .venv\Scripts\python.exe recriado na pasta atual).
            Verification: O VS Code exibe o interpretador válido selecionado na barra de status.
            
            c.Testar a execução de um programa simples:Navegue até a pasta atual do projeto e rode
                python --version e, em seguida, python seu_arquivo.py
            Verification: O terminal mostra a versão do Python e executa o programa normalmente, sem travar ou mudar para o caminho excluído ao apertar Ctrl + C.
            
AMBIENTE VIRTUAL, Poetry, uv, Pipenv, Conda/Miniconda, Docker

    1. O Poetry é uma das ferramentas mais populares hoje para gerenciamento de dependências e empacotamento, e ele se relaciona diretamente com o conceito de ambiente virtual (venv/virtualenv) dessas duas formas:

        1. Como o Poetry "confronta" (substitui o gerenciamento manual)
            
            Antes (modo tradicional): Você precisava criar o ambiente virtual manualmente (python -m venv .venv), ativá-lo, instalar bibliotecas com pip install ... e salvar tudo na mão em um arquivo requirements.txt (pip freeze > requirements.txt).

            Com o Poetry: Você não precisa criar nem ativar o venv manualmente no dia a dia. Ao rodar poetry add nome-da-biblioteca ou poetry run python seu_script.py, ele já cria, gerencia e usa um ambiente virtual isolado nos bastidores automaticamente, além de manter um arquivo moderno (pyproject.toml e poetry.lock) que resolve conflitos de versões de pacotes muito melhor que o pip.
        
        2. Como o Poetry "soma" (trabalha junto com o ambiente virtual)

            O Poetry não elimina o ambiente virtual por baixo dos panos — ele usa um venv padrão criado por ele mesmo (ou até um venv que você já tenha criado na pasta do projeto, se configurar virtualenvs.in-project = true).

            Ou seja, ele soma uma camada inteligente de gerenciamento de pacotes, controle exato de versões (poetry.lock) e publicação de projetos em cima do ambiente virtual isolado.
    
    2. uv (da Astral): Ferramenta ultrarrápida escrita em Rust que cria venv, instala pacotes e gerencia projetos substituindo pip, venv e até o próprio Poetry.

    3. Pipenv: Combina pip + virtualenv em um fluxo único (com Pipfile).

    4. Conda / Miniconda: Gerenciador tanto de ambientes virtuais quanto de pacotes (muito usado em Ciência de Dados e IA), que cria seus próprios ambientes isolados em vez de usar o venv nativo.

    5. Docker: Confronta/complementa num nível acima, isolando não só o Python e as bibliotecas, mas o sistema operacional inteiro em containers.

SOBRE O INTERPRETADOR DO PYTHON

    python mod.py (executa o modulo)
    python -u (unbuffered -> o codrunning diz para jogar tudo na tela, sem salvar no buffer)
    python -m mod (lib mod como script -> executa uma biblioteca do python como script)
    python -c 'cmd' (executa um comando no terminal)
    python -i mod.py (interativo com mod -> traz toda a saída do módulo e logo em seguida é possível interagir com o código.)

FILOSOFIAS DE BOAS PRATICAS DE PROGRAMAÇÃO

    EAFP(Easier to Ask Forgiveness than Permission)
        "É mais fácil pedir perdão do que permissão."
        Essa é a filosofia oficial do Python. Em vez de verificar o tipo ou o estado de um objeto antes de fazer alguma operação (o que seria "pedir permissão"), você simplesmente executa a operação e, se algo der errado, você trata o erro no except ("pede perdão").
        Se a exceção for rara, o código roda mais rápido porque evita checagens desnecessárias a cada ciclo.

    LBYL(Look Before You Leap)
        "Olhe antes de pular."
        Essa é a abordagem tradicional de linguagens como C ou Java. Você faz checagens preventivas (if, isinstance(), hasattr()) para garantir que tudo é seguro antes de executar a ação.

PROGRAMAS CRIADOS

    O ideal é que o executavel (__main__) fique na pasta raiz do projeto, para, a partir dele, o Python conseguir localizar todas os módulos criados no projeto. Isso minimiza problemas envolvendo o path.