"""
JSON (Java Script Object Notation)

    É uma estrutura de dados para transportar ou salvar dados.
    É uma estrutura de dados simples, muito mais simples do que a estrutura de dados que tem na linguagem de programação.

    É um formato leve de armazenamento e intercâmbio de dados em formato de texto simples. Ele foi derivado da sintaxe de objetos da linguagem JavaScript, mas é totalmente independente da linguagem. Lançado como uma alternativa leve ao XML, o JSON tornou-se um padrão universal na Web devido à sua simplicidade e facilidade de leitura tanto por humanos quanto por máquinas.

    O proprio arquivo settings do python é feito em .json

    Similaridades:
        Similar ao Dicionário, em Python.
        Similar ao JavaScript.
    
    Em um json só pode ter 5 tipos de dados:
        1. boleano (true e false)
        2. number(interiro ou flutuante)
        3. null
        4. "string"
        5. Array (representado por [], um grupo de valores)
        6. objeto(representado por {}, pra atribuir a alguma coisa mais de um valor, segue o padrão key-value)
    
    Limitação:
        O JSON não suporta nativamente objetos específicos do Python ou de outras linguagens, tais como arquivos abertos, leitores/escritores de CSV, expressões regulares ou instâncias diretas de classes personalizadas.

    Um json é válido até mesmo se tiver apenas um valor.

    CASOS DE USO:
        1. Comunicação e APIs Web (REST APIs) :
            O JSON é o formato dominante para enviar requisições e receber respostas em APIs web. Grandes plataformas como Google, Facebook, GitHub e Reddit disponibilizam suas APIs em formato JSON para que sistemas e aplicativos consumam seus dados de maneira padronizada.

        2. Sistemas Orientados a Eventos e Microsserviços :
            Em arquiteturas distribuídas, dados de eventos, comandos e payloads de requisições HTTP são serializados em JSON para transmissão via redes, barramentos de mensagens ou canais de Pub/Sub(Como o Redis).
        
        3. Arquivos de Configuração e Ingestão de Dados :
            Por ser estruturado e facilmente editável em qualquer editor de texto, o JSON é muito utilizado para armazenar configurações de aplicações ou para a troca de migração de dados entre bancos de dados e scripts de processamento.

    MANIPULAÇÃO DE JSON EM PYTHON
        O Python possui o módulo nativo json para converter (parsear e serializar) dados entre strings JSON e estruturas nativas:
            1. Leitura e Conversão para Python (Deserialização)
                a) json.loads(string_json) : Converte uma string formatada em JSON em um dicionário ou lista do Python.
                b) json.load(arquivo_json) : Lê o conteúdo de um arquivo .json aberto em disco e realiza a conversão direta para objetos Python.
            
            2. Escrita e Exportação para JSON (Serialização)
                a) json.dumps(objeto_python) : Converte um dicionário, lista ou tipo básico do Python em uma string formatada em JSON.
                b) json.dump(onjeto_python, arquivo_json) : Grave diretamente a estrutura de dados Python formatada como JSON em um arquivo no disco.

            3. Recursos Avançados do Módulo json
                a) Formatação Elegante:
                    O parâmetro indent(ex: json.dumps(dados, indent=2)) ou a função pprint.pprint() ajudam a formatar a saída com recuos para facilitar a leitura visual.
                b) Ordenação de Chaves:
                    O parâmetro sort_keys=True ordena as chaves alfabeticamente ao gerar o JSON.
                c) Personalização na Decodificação:
                    É possível definir parâmetros como object_pairs_hook=OrderedDict para preservar a ordem das chaves em dicionários ordenados ao ler um JSON.
                d) Serialização de Objetos Customizados:
                    Para converter instâncias de classes próprias em JSON, passa-se uma função de conversão customizada no parâmetro default de json.dumps().

"""
import json
import os

pessoas = [
    {
        "nome": "maria",
        "sobrenome": "vieira",
        "idade": 25,
        "ativo": False,
        "notas": ["A", "A+"],
        "telefones": {
            "residencial": "00 0000-0000",
            "celular": "00 0000-0000"
        }
    },
    {
        "nome": "Joana",
        "sobrenome": "Moreira",
        "idade": 32,
        "ativo": True,
        "notas": ["B", "A+"],
        "telefones": {
            "residencial": "00 0000-0000",
            "celular": "00 0000-0000"
        }
    },
]

BASE_DIR = os.path.dirname(__file__) #cria o caminho completo do arquivo onde esse programa está.
SAVE_TO = os.path.join(BASE_DIR, 'arquivo_python.json') #juntando para formar o caminho completo.

with open(SAVE_TO, 'w', encoding='utf-8') as file:
    json.dump(pessoas, file, indent=4) #usando indent=2 para melhorar a visualização.

print(f'Sem indent:\n{json.dumps(pessoas)}\n')
print(f'Com indent:\n{json.dumps(pessoas, indent=2)}\n')

#PARA CARREGAR UM JSON DE FORA:
with open(SAVE_TO, 'r', encoding='utf-8') as file:
    pessoas = json.load(file)

    for pessoa in pessoas:
        print(pessoa['nome'])

print()
#PARA CARREGAR UMA STRING
json_string = '''[{"nome": "Rafael", "sobrenome": "Oliveira", "idade": 25, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}, {"nome": "Maria", "sobrenome": "Alves", "idade": 32, "ativo": true, "notas": ["B", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}]'''

pessoas = json.loads(json_string)

for pessoa in pessoas:
    print(pessoa['nome'])