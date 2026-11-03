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


DOCUMENTAÇÃO PYTHON:
https://docs.python.org/pt-br/3.16/builtins/stdtypes.html

AMBIENTE VIRTUAL (venv)
É como se fosse uma bolha para cada projeto.
python -m venv nome_ambiente_virtual -> comando básico para criar um ambiente virtual. Vai executar o modulo venv como script.

SOBRE O INTERPRETADOR DO PYTHON

python mod.py (executa o modulo)
python -u (unbuffered -> o codrunning diz para jogar tudo na tela, sem salvar no buffer)
python -m mod (lib mod como script -> executa uma biblioteca do python como script)
python -c 'cmd' (executa um comando no terminal)
python -i mod.py (interativo com mod -> traz toda a saída do módulo e logo em seguida é possível interagir com o código.)