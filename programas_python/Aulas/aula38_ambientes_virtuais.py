"""
AMBIENTE VIRTUAIS EM PYTHON (venv)

    Um ambiente virtual carrega toda a sua instalação do Python para uma pasta caminho escolhida. Ao ativar um venv, a instalação do ambiente virtual será usada.
    Geralmente toda a instalação e biblioteca de terceiros vão para essa pasta, para o ambiente virtual.
    
    venv é o módulo que vamos usar para criar ambientes virtuais. É possível personalizar o nome do ambiente, mas os mais comuns são venv, env, .venv, .env
    (É usado . antes do nome porque não precisa ficar vendo a pasta.)

    Sobre nomeação:
        -> Cada projeto tem seu caminho, portanto, voce pode usar o mesmo nome do em todos. Eles não entram em conflito porque estão em diretórios diferentes.
        -> Se os ambientes virtuais ficarem numa pasta centralizada, deve-se usar nomes diferentes, porque senão um sobrescreve o outro na mesma pasta.

    Dica extra sobre o nome .env
        Por convenção, muita gente prefere nomear a pasta do ambiente virtual como .venv em vez de .env, porque .env costuma ser reservado para arquivos de variáveis de ambiente (como senhas, tokens e strings de conexão). Funciona de qualquer jeito, mas usar .venv evita confusão entre ambiente virtual e arquivo de configuração.

    Um ambiente vitual em Python é um diretório isolado que permite instalar módulos e pacotes de terceiros especificamente para um projeto, sem alterar a instalação global do Python no sistema operacional e sem necessitar de permissões de administrador.

    PROBLEMAS DE NÃO TER UM AMBIENTE VIRTUAL:
        1. Se você ter muitos projetos, se você não isolar as intalações para cada caso, sua máquina pode ficar muito pesada.
        2. As vezes um projeto feito há 5 anos atrás é compatível apenas com versões anteriores de instalações. Sem um ambiente virtual, os pacotes podem ser atualizado constantemente, e, quando for mexer num projeto antigo, pode ser que ele quebre, pois surgiram atualizações que "quebraram" o código.
            
        Com um ambiente virtual as versões são preservadas. Elas só são atualizadas se o programador estiver dentro do ambiente virtual para realizar as instalações.
        Usar ambientes virtuais cria uma camada de compatibilidade entre sistemas.

    Ambiente Virtual ou Docker?
        A preferência entre ambiente virtual e Docker, depende do contexto.
            Ambientes virtuais são mais leves e adequados para projetos Python isolados.
            Docker é recomendado para criar ambientes independentes, envolvendo várias tecnologias além do Python, como bancos de dados e servidores.
        Outras ferramentas: Poetry, uv, Pipenv, Conda.

    POR QUE USAR?
        Ao desenvolver projetos em Python, é comum depender de bibliotecas externas instaladas via ferramentas de pacotes como o pip. Se todos os projetos utilizarem a instalação global do sistema, surgem diversos problemas:

            1. Conflito de dependências:
                Um projeto pode necessitar da versão 1.0 de uma biblioteca, enquanto outro projeto necessita da versão 2.0 da mesma biblioteca.

            2. Permissões de sistema:
                Alterar o diretório global site-packages do sistema operacional muitas vezes exige privilégios de superusuário(sudo), o que pode ser arriscado ou inviável em ambientes compartilhados.

            3. Reprodutibilidade, isolamento e deploy:
                Manter um ambiente limpo permite garantir que o projeto contenha apenas as dependências estritamente necessárias para sua execução. Permite gerar um arquivo requirements.txt (ou pyproject.toml) com apenas as dependencias daquele projeto, facilitando rodar o código em outra máquina, no CI/CD ou em produção.
            
            4. Testes mais seguros:
                Se uma atualização de pacote quebrar algo, o impacto fica restrito àquele ambiente, facilitando recriá-lo do zero.
    
    FUNCIONAMENTO INTERNO
        Ao criar um ambiente virtual (seja utilizando venv ou a ferramenta pyvenv), o Python gera uma estrutura de diretórios contendo pastas como bin/(ou Scripts/ no Windows), include/, lib/ e o arquivo de configuração pyvenv.cfg.

            -> Estrutura leve e links simbólicos:
                O ambiente virtual não faz uma cópia inteira e pesada do Python; ele utiliza arquivos de configuração e links simbólicos que apontam para o interpretador e bibliotecas padrão originais do sistema.

            -> Redirecionamento do site-packages:
                A principal alteração ocorre no caminho busca de módulos(sys.path), que passa a apontar a pasta site-packages localizada dentro da estrutura do próprio ambiente virtual.

            -> Instalação isolada:
                Qualquer biblioteca instalada via pip enquanto o ambiente virtual estiver ativo será gravada exclusivamente nesse diretório site-packages local.

            -> Herança de pacotes do sistema:
                Por padrão, um ambiente virtual é criado totalmente limpo, mas é possível incluir os pacotes já instalados no Python do sistema utilizando a opção --system-site-packages na criação.

    COMO USAR:
        1. Criando o ambiente virtual:
            python -m venv .venv

            #cria a pasta .venv contendo toda a estrutura isolada do ambiente.

            IMPORTANTE: 
                COLOQUE A PASTA CRIADA NO .gitignore PARA QUE ELA NÃO SEJA VERSIONADA. Quem vai controlar essa parte de "versões" será o arquivo requirements.txt
        
        2. Ativando o ambiente:
            Linux -> source .venv/bin/activate
            Windows(PoweShell) -> .venv/Scripts/activate.ps1
            Windows(CMD) -> .venv/Scripts/activate.bat

            #Após ativação, o nome do ambiente (.venv) é exibido no início do prompt do terminal. Quando ativa, ao invés de usar o Python do sistema, o programador usará o Python do ambiente virtual.
        
        3. Instalando pacotes no ambiente:
            pip install requests

            #use pip normalmente. Os pacotes serão instalados isoladamente dentro da pasta site-packages do ambiente.

            Nota: Para utilitários globais de linha de comando, como ruff, black ou pipx, costuma-se usar ferramentas como pipx ou uv em vez de instalar tudo num venv de projeto.
        
        4. Desativando o ambiente virtual:
            deactivate

            #Para sair do ambiente virtual e retornar ao terminal global.

            Quando desativar:
                1. Vai mudar para outro projeto: Ao sair da pasta de um projeto e trabalhar em outro, desative o atual para não instalar pacotes ou rodar scripts no ambiente errado.
                2. Precisa rodar comandos do sistema / globais: Quando quiser usar ferramentas ou scripts instalados fora do ambiente virtual.
                3. Terminou de trabalhar no projeto e quer voltar ao shell padrão: Embora fechar a janela do terminal já encerre a sessão ativa, rodar deactivate limpa o prompt e o PATH na sessão atual.

    ONDE USAR:
        Praticamente em todo projeto Python: APIs web(FastAPI, Django, Flask), automações, scripts de dados, bots, ferramentas CLI e projetos com dependências externas.

        Na raiz do projeto: O padrão mais comum é criar a pasta dentro do diretório do projeto (geralmente chamada .venv ou venv) e adicionar essa pasta ao .gitignore, pois ambientes virtuais não devem ser versionados no Git.
        
        NÃO PRECISA ENVIAR A PASTA PARA O REPOSITÓRIO, PORQUE É CRIADO UM ARQUIVINHO CHAMADO requirements.txt, que nele é jogado tudo que foi instalado no ambiente virtual a fim de recriar esse ambiente.

    NOTA SOBRE APAGAR AMBIENTES VIRTUAIS:
        Desativar (deactivate) apenas sai do ambiente naquela sessão do terminal — a pasta .venv e os pacotes continuam intactos.

        Apagar a pasta .venv só é feito se você quiser recriar o ambiente do zero (por exemplo, para limpar dependências antigas ou resolver um ambiente corrompido) e depois reinstalar tudo com pip install -r requirements.txt.

"""

